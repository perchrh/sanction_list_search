#!/usr/bin/env python

#
# Generated Fri Jun  8 13:08:16 2018 by generateDS.py version 2.29.14.
# Python 3.6.4 (default, Mar  1 2018, 18:36:42)  [GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)]
#
# Command line options:
#   ('-o', 'un_global.py')
#   ('-s', 'un_global_subs.py')
#
# Command line arguments:
#   sc-sanctions.xsd
#
# Command line:
#   ../generateDS.py -o "un_global.py" -s "un_global_subs.py" sc-sanctions.xsd
#
# Current working directory (os.getcwd()):
#   un_global
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


class CONSOLIDATED_LISTSub(supermod.CONSOLIDATED_LIST):
    def __init__(self, dateGenerated=None, INDIVIDUALS=None, ENTITIES=None):
        super(CONSOLIDATED_LISTSub, self).__init__(dateGenerated, INDIVIDUALS, ENTITIES, )
supermod.CONSOLIDATED_LIST.subclass = CONSOLIDATED_LISTSub
# end class CONSOLIDATED_LISTSub


class INDIVIDUALSSub(supermod.INDIVIDUALS):
    def __init__(self, INDIVIDUAL=None):
        super(INDIVIDUALSSub, self).__init__(INDIVIDUAL, )
supermod.INDIVIDUALS.subclass = INDIVIDUALSSub
# end class INDIVIDUALSSub


class INDIVIDUALSub(supermod.INDIVIDUAL):
    def __init__(self, DATAID=None, VERSIONNUM=None, FIRST_NAME=None, SECOND_NAME=None, THIRD_NAME=None, FOURTH_NAME=None, UN_LIST_TYPE=None, REFERENCE_NUMBER=None, LISTED_ON=None, GENDER=None, SUBMITTED_BY=None, NAME_ORIGINAL_SCRIPT=None, COMMENTS1=None, NATIONALITY2=None, TITLE=None, DESIGNATION=None, NATIONALITY=None, LIST_TYPE=None, LAST_DAY_UPDATED=None, INDIVIDUAL_ALIAS=None, INDIVIDUAL_ADDRESS=None, INDIVIDUAL_DATE_OF_BIRTH=None, INDIVIDUAL_PLACE_OF_BIRTH=None, INDIVIDUAL_DOCUMENT=None, SORT_KEY=None, SORT_KEY_LAST_MOD=None, DELISTED_ON=None):
        super(INDIVIDUALSub, self).__init__(DATAID, VERSIONNUM, FIRST_NAME, SECOND_NAME, THIRD_NAME, FOURTH_NAME, UN_LIST_TYPE, REFERENCE_NUMBER, LISTED_ON, GENDER, SUBMITTED_BY, NAME_ORIGINAL_SCRIPT, COMMENTS1, NATIONALITY2, TITLE, DESIGNATION, NATIONALITY, LIST_TYPE, LAST_DAY_UPDATED, INDIVIDUAL_ALIAS, INDIVIDUAL_ADDRESS, INDIVIDUAL_DATE_OF_BIRTH, INDIVIDUAL_PLACE_OF_BIRTH, INDIVIDUAL_DOCUMENT, SORT_KEY, SORT_KEY_LAST_MOD, DELISTED_ON, )
supermod.INDIVIDUAL.subclass = INDIVIDUALSub
# end class INDIVIDUALSub


class TITLESub(supermod.TITLE):
    def __init__(self, VALUE=None):
        super(TITLESub, self).__init__(VALUE, )
supermod.TITLE.subclass = TITLESub
# end class TITLESub


class DESIGNATIONSub(supermod.DESIGNATION):
    def __init__(self, VALUE=None):
        super(DESIGNATIONSub, self).__init__(VALUE, )
supermod.DESIGNATION.subclass = DESIGNATIONSub
# end class DESIGNATIONSub


class NATIONALITYSub(supermod.NATIONALITY):
    def __init__(self, VALUE=None):
        super(NATIONALITYSub, self).__init__(VALUE, )
supermod.NATIONALITY.subclass = NATIONALITYSub
# end class NATIONALITYSub


class INDIVIDUAL_ALIASSub(supermod.INDIVIDUAL_ALIAS):
    def __init__(self, QUALITY=None, ALIAS_NAME=None, DATE_OF_BIRTH=None, CITY_OF_BIRTH=None, COUNTRY_OF_BIRTH=None, NOTE=None):
        super(INDIVIDUAL_ALIASSub, self).__init__(QUALITY, ALIAS_NAME, DATE_OF_BIRTH, CITY_OF_BIRTH, COUNTRY_OF_BIRTH, NOTE, )
supermod.INDIVIDUAL_ALIAS.subclass = INDIVIDUAL_ALIASSub
# end class INDIVIDUAL_ALIASSub


class INDIVIDUAL_ADDRESSSub(supermod.INDIVIDUAL_ADDRESS):
    def __init__(self, STREET=None, CITY=None, STATE_PROVINCE=None, ZIP_CODE=None, COUNTRY=None, NOTE=None):
        super(INDIVIDUAL_ADDRESSSub, self).__init__(STREET, CITY, STATE_PROVINCE, ZIP_CODE, COUNTRY, NOTE, )
supermod.INDIVIDUAL_ADDRESS.subclass = INDIVIDUAL_ADDRESSSub
# end class INDIVIDUAL_ADDRESSSub


class INDIVIDUAL_DATE_OF_BIRTHSub(supermod.INDIVIDUAL_DATE_OF_BIRTH):
    def __init__(self, TYPE_OF_DATE=None, NOTE=None, DATE=None, YEAR=None, FROM_YEAR=None, TO_YEAR=None):
        super(INDIVIDUAL_DATE_OF_BIRTHSub, self).__init__(TYPE_OF_DATE, NOTE, DATE, YEAR, FROM_YEAR, TO_YEAR, )
supermod.INDIVIDUAL_DATE_OF_BIRTH.subclass = INDIVIDUAL_DATE_OF_BIRTHSub
# end class INDIVIDUAL_DATE_OF_BIRTHSub


class INDIVIDUAL_PLACE_OF_BIRTHSub(supermod.INDIVIDUAL_PLACE_OF_BIRTH):
    def __init__(self, CITY=None, STATE_PROVINCE=None, COUNTRY=None, NOTE=None):
        super(INDIVIDUAL_PLACE_OF_BIRTHSub, self).__init__(CITY, STATE_PROVINCE, COUNTRY, NOTE, )
supermod.INDIVIDUAL_PLACE_OF_BIRTH.subclass = INDIVIDUAL_PLACE_OF_BIRTHSub
# end class INDIVIDUAL_PLACE_OF_BIRTHSub


class INDIVIDUAL_DOCUMENTSub(supermod.INDIVIDUAL_DOCUMENT):
    def __init__(self, TYPE_OF_DOCUMENT=None, TYPE_OF_DOCUMENT2=None, NUMBER=None, ISSUING_COUNTRY=None, DATE_OF_ISSUE=None, CITY_OF_ISSUE=None, COUNTRY_OF_ISSUE=None, NOTE=None):
        super(INDIVIDUAL_DOCUMENTSub, self).__init__(TYPE_OF_DOCUMENT, TYPE_OF_DOCUMENT2, NUMBER, ISSUING_COUNTRY, DATE_OF_ISSUE, CITY_OF_ISSUE, COUNTRY_OF_ISSUE, NOTE, )
supermod.INDIVIDUAL_DOCUMENT.subclass = INDIVIDUAL_DOCUMENTSub
# end class INDIVIDUAL_DOCUMENTSub


class ENTITIESSub(supermod.ENTITIES):
    def __init__(self, ENTITY=None, valueOf_=None):
        super(ENTITIESSub, self).__init__(ENTITY, )
supermod.ENTITIES.subclass = ENTITIESSub
# end class ENTITIESSub


class ENTITYSub(supermod.ENTITY):
    def __init__(self, DATAID=None, VERSIONNUM=None, FIRST_NAME=None, UN_LIST_TYPE=None, REFERENCE_NUMBER=None, LISTED_ON=None, SUBMITTED_ON=None, NAME_ORIGINAL_SCRIPT=None, COMMENTS1=None, LIST_TYPE=None, LAST_DAY_UPDATED=None, ENTITY_ALIAS=None, ENTITY_ADDRESS=None, SORT_KEY=None, SORT_KEY_LAST_MOD=None, DELISTED_ON=None, valueOf_=None):
        super(ENTITYSub, self).__init__(DATAID, VERSIONNUM, FIRST_NAME, UN_LIST_TYPE, REFERENCE_NUMBER, LISTED_ON, SUBMITTED_ON, NAME_ORIGINAL_SCRIPT, COMMENTS1, LIST_TYPE, LAST_DAY_UPDATED, ENTITY_ALIAS, ENTITY_ADDRESS, SORT_KEY, SORT_KEY_LAST_MOD, DELISTED_ON, )
supermod.ENTITY.subclass = ENTITYSub
# end class ENTITYSub


class ENTITY_ALIASSub(supermod.ENTITY_ALIAS):
    def __init__(self, QUALITY=None, ALIAS_NAME=None):
        super(ENTITY_ALIASSub, self).__init__(QUALITY, ALIAS_NAME, )
supermod.ENTITY_ALIAS.subclass = ENTITY_ALIASSub
# end class ENTITY_ALIASSub


class ENTITY_ADDRESSSub(supermod.ENTITY_ADDRESS):
    def __init__(self, STREET=None, CITY=None, STATE_PROVINCE=None, ZIP_CODE=None, COUNTRY=None, NOTE=None):
        super(ENTITY_ADDRESSSub, self).__init__(STREET, CITY, STATE_PROVINCE, ZIP_CODE, COUNTRY, NOTE, )
supermod.ENTITY_ADDRESS.subclass = ENTITY_ADDRESSSub
# end class ENTITY_ADDRESSSub


class LIST_TYPESub(supermod.LIST_TYPE):
    def __init__(self, VALUE=None):
        super(LIST_TYPESub, self).__init__(VALUE, )
supermod.LIST_TYPE.subclass = LIST_TYPESub
# end class LIST_TYPESub


class LAST_DAY_UPDATEDSub(supermod.LAST_DAY_UPDATED):
    def __init__(self, VALUE=None):
        super(LAST_DAY_UPDATEDSub, self).__init__(VALUE, )
supermod.LAST_DAY_UPDATED.subclass = LAST_DAY_UPDATEDSub
# end class LAST_DAY_UPDATEDSub


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
        rootTag = 'CONSOLIDATED_LIST'
        rootClass = supermod.CONSOLIDATED_LIST
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CONSOLIDATED_LIST'
        rootClass = supermod.CONSOLIDATED_LIST
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
        rootTag = 'CONSOLIDATED_LIST'
        rootClass = supermod.CONSOLIDATED_LIST
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CONSOLIDATED_LIST'
        rootClass = supermod.CONSOLIDATED_LIST
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
