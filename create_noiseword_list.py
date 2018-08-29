# Prints the most common words in the sanction lists.
# Manually inspect the lists to find noise words (stop words), like "The", "abd", and other words
# that do not contribute to search results.

from eu import reader as eu_reader
from ofac import reader as ofac_reader
from un import reader as un_reader
from collections import Counter
import normalizer


def print_word_frequencies(stop_words, stop_words_short, key):
    print("\nNormal length", key, ":")
    for (word, count) in stop_words:
        print(word, count)

    print("\nShort length", key, ":")
    for (word, count) in stop_words_short:
        print(word, count)


def find_most_common_words(sanction_entries, count):
    words = []
    short_words = []
    for sanction_entry in sanction_entries:
        (reference, list_subject) = sanction_entry
        (aliases, birthdates) = list_subject
        name_parts = normalizer.normalize_aliases(aliases)
        for name_part in name_parts:
            if len(name_part) < 2:
                continue  # ignored
            elif len(name_part) <= 4:
                short_words.append(name_part)
            else:
                words.append(name_part)

    word_counter = Counter()
    short_word_counter = Counter()

    word_counter.update(list(words))
    short_word_counter.update(list(short_words))
    stop_words = word_counter.most_common(count)
    stop_words_short = short_word_counter.most_common(count)
    return (stop_words, stop_words_short)


all_entities = []
all_persons = []

(persons, entities) = eu_reader.load_sanctions("eu/eu_global_full.xml")
for item in entities.items(): all_entities.append(item)
for item in persons.items(): all_persons.append(item)

(persons, entities) = un_reader.load_sanctions("un/consolidated.xml")
for item in entities.items(): all_entities.append(item)
for item in persons.items(): all_persons.append(item)

(persons, entities) = ofac_reader.load_sdn_sanctions("ofac/sdn_advanced.xml")
for item in entities.items(): all_entities.append(item)
for item in persons.items(): all_persons.append(item)

(persons, entities) = ofac_reader.load_consolidated_sanctions("ofac/cons_advanced.xml")
for item in entities.items(): all_entities.append(item)
for item in persons.items(): all_persons.append(item)

count = 100
print("Loaded {} entities and {} persons from sanction lists".format(len(all_entities), len(all_persons)))
print(count, "most commons words are:\n")

(stop_words, stop_words_short) = find_most_common_words(all_persons, count)
print_word_frequencies(stop_words, stop_words_short, "individuals")

(stop_words, stop_words_short) = find_most_common_words(all_entities, int(count*2.5))
print_word_frequencies(stop_words, stop_words_short, "entities")
entity_words = set()
for subject in stop_words + stop_words_short:
    entity_words.add((subject[0]))

business_entity_type_abbreviations = set()
for entity_abbreviation in open('business_entity_names'):
    business_entity_type_abbreviations.add(entity_abbreviation.strip())

print("Words both in common words for business names and for business entity names are:")
for word in sorted(business_entity_type_abbreviations.intersection(entity_words)):
    print(word)


