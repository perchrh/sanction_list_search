#!/usr/bin/env python3

import fuzzy
import unicodedata
from timeit import default_timer as timer
from collections import Counter

import eu_global

dmeta = fuzzy.DMetaphone()


def loadSanctions(filename):
    sanctions = eu_global.parse(filename, silence=True)

    id_to_name_entities = {}
    id_to_name_persons = {}
    for subject in sanctions.sanctionEntity:
        fixedRef = subject.logicalId
        aliases = []
        for alias in subject.nameAlias:
            if not alias.strong == 'true':  # filter for now
                continue
            name = alias.wholeName
            aliases.append(name)
        if subject.subjectType.code == "person":
            id_to_name_persons[fixedRef] = aliases
        else:
            id_to_name_entities[fixedRef] = aliases

    return (id_to_name_persons, id_to_name_entities)


def printSubjects(bin_to_id):
    for reference, names in bin_to_id.items():
        print(reference, names)


if __name__ == "__main__":
    start = timer()

    (id_to_name_persons, id_to_name_entities) = loadSanctions('eu_global_full_20180604.xml')

    end = timer()
    print("Total time usage for loading: {} ms".format(int(10 ** 3 * (end - start) + 0.5)))


    printSubjects(id_to_name_entities)
    printSubjects(id_to_name_persons)

