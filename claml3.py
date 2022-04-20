#!/usr/bin/env python

#
# Generated Thu Apr  8 15:08:49 2021 by generateDS.py version 2.38.5.
# Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)]
#
# Command line options:
#   ('-a', 'xml:')
#   ('-o', 'ClaML3Super.py')
#   ('-s', 'ClaML3.py')
#
# Command line arguments:
#   Y:\Termserver\MaLaC-CT\ClaML3.0.0.xsd
#
# Command line:
#   .\generateDS.py -a "xml:" -o "ClaML3Super.py" -s "ClaML3.py" Y:\Termserver\MaLaC-CT\ClaML3.0.0.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.38.5
#

import datetime
import os
import sys
from lxml import etree as etree_

import claml3super as supermod
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

def get_Meta_with_name(self,meta_name):
        for oneMeta in self.get_Classification()[0].get_Meta():
            if oneMeta.get_name == meta_name:
                return oneMeta.get_value()

class ClaML3Sub(supermod.ClaML3, pcam.PropCsvAndMaster):
    def __init__(self, version=None, Classification=None, **kwargs_):
        super(ClaML3Sub, self).__init__(version, Classification,  **kwargs_)

    # just for calling the outer method
    def parse(inFilename):
        return parse(inFilename)

    def get_resource(self):
        return get_Meta_with_name(self,'resource')

    def get_url(self):
        return get_Meta_with_name(self,'url')

    def get_identifier(self):
        identifiers = []
        for oneIdentifier in self.get_Classification()[0].get_Identifier():
            identifiers.append(oneIdentifier.get_uid())
        return identifiers

    def get_version(self):
        return self.get_Classification()[0].get_Title()[0].get_version()

    # todo: only override functions that are different to claml2
    def get_name(self):
        return self.get_Classification()[0].get_Title()[0].get_name()

    def get_title(self):
        return self.get_Classification()[0].get_Title()[0].get_valueOf_()

    def get_status(self):
        return self.get_Classification()[0].get_Identifier()[0].get_status()

    def get_experimental(self):
        return get_Meta_with_name(self,'experimental')

    def get_date(self):
        return self.get_Classification()[0].get_Identifier()[0].get_date()

    def get_publisher(self):
        return self.get_Classification()[0].get_Authors().get_Author()[0].get_name()

    def get_contact(self):
        return self.get_Classification()[0].get_Authors().get_Author()[0].get_valueOf_()

    def get_description(self):
        return get_Meta_with_name(self,'description')

    def get_usecontext(self):
        return get_Meta_with_name(self,'useContext')

    def get_jurisdiction(self):
        return get_Meta_with_name(self,'jurisdiction')

    def get_purpose(self):
        return get_Meta_with_name(self,'purpose')

    def get_copyright(self):
        return get_Meta_with_name(self,'copyright')

    def get_casesensitive(self):
        return get_Meta_with_name(self,'caseSensitive')

    def get_hierarchymeaning(self):
        return get_Meta_with_name(self,'hierarchyMeaning')

    def get_compositional(self):
        return get_Meta_with_name(self,'compositional')

    def get_versionneeded(self):
        return get_Meta_with_name(self,'versionNeeded')

    def get_content(self):
        return get_Meta_with_name(self,'content')

    def get_count(self):
        return len(self.get_Class())

    def get_filter(self):
        retArr = []
        for oneMeta in self.get_Classification()[0].get_Meta():
            if oneMeta.get_name == 'filter':
                oneFilter = pcam.Filter()
                oneFilter.code = oneMeta.get_value().split('|')[0]
                oneFilter.description = oneMeta.get_value().split('|')[1]
                oneFilter.operator = oneMeta.get_value().split('|')[2]
                oneFilter.value = oneMeta.get_value().split('|')[3]
                retArr.append(oneFilter)
        return retArr

    def get_property(self):
        retArr = []
        for oneMeta in self.get_Classification()[0].get_Meta():
            if oneMeta.get_name == 'property':
                oneProperty = pcam.Filter()
                oneProperty.code = oneMeta.get_value().split('|')[0]
                oneProperty.uri = oneMeta.get_value().split('|')[1]
                oneProperty.description = oneMeta.get_value().split('|')[2]
                oneProperty.type = oneMeta.get_value().split('|')[3]
                retArr.append(oneProperty)
        return self.appendAdditionalConceptProperties(retArr)

    def get_immutable(self):
        return get_Meta_with_name(self,'immutable')

    def get_lockeddate(self):
        return get_Meta_with_name(self,'lockedDate')

    def get_inactive(self):
        return get_Meta_with_name(self,'inactive')

    def get_implicitrules(self):
        return get_Meta_with_name(self,'implicitRules')

    def get_language(self):
        return self.get_Classification()[0].get_lang()

    def get_text(self):
        return get_Meta_with_name(self,'text')

    def get_contained(self):
        return get_Meta_with_name(self,'contained')

    def get_extension(self):
        return get_Meta_with_name(self,'extension')

    def get_modifierextension(self):
        return get_Meta_with_name(self,'modifierExtension')

    def get_concept(self):
        if hasattr(self, "concept") and self.concept:
            return self.concept
        else:
            retArr = []
            for oneClass in self.get_Classification()[0].get_class():
                theConcept = None
                theConcept = pcam.CSConcept
                theConcept.code = oneClass.get_code()
                for oneRubric in oneClass.get_Rubric():
                    if oneRubric.get_kind() == "preferred":
                        theConcept.display = oneRubric.get_Label()[0].get_valueOf_()
                    elif oneRubric.get_kind() == "definition":
                        theConcept.definition = oneRubric.get_Label()[0].get_valueOf_()
                    elif oneRubric.get_kind() == "designation":
                        splittedValue = oneRubric.get_Label()[0].get_valueOf_().split('|')
                        theDesignation = None
                        theDesignation = pcam.ConceptDesignation()
                        theDesignation.language = splittedValue[0]
                        theDesignation.use = splittedValue[1]
                        theDesignation.value = splittedValue[2]
                        theConcept.designation.append(theDesignation)
                for oneSuperClass in oneClass.get_SuperClass():
                    theProperty = None
                    theProperty = pcam.CSConcept.ConceptProperty
                    theProperty.code = "parent"
                    theProperty.value = oneSuperClass.get_code()
                    theConcept.property.append(theProperty)
                for oneSubClass in oneClass.get_SubClass():
                    theProperty = None
                    theProperty = pcam.CSConcept.ConceptProperty
                    theProperty.code = "child"
                    theProperty.value = oneSubClass.get_code()
                    theConcept.property.append(theProperty)
                for oneMeta in oneClass.get_Meta():
                    theProperty = None
                    theProperty = pcam.CSConcept.ConceptProperty
                    theProperty.code = oneMeta.get_name()
                    theProperty.value = oneMeta.get_value()
                    theConcept.property.append(theProperty)

                retArr.append(theConcept)
            self.concept = retArr
            return retArr

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        #required ClaMl3 fields
        claml3 = ClaML3Sub('3.0.0')
        if tmp := self.get_language():
            lang = self.get_language()
        elif argsLang is not None:
            lang = argsLang
        else:
            print("A language code is required in ClaMl3. Please type one in (i.e. 'en','de-DE' or 'de-AT') and press enter:")
            lang = input()
        title = TitleSub(self.get_name(),self.get_version(),None,self.get_title())
        claKinds = ClassKindsSub()
        claKinds.add_ClassKind(ClassKindSub("code"))
        rubKinds = RubricKindsSub()
        rubKinds.add_RubricKind(RubricKindSub("preferred"))

        #optional ClaMl3 fields
        #madatory FHIR fields
        metas = []
        metas.append(MetaSub('resource',self.get_resource()))
        metas.append(MetaSub('url',self.get_url()))
        identifiers = []
        mainIdent = IdentifierSub(status=self.get_status())
        identifiers.append(mainIdent)
        metas.append(MetaSub('description',self.get_description()))

        #conditional FHIR fields
        if self.get_resource() == 'CodeSystem': metas.append(MetaSub('content',self.get_content()))

        #optional FHIR fields
        if tmp := self.get_implicitrules(): metas.append(MetaSub('url',tmp))
        if tmp := self.get_text(): metas.append(MetaSub('text',tmp))
        if tmp := self.get_contained(): metas.append(MetaSub('contained',tmp))
        if tmp := self.get_extension(): metas.append(MetaSub('extension',tmp))
        if tmp := self.get_modifierextension(): metas.append(MetaSub('modifierextension',tmp))
        if tmp := self.get_identifier():
            for oneIdentifier in tmp:
                mainIdent.set_uid(oneIdentifier)
        if tmp := self.get_experimental(): metas.append(MetaSub('experimental',tmp))
        if tmp := self.get_date():
            mainIdent.set_date(datetime.datetime.strptime(tmp, '%Y-%m-%d'))
        authors = None
        if tmp := self.get_publisher():
            authors = AuthorsSub(Author=[AuthorSub(tmp)])
        if tmp := self.get_contact():
            if authors is None:
                authors = AuthorsSub()
            for oneContact in tmp:
                oneAuthor = AuthorSub(oneContact.name or None, None, oneContact.telecom[0].value or None)
                authors.get_Author().append(oneAuthor)
        if tmp := self.get_usecontext():
            for oneUseContext in tmp:
                metas.append(MetaSub('usecontext',oneUseContext))
        if tmp := self.get_jurisdiction():
            for oneJurisdiction in tmp:
                metas.append(MetaSub('jurisdiction',oneJurisdiction))
        if tmp := self.get_purpose(): metas.append(MetaSub("purpose",tmp))
        if tmp := self.get_copyright(): metas.append(MetaSub("copyright",tmp))
        if tmp := self.get_immutable(): metas.append(MetaSub("immutable",tmp))
        if tmp := self.get_lockeddate(): metas.append(MetaSub("lockedDate",tmp))
        if tmp := self.get_inactive(): metas.append(MetaSub("inactive",tmp))
        if tmp := self.get_casesensitive(): metas.append(MetaSub("caseSensitive",tmp))
        #todo valueset
        #if tmp := self.get_valueset(): csv_list.append(("valueSet",self.get_valueset()))
        if tmp := self.get_hierarchymeaning(): metas.append(MetaSub("hierarchyMeaning",tmp))
        if tmp := self.get_compositional(): metas.append(MetaSub("compositional",tmp))
        if tmp := self.get_versionneeded(): metas.append(MetaSub("versionNeeded",tmp))
        #todo supplements
        #if tmp := self.get_supplements(): csv_list.append(("supplements",tmp))
        if tmp := self.get_count(): metas.append(MetaSub("count",tmp))
        if tmp := self.get_filter():
            for oneFilter in tmp:
                metas.append(MetaSub("filter",oneFilter.code+"|"+oneFilter.description+"|"+oneFilter.operator+"|"+oneFilter.value))
        if tmp := self.get_property():
            for oneProperty in tmp:
                metas.append(MetaSub("property",str(oneProperty)))
        # end list of metaelements

        classes = []
        if tmp := self.get_concept():
            for oneConcept in tmp:
                theClass = None
                theClass = ClassSub()
                theClass.set_code(oneConcept.code)
                if hasattr(oneConcept,'display'):
                    theClass.add_Rubric(RubricSub(id="preferred",Label=[LabelSub(valueOf_=oneConcept.display)]))
                if hasattr(oneConcept,'definition'):
                    theClass.add_Rubric(RubricSub(id="definition",Label=[LabelSub(valueOf_=oneConcept.definition)]))
                if hasattr(oneConcept,'designation'):
                    for oneDesignation in oneConcept.designation:
                        theClass.add_Rubric(RubricSub(id="designation",Label=[LabelSub(valueOf_=oneDesignation)]))

                if hasattr(oneConcept,'property'):
                    for oneProperty in oneConcept.property:
                        if oneProperty.code == "parent":
                            theClass.add_SuperClass(SuperClassSub(oneProperty.value))
                        elif oneProperty.code == "child":
                            theClass.add_SubClass(SubClassSub(oneProperty.value))
                        else:
                            theClass.add_Meta(MetaSub(oneProperty.code, oneProperty.value))
                classes.append(theClass)

        claml3.add_Classification(ClassificationSub(lang,None,metas,identifiers,[title],authors,None,claKinds,None,rubKinds,None,None,classes))
        claml3.export(outfile, 0)

supermod.ClaML3.subclass = ClaML3Sub
# end class ClaML3Sub


class ClassificationSub(supermod.Classification):
    def __init__(self, lang=None, space='default', Meta=None, Identifier=None, Title=None, Authors=None, Variants=None, ClassKinds=None, UsageKinds=None, RubricKinds=None, Modifier=None, ModifierClass=None, Class=None, **kwargs_):
        super(ClassificationSub, self).__init__(lang, space, Meta, Identifier, Title, Authors, Variants, ClassKinds, UsageKinds, RubricKinds, Modifier, ModifierClass, Class,  **kwargs_)
supermod.Classification.subclass = ClassificationSub
# end class ClassificationSub


class VariantsSub(supermod.Variants):
    def __init__(self, Variant=None, **kwargs_):
        super(VariantsSub, self).__init__(Variant,  **kwargs_)
supermod.Variants.subclass = VariantsSub
# end class VariantsSub


class VariantSub(supermod.Variant):
    def __init__(self, name=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(VariantSub, self).__init__(name, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Variant.subclass = VariantSub
# end class VariantSub


class MetaSub(supermod.Meta):
    def __init__(self, name=None, value=None, variants=None, kind=None, **kwargs_):
        super(MetaSub, self).__init__(name, value, variants, kind,  **kwargs_)
supermod.Meta.subclass = MetaSub
# end class MetaSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, authority=None, uid=None, variants=None, date=None, effectivedate=None, expirationdate=None, status=None, **kwargs_):
        super(IdentifierSub, self).__init__(authority, uid, variants, date, effectivedate, expirationdate, status,  **kwargs_)
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class TitleSub(supermod.Title):
    def __init__(self, name=None, version=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(TitleSub, self).__init__(name, version, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Title.subclass = TitleSub
# end class TitleSub


class AuthorsSub(supermod.Authors):
    def __init__(self, variants=None, Author=None, **kwargs_):
        super(AuthorsSub, self).__init__(variants, Author,  **kwargs_)
supermod.Authors.subclass = AuthorsSub
# end class AuthorsSub


class AuthorSub(supermod.Author):
    def __init__(self, name=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(AuthorSub, self).__init__(name, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Author.subclass = AuthorSub
# end class AuthorSub


class ClassKindsSub(supermod.ClassKinds):
    def __init__(self, ClassKind=None, **kwargs_):
        super(ClassKindsSub, self).__init__(ClassKind,  **kwargs_)
supermod.ClassKinds.subclass = ClassKindsSub
# end class ClassKindsSub


class UsageKindsSub(supermod.UsageKinds):
    def __init__(self, variants=None, UsageKind=None, **kwargs_):
        super(UsageKindsSub, self).__init__(variants, UsageKind,  **kwargs_)
supermod.UsageKinds.subclass = UsageKindsSub
# end class UsageKindsSub


class RubricKindsSub(supermod.RubricKinds):
    def __init__(self, RubricKind=None, **kwargs_):
        super(RubricKindsSub, self).__init__(RubricKind,  **kwargs_)
supermod.RubricKinds.subclass = RubricKindsSub
# end class RubricKindsSub


class ClassKindSub(supermod.ClassKind):
    def __init__(self, name=None, variants=None, Display=None, **kwargs_):
        super(ClassKindSub, self).__init__(name, variants, Display,  **kwargs_)
supermod.ClassKind.subclass = ClassKindSub
# end class ClassKindSub


class UsageKindSub(supermod.UsageKind):
    def __init__(self, name=None, mark=None, variants=None, **kwargs_):
        super(UsageKindSub, self).__init__(name, mark, variants,  **kwargs_)
supermod.UsageKind.subclass = UsageKindSub
# end class UsageKindSub


class UsageSub(supermod.Usage):
    def __init__(self, kind=None, variants=None, **kwargs_):
        super(UsageSub, self).__init__(kind, variants,  **kwargs_)
supermod.Usage.subclass = UsageSub
# end class UsageSub


class RubricKindSub(supermod.RubricKind):
    def __init__(self, name=None, inherited=True, variants=None, Display=None, **kwargs_):
        super(RubricKindSub, self).__init__(name, inherited, variants, Display,  **kwargs_)
supermod.RubricKind.subclass = RubricKindSub
# end class RubricKindSub


class DisplaySub(supermod.Display):
    def __init__(self, lang=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(DisplaySub, self).__init__(lang, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Display.subclass = DisplaySub
# end class DisplaySub


class ModifierSub(supermod.Modifier):
    def __init__(self, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Meta=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierSub, self).__init__(code, kind, variants, version, effectivedate, expirationdate, status, Meta, SubClass, Rubric, History,  **kwargs_)
supermod.Modifier.subclass = ModifierSub
# end class ModifierSub


class ModifierClassSub(supermod.ModifierClass):
    def __init__(self, modifier=None, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Usage=None, Meta=None, SuperClass=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierClassSub, self).__init__(modifier, code, kind, variants, version, effectivedate, expirationdate, status, Usage, Meta, SuperClass, SubClass, Rubric, History,  **kwargs_)
supermod.ModifierClass.subclass = ModifierClassSub
# end class ModifierClassSub


class ClassSub(supermod.Class):
    def __init__(self, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Usage=None, Meta=None, SuperClass=None, SubClass=None, ModifiedBy=None, ValidModifierClass=None, ExcludeModifier=None, Rubric=None, History=None, **kwargs_):
        super(ClassSub, self).__init__(code, kind, variants, version, effectivedate, expirationdate, status, Usage, Meta, SuperClass, SubClass, ModifiedBy, ValidModifierClass, ExcludeModifier, Rubric, History,  **kwargs_)
supermod.Class.subclass = ClassSub
# end class ClassSub


class ModifiedBySub(supermod.ModifiedBy):
    def __init__(self, code=None, position=None, variants=None, optionalmodifier=False, Meta=None, **kwargs_):
        super(ModifiedBySub, self).__init__(code, position, variants, optionalmodifier, Meta,  **kwargs_)
supermod.ModifiedBy.subclass = ModifiedBySub
# end class ModifiedBySub


class ExcludeModifierSub(supermod.ExcludeModifier):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(ExcludeModifierSub, self).__init__(code, variants,  **kwargs_)
supermod.ExcludeModifier.subclass = ExcludeModifierSub
# end class ExcludeModifierSub


class ValidModifierClassSub(supermod.ValidModifierClass):
    def __init__(self, code=None, variants=None, position=None, Meta=None, ValidModifierClass_member=None, **kwargs_):
        super(ValidModifierClassSub, self).__init__(code, variants, position, Meta, ValidModifierClass_member,  **kwargs_)
supermod.ValidModifierClass.subclass = ValidModifierClassSub
# end class ValidModifierClassSub


class RubricSub(supermod.Rubric):
    def __init__(self, id=None, kind=None, variants=None, Usage=None, Label=None, History=None, **kwargs_):
        super(RubricSub, self).__init__(id, kind, variants, Usage, Label, History,  **kwargs_)
supermod.Rubric.subclass = RubricSub
# end class RubricSub


class LabelSub(supermod.Label):
    def __init__(self, lang=None, space='default', variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(LabelSub, self).__init__(lang, space, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Label.subclass = LabelSub
# end class LabelSub


class HistorySub(supermod.History):
    def __init__(self, author=None, date=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(HistorySub, self).__init__(author, date, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.History.subclass = HistorySub
# end class HistorySub


class SuperClassSub(supermod.SuperClass):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(SuperClassSub, self).__init__(code, variants,  **kwargs_)
supermod.SuperClass.subclass = SuperClassSub
# end class SuperClassSub


class SubClassSub(supermod.SubClass):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(SubClassSub, self).__init__(code, variants,  **kwargs_)
supermod.SubClass.subclass = SubClassSub
# end class SubClassSub


class FragmentSub(supermod.Fragment):
    def __init__(self, class_=None, type_='item', Usage=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(FragmentSub, self).__init__(class_, type_, Usage, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Fragment.subclass = FragmentSub
# end class FragmentSub


class IncludeSub(supermod.Include):
    def __init__(self, class_=None, rubric=None, **kwargs_):
        super(IncludeSub, self).__init__(class_, rubric,  **kwargs_)
supermod.Include.subclass = IncludeSub
# end class IncludeSub


class IncludeDescendantsSub(supermod.IncludeDescendants):
    def __init__(self, code=None, kind=None, **kwargs_):
        super(IncludeDescendantsSub, self).__init__(code, kind,  **kwargs_)
supermod.IncludeDescendants.subclass = IncludeDescendantsSub
# end class IncludeDescendantsSub


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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
