#!/usr/bin/env python3

import un_global
sanctions = un_global.parse('consolidated.xml', silence=True)

entities = sanctions.ENTITIES.ENTITY
individuals = sanctions.INDIVIDUALS.INDIVIDUAL

for entity in entities:
    aliases = []
    fixedRef = entity.REFERENCE_NUMBER
    if entity.DELISTED_ON:
        continue # don't include delisted entries
    aliases.append(entity.FIRST_NAME)
    for alias in entity.ENTITY_ALIAS:
        name = alias.ALIAS_NAME
        if name:
            aliases.append(name)
    print(fixedRef, aliases)

for individual in individuals:
    aliases = []
    fixedRef = individual.REFERENCE_NUMBER
    if individual.DELISTED_ON:
        continue # don't include delisted entries
    name_parts = [individual.FIRST_NAME , individual.SECOND_NAME, individual.THIRD_NAME, individual.FOURTH_NAME]
    aliases.append(" ".join([part for part in name_parts if part]))
    for alias in individual.INDIVIDUAL_ALIAS:
        name = alias.ALIAS_NAME
        if name:
            aliases.append(name)
    print(fixedRef, aliases)
