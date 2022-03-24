#!/usr/bin/env python

#
# Generated Thu Mar  3 11:30:59 2022 by generateDS.py version 2.40.8.
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'FHIR4CodeSystemSuper.py')
#   ('-s', 'FHIR4CodeSystem.py')
#
# Command line arguments:
#   codesystem.xsd
#
# Command line:
#   C:/Dokumente und Einstellungen/gkleinoscheg/Downloads/generateDS-2.40.8/generateDS.py -o "FHIR4CodeSystemSuper.py" -s "FHIR4CodeSystem.py" codesystem.xsd
#
# Current working directory (os.getcwd()):
#   FHIR
#

import os
import sys
from lxml import etree as etree_

import fhir4_codesystem_super as supermod
import prop_csv_and_master as pcam

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#

class CodeSystemSub(supermod.CodeSystem, pcam.PropCsvAndMaster):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extension=None, modifierExtension=None, url=None, identifier=None, version=None, name=None, title=None, status=None, experimental=None, date=None, publisher=None, contact=None, description=None, useContext=None, jurisdiction=None, purpose=None, copyright=None, caseSensitive=None, valueSet=None, hierarchyMeaning=None, compositional=None, versionNeeded=None, content=None, supplements=None, count=None, filter=None, property=None, concept=None, **kwargs_):
        super(CodeSystemSub, self).__init__(id, meta, implicitRules, language, extension, modifierExtension, url, identifier, version, name, title, status, experimental, date, publisher, contact, description, useContext, jurisdiction, purpose, copyright, caseSensitive, valueSet, hierarchyMeaning, compositional, versionNeeded, content, supplements, count, filter, property, concept,  **kwargs_)

    def get_resource():
        return pcam.Resource.CodeSystem.value

    def get_lockeddate(self):
        return None

    def get_content(self):
        return super().get_content().get_value()

supermod.CodeSystem.subclass = CodeSystemSub
# end class CodeSystemSub

class ElementSub(supermod.Element):
    def __init__(self, id=None, extension=None, extensiontype_=None, **kwargs_):
        super(ElementSub, self).__init__(id, extension, extensiontype_,  **kwargs_)
supermod.Element.subclass = ElementSub
# end class ElementSub


class MetaSub(supermod.Meta):
    def __init__(self, id=None, extension=None, versionId=None, lastUpdated=None, source=None, profile=None, security=None, tag=None, **kwargs_):
        super(MetaSub, self).__init__(id, extension, versionId, lastUpdated, source, profile, security, tag,  **kwargs_)
supermod.Meta.subclass = MetaSub
# end class MetaSub


class AddressSub(supermod.Address):
    def __init__(self, id=None, extension=None, use=None, type_=None, text=None, line=None, city=None, district=None, state=None, postalCode=None, country=None, period=None, **kwargs_):
        super(AddressSub, self).__init__(id, extension, use, type_, text, line, city, district, state, postalCode, country, period,  **kwargs_)
supermod.Address.subclass = AddressSub
# end class AddressSub


class AddressUseSub(supermod.AddressUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AddressUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AddressUse.subclass = AddressUseSub
# end class AddressUseSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AddressTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class ContributorSub(supermod.Contributor):
    def __init__(self, id=None, extension=None, type_=None, name=None, contact=None, **kwargs_):
        super(ContributorSub, self).__init__(id, extension, type_, name, contact,  **kwargs_)
supermod.Contributor.subclass = ContributorSub
# end class ContributorSub


class ContributorTypeSub(supermod.ContributorType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContributorTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContributorType.subclass = ContributorTypeSub
# end class ContributorTypeSub


class AttachmentSub(supermod.Attachment):
    def __init__(self, id=None, extension=None, contentType=None, language=None, data=None, url=None, size=None, hash=None, title=None, creation=None, **kwargs_):
        super(AttachmentSub, self).__init__(id, extension, contentType, language, data, url, size, hash, title, creation,  **kwargs_)
supermod.Attachment.subclass = AttachmentSub
# end class AttachmentSub


class DataRequirementSub(supermod.DataRequirement):
    def __init__(self, id=None, extension=None, type_=None, profile=None, subjectCodeableConcept=None, subjectReference=None, mustSupport=None, codeFilter=None, dateFilter=None, limit=None, sort=None, **kwargs_):
        super(DataRequirementSub, self).__init__(id, extension, type_, profile, subjectCodeableConcept, subjectReference, mustSupport, codeFilter, dateFilter, limit, sort,  **kwargs_)
supermod.DataRequirement.subclass = DataRequirementSub
# end class DataRequirementSub


class DataRequirement_CodeFilterSub(supermod.DataRequirement_CodeFilter):
    def __init__(self, id=None, extension=None, path=None, searchParam=None, valueSet=None, code=None, **kwargs_):
        super(DataRequirement_CodeFilterSub, self).__init__(id, extension, path, searchParam, valueSet, code,  **kwargs_)
supermod.DataRequirement_CodeFilter.subclass = DataRequirement_CodeFilterSub
# end class DataRequirement_CodeFilterSub


class DataRequirement_DateFilterSub(supermod.DataRequirement_DateFilter):
    def __init__(self, id=None, extension=None, path=None, searchParam=None, valueDateTime=None, valuePeriod=None, valueDuration=None, **kwargs_):
        super(DataRequirement_DateFilterSub, self).__init__(id, extension, path, searchParam, valueDateTime, valuePeriod, valueDuration,  **kwargs_)
supermod.DataRequirement_DateFilter.subclass = DataRequirement_DateFilterSub
# end class DataRequirement_DateFilterSub


class DataRequirement_SortSub(supermod.DataRequirement_Sort):
    def __init__(self, id=None, extension=None, path=None, direction=None, **kwargs_):
        super(DataRequirement_SortSub, self).__init__(id, extension, path, direction,  **kwargs_)
supermod.DataRequirement_Sort.subclass = DataRequirement_SortSub
# end class DataRequirement_SortSub


class SortDirectionSub(supermod.SortDirection):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SortDirectionSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SortDirection.subclass = SortDirectionSub
# end class SortDirectionSub


class MoneySub(supermod.Money):
    def __init__(self, id=None, extension=None, value=None, currency=None, **kwargs_):
        super(MoneySub, self).__init__(id, extension, value, currency,  **kwargs_)
supermod.Money.subclass = MoneySub
# end class MoneySub


class HumanNameSub(supermod.HumanName):
    def __init__(self, id=None, extension=None, use=None, text=None, family=None, given=None, prefix=None, suffix=None, period=None, **kwargs_):
        super(HumanNameSub, self).__init__(id, extension, use, text, family, given, prefix, suffix, period,  **kwargs_)
supermod.HumanName.subclass = HumanNameSub
# end class HumanNameSub


class NameUseSub(supermod.NameUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(NameUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.NameUse.subclass = NameUseSub
# end class NameUseSub


class ContactPointSub(supermod.ContactPoint):
    def __init__(self, id=None, extension=None, system=None, value=None, use=None, rank=None, period=None, **kwargs_):
        super(ContactPointSub, self).__init__(id, extension, system, value, use, rank, period,  **kwargs_)
supermod.ContactPoint.subclass = ContactPointSub
# end class ContactPointSub


class ContactPointSystemSub(supermod.ContactPointSystem):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContactPointSystemSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContactPointSystem.subclass = ContactPointSystemSub
# end class ContactPointSystemSub


class ContactPointUseSub(supermod.ContactPointUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContactPointUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContactPointUse.subclass = ContactPointUseSub
# end class ContactPointUseSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, id=None, extension=None, use=None, type_=None, system=None, value=None, period=None, assigner=None, **kwargs_):
        super(IdentifierSub, self).__init__(id, extension, use, type_, system, value, period, assigner,  **kwargs_)
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class IdentifierUseSub(supermod.IdentifierUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(IdentifierUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.IdentifierUse.subclass = IdentifierUseSub
# end class IdentifierUseSub


class CodingSub(supermod.Coding):
    def __init__(self, id=None, extension=None, system=None, version=None, code=None, display=None, userSelected=None, **kwargs_):
        super(CodingSub, self).__init__(id, extension, system, version, code, display, userSelected,  **kwargs_)
supermod.Coding.subclass = CodingSub
# end class CodingSub


class SampledDataSub(supermod.SampledData):
    def __init__(self, id=None, extension=None, origin=None, period=None, factor=None, lowerLimit=None, upperLimit=None, dimensions=None, data=None, **kwargs_):
        super(SampledDataSub, self).__init__(id, extension, origin, period, factor, lowerLimit, upperLimit, dimensions, data,  **kwargs_)
supermod.SampledData.subclass = SampledDataSub
# end class SampledDataSub


class SampledDataDataTypeSub(supermod.SampledDataDataType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SampledDataDataTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SampledDataDataType.subclass = SampledDataDataTypeSub
# end class SampledDataDataTypeSub


class RatioSub(supermod.Ratio):
    def __init__(self, id=None, extension=None, numerator=None, denominator=None, **kwargs_):
        super(RatioSub, self).__init__(id, extension, numerator, denominator,  **kwargs_)
supermod.Ratio.subclass = RatioSub
# end class RatioSub


class ReferenceSub(supermod.Reference):
    def __init__(self, id=None, extension=None, reference=None, type_=None, identifier=None, display=None, **kwargs_):
        super(ReferenceSub, self).__init__(id, extension, reference, type_, identifier, display,  **kwargs_)
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class TriggerDefinitionSub(supermod.TriggerDefinition):
    def __init__(self, id=None, extension=None, type_=None, name=None, timingTiming=None, timingReference=None, timingDate=None, timingDateTime=None, data=None, condition=None, **kwargs_):
        super(TriggerDefinitionSub, self).__init__(id, extension, type_, name, timingTiming, timingReference, timingDate, timingDateTime, data, condition,  **kwargs_)
supermod.TriggerDefinition.subclass = TriggerDefinitionSub
# end class TriggerDefinitionSub


class TriggerTypeSub(supermod.TriggerType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(TriggerTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.TriggerType.subclass = TriggerTypeSub
# end class TriggerTypeSub


class QuantitySub(supermod.Quantity):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, extensiontype_=None, **kwargs_):
        super(QuantitySub, self).__init__(id, extension, value, comparator, unit, system, code, extensiontype_,  **kwargs_)
supermod.Quantity.subclass = QuantitySub
# end class QuantitySub


class QuantityComparatorSub(supermod.QuantityComparator):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(QuantityComparatorSub, self).__init__(id, extension, value,  **kwargs_)
supermod.QuantityComparator.subclass = QuantityComparatorSub
# end class QuantityComparatorSub


class PeriodSub(supermod.Period):
    def __init__(self, id=None, extension=None, start=None, end=None, **kwargs_):
        super(PeriodSub, self).__init__(id, extension, start, end,  **kwargs_)
supermod.Period.subclass = PeriodSub
# end class PeriodSub


class DurationSub(supermod.Duration):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(DurationSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Duration.subclass = DurationSub
# end class DurationSub


class RangeSub(supermod.Range):
    def __init__(self, id=None, extension=None, low=None, high=None, **kwargs_):
        super(RangeSub, self).__init__(id, extension, low, high,  **kwargs_)
supermod.Range.subclass = RangeSub
# end class RangeSub


class RelatedArtifactSub(supermod.RelatedArtifact):
    def __init__(self, id=None, extension=None, type_=None, label=None, display=None, citation=None, url=None, document=None, resource=None, **kwargs_):
        super(RelatedArtifactSub, self).__init__(id, extension, type_, label, display, citation, url, document, resource,  **kwargs_)
supermod.RelatedArtifact.subclass = RelatedArtifactSub
# end class RelatedArtifactSub


class RelatedArtifactTypeSub(supermod.RelatedArtifactType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(RelatedArtifactTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.RelatedArtifactType.subclass = RelatedArtifactTypeSub
# end class RelatedArtifactTypeSub


class AnnotationSub(supermod.Annotation):
    def __init__(self, id=None, extension=None, authorReference=None, authorString=None, time=None, text=None, **kwargs_):
        super(AnnotationSub, self).__init__(id, extension, authorReference, authorString, time, text,  **kwargs_)
supermod.Annotation.subclass = AnnotationSub
# end class AnnotationSub


class ContactDetailSub(supermod.ContactDetail):
    def __init__(self, id=None, extension=None, name=None, telecom=None, **kwargs_):
        super(ContactDetailSub, self).__init__(id, extension, name, telecom,  **kwargs_)

    # TODO
    def __str__(self) -> str:
        return super().__str__()
supermod.ContactDetail.subclass = ContactDetailSub
# end class ContactDetailSub


class UsageContextSub(supermod.UsageContext):
    def __init__(self, id=None, extension=None, code=None, valueCodeableConcept=None, valueQuantity=None, valueRange=None, valueReference=None, **kwargs_):
        super(UsageContextSub, self).__init__(id, extension, code, valueCodeableConcept, valueQuantity, valueRange, valueReference,  **kwargs_)
supermod.UsageContext.subclass = UsageContextSub
# end class UsageContextSub


class ExpressionSub(supermod.Expression):
    def __init__(self, id=None, extension=None, description=None, name=None, language=None, expression=None, reference=None, **kwargs_):
        super(ExpressionSub, self).__init__(id, extension, description, name, language, expression, reference,  **kwargs_)
supermod.Expression.subclass = ExpressionSub
# end class ExpressionSub


class ExpressionLanguageSub(supermod.ExpressionLanguage):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ExpressionLanguageSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ExpressionLanguage.subclass = ExpressionLanguageSub
# end class ExpressionLanguageSub


class SignatureSub(supermod.Signature):
    def __init__(self, id=None, extension=None, type_=None, when=None, who=None, onBehalfOf=None, targetFormat=None, sigFormat=None, data=None, **kwargs_):
        super(SignatureSub, self).__init__(id, extension, type_, when, who, onBehalfOf, targetFormat, sigFormat, data,  **kwargs_)
supermod.Signature.subclass = SignatureSub
# end class SignatureSub


class UnitsOfTimeSub(supermod.UnitsOfTime):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(UnitsOfTimeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.UnitsOfTime.subclass = UnitsOfTimeSub
# end class UnitsOfTimeSub


class EventTimingSub(supermod.EventTiming):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(EventTimingSub, self).__init__(id, extension, value,  **kwargs_)
supermod.EventTiming.subclass = EventTimingSub
# end class EventTimingSub


class CodeableConceptSub(supermod.CodeableConcept):
    def __init__(self, id=None, extension=None, coding=None, text=None, **kwargs_):
        super(CodeableConceptSub, self).__init__(id, extension, coding, text,  **kwargs_)
supermod.CodeableConcept.subclass = CodeableConceptSub
# end class CodeableConceptSub


class ParameterDefinitionSub(supermod.ParameterDefinition):
    def __init__(self, id=None, extension=None, name=None, use=None, min=None, max=None, documentation=None, type_=None, profile=None, **kwargs_):
        super(ParameterDefinitionSub, self).__init__(id, extension, name, use, min, max, documentation, type_, profile,  **kwargs_)
supermod.ParameterDefinition.subclass = ParameterDefinitionSub
# end class ParameterDefinitionSub


class PropertyRepresentationSub(supermod.PropertyRepresentation):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(PropertyRepresentationSub, self).__init__(id, extension, value,  **kwargs_)
supermod.PropertyRepresentation.subclass = PropertyRepresentationSub
# end class PropertyRepresentationSub


class ConstraintSeveritySub(supermod.ConstraintSeverity):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ConstraintSeveritySub, self).__init__(id, extension, value,  **kwargs_)
supermod.ConstraintSeverity.subclass = ConstraintSeveritySub
# end class ConstraintSeveritySub


class AggregationModeSub(supermod.AggregationMode):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AggregationModeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AggregationMode.subclass = AggregationModeSub
# end class AggregationModeSub


class ReferenceVersionRulesSub(supermod.ReferenceVersionRules):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ReferenceVersionRulesSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ReferenceVersionRules.subclass = ReferenceVersionRulesSub
# end class ReferenceVersionRulesSub


class SlicingRulesSub(supermod.SlicingRules):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SlicingRulesSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SlicingRules.subclass = SlicingRulesSub
# end class SlicingRulesSub


class BindingStrengthSub(supermod.BindingStrength):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(BindingStrengthSub, self).__init__(id, extension, value,  **kwargs_)
supermod.BindingStrength.subclass = BindingStrengthSub
# end class BindingStrengthSub


class DiscriminatorTypeSub(supermod.DiscriminatorType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(DiscriminatorTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.DiscriminatorType.subclass = DiscriminatorTypeSub
# end class DiscriminatorTypeSub


class ResourceSub(supermod.Resource):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extensiontype_=None, **kwargs_):
        super(ResourceSub, self).__init__(id, meta, implicitRules, language, extensiontype_,  **kwargs_)
supermod.Resource.subclass = ResourceSub
# end class ResourceSub


class PublicationStatusSub(supermod.PublicationStatus):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(PublicationStatusSub, self).__init__(id, extension, value,  **kwargs_)
supermod.PublicationStatus.subclass = PublicationStatusSub
# end class PublicationStatusSub


class SearchParamTypeSub(supermod.SearchParamType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SearchParamTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SearchParamType.subclass = SearchParamTypeSub
# end class SearchParamTypeSub


class AdministrativeGenderSub(supermod.AdministrativeGender):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AdministrativeGenderSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AdministrativeGender.subclass = AdministrativeGenderSub
# end class AdministrativeGenderSub


class FHIRVersionSub(supermod.FHIRVersion):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(FHIRVersionSub, self).__init__(id, extension, value,  **kwargs_)
supermod.FHIRVersion.subclass = FHIRVersionSub
# end class FHIRVersionSub


class NoteTypeSub(supermod.NoteType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(NoteTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.NoteType.subclass = NoteTypeSub
# end class NoteTypeSub


class RemittanceOutcomeSub(supermod.RemittanceOutcome):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(RemittanceOutcomeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.RemittanceOutcome.subclass = RemittanceOutcomeSub
# end class RemittanceOutcomeSub


class ConceptMapEquivalenceSub(supermod.ConceptMapEquivalence):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ConceptMapEquivalenceSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ConceptMapEquivalence.subclass = ConceptMapEquivalenceSub
# end class ConceptMapEquivalenceSub


class DocumentReferenceStatusSub(supermod.DocumentReferenceStatus):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(DocumentReferenceStatusSub, self).__init__(id, extension, value,  **kwargs_)
supermod.DocumentReferenceStatus.subclass = DocumentReferenceStatusSub
# end class DocumentReferenceStatusSub


class DomainResourceSub(supermod.DomainResource):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extension=None, modifierExtension=None, extensiontype_=None, **kwargs_):
        super(DomainResourceSub, self).__init__(id, meta, implicitRules, language, extension, modifierExtension, extensiontype_,  **kwargs_)
supermod.DomainResource.subclass = DomainResourceSub
# end class DomainResourceSub


class AgeSub(supermod.Age):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(AgeSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Age.subclass = AgeSub
# end class AgeSub


class DistanceSub(supermod.Distance):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(DistanceSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Distance.subclass = DistanceSub
# end class DistanceSub


class CountSub(supermod.Count):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(CountSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Count.subclass = CountSub
# end class CountSub


class BackboneElementSub(supermod.BackboneElement):
    def __init__(self, id=None, extension=None, modifierExtension=None, extensiontype_=None, **kwargs_):
        super(BackboneElementSub, self).__init__(id, extension, modifierExtension, extensiontype_,  **kwargs_)
supermod.BackboneElement.subclass = BackboneElementSub
# end class BackboneElementSub


class ExtensionSub(supermod.Extension):
    def __init__(self, id=None, extension=None, url=None, valueBase64Binary=None, valueBoolean=None, valueCanonical=None, valueCode=None, valueDate=None, valueDateTime=None, valueDecimal=None, valueId=None, valueInstant=None, valueInteger=None, valueMarkdown=None, valueOid=None, valuePositiveInt=None, valueString=None, valueTime=None, valueUnsignedInt=None, valueUri=None, valueUrl=None, valueUuid=None, valueAddress=None, valueAge=None, valueAnnotation=None, valueAttachment=None, valueCodeableConcept=None, valueCoding=None, valueContactPoint=None, valueCount=None, valueDistance=None, valueDuration=None, valueHumanName=None, valueIdentifier=None, valueMoney=None, valuePeriod=None, valueQuantity=None, valueRange=None, valueRatio=None, valueReference=None, valueSampledData=None, valueSignature=None, valueTiming=None, valueContactDetail=None, valueContributor=None, valueDataRequirement=None, valueExpression=None, valueParameterDefinition=None, valueRelatedArtifact=None, valueTriggerDefinition=None, valueUsageContext=None, valueDosage=None, valueMeta=None, **kwargs_):
        super(ExtensionSub, self).__init__(id, extension, url, valueBase64Binary, valueBoolean, valueCanonical, valueCode, valueDate, valueDateTime, valueDecimal, valueId, valueInstant, valueInteger, valueMarkdown, valueOid, valuePositiveInt, valueString, valueTime, valueUnsignedInt, valueUri, valueUrl, valueUuid, valueAddress, valueAge, valueAnnotation, valueAttachment, valueCodeableConcept, valueCoding, valueContactPoint, valueCount, valueDistance, valueDuration, valueHumanName, valueIdentifier, valueMoney, valuePeriod, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueTiming, valueContactDetail, valueContributor, valueDataRequirement, valueExpression, valueParameterDefinition, valueRelatedArtifact, valueTriggerDefinition, valueUsageContext, valueDosage, valueMeta,  **kwargs_)
supermod.Extension.subclass = ExtensionSub
# end class ExtensionSub


class decimalSub(supermod.decimal):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(decimalSub, self).__init__(id, extension, value,  **kwargs_)
supermod.decimal.subclass = decimalSub
# end class decimalSub


class positiveIntSub(supermod.positiveInt):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(positiveIntSub, self).__init__(id, extension, value,  **kwargs_)
supermod.positiveInt.subclass = positiveIntSub
# end class positiveIntSub


class idSub(supermod.id):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(idSub, self).__init__(id, extension, value,  **kwargs_)
supermod.id.subclass = idSub
# end class idSub


class timeSub(supermod.time):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(timeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.time.subclass = timeSub
# end class timeSub


class markdownSub(supermod.markdown):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(markdownSub, self).__init__(id, extension, value,  **kwargs_)
supermod.markdown.subclass = markdownSub
# end class markdownSub


class unsignedIntSub(supermod.unsignedInt):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(unsignedIntSub, self).__init__(id, extension, value,  **kwargs_)
supermod.unsignedInt.subclass = unsignedIntSub
# end class unsignedIntSub


class base64BinarySub(supermod.base64Binary):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(base64BinarySub, self).__init__(id, extension, value,  **kwargs_)
supermod.base64Binary.subclass = base64BinarySub
# end class base64BinarySub


class booleanSub(supermod.boolean):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(booleanSub, self).__init__(id, extension, value,  **kwargs_)
supermod.boolean.subclass = booleanSub
# end class booleanSub


class instantSub(supermod.instant):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(instantSub, self).__init__(id, extension, value,  **kwargs_)
supermod.instant.subclass = instantSub
# end class instantSub


class urlSub(supermod.url):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(urlSub, self).__init__(id, extension, value,  **kwargs_)
supermod.url.subclass = urlSub
# end class urlSub


class uuidSub(supermod.uuid):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(uuidSub, self).__init__(id, extension, value,  **kwargs_)
supermod.uuid.subclass = uuidSub
# end class uuidSub


class uriSub(supermod.uri):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(uriSub, self).__init__(id, extension, value,  **kwargs_)
supermod.uri.subclass = uriSub
# end class uriSub


class canonicalSub(supermod.canonical):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(canonicalSub, self).__init__(id, extension, value,  **kwargs_)
supermod.canonical.subclass = canonicalSub
# end class canonicalSub


class oidSub(supermod.oid):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(oidSub, self).__init__(id, extension, value,  **kwargs_)
supermod.oid.subclass = oidSub
# end class oidSub


class integerSub(supermod.integer):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(integerSub, self).__init__(id, extension, value,  **kwargs_)
supermod.integer.subclass = integerSub
# end class integerSub


class stringSub(supermod.string):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(stringSub, self).__init__(id, extension, value,  **kwargs_)
supermod.string.subclass = stringSub
# end class stringSub


class codeSub(supermod.code):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(codeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.code.subclass = codeSub
# end class codeSub


class dateTimeSub(supermod.dateTime):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(dateTimeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.dateTime.subclass = dateTimeSub
# end class dateTimeSub


class dateSub(supermod.date):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(dateSub, self).__init__(id, extension, value,  **kwargs_)
supermod.date.subclass = dateSub
# end class dateSub


class CodeSystemContentModeSub(supermod.CodeSystemContentMode):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(CodeSystemContentModeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.CodeSystemContentMode.subclass = CodeSystemContentModeSub
# end class CodeSystemContentModeSub


class CodeSystemHierarchyMeaningSub(supermod.CodeSystemHierarchyMeaning):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(CodeSystemHierarchyMeaningSub, self).__init__(id, extension, value,  **kwargs_)
supermod.CodeSystemHierarchyMeaning.subclass = CodeSystemHierarchyMeaningSub
# end class CodeSystemHierarchyMeaningSub


class PropertyTypeSub(supermod.PropertyType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(PropertyTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.PropertyType.subclass = PropertyTypeSub
# end class PropertyTypeSub


class FilterOperatorSub(supermod.FilterOperator):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(FilterOperatorSub, self).__init__(id, extension, value,  **kwargs_)
supermod.FilterOperator.subclass = FilterOperatorSub
# end class FilterOperatorSub


class CodeSystem_Property1Sub(supermod.CodeSystem_Property1):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, valueCode=None, valueCoding=None, valueString=None, valueInteger=None, valueBoolean=None, valueDateTime=None, valueDecimal=None, **kwargs_):
        super(CodeSystem_Property1Sub, self).__init__(id, extension, modifierExtension, code, valueCode, valueCoding, valueString, valueInteger, valueBoolean, valueDateTime, valueDecimal,  **kwargs_)
supermod.CodeSystem_Property1.subclass = CodeSystem_Property1Sub
# end class CodeSystem_Property1Sub


class CodeSystem_DesignationSub(supermod.CodeSystem_Designation):
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, use=None, value=None, **kwargs_):
        super(CodeSystem_DesignationSub, self).__init__(id, extension, modifierExtension, language, use, value,  **kwargs_)
supermod.CodeSystem_Designation.subclass = CodeSystem_DesignationSub
# end class CodeSystem_DesignationSub


class CodeSystem_ConceptSub(supermod.CodeSystem_Concept):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, display=None, definition=None, designation=None, property=None, concept=None, **kwargs_):
        super(CodeSystem_ConceptSub, self).__init__(id, extension, modifierExtension, code, display, definition, designation, property, concept,  **kwargs_)
supermod.CodeSystem_Concept.subclass = CodeSystem_ConceptSub
# end class CodeSystem_ConceptSub


class CodeSystem_PropertySub(supermod.CodeSystem_Property):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, uri=None, description=None, type_=None, **kwargs_):
        super(CodeSystem_PropertySub, self).__init__(id, extension, modifierExtension, code, uri, description, type_,  **kwargs_)
supermod.CodeSystem_Property.subclass = CodeSystem_PropertySub
# end class CodeSystem_PropertySub


class CodeSystem_FilterSub(supermod.CodeSystem_Filter):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, description=None, operator=None, value=None, **kwargs_):
        super(CodeSystem_FilterSub, self).__init__(id, extension, modifierExtension, code, description, operator, value,  **kwargs_)
supermod.CodeSystem_Filter.subclass = CodeSystem_FilterSub
# end class CodeSystem_FilterSub

class ElementDefinition_DiscriminatorSub(supermod.ElementDefinition_Discriminator):
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, path=None, **kwargs_):
        super(ElementDefinition_DiscriminatorSub, self).__init__(id, extension, modifierExtension, type_, path,  **kwargs_)
supermod.ElementDefinition_Discriminator.subclass = ElementDefinition_DiscriminatorSub
# end class ElementDefinition_DiscriminatorSub


class ElementDefinition_BindingSub(supermod.ElementDefinition_Binding):
    def __init__(self, id=None, extension=None, modifierExtension=None, strength=None, description=None, valueSet=None, **kwargs_):
        super(ElementDefinition_BindingSub, self).__init__(id, extension, modifierExtension, strength, description, valueSet,  **kwargs_)
supermod.ElementDefinition_Binding.subclass = ElementDefinition_BindingSub
# end class ElementDefinition_BindingSub


class ElementDefinition_SlicingSub(supermod.ElementDefinition_Slicing):
    def __init__(self, id=None, extension=None, modifierExtension=None, discriminator=None, description=None, ordered=None, rules=None, **kwargs_):
        super(ElementDefinition_SlicingSub, self).__init__(id, extension, modifierExtension, discriminator, description, ordered, rules,  **kwargs_)
supermod.ElementDefinition_Slicing.subclass = ElementDefinition_SlicingSub
# end class ElementDefinition_SlicingSub


class ElementDefinition_ExampleSub(supermod.ElementDefinition_Example):
    def __init__(self, id=None, extension=None, modifierExtension=None, label=None, valueBase64Binary=None, valueBoolean=None, valueCanonical=None, valueCode=None, valueDate=None, valueDateTime=None, valueDecimal=None, valueId=None, valueInstant=None, valueInteger=None, valueMarkdown=None, valueOid=None, valuePositiveInt=None, valueString=None, valueTime=None, valueUnsignedInt=None, valueUri=None, valueUrl=None, valueUuid=None, valueAddress=None, valueAge=None, valueAnnotation=None, valueAttachment=None, valueCodeableConcept=None, valueCoding=None, valueContactPoint=None, valueCount=None, valueDistance=None, valueDuration=None, valueHumanName=None, valueIdentifier=None, valueMoney=None, valuePeriod=None, valueQuantity=None, valueRange=None, valueRatio=None, valueReference=None, valueSampledData=None, valueSignature=None, valueTiming=None, valueContactDetail=None, valueContributor=None, valueDataRequirement=None, valueExpression=None, valueParameterDefinition=None, valueRelatedArtifact=None, valueTriggerDefinition=None, valueUsageContext=None, valueDosage=None, valueMeta=None, **kwargs_):
        super(ElementDefinition_ExampleSub, self).__init__(id, extension, modifierExtension, label, valueBase64Binary, valueBoolean, valueCanonical, valueCode, valueDate, valueDateTime, valueDecimal, valueId, valueInstant, valueInteger, valueMarkdown, valueOid, valuePositiveInt, valueString, valueTime, valueUnsignedInt, valueUri, valueUrl, valueUuid, valueAddress, valueAge, valueAnnotation, valueAttachment, valueCodeableConcept, valueCoding, valueContactPoint, valueCount, valueDistance, valueDuration, valueHumanName, valueIdentifier, valueMoney, valuePeriod, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueTiming, valueContactDetail, valueContributor, valueDataRequirement, valueExpression, valueParameterDefinition, valueRelatedArtifact, valueTriggerDefinition, valueUsageContext, valueDosage, valueMeta,  **kwargs_)
supermod.ElementDefinition_Example.subclass = ElementDefinition_ExampleSub
# end class ElementDefinition_ExampleSub


class ElementDefinition_TypeSub(supermod.ElementDefinition_Type):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, profile=None, targetProfile=None, aggregation=None, versioning=None, **kwargs_):
        super(ElementDefinition_TypeSub, self).__init__(id, extension, modifierExtension, code, profile, targetProfile, aggregation, versioning,  **kwargs_)
supermod.ElementDefinition_Type.subclass = ElementDefinition_TypeSub
# end class ElementDefinition_TypeSub


class ElementDefinition_BaseSub(supermod.ElementDefinition_Base):
    def __init__(self, id=None, extension=None, modifierExtension=None, path=None, min=None, max=None, **kwargs_):
        super(ElementDefinition_BaseSub, self).__init__(id, extension, modifierExtension, path, min, max,  **kwargs_)
supermod.ElementDefinition_Base.subclass = ElementDefinition_BaseSub
# end class ElementDefinition_BaseSub


class ElementDefinition_MappingSub(supermod.ElementDefinition_Mapping):
    def __init__(self, id=None, extension=None, modifierExtension=None, identity=None, language=None, map=None, comment=None, **kwargs_):
        super(ElementDefinition_MappingSub, self).__init__(id, extension, modifierExtension, identity, language, map, comment,  **kwargs_)
supermod.ElementDefinition_Mapping.subclass = ElementDefinition_MappingSub
# end class ElementDefinition_MappingSub


class ElementDefinition_ConstraintSub(supermod.ElementDefinition_Constraint):
    def __init__(self, id=None, extension=None, modifierExtension=None, key=None, requirements=None, severity=None, human=None, expression=None, xpath=None, source=None, **kwargs_):
        super(ElementDefinition_ConstraintSub, self).__init__(id, extension, modifierExtension, key, requirements, severity, human, expression, xpath, source,  **kwargs_)
supermod.ElementDefinition_Constraint.subclass = ElementDefinition_ConstraintSub
# end class ElementDefinition_ConstraintSub


class ElementDefinitionSub(supermod.ElementDefinition):
    def __init__(self, id=None, extension=None, modifierExtension=None, path=None, representation=None, sliceName=None, sliceIsConstraining=None, label=None, code=None, slicing=None, short=None, definition=None, comment=None, requirements=None, alias=None, min=None, max=None, base=None, contentReference=None, type_=None, defaultValueBase64Binary=None, defaultValueBoolean=None, defaultValueCanonical=None, defaultValueCode=None, defaultValueDate=None, defaultValueDateTime=None, defaultValueDecimal=None, defaultValueId=None, defaultValueInstant=None, defaultValueInteger=None, defaultValueMarkdown=None, defaultValueOid=None, defaultValuePositiveInt=None, defaultValueString=None, defaultValueTime=None, defaultValueUnsignedInt=None, defaultValueUri=None, defaultValueUrl=None, defaultValueUuid=None, defaultValueAddress=None, defaultValueAge=None, defaultValueAnnotation=None, defaultValueAttachment=None, defaultValueCodeableConcept=None, defaultValueCoding=None, defaultValueContactPoint=None, defaultValueCount=None, defaultValueDistance=None, defaultValueDuration=None, defaultValueHumanName=None, defaultValueIdentifier=None, defaultValueMoney=None, defaultValuePeriod=None, defaultValueQuantity=None, defaultValueRange=None, defaultValueRatio=None, defaultValueReference=None, defaultValueSampledData=None, defaultValueSignature=None, defaultValueTiming=None, defaultValueContactDetail=None, defaultValueContributor=None, defaultValueDataRequirement=None, defaultValueExpression=None, defaultValueParameterDefinition=None, defaultValueRelatedArtifact=None, defaultValueTriggerDefinition=None, defaultValueUsageContext=None, defaultValueDosage=None, defaultValueMeta=None, meaningWhenMissing=None, orderMeaning=None, fixedBase64Binary=None, fixedBoolean=None, fixedCanonical=None, fixedCode=None, fixedDate=None, fixedDateTime=None, fixedDecimal=None, fixedId=None, fixedInstant=None, fixedInteger=None, fixedMarkdown=None, fixedOid=None, fixedPositiveInt=None, fixedString=None, fixedTime=None, fixedUnsignedInt=None, fixedUri=None, fixedUrl=None, fixedUuid=None, fixedAddress=None, fixedAge=None, fixedAnnotation=None, fixedAttachment=None, fixedCodeableConcept=None, fixedCoding=None, fixedContactPoint=None, fixedCount=None, fixedDistance=None, fixedDuration=None, fixedHumanName=None, fixedIdentifier=None, fixedMoney=None, fixedPeriod=None, fixedQuantity=None, fixedRange=None, fixedRatio=None, fixedReference=None, fixedSampledData=None, fixedSignature=None, fixedTiming=None, fixedContactDetail=None, fixedContributor=None, fixedDataRequirement=None, fixedExpression=None, fixedParameterDefinition=None, fixedRelatedArtifact=None, fixedTriggerDefinition=None, fixedUsageContext=None, fixedDosage=None, fixedMeta=None, patternBase64Binary=None, patternBoolean=None, patternCanonical=None, patternCode=None, patternDate=None, patternDateTime=None, patternDecimal=None, patternId=None, patternInstant=None, patternInteger=None, patternMarkdown=None, patternOid=None, patternPositiveInt=None, patternString=None, patternTime=None, patternUnsignedInt=None, patternUri=None, patternUrl=None, patternUuid=None, patternAddress=None, patternAge=None, patternAnnotation=None, patternAttachment=None, patternCodeableConcept=None, patternCoding=None, patternContactPoint=None, patternCount=None, patternDistance=None, patternDuration=None, patternHumanName=None, patternIdentifier=None, patternMoney=None, patternPeriod=None, patternQuantity=None, patternRange=None, patternRatio=None, patternReference=None, patternSampledData=None, patternSignature=None, patternTiming=None, patternContactDetail=None, patternContributor=None, patternDataRequirement=None, patternExpression=None, patternParameterDefinition=None, patternRelatedArtifact=None, patternTriggerDefinition=None, patternUsageContext=None, patternDosage=None, patternMeta=None, example=None, minValueDate=None, minValueDateTime=None, minValueInstant=None, minValueTime=None, minValueDecimal=None, minValueInteger=None, minValuePositiveInt=None, minValueUnsignedInt=None, minValueQuantity=None, maxValueDate=None, maxValueDateTime=None, maxValueInstant=None, maxValueTime=None, maxValueDecimal=None, maxValueInteger=None, maxValuePositiveInt=None, maxValueUnsignedInt=None, maxValueQuantity=None, maxLength=None, condition=None, constraint=None, mustSupport=None, isModifier=None, isModifierReason=None, isSummary=None, binding=None, mapping=None, **kwargs_):
        super(ElementDefinitionSub, self).__init__(id, extension, modifierExtension, path, representation, sliceName, sliceIsConstraining, label, code, slicing, short, definition, comment, requirements, alias, min, max, base, contentReference, type_, defaultValueBase64Binary, defaultValueBoolean, defaultValueCanonical, defaultValueCode, defaultValueDate, defaultValueDateTime, defaultValueDecimal, defaultValueId, defaultValueInstant, defaultValueInteger, defaultValueMarkdown, defaultValueOid, defaultValuePositiveInt, defaultValueString, defaultValueTime, defaultValueUnsignedInt, defaultValueUri, defaultValueUrl, defaultValueUuid, defaultValueAddress, defaultValueAge, defaultValueAnnotation, defaultValueAttachment, defaultValueCodeableConcept, defaultValueCoding, defaultValueContactPoint, defaultValueCount, defaultValueDistance, defaultValueDuration, defaultValueHumanName, defaultValueIdentifier, defaultValueMoney, defaultValuePeriod, defaultValueQuantity, defaultValueRange, defaultValueRatio, defaultValueReference, defaultValueSampledData, defaultValueSignature, defaultValueTiming, defaultValueContactDetail, defaultValueContributor, defaultValueDataRequirement, defaultValueExpression, defaultValueParameterDefinition, defaultValueRelatedArtifact, defaultValueTriggerDefinition, defaultValueUsageContext, defaultValueDosage, defaultValueMeta, meaningWhenMissing, orderMeaning, fixedBase64Binary, fixedBoolean, fixedCanonical, fixedCode, fixedDate, fixedDateTime, fixedDecimal, fixedId, fixedInstant, fixedInteger, fixedMarkdown, fixedOid, fixedPositiveInt, fixedString, fixedTime, fixedUnsignedInt, fixedUri, fixedUrl, fixedUuid, fixedAddress, fixedAge, fixedAnnotation, fixedAttachment, fixedCodeableConcept, fixedCoding, fixedContactPoint, fixedCount, fixedDistance, fixedDuration, fixedHumanName, fixedIdentifier, fixedMoney, fixedPeriod, fixedQuantity, fixedRange, fixedRatio, fixedReference, fixedSampledData, fixedSignature, fixedTiming, fixedContactDetail, fixedContributor, fixedDataRequirement, fixedExpression, fixedParameterDefinition, fixedRelatedArtifact, fixedTriggerDefinition, fixedUsageContext, fixedDosage, fixedMeta, patternBase64Binary, patternBoolean, patternCanonical, patternCode, patternDate, patternDateTime, patternDecimal, patternId, patternInstant, patternInteger, patternMarkdown, patternOid, patternPositiveInt, patternString, patternTime, patternUnsignedInt, patternUri, patternUrl, patternUuid, patternAddress, patternAge, patternAnnotation, patternAttachment, patternCodeableConcept, patternCoding, patternContactPoint, patternCount, patternDistance, patternDuration, patternHumanName, patternIdentifier, patternMoney, patternPeriod, patternQuantity, patternRange, patternRatio, patternReference, patternSampledData, patternSignature, patternTiming, patternContactDetail, patternContributor, patternDataRequirement, patternExpression, patternParameterDefinition, patternRelatedArtifact, patternTriggerDefinition, patternUsageContext, patternDosage, patternMeta, example, minValueDate, minValueDateTime, minValueInstant, minValueTime, minValueDecimal, minValueInteger, minValuePositiveInt, minValueUnsignedInt, minValueQuantity, maxValueDate, maxValueDateTime, maxValueInstant, maxValueTime, maxValueDecimal, maxValueInteger, maxValuePositiveInt, maxValueUnsignedInt, maxValueQuantity, maxLength, condition, constraint, mustSupport, isModifier, isModifierReason, isSummary, binding, mapping,  **kwargs_)
supermod.ElementDefinition.subclass = ElementDefinitionSub
# end class ElementDefinitionSub


class ProdCharacteristicSub(supermod.ProdCharacteristic):
    def __init__(self, id=None, extension=None, modifierExtension=None, height=None, width=None, depth=None, weight=None, nominalVolume=None, externalDiameter=None, shape=None, color=None, imprint=None, image=None, scoring=None, **kwargs_):
        super(ProdCharacteristicSub, self).__init__(id, extension, modifierExtension, height, width, depth, weight, nominalVolume, externalDiameter, shape, color, imprint, image, scoring,  **kwargs_)
supermod.ProdCharacteristic.subclass = ProdCharacteristicSub
# end class ProdCharacteristicSub


class Timing_RepeatSub(supermod.Timing_Repeat):
    def __init__(self, id=None, extension=None, modifierExtension=None, boundsDuration=None, boundsRange=None, boundsPeriod=None, count=None, countMax=None, duration=None, durationMax=None, durationUnit=None, frequency=None, frequencyMax=None, period=None, periodMax=None, periodUnit=None, dayOfWeek=None, timeOfDay=None, when=None, offset=None, **kwargs_):
        super(Timing_RepeatSub, self).__init__(id, extension, modifierExtension, boundsDuration, boundsRange, boundsPeriod, count, countMax, duration, durationMax, durationUnit, frequency, frequencyMax, period, periodMax, periodUnit, dayOfWeek, timeOfDay, when, offset,  **kwargs_)
supermod.Timing_Repeat.subclass = Timing_RepeatSub
# end class Timing_RepeatSub


class TimingSub(supermod.Timing):
    def __init__(self, id=None, extension=None, modifierExtension=None, event=None, repeat=None, code=None, **kwargs_):
        super(TimingSub, self).__init__(id, extension, modifierExtension, event, repeat, code,  **kwargs_)
supermod.Timing.subclass = TimingSub
# end class TimingSub


class ProductShelfLifeSub(supermod.ProductShelfLife):
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, type_=None, period=None, specialPrecautionsForStorage=None, **kwargs_):
        super(ProductShelfLifeSub, self).__init__(id, extension, modifierExtension, identifier, type_, period, specialPrecautionsForStorage,  **kwargs_)
supermod.ProductShelfLife.subclass = ProductShelfLifeSub
# end class ProductShelfLifeSub


class PopulationSub(supermod.Population):
    def __init__(self, id=None, extension=None, modifierExtension=None, ageRange=None, ageCodeableConcept=None, gender=None, race=None, physiologicalCondition=None, **kwargs_):
        super(PopulationSub, self).__init__(id, extension, modifierExtension, ageRange, ageCodeableConcept, gender, race, physiologicalCondition,  **kwargs_)
supermod.Population.subclass = PopulationSub
# end class PopulationSub


class SubstanceAmount_ReferenceRangeSub(supermod.SubstanceAmount_ReferenceRange):
    def __init__(self, id=None, extension=None, modifierExtension=None, lowLimit=None, highLimit=None, **kwargs_):
        super(SubstanceAmount_ReferenceRangeSub, self).__init__(id, extension, modifierExtension, lowLimit, highLimit,  **kwargs_)
supermod.SubstanceAmount_ReferenceRange.subclass = SubstanceAmount_ReferenceRangeSub
# end class SubstanceAmount_ReferenceRangeSub


class SubstanceAmountSub(supermod.SubstanceAmount):
    def __init__(self, id=None, extension=None, modifierExtension=None, amountQuantity=None, amountRange=None, amountString=None, amountType=None, amountText=None, referenceRange=None, **kwargs_):
        super(SubstanceAmountSub, self).__init__(id, extension, modifierExtension, amountQuantity, amountRange, amountString, amountType, amountText, referenceRange,  **kwargs_)
supermod.SubstanceAmount.subclass = SubstanceAmountSub
# end class SubstanceAmountSub


class MarketingStatusSub(supermod.MarketingStatus):
    def __init__(self, id=None, extension=None, modifierExtension=None, country=None, jurisdiction=None, status=None, dateRange=None, restoreDate=None, **kwargs_):
        super(MarketingStatusSub, self).__init__(id, extension, modifierExtension, country, jurisdiction, status, dateRange, restoreDate,  **kwargs_)
supermod.MarketingStatus.subclass = MarketingStatusSub
# end class MarketingStatusSub


class Dosage_DoseAndRateSub(supermod.Dosage_DoseAndRate):
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, doseRange=None, doseQuantity=None, rateRatio=None, rateRange=None, rateQuantity=None, **kwargs_):
        super(Dosage_DoseAndRateSub, self).__init__(id, extension, modifierExtension, type_, doseRange, doseQuantity, rateRatio, rateRange, rateQuantity,  **kwargs_)
supermod.Dosage_DoseAndRate.subclass = Dosage_DoseAndRateSub
# end class Dosage_DoseAndRateSub


class DosageSub(supermod.Dosage):
    def __init__(self, id=None, extension=None, modifierExtension=None, sequence=None, text=None, additionalInstruction=None, patientInstruction=None, timing=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, doseAndRate=None, maxDosePerPeriod=None, maxDosePerAdministration=None, maxDosePerLifetime=None, **kwargs_):
        super(DosageSub, self).__init__(id, extension, modifierExtension, sequence, text, additionalInstruction, patientInstruction, timing, asNeededBoolean, asNeededCodeableConcept, site, route, method, doseAndRate, maxDosePerPeriod, maxDosePerAdministration, maxDosePerLifetime,  **kwargs_)
supermod.Dosage.subclass = DosageSub
# end class DosageSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CodeSystem'
        rootClass = supermod.CodeSystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
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
        rootTag = 'CodeSystem'
        rootClass = supermod.CodeSystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
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
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'CodeSystem'
        rootClass = supermod.CodeSystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
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
        rootTag = 'CodeSystem'
        rootClass = supermod.CodeSystem
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
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
