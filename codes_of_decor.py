#!/usr/bin/env python

#
# Generated Tue May 18 07:56:22 2021 by generateDS.py version 2.38.6.
# Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'codes_of_decor_super.py')
#   ('-s', 'codes_of_decor.py')
#
# Command line arguments:
#   Codes-like-C-of-DECOR.xsd
#
# Command line:
#   generateDS.py -o "codes_of_decor_super.py" -s "codes_of_decor.py" Codes-like-C-of-DECOR.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.38.6
#

import os
import sys
from lxml import etree as etree_

import codes_of_decor_super as supermod
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


class decorSub(supermod.decor, pcam.PropCsvAndMaster):
    def __init__(self, repository=None, private=None, release='1000', versionDate=None, versionLabel=None, compilationDate=None, language=None, deeplinkprefix=None, deeplinkprefixservices=None, terminology=None, **kwargs_):
        super(decorSub, self).__init__(repository, private, release, versionDate, versionLabel, compilationDate, language, deeplinkprefix, deeplinkprefixservices, terminology,  **kwargs_)

    

supermod.decor.subclass = decorSub
# end class decorSub


class addrLineSub(supermod.addrLine):
    def __init__(self, type_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(addrLineSub, self).__init__(type_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.addrLine.subclass = addrLineSub
# end class addrLineSub


class identifierAssociationSub(supermod.identifierAssociation):
    def __init__(self, conceptId=None, conceptFlexibility=None, ref=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, refdisplay=None, **kwargs_):
        super(identifierAssociationSub, self).__init__(conceptId, conceptFlexibility, ref, effectiveDate, expirationDate, officialReleaseDate, versionLabel, refdisplay,  **kwargs_)
supermod.identifierAssociation.subclass = identifierAssociationSub
# end class identifierAssociationSub


class terminologySub(supermod.terminology):
    def __init__(self, terminologyAssociation=None, codeSystem=None, valueSet=None, conceptAssociation=None, **kwargs_):
        super(terminologySub, self).__init__(terminologyAssociation, codeSystem, valueSet, conceptAssociation,  **kwargs_)
supermod.terminology.subclass = terminologySub
# end class terminologySub


class terminologyAssociationSub(supermod.terminologyAssociation):
    def __init__(self, conceptId=None, conceptFlexibility=None, code=None, codeSystem=None, codeSystemName=None, displayName=None, valueSet=None, flexibility=None, strength='required', equivalence=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, valueSetName=None, **kwargs_):
        super(terminologyAssociationSub, self).__init__(conceptId, conceptFlexibility, code, codeSystem, codeSystemName, displayName, valueSet, flexibility, strength, equivalence, effectiveDate, expirationDate, officialReleaseDate, versionLabel, valueSetName,  **kwargs_)
supermod.terminologyAssociation.subclass = terminologyAssociationSub
# end class terminologyAssociationSub


class conceptAssociationSub(supermod.conceptAssociation):
    def __init__(self, id=None, displayName=None, statusCode=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, desc=None, source=None, target=None, group=None, **kwargs_):
        super(conceptAssociationSub, self).__init__(id, displayName, statusCode, effectiveDate, expirationDate, officialReleaseDate, versionLabel, desc, source, target, group,  **kwargs_)
supermod.conceptAssociation.subclass = conceptAssociationSub
# end class conceptAssociationSub


class SourceOrTargetValueSetSub(supermod.SourceOrTargetValueSet):
    def __init__(self, ref=None, flexibility=None, displayName=None, **kwargs_):
        super(SourceOrTargetValueSetSub, self).__init__(ref, flexibility, displayName,  **kwargs_)
supermod.SourceOrTargetValueSet.subclass = SourceOrTargetValueSetSub
# end class SourceOrTargetValueSetSub


class ConceptMapGroupDefinitionSub(supermod.ConceptMapGroupDefinition):
    def __init__(self, source=None, target=None, element=None, **kwargs_):
        super(ConceptMapGroupDefinitionSub, self).__init__(source, target, element,  **kwargs_)
supermod.ConceptMapGroupDefinition.subclass = ConceptMapGroupDefinitionSub
# end class ConceptMapGroupDefinitionSub


class SourceOrTargetCodeSystemSub(supermod.SourceOrTargetCodeSystem):
    def __init__(self, codeSystem=None, **kwargs_):
        super(SourceOrTargetCodeSystemSub, self).__init__(codeSystem,  **kwargs_)
supermod.SourceOrTargetCodeSystem.subclass = SourceOrTargetCodeSystemSub
# end class SourceOrTargetCodeSystemSub


class ConceptMapElementSub(supermod.ConceptMapElement):
    def __init__(self, code=None, displayName=None, target=None, **kwargs_):
        super(ConceptMapElementSub, self).__init__(code, displayName, target,  **kwargs_)
supermod.ConceptMapElement.subclass = ConceptMapElementSub
# end class ConceptMapElementSub


class ConceptMapTargetSub(supermod.ConceptMapTarget):
    def __init__(self, code=None, displayName=None, equivalence=None, comment=None, **kwargs_):
        super(ConceptMapTargetSub, self).__init__(code, displayName, equivalence, comment,  **kwargs_)
supermod.ConceptMapTarget.subclass = ConceptMapTargetSub
# end class ConceptMapTargetSub


class EquivalencyTypeDefinitionSub(supermod.EquivalencyTypeDefinition):
    def __init__(self, code=None, **kwargs_):
        super(EquivalencyTypeDefinitionSub, self).__init__(code,  **kwargs_)
supermod.EquivalencyTypeDefinition.subclass = EquivalencyTypeDefinitionSub
# end class EquivalencyTypeDefinitionSub


class valueSetSub(supermod.valueSet):
    def __init__(self, id=None, canonicalUri=None, ref=None, name=None, displayName=None, statusCode=None, experimental=None, flexibility=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, url=None, ident=None, referencedFrom=None, desc=None, sourceCodeSystem=None, publishingAuthority=None, endorsingAuthority=None, purpose=None, copyright=None, revisionHistory=None, completeCodeSystem=None, conceptList=None, **kwargs_):
        super(valueSetSub, self).__init__(id, canonicalUri, ref, name, displayName, statusCode, experimental, flexibility, effectiveDate, expirationDate, officialReleaseDate, versionLabel, url, ident, referencedFrom, desc, sourceCodeSystem, publishingAuthority, endorsingAuthority, purpose, copyright, revisionHistory, completeCodeSystem, conceptList,  **kwargs_)
supermod.valueSet.subclass = valueSetSub
# end class valueSetSub


class CodeSystemReferenceSub(supermod.CodeSystemReference):
    def __init__(self, codeSystem=None, codeSystemName=None, codeSystemVersion=None, flexibility=None, type_='D', **kwargs_):
        super(CodeSystemReferenceSub, self).__init__(codeSystem, codeSystemName, codeSystemVersion, flexibility, type_,  **kwargs_)
supermod.CodeSystemReference.subclass = CodeSystemReferenceSub
# end class CodeSystemReferenceSub


class ValueSetConceptListSub(supermod.ValueSetConceptList):
    def __init__(self, concept=None, include=None, exclude=None, exception=None, **kwargs_):
        super(ValueSetConceptListSub, self).__init__(concept, include, exclude, exception,  **kwargs_)
supermod.ValueSetConceptList.subclass = ValueSetConceptListSub
# end class ValueSetConceptListSub


class ValueSetConceptSub(supermod.ValueSetConcept):
    def __init__(self, code=None, codeSystem=None, codeSystemName=None, codeSystemVersion=None, displayName=None, ordinal=None, level=None, type_=None, designation=None, desc=None, **kwargs_):
        super(ValueSetConceptSub, self).__init__(code, codeSystem, codeSystemName, codeSystemVersion, displayName, ordinal, level, type_, designation, desc,  **kwargs_)
supermod.ValueSetConcept.subclass = ValueSetConceptSub
# end class ValueSetConceptSub


class ValueSetRefOrIntensionalOpSub(supermod.ValueSetRefOrIntensionalOp):
    def __init__(self, ref=None, flexibility=None, exception=False, url=None, ident=None, referencedFrom=None, op=None, code=None, codeSystem=None, codeSystemName=None, codeSystemVersion=None, displayName=None, designation=None, desc=None, **kwargs_):
        super(ValueSetRefOrIntensionalOpSub, self).__init__(ref, flexibility, exception, url, ident, referencedFrom, op, code, codeSystem, codeSystemName, codeSystemVersion, displayName, designation, desc,  **kwargs_)
supermod.ValueSetRefOrIntensionalOp.subclass = ValueSetRefOrIntensionalOpSub
# end class ValueSetRefOrIntensionalOpSub


class codeSystemSub(supermod.codeSystem):
    def __init__(self, id=None, canonicalUri=None, ref=None, name=None, displayName=None, statusCode=None, experimental=None, caseSensitive=True, flexibility=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, url=None, ident=None, referencedFrom=None, desc=None, publishingAuthority=None, endorsingAuthority=None, purpose=None, copyright=None, revisionHistory=None, conceptList=None, anytypeobjs_=None, **kwargs_):
        super(codeSystemSub, self).__init__(id, canonicalUri, ref, name, displayName, statusCode, experimental, caseSensitive, flexibility, effectiveDate, expirationDate, officialReleaseDate, versionLabel, url, ident, referencedFrom, desc, publishingAuthority, endorsingAuthority, purpose, copyright, revisionHistory, conceptList, anytypeobjs_,  **kwargs_)
supermod.codeSystem.subclass = codeSystemSub
# end class codeSystemSub


class CodeSystemConceptListSub(supermod.CodeSystemConceptList):
    def __init__(self, codedConcept=None, **kwargs_):
        super(CodeSystemConceptListSub, self).__init__(codedConcept,  **kwargs_)
supermod.CodeSystemConceptList.subclass = CodeSystemConceptListSub
# end class CodeSystemConceptListSub


class codedConceptSub(supermod.codedConcept):
    def __init__(self, code=None, statusCode='active', level=None, type_=None, ordinal=None, effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, designation=None, desc=None, **kwargs_):
        super(codedConceptSub, self).__init__(code, statusCode, level, type_, ordinal, effectiveDate, expirationDate, officialReleaseDate, versionLabel, designation, desc,  **kwargs_)
supermod.codedConcept.subclass = codedConceptSub
# end class codedConceptSub


class AuthorityTypeSub(supermod.AuthorityType):
    def __init__(self, id=None, name=None, addrLine=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(AuthorityTypeSub, self).__init__(id, name, addrLine, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.AuthorityType.subclass = AuthorityTypeSub
# end class AuthorityTypeSub


class ObjectHistorySub(supermod.ObjectHistory):
    def __init__(self, date=None, by=None, desc=None, **kwargs_):
        super(ObjectHistorySub, self).__init__(date, by, desc,  **kwargs_)
supermod.ObjectHistory.subclass = ObjectHistorySub
# end class ObjectHistorySub


class RuleDefinitionSub(supermod.RuleDefinition):
    def __init__(self, displayName=None, statusCode=None, name=None, include_attr=None, useWhere=False, contains=None, flexibility=None, conformance=None, isMandatory=None, id=None, datatype=None, isClosed=False, strength='required', effectiveDate=None, expirationDate=None, officialReleaseDate=None, versionLabel=None, minimumMultiplicity=None, maximumMultiplicity=None, desc=None, item=None, example=None, inherit=None, vocabulary=None, property=None, text=None, attribute=None, let=None, assert_=None, report=None, defineVariable=None, element=None, include=None, choice=None, constraint=None, **kwargs_):
        super(RuleDefinitionSub, self).__init__(displayName, statusCode, name, include_attr, useWhere, contains, flexibility, conformance, isMandatory, id, datatype, isClosed, strength, effectiveDate, expirationDate, officialReleaseDate, versionLabel, minimumMultiplicity, maximumMultiplicity, desc, item, example, inherit, vocabulary, property, text, attribute, let, assert_, report, defineVariable, element, include, choice, constraint,  **kwargs_)
supermod.RuleDefinition.subclass = RuleDefinitionSub
# end class RuleDefinitionSub


class IncludeDefinitionSub(supermod.IncludeDefinition):
    def __init__(self, ref=None, flexibility=None, scenario=None, effectiveDate=None, conformance=None, isMandatory=None, minimumMultiplicity=None, maximumMultiplicity=None, desc=None, item=None, example=None, constraint=None, **kwargs_):
        super(IncludeDefinitionSub, self).__init__(ref, flexibility, scenario, effectiveDate, conformance, isMandatory, minimumMultiplicity, maximumMultiplicity, desc, item, example, constraint,  **kwargs_)
supermod.IncludeDefinition.subclass = IncludeDefinitionSub
# end class IncludeDefinitionSub


class InheritDefinitionSub(supermod.InheritDefinition):
    def __init__(self, ref=None, effectiveDate=None, prefix=None, datasetId=None, datasetEffectiveDate=None, datasetExpirationDate=None, datasetStatusCode=None, datasetVersionLabel=None, iType=None, iStatusCode=None, iEffectiveDate=None, iVersionLabel=None, iExpirationDate=None, originalId=None, originalStatusCode=None, originalEffectiveDate=None, originalVersionLabel=None, originalExpirationDate=None, originalPrefix=None, refdisplay=None, localInherit=None, **kwargs_):
        super(InheritDefinitionSub, self).__init__(ref, effectiveDate, prefix, datasetId, datasetEffectiveDate, datasetExpirationDate, datasetStatusCode, datasetVersionLabel, iType, iStatusCode, iEffectiveDate, iVersionLabel, iExpirationDate, originalId, originalStatusCode, originalEffectiveDate, originalVersionLabel, originalExpirationDate, originalPrefix, refdisplay, localInherit,  **kwargs_)
supermod.InheritDefinition.subclass = InheritDefinitionSub
# end class InheritDefinitionSub


class ChoiceDefinitionSub(supermod.ChoiceDefinition):
    def __init__(self, minimumMultiplicity=None, maximumMultiplicity=None, desc=None, item=None, include=None, element=None, constraint=None, **kwargs_):
        super(ChoiceDefinitionSub, self).__init__(minimumMultiplicity, maximumMultiplicity, desc, item, include, element, constraint,  **kwargs_)
supermod.ChoiceDefinition.subclass = ChoiceDefinitionSub
# end class ChoiceDefinitionSub


class exampleSub(supermod.example):
    def __init__(self, type_='neutral', caption=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(exampleSub, self).__init__(type_, caption, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.example.subclass = exampleSub
# end class exampleSub


class letSub(supermod.let):
    def __init__(self, name=None, value=None, **kwargs_):
        super(letSub, self).__init__(name, value,  **kwargs_)
supermod.let.subclass = letSub
# end class letSub


class assert_Sub(supermod.assert_):
    def __init__(self, flag=None, see=None, role=None, test=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(assert_Sub, self).__init__(flag, see, role, test, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.assert_.subclass = assert_Sub
# end class assert_Sub


class reportSub(supermod.report):
    def __init__(self, flag=None, see=None, role=None, test=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(reportSub, self).__init__(flag, see, role, test, anytypeobjs_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.report.subclass = reportSub
# end class reportSub


class defineVariableSub(supermod.defineVariable):
    def __init__(self, name=None, path=None, code=None, use=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(defineVariableSub, self).__init__(name, path, code, use, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.defineVariable.subclass = defineVariableSub
# end class defineVariableSub


class VarCodeSub(supermod.VarCode):
    def __init__(self, code=None, codeSystem=None, **kwargs_):
        super(VarCodeSub, self).__init__(code, codeSystem,  **kwargs_)
supermod.VarCode.subclass = VarCodeSub
# end class VarCodeSub


class VarUseSub(supermod.VarUse):
    def __init__(self, path=None, as_=None, **kwargs_):
        super(VarUseSub, self).__init__(path, as_,  **kwargs_)
supermod.VarUse.subclass = VarUseSub
# end class VarUseSub


class itemSub(supermod.item):
    def __init__(self, label=None, desc=None, **kwargs_):
        super(itemSub, self).__init__(label, desc,  **kwargs_)
supermod.item.subclass = itemSub
# end class itemSub


class attributeSub(supermod.attribute):
    def __init__(self, name=None, value=None, classCode=None, contextConductionInd=None, contextControlCode=None, determinerCode=None, extension=None, independentInd=None, institutionSpecified=None, inversionInd=None, mediaType=None, moodCode=None, negationInd=None, nullFlavor=None, operator=None, qualifier=None, representation=None, root=None, typeCode=None, unit=None, use=None, isOptional=None, prohibited=None, datatype=None, id=None, desc=None, item=None, vocabulary=None, constraint=None, **kwargs_):
        super(attributeSub, self).__init__(name, value, classCode, contextConductionInd, contextControlCode, determinerCode, extension, independentInd, institutionSpecified, inversionInd, mediaType, moodCode, negationInd, nullFlavor, operator, qualifier, representation, root, typeCode, unit, use, isOptional, prohibited, datatype, id, desc, item, vocabulary, constraint,  **kwargs_)
supermod.attribute.subclass = attributeSub
# end class attributeSub


class propertySub(supermod.property):
    def __init__(self, unit=None, currency=None, minInclude=None, maxInclude=None, fractionDigits=None, minLength=None, maxLength=None, value=None, **kwargs_):
        super(propertySub, self).__init__(unit, currency, minInclude, maxInclude, fractionDigits, minLength, maxLength, value,  **kwargs_)
supermod.property.subclass = propertySub
# end class propertySub


class vocabularySub(supermod.vocabulary):
    def __init__(self, valueSet=None, flexibility=None, code=None, codeSystem=None, displayName=None, codeSystemName=None, domain=None, **kwargs_):
        super(vocabularySub, self).__init__(valueSet, flexibility, code, codeSystem, displayName, codeSystemName, domain,  **kwargs_)
supermod.vocabulary.subclass = vocabularySub
# end class vocabularySub


class BusinessNameWithLanguageSub(supermod.BusinessNameWithLanguage):
    def __init__(self, language='en-US', lastTranslated=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(BusinessNameWithLanguageSub, self).__init__(language, lastTranslated, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.BusinessNameWithLanguage.subclass = BusinessNameWithLanguageSub
# end class BusinessNameWithLanguageSub


class VariousMixedContentSub(supermod.VariousMixedContent):
    def __init__(self, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(VariousMixedContentSub, self).__init__(anytypeobjs_, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.VariousMixedContent.subclass = VariousMixedContentSub
# end class VariousMixedContentSub


class sourceCodeSystemTypeSub(supermod.sourceCodeSystemType):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(sourceCodeSystemTypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.sourceCodeSystemType.subclass = sourceCodeSystemTypeSub
# end class sourceCodeSystemTypeSub


class sourceCodeSystemType1Sub(supermod.sourceCodeSystemType1):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(sourceCodeSystemType1Sub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.sourceCodeSystemType1.subclass = sourceCodeSystemType1Sub
# end class sourceCodeSystemType1Sub


class FreeFormMarkupWithLanguageCodeSub(supermod.FreeFormMarkupWithLanguageCode):
    def __init__(self, anytypeobjs_=None, language=None, lastTranslated=None, mimeType=None, valueOf_=None, mixedclass_=None, content_=None, extensiontype_=None, **kwargs_):
        super(FreeFormMarkupWithLanguageCodeSub, self).__init__(anytypeobjs_, language, lastTranslated, mimeType, valueOf_, mixedclass_, content_, extensiontype_,  **kwargs_)
supermod.FreeFormMarkupWithLanguageCode.subclass = FreeFormMarkupWithLanguageCodeSub
# end class FreeFormMarkupWithLanguageCodeSub


class FreeFormMarkupWithLanguageSub(supermod.FreeFormMarkupWithLanguage):
    def __init__(self, anytypeobjs_=None, language=None, lastTranslated=None, mimeType=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(FreeFormMarkupWithLanguageSub, self).__init__(anytypeobjs_, language, lastTranslated, mimeType, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.FreeFormMarkupWithLanguage.subclass = FreeFormMarkupWithLanguageSub
# end class FreeFormMarkupWithLanguageSub


class designationSub(supermod.designation):
    def __init__(self, anytypeobjs_=None, language=None, lastTranslated=None, mimeType=None, type_=None, displayName=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(designationSub, self).__init__(anytypeobjs_, language, lastTranslated, mimeType, type_, displayName, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.designation.subclass = designationSub
# end class designationSub


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
        rootTag = 'decor'
        rootClass = supermod.decor
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


def parseEtree(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'decor'
        rootClass = supermod.decor
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


def parseString(inString, silence=True):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'decor'
        rootClass = supermod.decor
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


def parseLiteral(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'decor'
        rootClass = supermod.decor
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
