#!/usr/bin/env python3

import un_global
sanctions = un_global.parse('consolidated.xml', silence=True)

entities = sanctions.ENTITIES.ENTITY
individuals = sanctions.INDIVIDUALS.INDIVIDUAL

for entity in entities:
    aliases = []
    fixedRef = entity.REFERENCE_NUMBER.strip()
    if entity.DELISTED_ON:
        continue # don't include delisted entries

    aliases.append(entity.FIRST_NAME)
    for alias in entity.ENTITY_ALIAS:
        if alias.QUALITY == 'Low':
            continue #skip these for now
            
        name = alias.ALIAS_NAME
        if name:
            aliases.append(name)
    print(fixedRef, aliases)

for individual in individuals:
    aliases = set()
    fixedRef = individual.REFERENCE_NUMBER.strip()
    if individual.DELISTED_ON:
        continue # don't include delisted entries

    name_parts = [individual.FIRST_NAME , individual.SECOND_NAME, individual.THIRD_NAME, individual.FOURTH_NAME]
    name = " ".join([part for part in name_parts if part])
    aliases.add(name)
    for alias in individual.INDIVIDUAL_ALIAS:
        if alias.QUALITY == 'Low':
            continue #skip these for now

        alias_names = alias.ALIAS_NAME
        alias_names = " ".join(alias_names.split()) #remove white-space and linebreaks
        if alias_names:
            alias_list = alias_names.split(";")
            for item in alias_list: aliases.add(item)

    print(fixedRef, aliases)
