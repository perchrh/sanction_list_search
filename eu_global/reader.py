#!/usr/bin/env python3

import eu_global

sanctions = eu_global.parse('eu_global_full_20180604.xml', silence=True)

id_to_name = {}
for entity in sanctions.sanctionEntity:
    fixedRef = entity.logicalId
    aliases = []
    for alias in entity.nameAlias:
        if not alias.strong == 'true':  # filter for now
            continue
        name = alias.wholeName
        aliases.append(name)
    id_to_name[fixedRef] = aliases

for reference, names in id_to_name.items():
    print(reference, names)

# phonetic bin computation, WIP:

import fuzzy
import unicodedata
import string

dmeta = fuzzy.DMetaphone()

bin_to_id = {}
for reference, names in id_to_name.items():
    unique = set()
    for name in names:
        for name_part in name.split():
            normalized_name = name_part.lower()
            normalized_name.replace("-", " ").replace("'", " ").replace("’", " ")
            normalized_name = ''.join(x for x in unicodedata.normalize('NFKD', normalized_name) if x in string.printable)
            unique.add(normalized_name)

    for name_part in unique:
        if len(name_part) < 4:
            continue # FIXME refine this restriction, only certain of the short words should be excluded
        bins = []
        try:
            bins = dmeta(name_part)
        except UnicodeEncodeError:
            continue  # FIXME ignores non-latin words silently

        for bin in bins:
            if not bin in bin_to_id:
                bin_to_id[bin] = []

            bin_to_id[bin].append(reference)


for bin, references in bin_to_id.items():
    print(bin, references)

print("Computed", len(bin_to_id), "phonetic bins for", len(id_to_name), "list entries.")
