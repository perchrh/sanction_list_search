#!/usr/bin/env python3

import fuzzy
import unicodedata
from timeit import default_timer as timer
from collections import Counter

import eu_global


def loadSanctions(filename):
    sanctions = eu_global.parse(filename, silence=True)

    id_to_name = {}
    for entity in sanctions.sanctionEntity:
        fixedRef = entity.logicalId
        # TODO distinguish between entities and individuals
        aliases = []
        for alias in entity.nameAlias:
            if not alias.strong == 'true':  # filter for now
                continue
            name = alias.wholeName
            aliases.append(name)
        id_to_name[fixedRef] = aliases
    return id_to_name


def normalize_name_parts(names):
    unique_name_parts = set()
    for name in names:
        for name_part in name.split():
            normalized_name = normalize_word(name_part)
            if normalized_name:
                unique_name_parts.add(normalized_name)

    return unique_name_parts


import functools


def normalize_word(name_part):
    normalized_name = name_part.lower()
    split_characters = [x for x in normalized_name if not x.isalpha()]
    if split_characters:
        # replace non-alphabet letters with a space
        normalized_name = functools.reduce(lambda s, sep: s.replace(sep, ' '), split_characters, normalized_name).strip()

    # remove diacritics
    normalized_name = ''.join(x for x in unicodedata.normalize('NFKD', normalized_name))
    return normalized_name


def most_common_names(id_to_name):
    """
    TODO use n %% of these as stop-words?
    """
    words = []
    for reference, names in id_to_name.items():
        name_parts = normalize_name_parts(names)
        for name_part in name_parts:
            words.append(name_part)

    stopword_count = 25  # TODO use dynamic value

    counter = Counter()

    counter.update(list(words))
    most_common_words = set([word[0] for word in counter.most_common(stopword_count)])
    return most_common_words


def compute_phonetic_bin_lookup_table(id_to_name):
    """
            computation of hashmap of phonetic bin to list of list-entries, WIP
    """
    dmeta = fuzzy.DMetaphone()
    bin_to_id = {}
    for reference, names in id_to_name.items():
        unique_name_parts = normalize_name_parts(names)
        for name_part in unique_name_parts:

            if len(name_part) < 4:
                continue  # FIXME refine this restriction, only certain of the short words should be excluded. Instead check for stop words

            try:
                bins = dmeta(name_part)
            except UnicodeEncodeError:
                continue  # FIXME ignores non-latin words silently

            for bin in bins:
                if not bin in bin_to_id:  # if bin not already added to dictionary
                    bin_to_id[bin] = []  # begin a new list of references

                bin_to_id[bin].append(reference)

    max_count = len(id_to_name) / 8  # 12.5% or more of the entries has it
    filtered_dict = remove_outliers(bin_to_id, max_count)

    return filtered_dict


def remove_outliers(bin_to_id, max_count):
    # FIXME Poor mans removal for now. We should probably rather generate a list of stop words, and filter those out
    # possibly in addition remove statistical outliers, bins that have super-many references. They don't help in search either.
    outliers = []
    for bin, references in bin_to_id.items():
        if len(references) > max_count:
            outliers.append(bin)
    filtered_dict = {key: bin_to_id[key] for key in bin_to_id if key not in outliers}
    return filtered_dict


import resource

from fuzzywuzzy import fuzz


def search(name_string, bin_to_id):
    # TODO find candidate matches, by creating a list of bins from the name, and returning all references that match those bins
    # the candidates must then be filtered. A simple first version is to require fuzzywuzzy.fuzz.ratio(input, candidate) to be > 60
    dmeta = fuzzy.DMetaphone()

    bins = []
    name_parts = normalize_name_parts([name_string])
    for name_part in name_parts:
        for bin in dmeta(name_part):
            bins.append(bin)

    candidates = set()
    for bin in bins:
        if bin and bin in bin_to_id:
            candidates_in_bin = bin_to_id[bin]
            for c in candidates_in_bin: candidates.add(c)

    filtered_candidates = set()
    for candidate in candidates:
        candidate_names_in_sanction_entry = id_to_name[candidate]
        for list_entry_name in candidate_names_in_sanction_entry:
            similarity_ratio = fuzz.token_sort_ratio(list_entry_name, name_string)
            if similarity_ratio >= 60:  # hardcoded lower limit
                filtered_candidates.add(candidate)

    return filtered_candidates


import sys


def print_longest_overflow_bin_length(bin_to_id):
    longest_list = 0
    bin_of_longest_list = None
    for bin, references in bin_to_id.items():
        if len(references) > longest_list:
            longest_list = len(references)
            bin_of_longest_list = bin
    print("Longest overflow-bin had", longest_list, "items. With value", bin_of_longest_list)


if __name__ == "__main__":

    start = timer()

    id_to_name = loadSanctions('eu_global_full_20180604.xml')
    bin_to_id = compute_phonetic_bin_lookup_table(id_to_name)

    end = timer()
    print("Total time usage for loading: {} ms".format(int(10 ** 3 * (end - start) + 0.5)))

    for reference, names in id_to_name.items():
        # print(reference, names)
        pass

    print("Computed", len(bin_to_id), "phonetic bins for", len(id_to_name), "list entries.")
    print_longest_overflow_bin_length(bin_to_id)

    print("Most common name parts are", most_common_names(id_to_name))

    memory_usage_bytes = sys.getsizeof(id_to_name) + sys.getsizeof(bin_to_id)
    print("Memory usage of sanction-list data structures are", memory_usage_bytes / 2 ** 20, "MB")

    test_name = "Anastasiya Nikolayevna KAPRANOVA"
    start = timer()
    candidates = search(test_name, bin_to_id)
    end = timer()
    print("\nFound", len(candidates), "candidates in search for", test_name)
    for c in candidates:
        print("-", id_to_name[c])
    print("Total time usage for searching: {} ns".format(int(10 ** 6 * (end - start) + 0.5)))
