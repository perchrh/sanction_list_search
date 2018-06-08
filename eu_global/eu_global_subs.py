#!/usr/bin/env python

#
# Generated Fri Jun  8 12:39:26 2018 by generateDS.py version 2.29.14.
# Python 3.6.4 (default, Mar  1 2018, 18:36:42)  [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)]
#
# Command line options:
#   ('-o', 'eu_global.py')
#   ('-s', 'eu_global_subs.py')
#
# Command line arguments:
#   schema_1_1.xsd
#
# Command line:
#   ../generateDS.py -o "eu_global.py" -s "eu_global_subs.py" schema_1_1.xsd
#
# Current working directory (os.getcwd()):
#   eu_global
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class ExportTypeSub(supermod.ExportType):
    def __init__(self, generationDate=None, globalFileId=None, sanctionEntity=None):
        super(ExportTypeSub, self).__init__(generationDate, globalFileId, sanctionEntity, )
supermod.ExportType.subclass = ExportTypeSub
# end class ExportTypeSub


class OperableTypeSub(supermod.OperableType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, extensiontype_=None):
        super(OperableTypeSub, self).__init__(logicalId, remark, additionalInformation, extensiontype_, )
supermod.OperableType.subclass = OperableTypeSub
# end class OperableTypeSub


class RegulationTypeSub(supermod.RegulationType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationType=None, organisationType=None, publicationDate=None, entryIntoForceDate=None, numberTitle=None, programme=None, publicationUrl=None, corrigendum=None):
        super(RegulationTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationType, organisationType, publicationDate, entryIntoForceDate, numberTitle, programme, publicationUrl, corrigendum, )
supermod.RegulationType.subclass = RegulationTypeSub
# end class RegulationTypeSub


class RegulationSummaryTypeSub(supermod.RegulationSummaryType):
    def __init__(self, regulationType=None, publicationDate=None, numberTitle=None, publicationUrl=None):
        super(RegulationSummaryTypeSub, self).__init__(regulationType, publicationDate, numberTitle, publicationUrl, )
supermod.RegulationSummaryType.subclass = RegulationSummaryTypeSub
# end class RegulationSummaryTypeSub


class SanctionEntityTypeSub(supermod.SanctionEntityType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, delistingDate=None, designationDate=None, designationDetails=None, unitedNationId=None, euReferenceNumber=None, regulation=None, subjectType=None, nameAlias=None, citizenship=None, birthdate=None, address=None, identification=None):
        super(SanctionEntityTypeSub, self).__init__(logicalId, remark, additionalInformation, delistingDate, designationDate, designationDetails, unitedNationId, euReferenceNumber, regulation, subjectType, nameAlias, citizenship, birthdate, address, identification, )
supermod.SanctionEntityType.subclass = SanctionEntityTypeSub
# end class SanctionEntityTypeSub


class SubjectTypeTypeSub(supermod.SubjectTypeType):
    def __init__(self, code=None, classificationCode=None):
        super(SubjectTypeTypeSub, self).__init__(code, classificationCode, )
supermod.SubjectTypeType.subclass = SubjectTypeTypeSub
# end class SubjectTypeTypeSub


class SanctionableTypeSub(supermod.SanctionableType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, extensiontype_=None):
        super(SanctionableTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, extensiontype_, )
supermod.SanctionableType.subclass = SanctionableTypeSub
# end class SanctionableTypeSub


class NameAliasTypeSub(supermod.NameAliasType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, firstName=None, middleName=None, lastName=None, wholeName=None, function=None, gender=None, title=None, nameLanguage=None, strong=None):
        super(NameAliasTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, firstName, middleName, lastName, wholeName, function, gender, title, nameLanguage, strong, )
supermod.NameAliasType.subclass = NameAliasTypeSub
# end class NameAliasTypeSub


class CitizenshipTypeSub(supermod.CitizenshipType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, acquisitionDate=None, disenfranchisementDate=None, region=None, countryIso2Code=None, countryDescription=None):
        super(CitizenshipTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, acquisitionDate, disenfranchisementDate, region, countryIso2Code, countryDescription, )
supermod.CitizenshipType.subclass = CitizenshipTypeSub
# end class CitizenshipTypeSub


class BirthdateTypeSub(supermod.BirthdateType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, circa=None, calendarType=None, city=None, zipCode=None, birthdate=None, dayOfMonth=None, monthOfYear=None, year=None, yearRangeFrom=None, yearRangeTo=None, region=None, place=None, countryIso2Code=None, countryDescription=None):
        super(BirthdateTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, circa, calendarType, city, zipCode, birthdate, dayOfMonth, monthOfYear, year, yearRangeFrom, yearRangeTo, region, place, countryIso2Code, countryDescription, )
supermod.BirthdateType.subclass = BirthdateTypeSub
# end class BirthdateTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, city=None, street=None, poBox=None, zipCode=None, region=None, place=None, asAtListingTime=None, countryIso2Code=None, countryDescription=None, contactInfo=None):
        super(AddressTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, city, street, poBox, zipCode, region, place, asAtListingTime, countryIso2Code, countryDescription, contactInfo, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class IdentificationTypeSub(supermod.IdentificationType):
    def __init__(self, logicalId=None, remark=None, additionalInformation=None, regulationLanguage=None, regulationSummary=None, diplomatic=None, knownExpired=None, knownFalse=None, reportedLost=None, revokedByIssuer=None, issueDate=None, issuedBy=None, latinNumber=None, nameOnDocument=None, number=None, validFrom=None, validTo=None, region=None, identificationTypeCode=None, identificationTypeDescription=None, countryIso2Code=None, countryDescription=None):
        super(IdentificationTypeSub, self).__init__(logicalId, remark, additionalInformation, regulationLanguage, regulationSummary, diplomatic, knownExpired, knownFalse, reportedLost, revokedByIssuer, issueDate, issuedBy, latinNumber, nameOnDocument, number, validFrom, validTo, region, identificationTypeCode, identificationTypeDescription, countryIso2Code, countryDescription, )
supermod.IdentificationType.subclass = IdentificationTypeSub
# end class IdentificationTypeSub


class AdditionalInfoTypeSub(supermod.AdditionalInfoType):
    def __init__(self, key=None, value=None):
        super(AdditionalInfoTypeSub, self).__init__(key, value, )
supermod.AdditionalInfoType.subclass = AdditionalInfoTypeSub
# end class AdditionalInfoTypeSub


class ContactInfoTypeSub(supermod.ContactInfoType):
    def __init__(self, key=None, value=None):
        super(ContactInfoTypeSub, self).__init__(key, value, )
supermod.ContactInfoType.subclass = ContactInfoTypeSub
# end class ContactInfoTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExportType'
        rootClass = supermod.ExportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:fsdexport="http://eu.europa.ec/fpi/fsd/export"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExportType'
        rootClass = supermod.ExportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExportType'
        rootClass = supermod.ExportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:fsdexport="http://eu.europa.ec/fpi/fsd/export"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ExportType'
        rootClass = supermod.ExportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
