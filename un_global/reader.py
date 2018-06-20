#!/usr/bin/env python3

import un_global

sanctions = un_global.parse('consolidated.xml', silence=True)

entities = sanctions.ENTITIES.ENTITY
individuals = sanctions.INDIVIDUALS.INDIVIDUAL

for entity in entities:
    if entity.DELISTED_ON:
        continue  # don't include delisted entries

    fixedRef = entity.REFERENCE_NUMBER.strip()

    name_aliases = []
    name_aliases.append(" ".join(entity.FIRST_NAME.split()).strip()) # companies have only first names in list
    for alias in entity.ENTITY_ALIAS:
        if alias.QUALITY == 'Low':
            continue  # skip these for now

        name = alias.ALIAS_NAME
        name = " ".join(name.split())  # remove white-space and linebreaks
        if name:
            name_aliases.append(name)
    print(fixedRef, name_aliases)

multiple_dates = 0
for individual in individuals:
    if individual.DELISTED_ON:
        continue  # don't include delisted entries

    fixedRef = individual.REFERENCE_NUMBER.strip()
    name_aliases = set()

    name_parts = [individual.FIRST_NAME, individual.SECOND_NAME, individual.THIRD_NAME, individual.FOURTH_NAME]
    name_parts = [" ".join(name.split()) for name in name_parts if name]  # remove white-space and linebreaks
    name = " ".join(name_parts)
    name_aliases.add(name)

    date_aliases = set()
    for date_of_birth in individual.INDIVIDUAL_DATE_OF_BIRTH:
        if (date_of_birth.DATE):
            date_aliases.add(date_of_birth.DATE)

    for alias in individual.INDIVIDUAL_ALIAS:
        if alias.QUALITY == 'Low':
            continue  # skip these for now

        alias_names = alias.ALIAS_NAME
        alias_names = " ".join(alias_names.split())  # remove white-space and linebreaks
        if alias_names:
            alias_list = alias_names.split(";")
            for item in alias_list: name_aliases.add(item)

    if len(date_aliases) > 1:
        multiple_dates = multiple_dates + 1
    print(fixedRef, name_aliases, [d.strftime("%Y-%m-%d") for d in date_aliases])

print("Found", multiple_dates, "entries with multiple exact dates", 100.0*multiple_dates/len(individuals), "%")
