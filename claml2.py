#!/usr/bin/env python

#
# Generated Wed Jul 28 08:03:17 2021 by generateDS.py version 2.39.2.
# Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)]
#
# Command line options:
#   ('-s', 'claml2')
#   ('-o', 'claml2super')
#
# Command line arguments:
#   .\ClaML2.0.0.xsd
#
# Command line:
#   generateDS.py -s "claml2" -o "claml2super" .\ClaML2.0.0.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.39.2
#

import datetime
import os
import sys
import re
from typing import NoReturn
from lxml import etree as etree_

import claml2super as supermod
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
    for oneMeta in self.get_Meta():
        if oneMeta.get_name() == meta_name:
            return oneMeta.get_value()

#class Class(supermod.Class):
#    def get_sortierreihenfolge(self):
#        return get_Meta_with_name(self,'Sortierreihenfolge')

class ClaML2Sub(supermod.ClaML2, pcam.PropCsvAndMaster):
    def __init__(self, version=None, Meta=None, Identifier=None, Title=None, Authors=None, Variants=None, ClassKinds=None, UsageKinds=None, RubricKinds=None, Modifier=None, ModifierClass=None, Class=None, **kwargs_):
        super(ClaML2Sub, self).__init__(version, Meta, Identifier, Title, Authors, Variants, ClassKinds, UsageKinds, RubricKinds, Modifier, ModifierClass, Class,  **kwargs_)

    # just for calling the outer method
    def parse(inFilename):
        return parse(inFilename)

    def get_resource(self):
        if res := get_Meta_with_name(self,'resource'):
            return res
        else:
            return pcam.Resource.CodeSystem.value

    # todo create get url for other classifications
    def get_url(self):
        if tempUrl := self.globalUrl:
            return tempUrl+self.get_resource()+"-"+self.get_name()
        elif tempUrl := get_Meta_with_name(self,'url'):
            return tempUrl

    def get_identifier(self):
        identifiers = []
        for oneIdentifier in self.get_Identifier():
            if tmp := oneIdentifier.get_uid():
                identifiers.append(tmp)
        return identifiers

    def get_version(self):
        return self.get_Title().get_version().strip("_").strip("-").strip(" ")

    # replaces " " and "_" to "-", deletes up to 7 repetitions of "-". deletes all other caracters, strips/trimms "-" on ends and lowercase it
    def get_name(self):
        return (re.sub(r'[^A-Za-z0-9\-]+', '', self.get_Title().get_name().replace(" ","-").replace("_","-").replace("--","-").replace("---","-").replace("--","-"))).strip("-").lower()

    # primär: meta.titleLong / sekundär: title.name)
    def get_title(self):
        if tempTitle := get_Meta_with_name(self,'titleLong'):
            return tempTitle
        else:
            return self.get_Title().get_name()

    def get_status(self):
        if (tempStatus := get_Meta_with_name(self,'status')) in set(item.value for item in pcam.Status):
            return tempStatus
        elif get_Meta_with_name(self,'preliminary') == "true":
            return pcam.Status.draft.value
        else:
            return pcam.Status.active.value

    def get_experimental(self):
        return get_Meta_with_name(self,'experimental')

    def get_date(self):
        if not (tmp := self.get_Title().get_date()):
            if not (tmp := get_Meta_with_name(self,'last_change_date')[0:10]):
                tmp = get_Meta_with_name(self,'insert_ts')[0:10]
        return tmp

    def get_publisher(self):
        tmpAuthors = ""
        if authors := self.get_Authors():
            for author in authors.get_Author():
                if tmpAuthors != "":
                    tmpAuthors += " & "
                tmpAuthors += author.get_name()
        return tmpAuthors or None

    def get_contact(self):
        tempConDetS = []
        if authors := self.get_Authors():
            for oneAuthor in authors.get_Author():
                if tempValueOf := oneAuthor.get_valueOf_():
                    oneConDet = pcam.ContactDetail()
                    oneConDet.name = oneAuthor.get_name()
                    oneConPoi = pcam.ContactDetail.ContactPoint()
                    oneConPoi.value = tempValueOf
                    oneConDet.telecom = [oneConPoi]
                    tempConDetS.append(oneConDet)
        if (website := get_Meta_with_name(self,'website')) and not website == "":
            oneConDet = pcam.ContactDetail()
            oneConPoi = pcam.ContactDetail.ContactPoint()
            oneConPoi.value = website
            oneConPoi.system = pcam.ContactDetail.ContactPoint.ContactPointSystem.url.value
            oneConDet.telecom = [oneConPoi]
            tempConDetS.append(oneConDet)
        return tempConDetS

    def get_description(self):
        tempRet = ""
        boolAddedSomething = False
        if (tempDescEn := get_Meta_with_name(self,'description_eng')) and not tempDescEn == "":
            tempRet += "**Description:** "
            tempRet += tempDescEn
            boolAddedSomething = True

        if (tempDesc := get_Meta_with_name(self,'description')) and not tempDesc == "":
            if boolAddedSomething:
                tempRet += "\n\n"
            tempRet += "**Beschreibung:** "
            tempRet += tempDesc
            boolAddedSomething = True

        if (tempVerDesc := get_Meta_with_name(self,'version_description')) and not tempVerDesc == "":
            if boolAddedSomething:
                tempRet += "\n\n"
            tempRet += "**Versions-Beschreibung:** "
            tempRet += tempVerDesc

        if tempRet == "":
            tempRet = None
        return tempRet

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

    def get_valueset(self): #vs only
        return get_Meta_with_name(self,'valueset')

    def get_hierarchymeaning(self):
        return get_Meta_with_name(self,'hierarchyMeaning')

    def get_compositional(self):
        return get_Meta_with_name(self,'compositional')

    def get_versionneeded(self):
        return get_Meta_with_name(self,'versionNeeded')

    def get_supplements(self): #vs only
        return get_Meta_with_name(self,'supplements')

    def get_content(self):
        if tempContent := get_Meta_with_name(self,'content'):
            return tempContent
        elif tempContent := get_Meta_with_name(self,'unvollstaendig'):
            if tempContent == "false":
                return pcam.Content.complete.value
            elif tempContent == "true":
               return pcam.Content.fragment.value
        else:
            return pcam.Content.complete.value

    def get_count(self):
        return len(self.get_Class())

    def get_filter(self):
        retArr = []
        for oneMeta in self.get_Meta():
            if oneMeta.get_name() == 'filter':
                oneFilter = pcam.Filter()
                oneFilter.code = oneMeta.get_value().split('|')[0]
                oneFilter.description = oneMeta.get_value().split('|')[1]
                oneFilter.operator = oneMeta.get_value().split('|')[2]
                oneFilter.value = oneMeta.get_value().split('|')[3]
                retArr.append(oneFilter)
        return retArr

    def get_property(self):
        retArr = []
        for oneMeta in self.get_Meta():
            if oneMeta.get_name() == 'property':
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
        lan = get_Meta_with_name(self,'language')
        if lan is None:
            lan = get_Meta_with_name(self,'lang')
        return lan

    def get_text(self):
        return get_Meta_with_name(self,'text')

    def get_contained(self):
        return get_Meta_with_name(self,'contained')

    def get_extension(self):
        return get_Meta_with_name(self,'extension')

    def get_modifierextension(self):
        return get_Meta_with_name(self,'modifierExtension')

    # todo use get_concept also for claml3
    def get_concept(self):
        if hasattr(self, "concept") and self.concept:
            return self.concept
        else:
            retArr = []
            for oneClass in self.get_Class():
                theConcept = pcam.CSConcept()
                theConcept.code = oneClass.get_code()

                thePropertys = []
                retiredAlreadySet = False

                if tempKind := oneClass.get_kind():
                    theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                    theProperty.code = "kind"
                    theProperty.value = tempKind
                    theProperty.type = pcam.PropertyCodeType.string
                    thePropertys.append(theProperty)

                usedPreferredLong = False
                for oneRubric in oneClass.get_Rubric():
                    tmp = ""
                    if (tmp := oneRubric.get_Label()[0].get_valueOf_().strip()) == "":
                        for onePara in oneRubric.get_Label()[0].get_Para():
                            tmp += onePara.get_valueOf_()+" "
                        for oneFragment in oneRubric.get_Label()[0].get_Fragment():
                            tmp += oneFragment.get_valueOf_()+" "
                        for oneReference in oneRubric.get_Label()[0].get_Reference():
                            tmp += oneReference.get_valueOf_()+" "
                        for oneTable in oneRubric.get_Label()[0].get_Table():
                            # todo: find a solution to get the whole table into a fhir element
                            tmp += "!ignored Table!"

                    if (tmp.lower().endswith("[veraltet]") or tmp.lower().startswith("deprecated")) and not retiredAlreadySet:
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "status"
                        theProp.value = "retired"
                        theProp.type = pcam.PropertyCodeType.code
                        thePropertys.append(theProp)
                        retiredAlreadySet = True

                    if oneRubric.get_kind() == "preferredLong":
                        theConcept.display = tmp
                        usedPreferredLong = True
                    elif not usedPreferredLong and oneRubric.get_kind() == "preferred":
                        theConcept.display = tmp
                    elif oneRubric.get_kind() == "definition":
                        theConcept.definition = tmp
                    elif oneRubric.get_kind() == "note":
                        theConcept.definition = tmp
                    elif oneRubric.get_kind() == "designation":
                        theConcept.designation.append(pcam.ConceptDesignation(tmp))
                    else:
                        theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                        """TODO Rubrics exist that do not have @kind. As a quick fix "None" will be assumed as code
                                for these properties.
                        """
                        theProperty.code = oneRubric.get_kind() or "None"
                        theProperty.value = tmp
                        theProperty.type = pcam.PropertyCodeType.string
                        thePropertys.append(theProperty)

                for oneSuperClass in oneClass.get_SuperClass():
                    theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                    theProperty.code = "parent"
                    theProperty.value = oneSuperClass.get_code()
                    theProperty.type = pcam.PropertyCodeType.code
                    thePropertys.append(theProperty)

                for oneSubClass in oneClass.get_SubClass():
                    theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                    theProperty.code = "child"
                    theProperty.value = oneSubClass.get_code()
                    theProperty.type = pcam.PropertyCodeType.code
                    thePropertys.append(theProperty)

                for oneMeta in oneClass.get_Meta():
                    # skip the old TS_ATTRIBUTE_* and Level properties, only let TS_ATTRIBUTE_HINTS through
                    if (not oneMeta.get_name().startswith("TS_ATTRIBUTE_") or oneMeta.get_name() == "TS_ATTRIBUTE_HINTS" or oneMeta.get_name() == "TS_ATTRIBUTE_MEANING") and not oneMeta.get_name() == "Level":
                        theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                        if oneMeta.get_name().startswith("TS_ATTRIBUTE_HINTS"):
                            if not retiredAlreadySet and (oneMeta.get_value().startswith("DEPRECATED") or oneMeta.get_value().startswith("inaktiv")):
                                theProp = pcam.CSConcept.ConceptProperty()
                                theProp.code = "status"
                                theProp.value = "retired"
                                theProp.type = pcam.PropertyCodeType.code
                                thePropertys.append(theProp)
                                retiredAlreadySet = True
                            if oneMeta.get_value() != "DEPRECATED" or oneMeta.get_value() != "inaktiv":
                                theProperty.code = "hints"
                                theProperty.value = oneMeta.get_value()
                                theProperty.type = pcam.PropertyCodeType.string
                                thePropertys.append(theProperty)
                        elif oneMeta.get_name().startswith("TS_ATTRIBUTE_MEANING"):
                            theDesignation = pcam.ConceptDesignation()
                            theDesignation.language = "de-AT"
                            theDesignation.value = oneMeta.get_value()
                            theConcept.designation.append(theDesignation)
                        elif oneMeta.get_name() == "Type":
                            if not retiredAlreadySet and oneMeta.get_value() == "D":
                                theProp = pcam.CSConcept.ConceptProperty()
                                theProp.code = "status"
                                theProp.value = "retired"
                                theProp.type = pcam.PropertyCodeType.code
                                thePropertys.append(theProp)
                                retiredAlreadySet = True
                        elif oneMeta.get_name() == "notSelectable" and oneMeta.get_value() == "true":
                            theProperty.code = oneMeta.get_name()
                            theProperty.value = oneMeta.get_value()
                            theProperty.type = pcam.PropertyCodeType.boolean
                            thePropertys.append(theProperty)
                        else:
                            theProperty.code = oneMeta.get_name()#[0].lower()+oneMeta.get_name()[1:]
                            theProperty.value = oneMeta.get_value()
                            theProperty.type = pcam.PropertyCodeType.string
                            thePropertys.append(theProperty)

                if len(thePropertys) > 0:
                    theConcept.property = thePropertys

                retArr.append(theConcept)
                self.concept = retArr
            return retArr

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        # required ClaMl3 fields
        title = TitleSub(self.get_name(),self.get_version(),valueOf_=self.get_title())
        claKinds = ClassKindsSub()
        claKinds.add_ClassKind(ClassKindSub("code"))
        rubKinds = RubricKindsSub()
        # TODO rubricKinds should be added when some are gathered
        rubKinds.add_RubricKind(RubricKindSub("preferred"))

        # optional ClaMl3 fields
        # madatory FHIR R4 fields
        metas = []
        metas.append(MetaSub('resource',self.get_resource()))
        metas.append(MetaSub('url',self.get_url()))
        # if the status is draft or active, a prelim attribute is created
        if self.get_status() == "draft":
            metas.append(MetaSub('preliminary', "true"))
        elif self.get_status() == "active":
            metas.append(MetaSub('preliminary', "false"))
        metas.append(MetaSub('status', self.get_status()))
        metas.append(MetaSub('description',self.get_description()))

        # conditional and mandatory FHIR R4 fields
        if self.get_resource() == 'CodeSystem': metas.append(MetaSub('content',self.get_content()))

        # optional FHIR fields
        if language := self.get_language():
            metas.append(MetaSub('language',language))

        if tmp := self.get_implicitrules(): metas.append(MetaSub('implicitrules',tmp))
        if tmp := self.get_text(): metas.append(MetaSub('text',tmp))
        if tmp := self.get_contained(): metas.append(MetaSub('contained',tmp))
        if tmp := self.get_extension(): metas.append(MetaSub('extension',tmp))
        if tmp := self.get_modifierextension(): metas.append(MetaSub('modifierextension',tmp))
        identifiers = None
        if tmp := self.get_identifier():
            identifiers = []
            for oneIdentifier in tmp:
                identifiers.append(IdentifierSub(None,oneIdentifier))
        if tmp := self.get_experimental(): metas.append(MetaSub('experimental',tmp))
        if tmp := self.get_date(): title.date = datetime.datetime.strptime(tmp, '%Y-%m-%d')
        authors = None
        if tmp := self.get_publisher():
            authors = AuthorsSub([AuthorSub(tmp)])
        if tmp := self.get_contact():
            if authors is None:
                authors = AuthorsSub()
            for oneContact in tmp:
                oneAuthor = AuthorSub(oneContact.name or None, None if not oneContact.telecom else oneContact.telecom[0].value or None)
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
        # TODO valueset
        #if tmp := self.get_valueset(): csv_list.append(("valueSet",self.get_valueset()))
        if tmp := self.get_hierarchymeaning(): metas.append(MetaSub("hierarchyMeaning",tmp))
        if tmp := self.get_compositional(): metas.append(MetaSub("compositional",tmp))
        if tmp := self.get_versionneeded(): metas.append(MetaSub("versionNeeded",tmp))
        # TODO supplements
        #if tmp := self.get_supplements(): csv_list.append(("supplements",self.get_supplements()))
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
                    theClass.add_Rubric(RubricSub(kind="preferred",Label=[LabelSub(lang=language,valueOf_=oneConcept.display)]))
                if hasattr(oneConcept,'definition'):
                    theClass.add_Rubric(RubricSub(kind="definition",Label=[LabelSub(lang=language,valueOf_=oneConcept.definition)]))
                if  hasattr(oneConcept,'designation'):
                    for oneDesignation in oneConcept.designation:
                        theClass.add_Rubric(RubricSub(kind="designation",Label=[LabelSub(lang=language,valueOf_=supermod.quote_xml(str(oneDesignation)))]))

                if  hasattr(oneConcept,'property'):
                    for oneProperty in oneConcept.property:
                        if oneProperty.code == "kind": # if there is more than one kind in the propertys, the last one is used
                            theClass.set_kind(oneProperty.value)
                        elif oneProperty.code == "parent":
                            theClass.add_SuperClass(SuperClassSub(oneProperty.value))
                        elif oneProperty.code == "child":
                            theClass.add_SubClass(SubClassSub(oneProperty.value))
                        elif oneProperty.type == pcam.PropertyCodeType.code or oneProperty.type == pcam.PropertyCodeType.boolean:
                            theClass.add_Meta(MetaSub(oneProperty.code, oneProperty.value))
                        else:
                            theClass.add_Rubric(RubricSub(kind=oneProperty.code, Label=[LabelSub(lang=language, valueOf_=oneProperty.value)]))

                # if there was no kind given, create one with "noKind"
                if temp := theClass.get_kind():
                    theClass.set_kind("noKind")

                classes.append(theClass)

        claml2 = ClaML2Sub('2.0.0',metas,identifiers,title,authors,None,claKinds,None,rubKinds,None,None,classes)
        claml2.export(outfile, 0)

supermod.ClaML2.subclass = ClaML2Sub
# end class ClaML2Sub


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
    def __init__(self, name=None, value=None, variants=None, **kwargs_):
        super(MetaSub, self).__init__(name, value, variants,  **kwargs_)
supermod.Meta.subclass = MetaSub
# end class MetaSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, authority=None, uid=None, **kwargs_):
        super(IdentifierSub, self).__init__(authority, uid,  **kwargs_)
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class TitleSub(supermod.Title):
    def __init__(self, name=None, version=None, date=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(TitleSub, self).__init__(name, version, date, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Title.subclass = TitleSub
# end class TitleSub


class AuthorsSub(supermod.Authors):
    def __init__(self, Author=None, **kwargs_):
        super(AuthorsSub, self).__init__(Author,  **kwargs_)
supermod.Authors.subclass = AuthorsSub
# end class AuthorsSub


class AuthorSub(supermod.Author):
    def __init__(self, name=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(AuthorSub, self).__init__(name, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Author.subclass = AuthorSub
# end class AuthorSub


class ClassKindsSub(supermod.ClassKinds):
    def __init__(self, ClassKind=None, **kwargs_):
        super(ClassKindsSub, self).__init__(ClassKind,  **kwargs_)
supermod.ClassKinds.subclass = ClassKindsSub
# end class ClassKindsSub


class UsageKindsSub(supermod.UsageKinds):
    def __init__(self, UsageKind=None, **kwargs_):
        super(UsageKindsSub, self).__init__(UsageKind,  **kwargs_)
supermod.UsageKinds.subclass = UsageKindsSub
# end class UsageKindsSub


class RubricKindsSub(supermod.RubricKinds):
    def __init__(self, RubricKind=None, **kwargs_):
        super(RubricKindsSub, self).__init__(RubricKind,  **kwargs_)
supermod.RubricKinds.subclass = RubricKindsSub
# end class RubricKindsSub


class ClassKindSub(supermod.ClassKind):
    def __init__(self, name=None, Display=None, **kwargs_):
        super(ClassKindSub, self).__init__(name, Display,  **kwargs_)
supermod.ClassKind.subclass = ClassKindSub
# end class ClassKindSub


class UsageKindSub(supermod.UsageKind):
    def __init__(self, name=None, mark=None, **kwargs_):
        super(UsageKindSub, self).__init__(name, mark,  **kwargs_)
supermod.UsageKind.subclass = UsageKindSub
# end class UsageKindSub


class RubricKindSub(supermod.RubricKind):
    def __init__(self, name=None, inherited=True, Display=None, **kwargs_):
        super(RubricKindSub, self).__init__(name, inherited, Display,  **kwargs_)
supermod.RubricKind.subclass = RubricKindSub
# end class RubricKindSub


class DisplaySub(supermod.Display):
    def __init__(self, lang=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(DisplaySub, self).__init__(lang, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Display.subclass = DisplaySub
# end class DisplaySub


class ModifierSub(supermod.Modifier):
    def __init__(self, code=None, variants=None, Meta=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierSub, self).__init__(code, variants, Meta, SubClass, Rubric, History,  **kwargs_)
supermod.Modifier.subclass = ModifierSub
# end class ModifierSub


class ModifierClassSub(supermod.ModifierClass):
    def __init__(self, modifier=None, code=None, usage=None, variants=None, Meta=None, SuperClass=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierClassSub, self).__init__(modifier, code, usage, variants, Meta, SuperClass, SubClass, Rubric, History,  **kwargs_)
supermod.ModifierClass.subclass = ModifierClassSub
# end class ModifierClassSub


class ClassSub(supermod.Class):
    def __init__(self, code=None, kind=None, usage=None, variants=None, Meta=None, SuperClass=None, SubClass=None, ModifiedBy=None, ExcludeModifier=None, Rubric=None, History=None, **kwargs_):
        super(ClassSub, self).__init__(code, kind, usage, variants, Meta, SuperClass, SubClass, ModifiedBy, ExcludeModifier, Rubric, History,  **kwargs_)
supermod.Class.subclass = ClassSub
# end class ClassSub


class ModifiedBySub(supermod.ModifiedBy):
    def __init__(self, code=None, all=True, position=None, variants=None, Meta=None, ValidModifierClass=None, **kwargs_):
        super(ModifiedBySub, self).__init__(code, all, position, variants, Meta, ValidModifierClass,  **kwargs_)
supermod.ModifiedBy.subclass = ModifiedBySub
# end class ModifiedBySub


class ExcludeModifierSub(supermod.ExcludeModifier):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(ExcludeModifierSub, self).__init__(code, variants,  **kwargs_)
supermod.ExcludeModifier.subclass = ExcludeModifierSub
# end class ExcludeModifierSub


class ValidModifierClassSub(supermod.ValidModifierClass):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(ValidModifierClassSub, self).__init__(code, variants,  **kwargs_)
supermod.ValidModifierClass.subclass = ValidModifierClassSub
# end class ValidModifierClassSub


class RubricSub(supermod.Rubric):
    def __init__(self, id=None, kind=None, usage=None, Label=None, History=None, **kwargs_):
        super(RubricSub, self).__init__(id, kind, usage, Label, History,  **kwargs_)
supermod.Rubric.subclass = RubricSub
# end class RubricSub


class LabelSub(supermod.Label):
    def __init__(self, lang=None, space='default', variants=None, Reference=None, Term=None, Para=None, Include=None, IncludeDescendants=None, Fragment=None, List=None, Table=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(LabelSub, self).__init__(lang, space, variants, Reference, Term, Para, Include, IncludeDescendants, Fragment, List, Table, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Label.subclass = LabelSub
# end class LabelSub


class HistorySub(supermod.History):
    def __init__(self, author=None, date=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(HistorySub, self).__init__(author, date, valueOf_, mixedclass_, content_,  **kwargs_)
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


class ReferenceSub(supermod.Reference):
    def __init__(self, class_=None, authority=None, uid=None, code=None, usage=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(ReferenceSub, self).__init__(class_, authority, uid, code, usage, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class ParaSub(supermod.Para):
    def __init__(self, class_=None, Reference=None, Term=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(ParaSub, self).__init__(class_, Reference, Term, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Para.subclass = ParaSub
# end class ParaSub


class FragmentSub(supermod.Fragment):
    def __init__(self, class_=None, usage=None, type_='item', Reference=None, Term=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(FragmentSub, self).__init__(class_, usage, type_, Reference, Term, valueOf_, mixedclass_, content_,  **kwargs_)
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


class ListSub(supermod.List):
    def __init__(self, class_=None, ListItem=None, **kwargs_):
        super(ListSub, self).__init__(class_, ListItem,  **kwargs_)
supermod.List.subclass = ListSub
# end class ListSub


class ListItemSub(supermod.ListItem):
    def __init__(self, class_=None, Reference=None, Term=None, Para=None, Include=None, List=None, Table=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(ListItemSub, self).__init__(class_, Reference, Term, Para, Include, List, Table, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.ListItem.subclass = ListItemSub
# end class ListItemSub


class TableSub(supermod.Table):
    def __init__(self, class_=None, Caption=None, THead=None, TBody=None, TFoot=None, **kwargs_):
        super(TableSub, self).__init__(class_, Caption, THead, TBody, TFoot,  **kwargs_)
supermod.Table.subclass = TableSub
# end class TableSub


class CaptionSub(supermod.Caption):
    def __init__(self, class_=None, Reference=None, Term=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(CaptionSub, self).__init__(class_, Reference, Term, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Caption.subclass = CaptionSub
# end class CaptionSub


class THeadSub(supermod.THead):
    def __init__(self, class_=None, Row=None, **kwargs_):
        super(THeadSub, self).__init__(class_, Row,  **kwargs_)
supermod.THead.subclass = THeadSub
# end class THeadSub


class TBodySub(supermod.TBody):
    def __init__(self, class_=None, Row=None, **kwargs_):
        super(TBodySub, self).__init__(class_, Row,  **kwargs_)
supermod.TBody.subclass = TBodySub
# end class TBodySub


class TFootSub(supermod.TFoot):
    def __init__(self, class_=None, Row=None, **kwargs_):
        super(TFootSub, self).__init__(class_, Row,  **kwargs_)
supermod.TFoot.subclass = TFootSub
# end class TFootSub


class RowSub(supermod.Row):
    def __init__(self, class_=None, Cell=None, **kwargs_):
        super(RowSub, self).__init__(class_, Cell,  **kwargs_)
supermod.Row.subclass = RowSub
# end class RowSub


class CellSub(supermod.Cell):
    def __init__(self, class_=None, rowspan=None, colspan=None, Reference=None, Term=None, Para=None, Include=None, List=None, Table=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(CellSub, self).__init__(class_, rowspan, colspan, Reference, Term, Para, Include, List, Table, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Cell.subclass = CellSub
# end class CellSub


class TermSub(supermod.Term):
    def __init__(self, class_=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(TermSub, self).__init__(class_, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Term.subclass = TermSub
# end class TermSub


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
        rootClass = supermod.ClaML2
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
        rootClass = supermod.ClaML2
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
        rootClass = supermod.ClaML2
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
        rootClass = supermod.ClaML2
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
