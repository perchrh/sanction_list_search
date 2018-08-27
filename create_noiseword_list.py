from eu import reader as eu_reader
from ofac import reader as ofac_reader
from un import reader as un_reader
from collections import Counter
from normalizer import normalize_aliases


def find_most_common_words(sanction_entries):
    words = []
    short_words = []
    for sanction_entry in sanction_entries:
        (reference, list_subject) = sanction_entry
        (aliases, birthdates) = list_subject
        name_parts = normalize_aliases(aliases)
        for name_part in name_parts:
            if len(name_part) < 2:
                continue  # ignored
            elif len(name_part) <= 4:
                short_words.append(name_part)
            else:
                words.append(name_part)

    different_words = set(words)
    different_shortwords = set(short_words)
    stopword_count = int(15 * len(words) / len(different_words))  # heuristic
    stopword_count_short_words = int(20 * len(short_words) / len(different_shortwords))  # heuristic

    word_counter = Counter()
    short_word_counter = Counter()

    word_counter.update(list(words))
    short_word_counter.update(list(short_words))
    stop_words = [word[0] for word in word_counter.most_common(stopword_count)]
    stop_words_short = [word[0] for word in short_word_counter.most_common(stopword_count_short_words)]
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

print("Loaded {} entities and {} persons from sanction lists".format(len(all_entities), len(all_persons)))

(stop_words, stop_words_short) = find_most_common_words(all_persons)
print("Most common words for individuals:")
print("Normal length:", stop_words)
print("Short length:", stop_words_short)

(stop_words, stop_words_short) = find_most_common_words(all_entities)
print("\nMost common words for entities:")
print("Normal length:", stop_words)
print("Short length:", stop_words_short)
