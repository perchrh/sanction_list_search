#!/usr/bin/env python3

import sdn
consolidated_list = sdn.parse('cons_advanced.xml', silence=True)
sdn_list = sdn.parse('sdn_advanced.xml', silence=True)


for sanction_list in [consolidated_list, sdn_list]:
    sanctioned_parties = sanction_list.DistinctParties.get_DistinctParty()

    number_of_parties = len(sanctioned_parties)

    print("Number of sanctioned parties in OFAC list is", number_of_parties)

    # print person names in list 

    for party in sanctioned_parties:
        for profile in party.Profile:
            if profile.PartySubTypeID == 4: # consider only persons for now
                for identity in profile.Identity:
                    for alias in identity.Alias:
                        for name in alias.DocumentedName:
                            parts = []
                            for namepart in name.DocumentedNamePart:
                                namepart_value = namepart.NamePartValue
                                namevalue = namepart_value.get_valueOf_()
                                parts.append(namevalue)
                            print(party.FixedRef, parts)
                print("") # new line

