from eu import reader as eu_reader
from ofac import reader as ofac_reader
from un import reader as un_reader

all_entities = []
all_persons = []

(entities, persons) = eu_reader.load_sanctions("eu/eu_global_full.xml")
[all_entities.append(p) for p in entities]
[all_persons.append(p) for p in persons]

(entities, persons) = un_reader.load_sanctions("un/consolidated.xml")
[all_entities.append(p) for p in entities]
[all_persons.append(p) for p in persons]

(entities, persons) = ofac_reader.load_sdn_sanctions("ofac/sdn_advanced.xml")
[all_entities.append(p) for p in entities]
[all_persons.append(p) for p in persons]

(entities, persons) = ofac_reader.load_consolidated_sanctions("ofac/cons_advanced.xml")
[all_entities.append(p) for p in entities]
[all_persons.append(p) for p in persons]

print("Loaded {} entities and {} persons from sanction lists".format(len(all_entities), len(all_persons)))

# TODO count all normalized name parts