from eu import reader as eu_reader
from ofac import reader as ofac_reader
from un import reader as un_reader
import json
import datetime

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

person_data = []
for person in all_persons:
    (person_key, person_values) = person
    (alias_names, alias_birthdates) = person_values
    person = {"reference": person_key,
              "name_aliases": [str(x) for x in alias_names],
              "birthdate_aliases": [datetime.datetime.strftime(x, "%Y-%m-%d") for x in alias_birthdates if x],
              "birthyear_aliases": None  # TBD
              }
    person_data.append(person)

entity_data = []
for entity in all_entities:
    (key, value) = entity
    (alias_names, alias_birthdates) = value
    person = {"reference": key,
              "name_aliases": [str(x) for x in alias_names]
              }
    entity_data.append(person)

output_file = 'composite_list_export_persons.json'
print("Exporting composite person list to file:", output_file)
with open(output_file, 'w') as outfile:
    json.dump(person_data, outfile, indent=4)

output_file = 'composite_list_export_entities.json'
print("Exporting composite entity list to file:", output_file)
with open(output_file, 'w') as outfile:
    json.dump(entity_data, outfile, indent=4)
