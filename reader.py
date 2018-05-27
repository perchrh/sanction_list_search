#!/usr/bin/env python3

import sdn
rootObject = sdn.parse('cons_advanced.xml', silence=True)

sanctioned_parties = rootObject.DistinctParties.get_DistinctParty()

number_of_parties = len(sanctioned_parties)

print("Number of sanctioned parties in OFAC consolidated sanctions list is", number_of_parties)

# test av party 0

for party in sanctioned_parties:
    for profile in party.Profile:
        if profile.PartySubTypeID == 4:
            for identity in profile.Identity:
                for alias in identity.Alias:
                    for name in alias.DocumentedName:
                        for namepart in name.DocumentedNamePart:
                            value = namepart.NamePartValue
                            namevalue = value.get_valueOf_()
                            print(namevalue)

