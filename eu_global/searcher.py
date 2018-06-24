#!/usr/bin/env python3

import fuzzy
import unicodedata
from timeit import default_timer as timer
from collections import Counter
from reader import loadSanctions
from dataobjects import NamePart
from dataobjects import NameAlias

import eu_global

dmeta = fuzzy.DMetaphone()


def normalize_name_parts(names):
    all_name_parts = set()
    for name_alias in names:
        for name_part in name_alias.name_parts:
            name_part_value = name_part.part
            split_characters = [x for x in name_part_value if not x.isalpha()]
            if split_characters:
                name_part_value = functools.reduce(lambda s, sep: s.replace(sep, ' '), split_characters,
                                             name_part_value).strip()
                for name_part_part in name_part_value.split():
                    normalized_name = normalize_word(name_part_part)
                    all_name_parts.add(normalized_name)
            else:
                normalized_name = normalize_word(name_part_value)
                all_name_parts.add(normalized_name)

    return all_name_parts


import functools


def normalize_word(word):
    return remove_diacritics(word.lower())

def remove_diacritics(word):
    return ''.join(x for x in unicodedata.normalize('NFKD', word))


def find_stop_words(id_to_name):
    """
    Finds the most common words in the corpus. Use them as stopwords. Uses a higher percentage for stopwords from especially short words.
    """
    words = []
    short_words = []
    for reference, names in id_to_name.items():
        name_parts = normalize_name_parts(names)
        for name_part in name_parts:
            if len(name_part) < 2:
                continue
            elif len(name_part) <= 4:
                short_words.append(name_part)
            else:
                words.append(name_part)

    different_words = set(words)
    different_shortwords = set(short_words)
    stopword_count = int(1.5 * len(words) / len(different_words))  # heuristic
    stopword_count_short_words = int(2 * len(short_words) / len(different_shortwords))  # heuristic

    word_counter = Counter()
    short_word_counter = Counter()

    word_counter.update(list(words))
    short_word_counter.update(list(short_words))
    stop_words = set([word[0] for word in word_counter.most_common(stopword_count)])
    stop_words_short = set([word[0] for word in short_word_counter.most_common(stopword_count_short_words)])
    return stop_words.union(stop_words_short)


def compute_phonetic_bin_lookup_table(id_to_name, stop_words):
    """
        Computation of hashmap of phonetic bin to list of list-entries, WIP
        TODO should distinguish between names, not just put all names of a subject in the same list
    """
    bin_to_id = {}
    for reference, names in id_to_name.items():
        unique_name_parts = set(normalize_name_parts(names))
        for name_part in unique_name_parts:
            if len(name_part) < 2 or name_part in stop_words:
                # skip stop words and words of one character only. todo consider including stopwords, but penalise matches by stopword only
                continue

            try:
                bins = [b for b in dmeta(name_part) if b] #dmeta sometimes outputs an empty 'None' bin, filter it out
            except UnicodeEncodeError:
                continue  # Ignores non-latin words silently. That's ok when input is latin alphabet only.

            for bin in bins:
                if not bin in bin_to_id:  # if bin not already added to dictionary
                    bin_to_id[bin] = []  # begin a new list of references

                bin_to_id[bin].append(reference)

    max_count = len(id_to_name) / 8  # if 100%/8 = 12.5% or more of the entries has it
    filtered_dict = remove_outliers(bin_to_id, max_count)

    return filtered_dict


def remove_outliers(bin_to_id, max_count):
    outliers = []
    for bin, references in bin_to_id.items():
        if len(references) > max_count:  # number of elements in the hashbin is greater than
            # the number of subjects in total
            outliers.append(bin)
    filtered_dict = {key: bin_to_id[key] for key in bin_to_id if key not in outliers}
    return filtered_dict


from fuzzywuzzy import fuzz


def search(name_string, bin_to_id, id_to_name, similarity_threshold=60):
    # TODO give a boost when the number of bins that match are higher than 1
    # TODO should distinguish between first name (less reliable match) and other names.
    # consider storing in each bin, a namepart object linking to its name linking to its subject, that has name.isFirstName:bool

    # 1. calculate the phonetics bins of the input name
    name_parts = [NamePart(name_string)]
    name_aliases = [NameAlias(name_parts, None)]
    name_parts = set(normalize_name_parts(name_aliases))

    bins = []
    for name_part in name_parts:
        name_part_bins = [b for b in dmeta(name_part) if b] #dmeta sometimes outputs an empty 'None' bin, filter it out
        for bin in name_part_bins:
            bins.append(bin)

    #2. find candidates with one or more maching bins
    candidates = set()
    for bin in bins:
        if bin in bin_to_id:
            candidates_in_bin = bin_to_id[bin]
            for c in candidates_in_bin:
                # TODO check if norm. levensthein > 0.60, otherwise don't add. Must then store namepart in bin, together with candidate-id
                candidates.add(c)

    # TODO count the number of bins that matched each candidate-alias

    #3. look up candidate names, filter out matches that are really bad, sort the other matches on similarity ratio
    filtered_candidates = []
    for candidate in candidates:
        candidate_names_in_sanction_entry = id_to_name[candidate]
        for list_entry_name in candidate_names_in_sanction_entry:
            similarity_ratio = fuzz.token_sort_ratio(list_entry_name, name_string)
            if similarity_ratio >= similarity_threshold:
                element = (candidate, similarity_ratio, list_entry_name)
                filtered_candidates.append(element)

    filtered_candidates.sort(key=lambda tup: tup[1], reverse=True)

    return filtered_candidates


import sys


def print_longest_overflow_bin_length(bin_to_id, subjectType):
    longest_list = 0
    bin_of_longest_list = None
    for bin, references in bin_to_id.items():
        if len(references) > longest_list:
            longest_list = len(references)
            bin_of_longest_list = bin
    print("Longest overflow-bin for subject type", subjectType, "had", longest_list, "items. With value",
          bin_of_longest_list)


def printSubjects(bin_to_id):
    for reference, names in bin_to_id.items():
        print(reference, names)


if __name__ == "__main__":
    start = timer()

    (id_to_name_persons, id_to_name_entities) = loadSanctions('eu_global_full_20180618.xml')

    stop_words_persons = find_stop_words(id_to_name_persons)
    stop_words_entities = find_stop_words(id_to_name_entities)

    bin_to_id_persons = compute_phonetic_bin_lookup_table(id_to_name_persons, stop_words_persons)
    bin_to_id_entities = compute_phonetic_bin_lookup_table(id_to_name_entities, stop_words_entities)

    end = timer()
    print("Total time usage for loading: {} ms".format(int(10 ** 3 * (end - start) + 0.5)))
    print("Most common name parts for persons are", stop_words_persons)
    print("Most common name parts for entities are", stop_words_entities)

    print("Computed", len(bin_to_id_persons), "phonetic bins for", len(id_to_name_persons),
          "list subjects of type person.")
    print("Computed", len(bin_to_id_entities), "phonetic bins for", len(id_to_name_entities),
          "list subjects of type entity.")
    print_longest_overflow_bin_length(bin_to_id_persons, "person")
    print_longest_overflow_bin_length(bin_to_id_entities, "entity")

    memory_usage_bytes = sys.getsizeof(id_to_name_entities) + sys.getsizeof(id_to_name_persons) \
                         + sys.getsizeof(bin_to_id_persons) + sys.getsizeof(bin_to_id_entities)
    print("Memory usage of sanction-list data structures are", memory_usage_bytes / 2 ** 20, "MB")

    test_name = "Anastasiya Nikolayevna KARPANOVA"
    start = timer()
    matches = search(test_name, bin_to_id_persons, id_to_name_persons, similarity_threshold=80)
    end = timer()
    print("\nFound", len(matches), "matches in search for", test_name)
    for m in matches:
        (candidate, similarity_ratio, list_entry_name) = m
        print("-", list_entry_name, candidate, str(similarity_ratio) + "%")

    print("Total time usage for searching: {} ns".format(int(10 ** 6 * (end - start) + 0.5)))
