#!/usr/bin/env python3

from timeit import default_timer as timer
from dataobjects import NamePart
from dataobjects import NameAlias
from datetime import datetime

def datePeriodPrinter(DatePeriod):
    start_date_from = create_single_date(DatePeriod.Start.From)
    start_date_to = create_single_date(DatePeriod.Start.To)

    end_date_from = create_single_date(DatePeriod.End.From)
    end_date_to = create_single_date(DatePeriod.End.To)

    if start_date_from == start_date_to:
        if end_date_from == end_date_to:
            if start_date_from == end_date_from:
                return start_date_from # all values equal, this is a single exact date
            else:
                # TODO ranges not supported
                return None #(start_date_from, end_date_from) # equal pairs
    else:
        # TODO ranges not supported
        # what is this case supposed to represent? that the whole year is included?
        #values = [start_date_from, start_date_to, end_date_to, end_date_from]
        #return tuple(values)
        return None


def create_single_date(date):
    month = date.Month.valueOf_
    day = date.Day.valueOf_
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day

    return datetime.strptime("{} {} {}".format(date.Year.valueOf_, month, day), '%Y %m %d')


import sdn

def load_sanctions(cons_filename, sdn_filename):
    consolidated_list = sdn.parse(cons_filename, silence=True)
    sdn_list = sdn.parse(sdn_filename, silence=True)

    id_to_name_entities = {}
    id_to_name_persons = {}

    sources = [consolidated_list, sdn_list]
    for sanction_list in sources:
        multiple_date_counter = 0

        sanctioned_parties = sanction_list.DistinctParties.get_DistinctParty()

        number_of_parties = len(sanctioned_parties)

        print("Number of sanctioned parties in OFAC list is", number_of_parties)

        # print person names in list

        persons = []
        entities = []

        for party in sanctioned_parties:
            name_aliases = []
            date_aliases = []
            for profile in party.Profile:
                for feature in profile.Feature:
                    if feature.FeatureTypeID == 8:  # birthdate
                        for version in feature.FeatureVersion:
                            # there is currently never more than one version in the list, and its unclear how versions are to be marked current and outdated
                            if version.ReliabilityID == 1561:  # 1561 means it's been proven false, so skip it
                                continue

                            for period in version.DatePeriod:
                                date_aliases.append(period)
                for identity in profile.Identity:
                    for alias in identity.Alias:
                        if alias.LowQuality == False: # TODO include these too, but mark them as bad
                            for name in alias.DocumentedName:
                                parts = [] #TODO modify
                                for namepart in name.DocumentedNamePart:
                                    namepart_value = namepart.NamePartValue
                                    if namepart_value.ScriptID == 215:  # our input is latin only, so we match against latin only
                                        namevalue = namepart_value.valueOf_
                                        parts.append(namevalue) #TODO modify
                                if parts:
                                    name_aliases.append(parts) # TODO modify

            if name_aliases:
                if profile.PartySubTypeID == 4:  # person
                    dates = [datePeriodPrinter(d) for d in date_aliases]
                    date_prints = [d.strftime("%Y-%m-%d") for d in dates if d]

                    persons.append((party.FixedRef, name_aliases, date_prints))
                else:  # not a person
                    entities.append((party.FixedRef, name_aliases))
    for item in entities:
        print(item)

    for item in persons:
        print(item)


def printSubjects(bin_to_id):
    for reference, names in bin_to_id.items():
        print(reference, names)


if __name__ == "__main__":
    start = timer()

    #(id_to_name_persons, id_to_name_entities) = load_sanctions('cons_advanced.xml', 'sdn_advanced.xml')
    load_sanctions('cons_advanced.xml', 'sdn_advanced.xml')

    end = timer()
    print("Total time usage for loading: {} ms".format(int(10 ** 3 * (end - start) + 0.5)))
    #print("Loaded {} entities and {} persons".format(len(id_to_name_entities), len(id_to_name_persons)))

    #printSubjects(id_to_name_entities)
    #printSubjects(id_to_name_persons)
