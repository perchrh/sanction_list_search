#!/usr/bin/env python3

import eu_global

sanctions = eu_global.parse('eu_global_full_20180604.xml', silence=True)

for entity in sanctions.sanctionEntity:
    fixedRef = entity.logicalId
    aliases = []
    for alias in entity.nameAlias:
        if not alias.strong == 'true':  # filter for now
            continue
        name = alias.wholeName
        aliases.append(name)
    print(fixedRef, aliases)
