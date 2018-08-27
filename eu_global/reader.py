#!/usr/bin/env python3

from timeit import default_timer as timer
from dataobjects import NamePart
from dataobjects import NameAlias
from datetime import datetime

import eu_global as parser


def load_sanctions(filename="eu_global_full.xml"):
    sanctions = parser.parse(filename, silence=True)

    id_to_name_entities = {}
    id_to_name_persons = {}
    for subject in sanctions.sanctionEntity:
        fixedRef = subject.logicalId
        aliases = []
        if subject.delistingDate:
            continue  # delisted, ignore it

        for alias in subject.nameAlias:
            if not alias.strong == 'true':  # filter for now
                continue

            gender_of_alias = alias.gender  # M, F or None

            name_parts = [NamePart(alias.wholeName)]  # TODO correctly separate firstname and other names
            name_alias = NameAlias(name_parts, alias.nameLanguage, gender_of_alias)

            aliases.append(name_alias)

        if subject.subjectType.code == "person":
            birth_dates_strings = [b.birthdate for b in subject.birthdate if b.circa != "true"]  # TODO also support year only etc
            birth_dates = [datetime.strptime(b, '%Y-%m-%d') for b in birth_dates_strings if b]

            id_to_name_persons[fixedRef] = (aliases, birth_dates)
        else:
            id_to_name_entities[fixedRef] = (aliases, [])

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
