#!/usr/bin/env python3

import sdn

consolidated_list = sdn.parse('cons_advanced.xml', silence=True)
sdn_list = sdn.parse('sdn_advanced.xml', silence=True)

sources = [consolidated_list, sdn_list]
for sanction_list in sources:
    sanctioned_parties = sanction_list.DistinctParties.get_DistinctParty()

    number_of_parties = len(sanctioned_parties)

    print("Number of sanctioned parties in OFAC list is", number_of_parties)

    # print person names in list

    for party in sanctioned_parties:
        name_aliases = []
        for profile in party.Profile:
            if profile.PartySubTypeID == 4:  # consider only persons for now
                for identity in profile.Identity:
                    for alias in identity.Alias:
                        if alias.LowQuality == False:
                            for name in alias.DocumentedName:
                                if name.DocNameStatusID == 1:  # primary latin alphabet
                                    parts = []
                                    for namepart in name.DocumentedNamePart:
                                        namepart_value = namepart.NamePartValue
                                        namevalue = namepart_value.get_valueOf_()
                                        parts.append(namevalue)
                                    if parts:
                                        name_aliases.append(parts)
        if name_aliases:
            print(party.FixedRef, name_aliases)
