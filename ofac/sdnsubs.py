#!/usr/bin/env python

#
# Generated Sun May 27 20:05:59 2018 by generateDS.py version 2.29.14.
# Python 3.6.5 (default, Apr  1 2018, 05:46:30)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'sdn.py')
#   ('-s', 'sdnsubs.py')
#
# Command line arguments:
#   sdn_advanced.xsd
#
# Command line:
#   generateDS.py -o "sdn.py" -s "sdnsubs.py" sdn_advanced.xsd
#
# Current working directory (os.getcwd()):
#   consolidated_ofac_list
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


class SanctionsSub(supermod.Sanctions):
    def __init__(self, Version=None, DeltaBaseVersion=None, DateOfIssue=None, ReferenceValueSets=None, Locations=None, IDRegDocuments=None, DistinctParties=None, ProfileRelationships=None, SanctionsEntries=None, SanctionsEntryLinks=None):
        super(SanctionsSub, self).__init__(Version, DeltaBaseVersion, DateOfIssue, ReferenceValueSets, Locations, IDRegDocuments, DistinctParties, ProfileRelationships, SanctionsEntries, SanctionsEntryLinks, )
supermod.Sanctions.subclass = SanctionsSub
# end class SanctionsSub


class CommentSub(supermod.Comment):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(CommentSub, self).__init__(DeltaAction, valueOf_, )
supermod.Comment.subclass = CommentSub
# end class CommentSub


class FeatureVersionReferenceSub(supermod.FeatureVersionReference):
    def __init__(self, FeatureVersionID=None, DeltaAction=None):
        super(FeatureVersionReferenceSub, self).__init__(FeatureVersionID, DeltaAction, )
supermod.FeatureVersionReference.subclass = FeatureVersionReferenceSub
# end class FeatureVersionReferenceSub


class IDRegDocumentReferenceSub(supermod.IDRegDocumentReference):
    def __init__(self, IDRegDocumentID=None, DeltaAction=None):
        super(IDRegDocumentReferenceSub, self).__init__(IDRegDocumentID, DeltaAction, )
supermod.IDRegDocumentReference.subclass = IDRegDocumentReferenceSub
# end class IDRegDocumentReferenceSub


class ProfileRelationshipReferenceSub(supermod.ProfileRelationshipReference):
    def __init__(self, ProfileRelationshipID=None, DeltaAction=None):
        super(ProfileRelationshipReferenceSub, self).__init__(ProfileRelationshipID, DeltaAction, )
supermod.ProfileRelationshipReference.subclass = ProfileRelationshipReferenceSub
# end class ProfileRelationshipReferenceSub


class DatePeriodSub(supermod.DatePeriod):
    def __init__(self, CalendarTypeID=None, YearFixed=None, MonthFixed=None, DayFixed=None, DeltaAction=None, Comment=None, Start=None, End=None, DurationMinimum=None, DurationMaximum=None):
        super(DatePeriodSub, self).__init__(CalendarTypeID, YearFixed, MonthFixed, DayFixed, DeltaAction, Comment, Start, End, DurationMinimum, DurationMaximum, )
supermod.DatePeriod.subclass = DatePeriodSub
# end class DatePeriodSub


class DirectURLSub(supermod.DirectURL):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(DirectURLSub, self).__init__(DeltaAction, valueOf_, )
supermod.DirectURL.subclass = DirectURLSub
# end class DirectURLSub


class YearSub(supermod.Year):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(YearSub, self).__init__(DeltaAction, valueOf_, )
supermod.Year.subclass = YearSub
# end class YearSub


class MonthSub(supermod.Month):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(MonthSub, self).__init__(DeltaAction, valueOf_, )
supermod.Month.subclass = MonthSub
# end class MonthSub


class DaySub(supermod.Day):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(DaySub, self).__init__(DeltaAction, valueOf_, )
supermod.Day.subclass = DaySub
# end class DaySub


class ReferenceValueSetsSchemaTypeSub(supermod.ReferenceValueSetsSchemaType):
    def __init__(self, AliasTypeValues=None, AreaCodeValues=None, AreaCodeTypeValues=None, CalendarTypeValues=None, CountryValues=None, CountryRelevanceValues=None, DecisionMakingBodyValues=None, DetailReferenceValues=None, DetailTypeValues=None, DocNameStatusValues=None, EntryEventTypeValues=None, EntryLinkTypeValues=None, ExRefTypeValues=None, FeatureTypeValues=None, FeatureTypeGroupValues=None, IDRegDocDateTypeValues=None, IDRegDocTypeValues=None, IdentityFeatureLinkTypeValues=None, LegalBasisValues=None, LegalBasisTypeValues=None, ListValues=None, LocPartTypeValues=None, LocPartValueStatusValues=None, LocPartValueTypeValues=None, NamePartTypeValues=None, OrganisationValues=None, PartySubTypeValues=None, PartyTypeValues=None, RelationQualityValues=None, RelationTypeValues=None, ReliabilityValues=None, SanctionsProgramValues=None, SanctionsTypeValues=None, ScriptValues=None, ScriptStatusValues=None, SubsidiaryBodyValues=None, SupInfoTypeValues=None, TargetTypeValues=None, ValidityValues=None):
        super(ReferenceValueSetsSchemaTypeSub, self).__init__(AliasTypeValues, AreaCodeValues, AreaCodeTypeValues, CalendarTypeValues, CountryValues, CountryRelevanceValues, DecisionMakingBodyValues, DetailReferenceValues, DetailTypeValues, DocNameStatusValues, EntryEventTypeValues, EntryLinkTypeValues, ExRefTypeValues, FeatureTypeValues, FeatureTypeGroupValues, IDRegDocDateTypeValues, IDRegDocTypeValues, IdentityFeatureLinkTypeValues, LegalBasisValues, LegalBasisTypeValues, ListValues, LocPartTypeValues, LocPartValueStatusValues, LocPartValueTypeValues, NamePartTypeValues, OrganisationValues, PartySubTypeValues, PartyTypeValues, RelationQualityValues, RelationTypeValues, ReliabilityValues, SanctionsProgramValues, SanctionsTypeValues, ScriptValues, ScriptStatusValues, SubsidiaryBodyValues, SupInfoTypeValues, TargetTypeValues, ValidityValues, )
supermod.ReferenceValueSetsSchemaType.subclass = ReferenceValueSetsSchemaTypeSub
# end class ReferenceValueSetsSchemaTypeSub


class DateBoundarySchemaTypeSub(supermod.DateBoundarySchemaType):
    def __init__(self, Approximate=None, YearFixed=None, MonthFixed=None, DayFixed=None, DeltaAction=None, From=None, To=None):
        super(DateBoundarySchemaTypeSub, self).__init__(Approximate, YearFixed, MonthFixed, DayFixed, DeltaAction, From, To, )
supermod.DateBoundarySchemaType.subclass = DateBoundarySchemaTypeSub
# end class DateBoundarySchemaTypeSub


class DatePointSchemaTypeSub(supermod.DatePointSchemaType):
    def __init__(self, DeltaAction=None, Year=None, Month=None, Day=None):
        super(DatePointSchemaTypeSub, self).__init__(DeltaAction, Year, Month, Day, )
supermod.DatePointSchemaType.subclass = DatePointSchemaTypeSub
# end class DatePointSchemaTypeSub


class DurationSchemaTypeSub(supermod.DurationSchemaType):
    def __init__(self, Approximate=None, DeltaAction=None, Years=None, Months=None, Days=None):
        super(DurationSchemaTypeSub, self).__init__(Approximate, DeltaAction, Years, Months, Days, )
supermod.DurationSchemaType.subclass = DurationSchemaTypeSub
# end class DurationSchemaTypeSub


class DateSchemaTypeSub(supermod.DateSchemaType):
    def __init__(self, CalendarTypeID=None, DeltaAction=None, Year=None, Month=None, Day=None):
        super(DateSchemaTypeSub, self).__init__(CalendarTypeID, DeltaAction, Year, Month, Day, )
supermod.DateSchemaType.subclass = DateSchemaTypeSub
# end class DateSchemaTypeSub


class LocationSchemaTypeSub(supermod.LocationSchemaType):
    def __init__(self, ID=None, DeltaAction=None, Comment=None, LocationAreaCode=None, LocationCountry=None, LocationPart=None, FeatureVersionReference=None, IDRegDocumentReference=None):
        super(LocationSchemaTypeSub, self).__init__(ID, DeltaAction, Comment, LocationAreaCode, LocationCountry, LocationPart, FeatureVersionReference, IDRegDocumentReference, )
supermod.LocationSchemaType.subclass = LocationSchemaTypeSub
# end class LocationSchemaTypeSub


class IDRegDocumentSchemaTypeSub(supermod.IDRegDocumentSchemaType):
    def __init__(self, ID=None, IDRegDocTypeID=None, IdentityID=None, IssuedBy_CountryID=None, IssuedIn_LocationID=None, ValidityID=None, DeltaAction=None, Comment=None, IDRegistrationNo=None, IssuingAuthority=None, DocumentDate=None, IDRegDocumentMention=None, FeatureVersionReference=None, DocumentedNameReference=None, ProfileRelationshipReference=None):
        super(IDRegDocumentSchemaTypeSub, self).__init__(ID, IDRegDocTypeID, IdentityID, IssuedBy_CountryID, IssuedIn_LocationID, ValidityID, DeltaAction, Comment, IDRegistrationNo, IssuingAuthority, DocumentDate, IDRegDocumentMention, FeatureVersionReference, DocumentedNameReference, ProfileRelationshipReference, )
supermod.IDRegDocumentSchemaType.subclass = IDRegDocumentSchemaTypeSub
# end class IDRegDocumentSchemaTypeSub


class DistinctPartySchemaTypeSub(supermod.DistinctPartySchemaType):
    def __init__(self, FixedRef=None, DeltaAction=None, Comment=None, Profile=None):
        super(DistinctPartySchemaTypeSub, self).__init__(FixedRef, DeltaAction, Comment, Profile, )
supermod.DistinctPartySchemaType.subclass = DistinctPartySchemaTypeSub
# end class DistinctPartySchemaTypeSub


class FeatureSchemaTypeSub(supermod.FeatureSchemaType):
    def __init__(self, ID=None, FeatureTypeID=None, DeltaAction=None, FeatureVersion=None, IdentityReference=None):
        super(FeatureSchemaTypeSub, self).__init__(ID, FeatureTypeID, DeltaAction, FeatureVersion, IdentityReference, )
supermod.FeatureSchemaType.subclass = FeatureSchemaTypeSub
# end class FeatureSchemaTypeSub


class IdentitySchemaTypeSub(supermod.IdentitySchemaType):
    def __init__(self, ID=None, FixedRef=None, Primary=None, False_=None, DeltaAction=None, Comment=None, Alias=None, NamePartGroups=None, IDRegDocumentReference=None):
        super(IdentitySchemaTypeSub, self).__init__(ID, FixedRef, Primary, False_, DeltaAction, Comment, Alias, NamePartGroups, IDRegDocumentReference, )
supermod.IdentitySchemaType.subclass = IdentitySchemaTypeSub
# end class IdentitySchemaTypeSub


class DocumentedNameSchemaTypeSub(supermod.DocumentedNameSchemaType):
    def __init__(self, ID=None, FixedRef=None, DocNameStatusID=None, DeltaAction=None, Comment=None, DocumentedNamePart=None, DocumentedNameCountry=None, IDRegDocumentReference=None):
        super(DocumentedNameSchemaTypeSub, self).__init__(ID, FixedRef, DocNameStatusID, DeltaAction, Comment, DocumentedNamePart, DocumentedNameCountry, IDRegDocumentReference, )
supermod.DocumentedNameSchemaType.subclass = DocumentedNameSchemaTypeSub
# end class DocumentedNameSchemaTypeSub


class ProfileRelationshipSchemaTypeSub(supermod.ProfileRelationshipSchemaType):
    def __init__(self, ID=None, From_ProfileID=None, To_ProfileID=None, RelationTypeID=None, RelationQualityID=None, Former=None, SanctionsEntryID=None, DeltaAction=None, Comment=None, DatePeriod=None, IDRegDocumentReference=None):
        super(ProfileRelationshipSchemaTypeSub, self).__init__(ID, From_ProfileID, To_ProfileID, RelationTypeID, RelationQualityID, Former, SanctionsEntryID, DeltaAction, Comment, DatePeriod, IDRegDocumentReference, )
supermod.ProfileRelationshipSchemaType.subclass = ProfileRelationshipSchemaTypeSub
# end class ProfileRelationshipSchemaTypeSub


class SanctionsEntrySchemaTypeSub(supermod.SanctionsEntrySchemaType):
    def __init__(self, ID=None, ProfileID=None, ListID=None, EntryProfileRef=None, EntryDeltaFlag=None, DeltaAction=None, Comment=None, LimitationsToListing=None, EntryEvent=None, SanctionsMeasure=None, SupportingInfo=None, ProfileRelationshipReference=None):
        super(SanctionsEntrySchemaTypeSub, self).__init__(ID, ProfileID, ListID, EntryProfileRef, EntryDeltaFlag, DeltaAction, Comment, LimitationsToListing, EntryEvent, SanctionsMeasure, SupportingInfo, ProfileRelationshipReference, )
supermod.SanctionsEntrySchemaType.subclass = SanctionsEntrySchemaTypeSub
# end class SanctionsEntrySchemaTypeSub


class SanctionsEntryLinkSchemaTypeSub(supermod.SanctionsEntryLinkSchemaType):
    def __init__(self, ID=None, EntryA_SanctionsEntryID=None, EntryB_SanctionsEntryID=None, EntryLinkTypeID=None, DeltaAction=None, Comment=None, Date=None):
        super(SanctionsEntryLinkSchemaTypeSub, self).__init__(ID, EntryA_SanctionsEntryID, EntryB_SanctionsEntryID, EntryLinkTypeID, DeltaAction, Comment, Date, )
supermod.SanctionsEntryLinkSchemaType.subclass = SanctionsEntryLinkSchemaTypeSub
# end class SanctionsEntryLinkSchemaTypeSub


class LocationsTypeSub(supermod.LocationsType):
    def __init__(self, Location=None):
        super(LocationsTypeSub, self).__init__(Location, )
supermod.LocationsType.subclass = LocationsTypeSub
# end class LocationsTypeSub


class IDRegDocumentsTypeSub(supermod.IDRegDocumentsType):
    def __init__(self, IDRegDocument=None):
        super(IDRegDocumentsTypeSub, self).__init__(IDRegDocument, )
supermod.IDRegDocumentsType.subclass = IDRegDocumentsTypeSub
# end class IDRegDocumentsTypeSub


class DistinctPartiesTypeSub(supermod.DistinctPartiesType):
    def __init__(self, DistinctParty=None):
        super(DistinctPartiesTypeSub, self).__init__(DistinctParty, )
supermod.DistinctPartiesType.subclass = DistinctPartiesTypeSub
# end class DistinctPartiesTypeSub


class ProfileRelationshipsTypeSub(supermod.ProfileRelationshipsType):
    def __init__(self, ProfileRelationship=None):
        super(ProfileRelationshipsTypeSub, self).__init__(ProfileRelationship, )
supermod.ProfileRelationshipsType.subclass = ProfileRelationshipsTypeSub
# end class ProfileRelationshipsTypeSub


class SanctionsEntriesTypeSub(supermod.SanctionsEntriesType):
    def __init__(self, SanctionsEntry=None):
        super(SanctionsEntriesTypeSub, self).__init__(SanctionsEntry, )
supermod.SanctionsEntriesType.subclass = SanctionsEntriesTypeSub
# end class SanctionsEntriesTypeSub


class SanctionsEntryLinksTypeSub(supermod.SanctionsEntryLinksType):
    def __init__(self, SanctionsEntryLink=None):
        super(SanctionsEntryLinksTypeSub, self).__init__(SanctionsEntryLink, )
supermod.SanctionsEntryLinksType.subclass = SanctionsEntryLinksTypeSub
# end class SanctionsEntryLinksTypeSub


class AliasTypeValuesTypeSub(supermod.AliasTypeValuesType):
    def __init__(self, AliasType=None):
        super(AliasTypeValuesTypeSub, self).__init__(AliasType, )
supermod.AliasTypeValuesType.subclass = AliasTypeValuesTypeSub
# end class AliasTypeValuesTypeSub


class AliasTypeTypeSub(supermod.AliasTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(AliasTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.AliasTypeType.subclass = AliasTypeTypeSub
# end class AliasTypeTypeSub


class AreaCodeValuesTypeSub(supermod.AreaCodeValuesType):
    def __init__(self, AreaCode=None):
        super(AreaCodeValuesTypeSub, self).__init__(AreaCode, )
supermod.AreaCodeValuesType.subclass = AreaCodeValuesTypeSub
# end class AreaCodeValuesTypeSub


class AreaCodeType1Sub(supermod.AreaCodeType1):
    def __init__(self, ID=None, CountryID=None, Description=None, AreaCodeTypeID=None, DeltaAction=None, valueOf_=None):
        super(AreaCodeType1Sub, self).__init__(ID, CountryID, Description, AreaCodeTypeID, DeltaAction, valueOf_, )
supermod.AreaCodeType1.subclass = AreaCodeType1Sub
# end class AreaCodeType1Sub


class AreaCodeTypeValuesTypeSub(supermod.AreaCodeTypeValuesType):
    def __init__(self, AreaCodeType=None):
        super(AreaCodeTypeValuesTypeSub, self).__init__(AreaCodeType, )
supermod.AreaCodeTypeValuesType.subclass = AreaCodeTypeValuesTypeSub
# end class AreaCodeTypeValuesTypeSub


class AreaCodeTypeTypeSub(supermod.AreaCodeTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(AreaCodeTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.AreaCodeTypeType.subclass = AreaCodeTypeTypeSub
# end class AreaCodeTypeTypeSub


class CalendarTypeValuesTypeSub(supermod.CalendarTypeValuesType):
    def __init__(self, CalendarType=None):
        super(CalendarTypeValuesTypeSub, self).__init__(CalendarType, )
supermod.CalendarTypeValuesType.subclass = CalendarTypeValuesTypeSub
# end class CalendarTypeValuesTypeSub


class CalendarTypeTypeSub(supermod.CalendarTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(CalendarTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.CalendarTypeType.subclass = CalendarTypeTypeSub
# end class CalendarTypeTypeSub


class CountryValuesTypeSub(supermod.CountryValuesType):
    def __init__(self, Country=None):
        super(CountryValuesTypeSub, self).__init__(Country, )
supermod.CountryValuesType.subclass = CountryValuesTypeSub
# end class CountryValuesTypeSub


class CountryTypeSub(supermod.CountryType):
    def __init__(self, ID=None, Comment=None, IS03166_3Code=None, ISO3=None, ISO2=None, DeltaAction=None, valueOf_=None):
        super(CountryTypeSub, self).__init__(ID, Comment, IS03166_3Code, ISO3, ISO2, DeltaAction, valueOf_, )
supermod.CountryType.subclass = CountryTypeSub
# end class CountryTypeSub


class CountryRelevanceValuesTypeSub(supermod.CountryRelevanceValuesType):
    def __init__(self, CountryRelevance=None):
        super(CountryRelevanceValuesTypeSub, self).__init__(CountryRelevance, )
supermod.CountryRelevanceValuesType.subclass = CountryRelevanceValuesTypeSub
# end class CountryRelevanceValuesTypeSub


class CountryRelevanceTypeSub(supermod.CountryRelevanceType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(CountryRelevanceTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.CountryRelevanceType.subclass = CountryRelevanceTypeSub
# end class CountryRelevanceTypeSub


class DecisionMakingBodyValuesTypeSub(supermod.DecisionMakingBodyValuesType):
    def __init__(self, DecisionMakingBody=None):
        super(DecisionMakingBodyValuesTypeSub, self).__init__(DecisionMakingBody, )
supermod.DecisionMakingBodyValuesType.subclass = DecisionMakingBodyValuesTypeSub
# end class DecisionMakingBodyValuesTypeSub


class DecisionMakingBodyTypeSub(supermod.DecisionMakingBodyType):
    def __init__(self, ID=None, OrganisationID=None, DeltaAction=None, valueOf_=None):
        super(DecisionMakingBodyTypeSub, self).__init__(ID, OrganisationID, DeltaAction, valueOf_, )
supermod.DecisionMakingBodyType.subclass = DecisionMakingBodyTypeSub
# end class DecisionMakingBodyTypeSub


class DetailReferenceValuesTypeSub(supermod.DetailReferenceValuesType):
    def __init__(self, DetailReference=None):
        super(DetailReferenceValuesTypeSub, self).__init__(DetailReference, )
supermod.DetailReferenceValuesType.subclass = DetailReferenceValuesTypeSub
# end class DetailReferenceValuesTypeSub


class DetailReferenceTypeSub(supermod.DetailReferenceType):
    def __init__(self, ID=None, DetailCode=None, DeltaAction=None, valueOf_=None):
        super(DetailReferenceTypeSub, self).__init__(ID, DetailCode, DeltaAction, valueOf_, )
supermod.DetailReferenceType.subclass = DetailReferenceTypeSub
# end class DetailReferenceTypeSub


class DetailTypeValuesTypeSub(supermod.DetailTypeValuesType):
    def __init__(self, DetailType=None):
        super(DetailTypeValuesTypeSub, self).__init__(DetailType, )
supermod.DetailTypeValuesType.subclass = DetailTypeValuesTypeSub
# end class DetailTypeValuesTypeSub


class DetailTypeTypeSub(supermod.DetailTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(DetailTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.DetailTypeType.subclass = DetailTypeTypeSub
# end class DetailTypeTypeSub


class DocNameStatusValuesTypeSub(supermod.DocNameStatusValuesType):
    def __init__(self, DocNameStatus=None):
        super(DocNameStatusValuesTypeSub, self).__init__(DocNameStatus, )
supermod.DocNameStatusValuesType.subclass = DocNameStatusValuesTypeSub
# end class DocNameStatusValuesTypeSub


class DocNameStatusTypeSub(supermod.DocNameStatusType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(DocNameStatusTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.DocNameStatusType.subclass = DocNameStatusTypeSub
# end class DocNameStatusTypeSub


class EntryEventTypeValuesTypeSub(supermod.EntryEventTypeValuesType):
    def __init__(self, EntryEventType=None):
        super(EntryEventTypeValuesTypeSub, self).__init__(EntryEventType, )
supermod.EntryEventTypeValuesType.subclass = EntryEventTypeValuesTypeSub
# end class EntryEventTypeValuesTypeSub


class EntryEventTypeTypeSub(supermod.EntryEventTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(EntryEventTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.EntryEventTypeType.subclass = EntryEventTypeTypeSub
# end class EntryEventTypeTypeSub


class EntryLinkTypeValuesTypeSub(supermod.EntryLinkTypeValuesType):
    def __init__(self, EntryLinkType=None):
        super(EntryLinkTypeValuesTypeSub, self).__init__(EntryLinkType, )
supermod.EntryLinkTypeValuesType.subclass = EntryLinkTypeValuesTypeSub
# end class EntryLinkTypeValuesTypeSub


class EntryLinkTypeTypeSub(supermod.EntryLinkTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(EntryLinkTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.EntryLinkTypeType.subclass = EntryLinkTypeTypeSub
# end class EntryLinkTypeTypeSub


class ExRefTypeValuesTypeSub(supermod.ExRefTypeValuesType):
    def __init__(self, ExRefType=None):
        super(ExRefTypeValuesTypeSub, self).__init__(ExRefType, )
supermod.ExRefTypeValuesType.subclass = ExRefTypeValuesTypeSub
# end class ExRefTypeValuesTypeSub


class ExRefTypeTypeSub(supermod.ExRefTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(ExRefTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.ExRefTypeType.subclass = ExRefTypeTypeSub
# end class ExRefTypeTypeSub


class FeatureTypeValuesTypeSub(supermod.FeatureTypeValuesType):
    def __init__(self, FeatureType=None):
        super(FeatureTypeValuesTypeSub, self).__init__(FeatureType, )
supermod.FeatureTypeValuesType.subclass = FeatureTypeValuesTypeSub
# end class FeatureTypeValuesTypeSub


class FeatureTypeTypeSub(supermod.FeatureTypeType):
    def __init__(self, ID=None, FeatureTypeGroupID=None, DeltaAction=None, valueOf_=None):
        super(FeatureTypeTypeSub, self).__init__(ID, FeatureTypeGroupID, DeltaAction, valueOf_, )
supermod.FeatureTypeType.subclass = FeatureTypeTypeSub
# end class FeatureTypeTypeSub


class FeatureTypeGroupValuesTypeSub(supermod.FeatureTypeGroupValuesType):
    def __init__(self, FeatureTypeGroup=None):
        super(FeatureTypeGroupValuesTypeSub, self).__init__(FeatureTypeGroup, )
supermod.FeatureTypeGroupValuesType.subclass = FeatureTypeGroupValuesTypeSub
# end class FeatureTypeGroupValuesTypeSub


class FeatureTypeGroupTypeSub(supermod.FeatureTypeGroupType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(FeatureTypeGroupTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.FeatureTypeGroupType.subclass = FeatureTypeGroupTypeSub
# end class FeatureTypeGroupTypeSub


class IDRegDocDateTypeValuesTypeSub(supermod.IDRegDocDateTypeValuesType):
    def __init__(self, IDRegDocDateType=None):
        super(IDRegDocDateTypeValuesTypeSub, self).__init__(IDRegDocDateType, )
supermod.IDRegDocDateTypeValuesType.subclass = IDRegDocDateTypeValuesTypeSub
# end class IDRegDocDateTypeValuesTypeSub


class IDRegDocDateTypeTypeSub(supermod.IDRegDocDateTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(IDRegDocDateTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.IDRegDocDateTypeType.subclass = IDRegDocDateTypeTypeSub
# end class IDRegDocDateTypeTypeSub


class IDRegDocTypeValuesTypeSub(supermod.IDRegDocTypeValuesType):
    def __init__(self, IDRegDocType=None):
        super(IDRegDocTypeValuesTypeSub, self).__init__(IDRegDocType, )
supermod.IDRegDocTypeValuesType.subclass = IDRegDocTypeValuesTypeSub
# end class IDRegDocTypeValuesTypeSub


class IDRegDocTypeTypeSub(supermod.IDRegDocTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(IDRegDocTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.IDRegDocTypeType.subclass = IDRegDocTypeTypeSub
# end class IDRegDocTypeTypeSub


class IdentityFeatureLinkTypeValuesTypeSub(supermod.IdentityFeatureLinkTypeValuesType):
    def __init__(self, IdentityFeatureLinkType=None):
        super(IdentityFeatureLinkTypeValuesTypeSub, self).__init__(IdentityFeatureLinkType, )
supermod.IdentityFeatureLinkTypeValuesType.subclass = IdentityFeatureLinkTypeValuesTypeSub
# end class IdentityFeatureLinkTypeValuesTypeSub


class IdentityFeatureLinkTypeTypeSub(supermod.IdentityFeatureLinkTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(IdentityFeatureLinkTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.IdentityFeatureLinkTypeType.subclass = IdentityFeatureLinkTypeTypeSub
# end class IdentityFeatureLinkTypeTypeSub


class LegalBasisValuesTypeSub(supermod.LegalBasisValuesType):
    def __init__(self, LegalBasis=None):
        super(LegalBasisValuesTypeSub, self).__init__(LegalBasis, )
supermod.LegalBasisValuesType.subclass = LegalBasisValuesTypeSub
# end class LegalBasisValuesTypeSub


class LegalBasisType2Sub(supermod.LegalBasisType2):
    def __init__(self, ID=None, LegalBasisShortRef=None, LegalBasisTypeID=None, SanctionsProgramID=None, DeltaAction=None, valueOf_=None):
        super(LegalBasisType2Sub, self).__init__(ID, LegalBasisShortRef, LegalBasisTypeID, SanctionsProgramID, DeltaAction, valueOf_, )
supermod.LegalBasisType2.subclass = LegalBasisType2Sub
# end class LegalBasisType2Sub


class LegalBasisTypeValuesTypeSub(supermod.LegalBasisTypeValuesType):
    def __init__(self, LegalBasisType=None):
        super(LegalBasisTypeValuesTypeSub, self).__init__(LegalBasisType, )
supermod.LegalBasisTypeValuesType.subclass = LegalBasisTypeValuesTypeSub
# end class LegalBasisTypeValuesTypeSub


class LegalBasisTypeTypeSub(supermod.LegalBasisTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(LegalBasisTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.LegalBasisTypeType.subclass = LegalBasisTypeTypeSub
# end class LegalBasisTypeTypeSub


class ListValuesTypeSub(supermod.ListValuesType):
    def __init__(self, List=None):
        super(ListValuesTypeSub, self).__init__(List, )
supermod.ListValuesType.subclass = ListValuesTypeSub
# end class ListValuesTypeSub


class ListTypeSub(supermod.ListType):
    def __init__(self, ID=None, Comment=None, DeltaAction=None, valueOf_=None):
        super(ListTypeSub, self).__init__(ID, Comment, DeltaAction, valueOf_, )
supermod.ListType.subclass = ListTypeSub
# end class ListTypeSub


class LocPartTypeValuesTypeSub(supermod.LocPartTypeValuesType):
    def __init__(self, LocPartType=None):
        super(LocPartTypeValuesTypeSub, self).__init__(LocPartType, )
supermod.LocPartTypeValuesType.subclass = LocPartTypeValuesTypeSub
# end class LocPartTypeValuesTypeSub


class LocPartTypeTypeSub(supermod.LocPartTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(LocPartTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.LocPartTypeType.subclass = LocPartTypeTypeSub
# end class LocPartTypeTypeSub


class LocPartValueStatusValuesTypeSub(supermod.LocPartValueStatusValuesType):
    def __init__(self, LocPartValueStatus=None):
        super(LocPartValueStatusValuesTypeSub, self).__init__(LocPartValueStatus, )
supermod.LocPartValueStatusValuesType.subclass = LocPartValueStatusValuesTypeSub
# end class LocPartValueStatusValuesTypeSub


class LocPartValueStatusTypeSub(supermod.LocPartValueStatusType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(LocPartValueStatusTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.LocPartValueStatusType.subclass = LocPartValueStatusTypeSub
# end class LocPartValueStatusTypeSub


class LocPartValueTypeValuesTypeSub(supermod.LocPartValueTypeValuesType):
    def __init__(self, LocPartValueType=None):
        super(LocPartValueTypeValuesTypeSub, self).__init__(LocPartValueType, )
supermod.LocPartValueTypeValuesType.subclass = LocPartValueTypeValuesTypeSub
# end class LocPartValueTypeValuesTypeSub


class LocPartValueTypeTypeSub(supermod.LocPartValueTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(LocPartValueTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.LocPartValueTypeType.subclass = LocPartValueTypeTypeSub
# end class LocPartValueTypeTypeSub


class NamePartTypeValuesTypeSub(supermod.NamePartTypeValuesType):
    def __init__(self, NamePartType=None):
        super(NamePartTypeValuesTypeSub, self).__init__(NamePartType, )
supermod.NamePartTypeValuesType.subclass = NamePartTypeValuesTypeSub
# end class NamePartTypeValuesTypeSub


class NamePartTypeTypeSub(supermod.NamePartTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(NamePartTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.NamePartTypeType.subclass = NamePartTypeTypeSub
# end class NamePartTypeTypeSub


class OrganisationValuesTypeSub(supermod.OrganisationValuesType):
    def __init__(self, Organisation=None):
        super(OrganisationValuesTypeSub, self).__init__(Organisation, )
supermod.OrganisationValuesType.subclass = OrganisationValuesTypeSub
# end class OrganisationValuesTypeSub


class OrganisationTypeSub(supermod.OrganisationType):
    def __init__(self, ID=None, CountryID=None, DeltaAction=None, valueOf_=None):
        super(OrganisationTypeSub, self).__init__(ID, CountryID, DeltaAction, valueOf_, )
supermod.OrganisationType.subclass = OrganisationTypeSub
# end class OrganisationTypeSub


class PartySubTypeValuesTypeSub(supermod.PartySubTypeValuesType):
    def __init__(self, PartySubType=None):
        super(PartySubTypeValuesTypeSub, self).__init__(PartySubType, )
supermod.PartySubTypeValuesType.subclass = PartySubTypeValuesTypeSub
# end class PartySubTypeValuesTypeSub


class PartySubTypeTypeSub(supermod.PartySubTypeType):
    def __init__(self, ID=None, PartyTypeID=None, DeltaAction=None, valueOf_=None):
        super(PartySubTypeTypeSub, self).__init__(ID, PartyTypeID, DeltaAction, valueOf_, )
supermod.PartySubTypeType.subclass = PartySubTypeTypeSub
# end class PartySubTypeTypeSub


class PartyTypeValuesTypeSub(supermod.PartyTypeValuesType):
    def __init__(self, PartyType=None):
        super(PartyTypeValuesTypeSub, self).__init__(PartyType, )
supermod.PartyTypeValuesType.subclass = PartyTypeValuesTypeSub
# end class PartyTypeValuesTypeSub


class PartyTypeTypeSub(supermod.PartyTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(PartyTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.PartyTypeType.subclass = PartyTypeTypeSub
# end class PartyTypeTypeSub


class RelationQualityValuesTypeSub(supermod.RelationQualityValuesType):
    def __init__(self, RelationQuality=None):
        super(RelationQualityValuesTypeSub, self).__init__(RelationQuality, )
supermod.RelationQualityValuesType.subclass = RelationQualityValuesTypeSub
# end class RelationQualityValuesTypeSub


class RelationQualityTypeSub(supermod.RelationQualityType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(RelationQualityTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.RelationQualityType.subclass = RelationQualityTypeSub
# end class RelationQualityTypeSub


class RelationTypeValuesTypeSub(supermod.RelationTypeValuesType):
    def __init__(self, RelationType=None):
        super(RelationTypeValuesTypeSub, self).__init__(RelationType, )
supermod.RelationTypeValuesType.subclass = RelationTypeValuesTypeSub
# end class RelationTypeValuesTypeSub


class RelationTypeTypeSub(supermod.RelationTypeType):
    def __init__(self, ID=None, Symmetrical=None, DeltaAction=None, valueOf_=None):
        super(RelationTypeTypeSub, self).__init__(ID, Symmetrical, DeltaAction, valueOf_, )
supermod.RelationTypeType.subclass = RelationTypeTypeSub
# end class RelationTypeTypeSub


class ReliabilityValuesTypeSub(supermod.ReliabilityValuesType):
    def __init__(self, Reliability=None):
        super(ReliabilityValuesTypeSub, self).__init__(Reliability, )
supermod.ReliabilityValuesType.subclass = ReliabilityValuesTypeSub
# end class ReliabilityValuesTypeSub


class ReliabilityTypeSub(supermod.ReliabilityType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(ReliabilityTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.ReliabilityType.subclass = ReliabilityTypeSub
# end class ReliabilityTypeSub


class SanctionsProgramValuesTypeSub(supermod.SanctionsProgramValuesType):
    def __init__(self, SanctionsProgram=None):
        super(SanctionsProgramValuesTypeSub, self).__init__(SanctionsProgram, )
supermod.SanctionsProgramValuesType.subclass = SanctionsProgramValuesTypeSub
# end class SanctionsProgramValuesTypeSub


class SanctionsProgramTypeSub(supermod.SanctionsProgramType):
    def __init__(self, ID=None, SubsidiaryBodyID=None, DeltaAction=None, valueOf_=None):
        super(SanctionsProgramTypeSub, self).__init__(ID, SubsidiaryBodyID, DeltaAction, valueOf_, )
supermod.SanctionsProgramType.subclass = SanctionsProgramTypeSub
# end class SanctionsProgramTypeSub


class SanctionsTypeValuesTypeSub(supermod.SanctionsTypeValuesType):
    def __init__(self, SanctionsType=None):
        super(SanctionsTypeValuesTypeSub, self).__init__(SanctionsType, )
supermod.SanctionsTypeValuesType.subclass = SanctionsTypeValuesTypeSub
# end class SanctionsTypeValuesTypeSub


class SanctionsTypeTypeSub(supermod.SanctionsTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(SanctionsTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.SanctionsTypeType.subclass = SanctionsTypeTypeSub
# end class SanctionsTypeTypeSub


class ScriptValuesTypeSub(supermod.ScriptValuesType):
    def __init__(self, Script=None):
        super(ScriptValuesTypeSub, self).__init__(Script, )
supermod.ScriptValuesType.subclass = ScriptValuesTypeSub
# end class ScriptValuesTypeSub


class ScriptTypeSub(supermod.ScriptType):
    def __init__(self, ID=None, ScriptCode=None, DeltaAction=None, valueOf_=None):
        super(ScriptTypeSub, self).__init__(ID, ScriptCode, DeltaAction, valueOf_, )
supermod.ScriptType.subclass = ScriptTypeSub
# end class ScriptTypeSub


class ScriptStatusValuesTypeSub(supermod.ScriptStatusValuesType):
    def __init__(self, ScriptStatus=None):
        super(ScriptStatusValuesTypeSub, self).__init__(ScriptStatus, )
supermod.ScriptStatusValuesType.subclass = ScriptStatusValuesTypeSub
# end class ScriptStatusValuesTypeSub


class ScriptStatusTypeSub(supermod.ScriptStatusType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(ScriptStatusTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.ScriptStatusType.subclass = ScriptStatusTypeSub
# end class ScriptStatusTypeSub


class SubsidiaryBodyValuesTypeSub(supermod.SubsidiaryBodyValuesType):
    def __init__(self, SubsidiaryBody=None):
        super(SubsidiaryBodyValuesTypeSub, self).__init__(SubsidiaryBody, )
supermod.SubsidiaryBodyValuesType.subclass = SubsidiaryBodyValuesTypeSub
# end class SubsidiaryBodyValuesTypeSub


class SubsidiaryBodyTypeSub(supermod.SubsidiaryBodyType):
    def __init__(self, ID=None, Notional=None, DecisionMakingBodyID=None, DeltaAction=None, valueOf_=None):
        super(SubsidiaryBodyTypeSub, self).__init__(ID, Notional, DecisionMakingBodyID, DeltaAction, valueOf_, )
supermod.SubsidiaryBodyType.subclass = SubsidiaryBodyTypeSub
# end class SubsidiaryBodyTypeSub


class SupInfoTypeValuesTypeSub(supermod.SupInfoTypeValuesType):
    def __init__(self, SupInfoType=None):
        super(SupInfoTypeValuesTypeSub, self).__init__(SupInfoType, )
supermod.SupInfoTypeValuesType.subclass = SupInfoTypeValuesTypeSub
# end class SupInfoTypeValuesTypeSub


class SupInfoTypeTypeSub(supermod.SupInfoTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(SupInfoTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.SupInfoTypeType.subclass = SupInfoTypeTypeSub
# end class SupInfoTypeTypeSub


class TargetTypeValuesTypeSub(supermod.TargetTypeValuesType):
    def __init__(self, TargetType=None):
        super(TargetTypeValuesTypeSub, self).__init__(TargetType, )
supermod.TargetTypeValuesType.subclass = TargetTypeValuesTypeSub
# end class TargetTypeValuesTypeSub


class TargetTypeTypeSub(supermod.TargetTypeType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(TargetTypeTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.TargetTypeType.subclass = TargetTypeTypeSub
# end class TargetTypeTypeSub


class ValidityValuesTypeSub(supermod.ValidityValuesType):
    def __init__(self, Validity=None):
        super(ValidityValuesTypeSub, self).__init__(Validity, )
supermod.ValidityValuesType.subclass = ValidityValuesTypeSub
# end class ValidityValuesTypeSub


class ValidityTypeSub(supermod.ValidityType):
    def __init__(self, ID=None, DeltaAction=None, valueOf_=None):
        super(ValidityTypeSub, self).__init__(ID, DeltaAction, valueOf_, )
supermod.ValidityType.subclass = ValidityTypeSub
# end class ValidityTypeSub


class YearsTypeSub(supermod.YearsType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(YearsTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.YearsType.subclass = YearsTypeSub
# end class YearsTypeSub


class MonthsTypeSub(supermod.MonthsType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(MonthsTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.MonthsType.subclass = MonthsTypeSub
# end class MonthsTypeSub


class DaysTypeSub(supermod.DaysType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(DaysTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.DaysType.subclass = DaysTypeSub
# end class DaysTypeSub


class LocationAreaCodeTypeSub(supermod.LocationAreaCodeType):
    def __init__(self, AreaCodeID=None, DeltaAction=None):
        super(LocationAreaCodeTypeSub, self).__init__(AreaCodeID, DeltaAction, )
supermod.LocationAreaCodeType.subclass = LocationAreaCodeTypeSub
# end class LocationAreaCodeTypeSub


class LocationCountryTypeSub(supermod.LocationCountryType):
    def __init__(self, CountryID=None, CountryRelevanceID=None, DeltaAction=None):
        super(LocationCountryTypeSub, self).__init__(CountryID, CountryRelevanceID, DeltaAction, )
supermod.LocationCountryType.subclass = LocationCountryTypeSub
# end class LocationCountryTypeSub


class LocationPartTypeSub(supermod.LocationPartType):
    def __init__(self, LocPartTypeID=None, DeltaAction=None, LocationPartValue=None):
        super(LocationPartTypeSub, self).__init__(LocPartTypeID, DeltaAction, LocationPartValue, )
supermod.LocationPartType.subclass = LocationPartTypeSub
# end class LocationPartTypeSub


class LocationPartValueTypeSub(supermod.LocationPartValueType):
    def __init__(self, Primary=None, LocPartValueTypeID=None, LocPartValueStatusID=None, DeltaAction=None, Comment=None, Value=None):
        super(LocationPartValueTypeSub, self).__init__(Primary, LocPartValueTypeID, LocPartValueStatusID, DeltaAction, Comment, Value, )
supermod.LocationPartValueType.subclass = LocationPartValueTypeSub
# end class LocationPartValueTypeSub


class ValueTypeSub(supermod.ValueType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(ValueTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.ValueType.subclass = ValueTypeSub
# end class ValueTypeSub


class IDRegistrationNoTypeSub(supermod.IDRegistrationNoType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(IDRegistrationNoTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.IDRegistrationNoType.subclass = IDRegistrationNoTypeSub
# end class IDRegistrationNoTypeSub


class IssuingAuthorityTypeSub(supermod.IssuingAuthorityType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(IssuingAuthorityTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.IssuingAuthorityType.subclass = IssuingAuthorityTypeSub
# end class IssuingAuthorityTypeSub


class DocumentDateTypeSub(supermod.DocumentDateType):
    def __init__(self, IDRegDocDateTypeID=None, DeltaAction=None, DatePeriod=None):
        super(DocumentDateTypeSub, self).__init__(IDRegDocDateTypeID, DeltaAction, DatePeriod, )
supermod.DocumentDateType.subclass = DocumentDateTypeSub
# end class DocumentDateTypeSub


class IDRegDocumentMentionTypeSub(supermod.IDRegDocumentMentionType):
    def __init__(self, IDRegDocumentID=None, ReferenceType=None, DeltaAction=None):
        super(IDRegDocumentMentionTypeSub, self).__init__(IDRegDocumentID, ReferenceType, DeltaAction, )
supermod.IDRegDocumentMentionType.subclass = IDRegDocumentMentionTypeSub
# end class IDRegDocumentMentionTypeSub


class DocumentedNameReferenceTypeSub(supermod.DocumentedNameReferenceType):
    def __init__(self, DocumentedNameID=None, DeltaAction=None):
        super(DocumentedNameReferenceTypeSub, self).__init__(DocumentedNameID, DeltaAction, )
supermod.DocumentedNameReferenceType.subclass = DocumentedNameReferenceTypeSub
# end class DocumentedNameReferenceTypeSub


class ProfileTypeSub(supermod.ProfileType):
    def __init__(self, ID=None, PartySubTypeID=None, DeltaAction=None, Comment=None, Identity=None, Feature=None, SanctionsEntryReference=None, ExternalReference=None):
        super(ProfileTypeSub, self).__init__(ID, PartySubTypeID, DeltaAction, Comment, Identity, Feature, SanctionsEntryReference, ExternalReference, )
supermod.ProfileType.subclass = ProfileTypeSub
# end class ProfileTypeSub


class SanctionsEntryReferenceTypeSub(supermod.SanctionsEntryReferenceType):
    def __init__(self, SanctionsEntryID=None, DeltaAction=None):
        super(SanctionsEntryReferenceTypeSub, self).__init__(SanctionsEntryID, DeltaAction, )
supermod.SanctionsEntryReferenceType.subclass = SanctionsEntryReferenceTypeSub
# end class SanctionsEntryReferenceTypeSub


class ExternalReferenceTypeSub(supermod.ExternalReferenceType):
    def __init__(self, ExRefTypeID=None, DeltaAction=None, Comment=None, ExRefValue=None, DirectURL=None, SubLink=None):
        super(ExternalReferenceTypeSub, self).__init__(ExRefTypeID, DeltaAction, Comment, ExRefValue, DirectURL, SubLink, )
supermod.ExternalReferenceType.subclass = ExternalReferenceTypeSub
# end class ExternalReferenceTypeSub


class ExRefValueTypeSub(supermod.ExRefValueType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(ExRefValueTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.ExRefValueType.subclass = ExRefValueTypeSub
# end class ExRefValueTypeSub


class SubLinkTypeSub(supermod.SubLinkType):
    def __init__(self, TargetTypeID=None, DeltaAction=None, Description=None, DirectURL=None):
        super(SubLinkTypeSub, self).__init__(TargetTypeID, DeltaAction, Description, DirectURL, )
supermod.SubLinkType.subclass = SubLinkTypeSub
# end class SubLinkTypeSub


class DescriptionTypeSub(supermod.DescriptionType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(DescriptionTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.DescriptionType.subclass = DescriptionTypeSub
# end class DescriptionTypeSub


class FeatureVersionTypeSub(supermod.FeatureVersionType):
    def __init__(self, ID=None, ReliabilityID=None, DeltaAction=None, Comment=None, DatePeriod=None, VersionDetail=None, VersionLocation=None, IDRegDocumentReference=None):
        super(FeatureVersionTypeSub, self).__init__(ID, ReliabilityID, DeltaAction, Comment, DatePeriod, VersionDetail, VersionLocation, IDRegDocumentReference, )
supermod.FeatureVersionType.subclass = FeatureVersionTypeSub
# end class FeatureVersionTypeSub


class VersionDetailTypeSub(supermod.VersionDetailType):
    def __init__(self, DetailTypeID=None, DetailReferenceID=None, DeltaAction=None, valueOf_=None):
        super(VersionDetailTypeSub, self).__init__(DetailTypeID, DetailReferenceID, DeltaAction, valueOf_, )
supermod.VersionDetailType.subclass = VersionDetailTypeSub
# end class VersionDetailTypeSub


class VersionLocationTypeSub(supermod.VersionLocationType):
    def __init__(self, LocationID=None, DeltaAction=None):
        super(VersionLocationTypeSub, self).__init__(LocationID, DeltaAction, )
supermod.VersionLocationType.subclass = VersionLocationTypeSub
# end class VersionLocationTypeSub


class IdentityReferenceTypeSub(supermod.IdentityReferenceType):
    def __init__(self, IdentityID=None, IdentityFeatureLinkTypeID=None, DeltaAction=None):
        super(IdentityReferenceTypeSub, self).__init__(IdentityID, IdentityFeatureLinkTypeID, DeltaAction, )
supermod.IdentityReferenceType.subclass = IdentityReferenceTypeSub
# end class IdentityReferenceTypeSub


class AliasType3Sub(supermod.AliasType3):
    def __init__(self, FixedRef=None, AliasTypeID=None, Primary=None, LowQuality=None, DeltaAction=None, Comment=None, DatePeriod=None, DocumentedName=None):
        super(AliasType3Sub, self).__init__(FixedRef, AliasTypeID, Primary, LowQuality, DeltaAction, Comment, DatePeriod, DocumentedName, )
supermod.AliasType3.subclass = AliasType3Sub
# end class AliasType3Sub


class NamePartGroupsTypeSub(supermod.NamePartGroupsType):
    def __init__(self, DeltaAction=None, MasterNamePartGroup=None):
        super(NamePartGroupsTypeSub, self).__init__(DeltaAction, MasterNamePartGroup, )
supermod.NamePartGroupsType.subclass = NamePartGroupsTypeSub
# end class NamePartGroupsTypeSub


class MasterNamePartGroupTypeSub(supermod.MasterNamePartGroupType):
    def __init__(self, DeltaAction=None, NamePartGroup=None):
        super(MasterNamePartGroupTypeSub, self).__init__(DeltaAction, NamePartGroup, )
supermod.MasterNamePartGroupType.subclass = MasterNamePartGroupTypeSub
# end class MasterNamePartGroupTypeSub


class NamePartGroupTypeSub(supermod.NamePartGroupType):
    def __init__(self, ID=None, NamePartTypeID=None, DeltaAction=None):
        super(NamePartGroupTypeSub, self).__init__(ID, NamePartTypeID, DeltaAction, )
supermod.NamePartGroupType.subclass = NamePartGroupTypeSub
# end class NamePartGroupTypeSub


class DocumentedNamePartTypeSub(supermod.DocumentedNamePartType):
    def __init__(self, LeadingChars=None, TrailingChars=None, DeltaAction=None, NamePartValue=None):
        super(DocumentedNamePartTypeSub, self).__init__(LeadingChars, TrailingChars, DeltaAction, NamePartValue, )
supermod.DocumentedNamePartType.subclass = DocumentedNamePartTypeSub
# end class DocumentedNamePartTypeSub


class NamePartValueTypeSub(supermod.NamePartValueType):
    def __init__(self, NamePartGroupID=None, ScriptID=None, ScriptStatusID=None, Acronym=None, DeltaAction=None, valueOf_=None):
        super(NamePartValueTypeSub, self).__init__(NamePartGroupID, ScriptID, ScriptStatusID, Acronym, DeltaAction, valueOf_, )
supermod.NamePartValueType.subclass = NamePartValueTypeSub
# end class NamePartValueTypeSub


class DocumentedNameCountryTypeSub(supermod.DocumentedNameCountryType):
    def __init__(self, CountryID=None, DeltaAction=None, Comment=None):
        super(DocumentedNameCountryTypeSub, self).__init__(CountryID, DeltaAction, Comment, )
supermod.DocumentedNameCountryType.subclass = DocumentedNameCountryTypeSub
# end class DocumentedNameCountryTypeSub


class LimitationsToListingTypeSub(supermod.LimitationsToListingType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(LimitationsToListingTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.LimitationsToListingType.subclass = LimitationsToListingTypeSub
# end class LimitationsToListingTypeSub


class EntryEventType4Sub(supermod.EntryEventType4):
    def __init__(self, ID=None, EntryEventTypeID=None, LegalBasisID=None, DeltaAction=None, Comment=None, Date=None):
        super(EntryEventType4Sub, self).__init__(ID, EntryEventTypeID, LegalBasisID, DeltaAction, Comment, Date, )
supermod.EntryEventType4.subclass = EntryEventType4Sub
# end class EntryEventType4Sub


class SanctionsMeasureTypeSub(supermod.SanctionsMeasureType):
    def __init__(self, ID=None, SanctionsTypeID=None, DeltaAction=None, Comment=None, DatePeriod=None):
        super(SanctionsMeasureTypeSub, self).__init__(ID, SanctionsTypeID, DeltaAction, Comment, DatePeriod, )
supermod.SanctionsMeasureType.subclass = SanctionsMeasureTypeSub
# end class SanctionsMeasureTypeSub


class SupportingInfoTypeSub(supermod.SupportingInfoType):
    def __init__(self, ID=None, SupInfoTypeID=None, DeltaAction=None, Text=None, DirectURL=None):
        super(SupportingInfoTypeSub, self).__init__(ID, SupInfoTypeID, DeltaAction, Text, DirectURL, )
supermod.SupportingInfoType.subclass = SupportingInfoTypeSub
# end class SupportingInfoTypeSub


class TextTypeSub(supermod.TextType):
    def __init__(self, DeltaAction=None, valueOf_=None):
        super(TextTypeSub, self).__init__(DeltaAction, valueOf_, )
supermod.TextType.subclass = TextTypeSub
# end class TextTypeSub


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
        rootTag = 'Sanctions'
        rootClass = supermod.Sanctions
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:un="http://www.un.org/sanctions/1.0"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Sanctions'
        rootClass = supermod.Sanctions
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
        rootTag = 'Sanctions'
        rootClass = supermod.Sanctions
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:un="http://www.un.org/sanctions/1.0"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Sanctions'
        rootClass = supermod.Sanctions
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
