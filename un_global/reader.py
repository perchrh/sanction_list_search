#!/usr/bin/env python3

from timeit import default_timer as timer
from dataobjects import NamePart
from dataobjects import NameAlias

import un_global as parser


def load_sanctions(filename='consolidated.xml'):
    sanctions = parser.parse(filename, silence=True)

    entities = sanctions.ENTITIES.ENTITY
    individuals = sanctions.INDIVIDUALS.INDIVIDUAL

    id_to_name_entities = {}
    for entity in entities:
        if entity.DELISTED_ON:
            continue  # don't include delisted entries

        fixedRef = entity.REFERENCE_NUMBER.strip()

        name_aliases = []
        name_aliases.append(" ".join(entity.FIRST_NAME.split()).strip())  # companies have only first names in list
        for alias in entity.ENTITY_ALIAS:
            if alias.QUALITY == 'Low':
                continue  # skip these for now, TODO include them, but mark as low quality

            name = alias.ALIAS_NAME
            name = " ".join(name.split())  # remove white-space and linebreaks
            name_parts = [NamePart(p) for p in name.split() if p]

            if name_parts:
                name_aliases.append(NameAlias(name_parts))

        id_to_name_entities[fixedRef] = (name_aliases, [])

    id_to_name_persons = {}
    for individual in individuals:
        if individual.DELISTED_ON:
            continue  # don't include delisted entries

        fixedRef = individual.REFERENCE_NUMBER.strip()
        name_aliases = set()

        name_parts = [individual.FIRST_NAME, individual.SECOND_NAME, individual.THIRD_NAME, individual.FOURTH_NAME]
        name_parts = [" ".join(name.split()) for name in name_parts if name]  # remove white-space and linebreaks
        name_parts = [NamePart(p) for p in name_parts]
        name_aliases.add(NameAlias(name_parts))

        date_aliases = set()
        for date_of_birth in individual.INDIVIDUAL_DATE_OF_BIRTH:
            if (date_of_birth.DATE):
                date_aliases.add(date_of_birth.DATE)  # uses python's datetime object

        for alias in individual.INDIVIDUAL_ALIAS:
            if alias.QUALITY == 'Low':
                continue  # skip these for now

            alias_names = alias.ALIAS_NAME
            alias_names = " ".join(alias_names.split())  # remove white-space and linebreaks
            if alias_names:
                alias_list = alias_names.split(";")
                for item in alias_list:
                    name_parts = [NamePart(p) for p in item.split()]
                    name_aliases.add(NameAlias(name_parts))

        id_to_name_persons[fixedRef] = (name_aliases, date_aliases)

    return (id_to_name_persons, id_to_name_entities)


def printSubjects(bin_to_id):
    for reference, names in bin_to_id.items():
        print(reference, names)


if __name__ == "__main__":
    start = timer()

    (id_to_name_persons, id_to_name_entities) = load_sanctions()

    end = timer()
    print("Total time usage for loading: {} ms".format(int(10 ** 3 * (end - start) + 0.5)))
    print("Loaded {} entities and {} persons".format(len(id_to_name_entities), len(id_to_name_persons)))

    printSubjects(id_to_name_entities)
    printSubjects(id_to_name_persons)
