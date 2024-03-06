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

def get_meta_list_with_name(self, meta_name):
    meta_list = []

    for one_meta in self.get_Meta():
        if one_meta.get_name() == meta_name:
            meta_list.append(one_meta.get_value())

    return meta_list

def exporto_extension_to_class(claml_metas, extensions_written_to_metas, claml_class, pcam_source):
    """Write all extensions from the pcam_source to claml.

    claml_metas -- list of metas that will contain meta-information about extension

    claml_class -- claml class that will contain the value of the extension

    pcam_source -- the object whose extension according to the extension_url will be written to claml.
    """
    if hasattr(pcam_source, 'extension'):
        for one_extension in pcam_source.extension:
            if one_extension.url not in extensions_written_to_metas:
                extensions_written_to_metas.add(one_extension.url)
                claml_metas.append(MetaSub('extension', one_extension.url + '|' + one_extension.type.value if one_extension.type else ''))

            if value := one_extension.value:
                claml_class.add_Meta(MetaSub(one_extension.url, value))

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

    def get_id(self):
        if tmp_id := get_Meta_with_name(self, 'id'):
            return tmp_id
        else:
            return self.get_name()

    def get_profiles(self):
        return get_meta_list_with_name(self, 'profile')

    # todo create get url for other classifications
    def get_url(self):
        if tempUrl := get_Meta_with_name(self,'url'):
            return tempUrl
        elif tempUrl := self.globalUrl:
            return tempUrl+self.get_resource() + "/" + self.get_id()

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
        if temp_title_long := get_Meta_with_name(self,'titleLong'):
            return temp_title_long
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
        author_name_list = []
        if authors := self.get_Authors():
            for author in authors.get_Author():
                if tmp_name := author.get_name():
                    author_name_list.append(tmp_name)
        return ' & '.join(author_name_list) or None

    def get_contact(self):
        tempConDetS = []
        website = get_Meta_with_name(self,'website')
        website_in_authors = False
        if authors := self.get_Authors():
            for oneAuthor in authors.get_Author():
                if tempValueOf := oneAuthor.get_valueOf_():
                    if tempValueOf.count("^") % 5 == 0 and (oneConDet := pcam.ContactDetail.from_string((oneAuthor.get_name() or "")+"|"+tempValueOf)):
                        for oneConDetTele in oneConDet.telecom:
                            if oneConDetTele.system == pcam.ContactDetail.ContactPoint.ContactPointSystem.url:
                                if website and oneConDetTele.value and oneConDetTele.value.strip() in website.strip():
                                    website_in_authors = True
                        tempConDetS.append(oneConDet)
                    else:
                        oneConDet = pcam.ContactDetail()
                        oneConDet.name = oneAuthor.get_name() or ""
                        oneConPoi = pcam.ContactDetail.ContactPoint()
                        oneConPoi.value = tempValueOf
                        oneConPoi.system = pcam.ContactDetail.ContactPoint.ContactPointSystem.other
                        oneConDet.telecom = [oneConPoi]
                        tempConDetS.append(oneConDet)
        if website and not website_in_authors:
            oneConDet = pcam.ContactDetail()
            oneConPoi = pcam.ContactDetail.ContactPoint()
            oneConPoi.value = website
            oneConPoi.system = pcam.ContactDetail.ContactPoint.ContactPointSystem.url
            oneConDet.telecom = [oneConPoi]
            tempConDetS.append(oneConDet)
        return tempConDetS

    def get_description(self):
        tempRet = ""
        boolAddedSomething = False

        version_description = None
        if (tempVerDesc := get_Meta_with_name(self,'version_description')) and not tempVerDesc == "":
            version_description = "**Versions-Beschreibung:** " + tempVerDesc

        # if description AND description_eng exist AND if they are not empty, they will be concatenated
        if (tempDescEn := get_Meta_with_name(self,'description_eng')) and not tempDescEn == "" and (tempDesc := get_Meta_with_name(self,'description')) and not tempDesc == "":
            if tempDescEn.strip() == tempDesc.strip():
                tempRet += tempDesc
            else:
                tempRet += "**Description:** "
                tempRet += tempDescEn
                tempRet += "\n\n"

                tempRet += "**Beschreibung:** "
                tempRet += tempDesc
            boolAddedSomething = True
        elif (tempDesc := get_Meta_with_name(self,'description')) and not tempDesc == "":
            if version_description:
                tempRet += "**Beschreibung:** "
            tempRet += tempDesc
            boolAddedSomething = True
        elif (tempDescEn := get_Meta_with_name(self,'description_eng')) and not tempDescEn == "":
            if version_description:
                tempRet += "**Description:** "
            tempRet += tempDescEn
            boolAddedSomething = True

        if version_description:
            if boolAddedSomething:
                tempRet += "\n\n"
            tempRet += version_description

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
        if tmp := get_Meta_with_name(self,'hierarchyMeaning'):
            return pcam.HierarchyMeaning(tmp)
        return None

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
                oneProperty = pcam.Property()
                oneProperty.code = oneMeta.get_value().split('|')[0]
                oneProperty.uri = oneMeta.get_value().split('|')[1]
                oneProperty.description = oneMeta.get_value().split('|')[2]
                oneProperty.type = pcam.PropertyCodeType(oneMeta.get_value().split('|')[3])
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
        # Currently, no extensions are supported on this level
        return None

    def get_modifierextension(self):
        return get_Meta_with_name(self,'modifierExtension')

    # todo use get_concept also for claml3
    def get_concept(self):
        if hasattr(self, "concept") and self.concept:
            return self.concept
        else:
            # retrieve meta information about extensions
            extension = get_meta_list_with_name(self, 'extension')
            extension_datatype_dict = {}
            for extension in extension:
                extension_split = extension.split('|')
                extension_datatype_dict[extension_split[0]] = extension_split[1]

            retArr = []
            theMemberParent = [None]*9
            for oneClass in self.get_Class():
                if self.get_resource() == "CodeSystem":
                    theConcept = pcam.CSConcept()
                elif self.get_resource() == "ValueSet":
                    theConcept = pcam.VSConcept()

                theConcept.code = oneClass.get_code()

                thePropertys = []
                retiredAlreadySet = False
                thereIsAlreadyOneHints = False
                thereIsAlreadyOneMeaning = False

                if tempKind := oneClass.get_kind():
                    theProperty = pcam.CSConcept.ConceptProperty()
                    theProperty.code = "kind"
                    theProperty.value = tempKind
                    theProperty.type = pcam.PropertyCodeType.string
                    thePropertys.append(theProperty)

                usedPreferredLong = False
                usedDefinition = False
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
                        if self.get_resource() == "CodeSystem":
                            self.set_statusToRetired(theConcept)
                        elif self.get_resource() == "ValueSet":
                            theConcept.inactive = True
                        retiredAlreadySet = True

                    if oneRubric.get_kind() == "preferredLong":
                        theConcept.display = tmp
                        usedPreferredLong = True
                    elif not usedPreferredLong and oneRubric.get_kind() == "preferred":
                        theConcept.display = tmp
                    elif oneRubric.get_kind() == "definition":
                        if theConcept.display != tmp:
                            theConcept.definition = tmp
                            usedDefinition = True
                    elif not usedDefinition and oneRubric.get_kind() == "note":
                        if theConcept.display != tmp:
                            theConcept.definition = tmp
                    elif oneRubric.get_kind() == "designation":
                        if theConcept.display != tmp and theConcept.display != tmp.split("|")[-1]:
                            theConcept.designation.append(pcam.ConceptDesignation(tmp))
                        if tmp.startswith("de-AT"):
                            thereIsAlreadyOneMeaning = True
                        if not thereIsAlreadyOneHints and tmp.split("|")[1].startswith("hints"):
                            thereIsAlreadyOneHints = True
                    elif oneRubric.get_kind() == "None":
                        theDesignation = pcam.ConceptDesignation()
                        theDesignation.value = tmp
                        theConcept.designation.append(theDesignation)
                    elif not oneRubric.get_kind() == "hints" or (oneRubric.get_kind() == "hints" and not thereIsAlreadyOneHints):
                        theProperty = pcam.CSConcept.ConceptProperty()
                        theProperty.code = oneRubric.get_kind()
                        theProperty.value = tmp
                        theProperty.type = pcam.PropertyCodeType.string
                        thePropertys.append(theProperty)
                        if oneRubric.get_kind() == "hints":
                            thereIsAlreadyOneHints = True

                for oneSuperClass in oneClass.get_SuperClass():
                    theProperty = pcam.CSConcept.ConceptProperty()
                    theProperty.code = "parent"
                    theProperty.value = oneSuperClass.get_code()
                    theProperty.type = pcam.PropertyCodeType.code
                    thePropertys.append(theProperty)

                for oneSubClass in oneClass.get_SubClass():
                    theProperty = pcam.CSConcept.ConceptProperty()
                    theProperty.code = "child"
                    theProperty.value = oneSubClass.get_code()
                    theProperty.type = pcam.PropertyCodeType.code
                    thePropertys.append(theProperty)

                for oneMeta in oneClass.get_Meta():
                    # skip the old TS_ATTRIBUTE_* properties, only let TS_ATTRIBUTE_HINTS or TS_ATTRIBUTE_MEANING through
                    if ((not oneMeta.get_name().startswith("TS_ATTRIBUTE_") or oneMeta.get_name() == "TS_ATTRIBUTE_HINTS" or oneMeta.get_name() == "TS_ATTRIBUTE_MEANING") and
                            oneMeta.get_value().strip() != ""):
                        theProperty = pcam.CSConcept.ConceptProperty()
                        if oneMeta.get_name().startswith("TS_ATTRIBUTE_HINTS") or oneMeta.get_name().startswith("hints"):
                            if not retiredAlreadySet and (oneMeta.get_value().startswith("DEPRECATED") or oneMeta.get_value().startswith("inaktiv")):
                                if self.get_resource() == "CodeSystem":
                                    self.set_statusToRetired(theConcept)
                                elif self.get_resource() == "ValueSet":
                                    theConcept.inactive = True
                                retiredAlreadySet = True
                            if not thereIsAlreadyOneHints and (not oneMeta.get_value().startswith("DEPRECATED") and not oneMeta.get_value().startswith("inaktiv")):
                                theProperty.code = "hints"
                                theProperty.value = oneMeta.get_value()
                                theProperty.type = pcam.PropertyCodeType.string
                                thePropertys.append(theProperty)
                                thereIsAlreadyOneHints = True
                        elif oneMeta.get_name().startswith("TS_ATTRIBUTE_MEANING"):
                            if not thereIsAlreadyOneMeaning and theConcept.display != oneMeta.get_value():
                                theDesignation = pcam.ConceptDesignation()
                                theDesignation.language = "de-AT"
                                theDesignation.value = oneMeta.get_value()
                                theConcept.designation.append(theDesignation)
                                thereIsAlreadyOneMeaning = True
                        elif oneMeta.get_name() == "Level":
                            if self.get_resource() == "ValueSet":
                                if 0 <= (tmpLevel := int(oneMeta.get_value().strip())):
                                    theConcept.level = tmpLevel
                                    theMemberParent[tmpLevel] = theConcept
                                    if tmpLevel > 0:
                                        parent = theMemberParent[tmpLevel-1]
                                        # setting theConcept as child of the parent
                                        parent.member.append(theConcept)
                                        # setting the parent of theConcept
                                        theConcept.parent = parent
                        elif oneMeta.get_name() == "Type":
                            if oneMeta.get_value() == "A":
                                theConcept.abstract = True
                            if not retiredAlreadySet and oneMeta.get_value() == "D":
                                if self.get_resource() == "CodeSystem":
                                    self.set_statusToRetired(theConcept)
                                elif self.get_resource() == "ValueSet":
                                    theConcept.inactive = True
                                retiredAlreadySet = True
                        elif oneMeta.get_name() == "status":
                            # separately check if retiredAlreadySet is false, otherwise the
                            # status-property might be created within the 'else'-branch of the whole
                            # elif-section
                            if not retiredAlreadySet:
                                if oneMeta.get_value() == "retired":
                                    retiredAlreadySet = True
                                theProp = pcam.CSConcept.ConceptProperty()
                                theProp.code = "status"
                                theProp.value = oneMeta.get_value()
                                theProp.type = pcam.PropertyCodeType.code
                                # TODO instead of using 'retiredAlreadySet' the ConceptProperty should keep track of
                                #      the properties already set in a dictionary and dismiss duplicated entries.
                                #      Discuss: what happens if the same property occurs with different values
                                thePropertys.append(theProp)
                        elif oneMeta.get_name() == "notSelectable" and oneMeta.get_value() == "true":
                            theProperty.code = oneMeta.get_name()
                            theProperty.value = oneMeta.get_value()
                            theProperty.type = pcam.PropertyCodeType.boolean
                            thePropertys.append(theProperty)
                        elif oneMeta.get_name() == "codeSystem":
                            theConcept.system = oneMeta.get_value()
                        elif oneMeta.get_name() == "codeSystemVersion":
                            theConcept.version = oneMeta.get_value()
                        elif oneMeta.get_name() in extension_datatype_dict:
                            the_extension = pcam.Extension()
                            the_extension.url = oneMeta.get_name()
                            the_extension.type = pcam.ExtensionType(extension_datatype_dict[oneMeta.get_name()])
                            if the_extension.type != pcam.ExtensionType.coding:
                                the_extension.value = oneMeta.get_value()
                            else:
                                the_extension.value = pcam.Coding(oneMeta.get_value())
                            theConcept.extension.append(the_extension)
                        else:
                            theProperty.code = oneMeta.get_name()#[0].lower()+oneMeta.get_name()[1:]
                            theProperty.value = oneMeta.get_value()
                            theProperty.type = pcam.PropertyCodeType.string
                            thePropertys.append(theProperty)

                if len(thePropertys) > 0 and self.get_resource() == "CodeSystem":
                    theConcept.property += thePropertys

                retArr.append(theConcept)
                self.concept = retArr
            return retArr

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        metas = []

        # required ClaMl3 fields
        # TODO recreate super-class with generateDS
        title = TitleSub(self.get_name(),self.get_version(), valueOf_=(self.get_title() or ""))
        metas.append(MetaSub('titleLong',self.get_title()))
        claKinds = ClassKindsSub()
        claKinds.add_ClassKind(ClassKindSub("code"))
        rubKinds = RubricKindsSub()
        # TODO only rubricKinds, that are beeing used, should be added
        rubKinds.add_RubricKind(RubricKindSub("preferred"))

        # optional ClaMl3 fields
        # madatory FHIR R4 fields
        metas.append(MetaSub('resource',self.get_resource()))
        metas.append(MetaSub('id', self.get_id()))

        if one_profile_list := self.get_profiles():
            for one_profile in one_profile_list:
                metas.append(MetaSub('profile', one_profile))

        metas.append(MetaSub('url',self.get_url()))
        # if the status is draft or active, a prelim attribute is created
        if self.get_status() == "draft":
            metas.append(MetaSub('preliminary', "true"))
        elif self.get_status() == "active":
            metas.append(MetaSub('preliminary', "false"))
        metas.append(MetaSub('status', self.get_status()))
        if (tmp := self.get_description()) and tmp.strip() != "":
            desc_splitted_by_star_star = tmp.split('**')
            headers = False
            versionheader = False
            if "Description:" in desc_splitted_by_star_star:
                metas.append(MetaSub('description_eng',desc_splitted_by_star_star[desc_splitted_by_star_star.index("Description:")+1].strip()))
                headers = True
            if "Beschreibung:" in desc_splitted_by_star_star:
                metas.append(MetaSub('description',desc_splitted_by_star_star[desc_splitted_by_star_star.index("Beschreibung:")+1].strip()))
                headers = True
            if "Versions-Beschreibung:" in desc_splitted_by_star_star:
                metas.append(MetaSub('version_description',desc_splitted_by_star_star[desc_splitted_by_star_star.index("Versions-Beschreibung:")+1].strip()))
                versionheader = True
            if not headers:
                if not versionheader:
                    metas.append(MetaSub('description',tmp.strip()))
                    metas.append(MetaSub('description_eng',tmp.strip()))
                else:
                    metas.append(MetaSub('description',desc_splitted_by_star_star[desc_splitted_by_star_star.index("Versions-Beschreibung:")-1].strip()))
                    metas.append(MetaSub('description_eng',desc_splitted_by_star_star[desc_splitted_by_star_star.index("Versions-Beschreibung:")-1].strip()))

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
        if tmp := self.get_date(): title.date = tmp
        authors = None
        if (tmp := self.get_publisher()) and (tmp != "None"):
            # setting valueOf_ of Author to '' explicitly - other wise the Author-tag will be filled with 'None', i.e. <Author name="name_of_author">None</Author>
            authors = AuthorsSub([AuthorSub(tmp, '')])
        if tmp := self.get_contact():
            if authors is None:
                authors = AuthorsSub()
            website = ""
            for oneContact in tmp:
                oneAuthor = AuthorSub(oneContact.name or "", str(oneContact).split('|',2)[1])
                authors.add_Author(oneAuthor)
                for oneConTele in oneContact.telecom:
                    if oneConTele.system == pcam.ContactDetail.ContactPoint.ContactPointSystem.url:
                        if website == "":
                            website = oneConTele.value
                        else:
                            website += " & " + oneConTele.value
            # explicitly don't add the author information as website-meta, like it once was in the austrian termpub, can't deliver name and telecom in one meta
            metas.append(MetaSub("website",website))

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
        if tmp := self.get_hierarchymeaning(): metas.append(MetaSub("hierarchyMeaning",tmp.value))
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
            if self.get_resource() == "CodeSystem":
                concept_dict = self.buildConceptDictWithAttr('code')
            elif self.get_resource() == "ValueSet":
                concept_dict = self.buildConceptDictWithAttr('code', 'system')

            # keep track of extensions that have already been documented in metas
            extensions_written_to_metas = set()

            for oneConcept in tmp:
                theClass = None
                theClass = ClassSub()
                theClass.set_code(oneConcept.code)

                if self.get_resource() == "ValueSet":
                    # write the system if existent
                    if tmp := oneConcept.system:
                        theClass.add_Meta(MetaSub('codeSystem', tmp))

                    # write the system version if existent
                    if tmp := oneConcept.version:
                        theClass.add_Meta(MetaSub('codeSystemVersion', tmp))
                    else:
                        # retrieve version from metadata

                        # theoretically oneConcept.system could be either canonical or OID in
                        # most cases, however, it would be the canonical
                        if tmp := self.gainVersionFromCanonical(oneConcept.system):
                            theClass.add_Meta(MetaSub('codeSystemVersion', tmp))
                        elif tmp := self.gainVersionFromOid(oneConcept.system):
                            theClass.add_Meta(MetaSub('codeSystemVersion', tmp))

                if hasattr(oneConcept,'display'):
                    theClass.add_Rubric(RubricSub(kind="preferred",Label=[LabelSub(lang=language,valueOf_=oneConcept.display)]))
                if hasattr(oneConcept,'definition') and (tmp := oneConcept.definition):
                    theClass.add_Rubric(RubricSub(kind="note",Label=[LabelSub(lang=language,valueOf_=tmp)]))
                if  hasattr(oneConcept,'designation'):
                    for oneDesignation in oneConcept.designation:
                        theClass.add_Rubric(RubricSub(kind="designation",Label=[LabelSub(lang=language,valueOf_=str(oneDesignation))]))
                        if oneDesignation.use.code == "hints" or oneDesignation.use.code == "hinweise":
                            theClass.add_Meta(MetaSub("TS_ATTRIBUTE_HINTS", oneDesignation.value))
                        if oneDesignation.language == "de-AT":
                            theClass.add_Meta(MetaSub("TS_ATTRIBUTE_MEANING", oneDesignation.value))

                type_ = "L"
                if self.get_resource() == "CodeSystem" and hasattr(oneConcept,'property'):
                    for oneProperty in oneConcept.property:
                        if oneProperty.code == "kind": # if there is more than one kind in the propertys, the last one is used
                            theClass.set_kind(oneProperty.value)
                        elif oneProperty.code == "parent":
                            theClass.add_SuperClass(SuperClassSub(oneProperty.value))
                        elif oneProperty.code == "child":
                            theClass.add_SubClass(SubClassSub(oneProperty.value))
                            type_ = "S"
                        elif oneProperty.type == pcam.PropertyCodeType.code or oneProperty.type == pcam.PropertyCodeType.boolean or oneProperty.code == "Relationships":
                            theClass.add_Meta(MetaSub(oneProperty.code, oneProperty.value))
                        elif oneProperty.code == "None":
                            the_desig = pcam.ConceptDesignation()
                            the_desig.value = oneProperty.value
                            theClass.add_Rubric(RubricSub(kind="designation", Label=[LabelSub(valueOf_=the_desig)]))
                        else:
                            # normally, a string property should be a rubric, because it is not specificly defined or structured, for legacy purposes it will be set as meta
                            theClass.add_Meta(MetaSub(oneProperty.code, oneProperty.value))
                            #theClass.add_Rubric(RubricSub(kind=(oneProperty.code if oneProperty.code != "None" else None), Label=[LabelSub(lang=language, valueOf_=oneProperty.value)]))
                            # additionally add this to a austrian termpub attribute
                            if oneProperty.code == "hints" or oneProperty.code == "hinweise":
                                theClass.add_Meta(MetaSub("TS_ATTRIBUTE_HINTS", oneProperty.value))

                if self.get_resource() == "ValueSet":
                    if oneConcept.abstract:
                        type_ = "A"
                    elif oneConcept.inactive:
                        type_ = "D"
                        theClass.add_Meta(MetaSub("inactive", "true"))
                    elif oneConcept.member != []:
                        type_ = "S"

                theClass.add_Meta(MetaSub("TS_ATTRIBUTE_ISLEAF", "true" if type_ == "L" else "false"))
                if self.get_resource() == "CodeSystem":
                    theClass.add_Meta(MetaSub("Level", self.retrieve_level_of_CS_concept(concept_dict,oneConcept)))
                if self.get_resource() == "ValueSet":
                    theClass.add_Meta(MetaSub("Level", self.retrieve_level_of_VS_concept(oneConcept)))
                theClass.add_Meta(MetaSub("Type", type_))

                # if there was no kind given, create one with "noKind"
                if temp := theClass.get_kind():
                    theClass.set_kind("noKind")

                exporto_extension_to_class(metas, extensions_written_to_metas, theClass, oneConcept)

                classes.append(theClass)

        claml2 = ClaML2Sub('2.0.0',metas,identifiers,title,authors,None,claKinds,None,rubKinds,None,None,classes)
        claml2.export(outfile, 0, namespacedef_="")

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
