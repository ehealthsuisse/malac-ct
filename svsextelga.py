#!/usr/bin/env python

#
# Generated Wed Jun  1 13:33:35 2022 by generateDS.py version 2.40.12.
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'svsextelga1super2.py')
#   ('-s', 'svsextelga2.py')
#
# Command line arguments:
#   .\SVS-extELGA2.xsd
#
# Command line:
#   generateDS.py -o "svsextelga1super2.py" -s "svsextelga2.py" .\SVS-extELGA2.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.40.12
#

from datetime import date
from fileinput import filename
import os
import re
import sys
from lxml import etree as etree_

import svsextelga2super as supermod
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

class SVSextELGA1Sub(supermod.SVSextELGA2, pcam.PropCsvAndMaster):
    def __init__(self, beschreibung=None, description=None, displayName=None, effectiveDate=None, gueltigkeitsbereich=None, id=None, last_change_date=None, name=None, statusCode=None, status_date=None, verantw_Org=None, version=None, website=None, conceptList=None, versionSVSextELGA=1, **kwargs_):
        self.versionSVSextELGA = versionSVSextELGA
        super(SVSextELGA1Sub, self).__init__(beschreibung, description, displayName, effectiveDate, gueltigkeitsbereich, id, last_change_date, name, statusCode, status_date, verantw_Org, version, website, conceptList,  **kwargs_)

    # just for calling the outer method
    def parse(inFilename):
        return parse(inFilename)

    def get_resource(self):
        if hasattr(self,"resource") and (res := self.resource):
            return res
        elif hasattr(self,"filename") and (fn := self.filename):
            if os.path.basename(fn).startswith("CodeSystem-"):
                return pcam.Resource.CodeSystem.value
            elif os.path.basename(fn).startswith("ValueSet-"):
                return pcam.Resource.ValueSet.value
        else:
            return pcam.Resource.ValueSet.value

    def get_url(self):
        if tempUrl := self.globalUrl:
            return tempUrl+self.get_resource()+"-"+self.get_name()
        return None

    #def get_version(self):
    #    return self.get_version()

    def get_name(self):
        return (re.sub(r'[^A-Za-z0-9\-]+', '', super(SVSextELGA1Sub,self).get_name().replace(" ","-").replace("_","-").replace("--","-").replace("---","-").replace("--","-"))).strip("-").lower()

    def get_title(self):
        return super(SVSextELGA1Sub,self).get_name()

    def get_status(self):
        return pcam.Status.active.value

    def get_description(self):
        tempRet = ""
        boolAddedSomething = False
        if (tempDescEn := super(SVSextELGA1Sub,self).get_description()) and not tempDescEn == "":
            tempRet += "**Description:** "
            tempRet += tempDescEn
            boolAddedSomething = True

        if (tempBesch := self.get_beschreibung()) and not tempBesch == "":
            if boolAddedSomething:
                tempRet += "\n\n"
            tempRet += "**Beschreibung:** "
            tempRet += tempBesch
            boolAddedSomething = True

        # TODO check if there is no version description in svs

        if tempRet == "":
            tempRet = None
        return tempRet

    def get_content(self):
        if hasattr(self,"content") and (tmp := self.content):
            return tmp
        else:
            return pcam.Content.complete.value

    def get_implicitrules(self):
        return None

    def get_language(self):
        return None

    def get_text(self):
        return None

    def get_contained(self):
        return None

    def get_extension(self):
        return None

    def get_modifierextension(self):
        return None

    def get_identifier(self):
        if hasattr(self,"identifier"):
            return self.identifier
        identifiers = []
        if tempID := self.get_id():
            identifiers.append(tempID)
        return identifiers

    def get_experimental(self):
        return None

    def get_date(self):
        return str(self.get_effectiveDate())

    def get_publisher(self):
        if (tmp := self.get_verantw_Org()) and tmp != "":
            return tmp
        return None

    def get_contact(self):
        tempConDetS = []
        if (website := self.get_website()) and not website == "":
            oneConDet = pcam.ContactDetail()
            oneConPoi = pcam.ContactDetail.ContactPoint()
            oneConPoi.value = website
            oneConPoi.system = pcam.ContactDetail.ContactPoint.ContactPointSystem.url.value
            oneConDet.telecom.append(oneConPoi)
            tempConDetS.append(oneConDet)
        return tempConDetS

    def get_usecontext(self):
        return None

    def get_jurisdiction(self):
        return None

    def get_purpose(self):
        return None

    def get_copyright(self):
        return None

    def get_immutable(self):
        return None

    def get_lockeddate(self):
        return None

    def get_inactive(self):
        return None

    def get_casesensitive(self):
        return None

    def get_valueset(self):
        return None

    def get_hierarchymeaning(self):
        return None

    def get_compositional(self):
        return None

    def get_versionneeded(self):
        return None

    def get_supplements(self):
        tmpSupplUrl = ""
        if tempUrl := self.globalUrl:
            tmpSupplUrl += tempUrl
        if hasattr(self,"supplements") and (tmp := self.supplements) and tmp != "":
            return tmpSupplUrl+tmp
        return None

    def get_count(self):
        return len(self.get_concept())

    def get_filter(self):
        return None

    def get_concept(self):
        if hasattr(self, "concept") and self.concept:
            return self.concept
        else:
            retArr = []
            theMemberParent = [None]*9
            # sort with the orderNumber or sort after code
            sortedConceptList = self.get_conceptList().get_concept()
            if sortedConceptList[0].get_orderNumber() is not None:
                sortedConceptList.sort(key=supermod.concept.get_orderNumber)
            else:
                sortedConceptList.sort(key=supermod.concept.get_code)
            # iterate though the list
            if self.get_resource() == "ValueSet":
                for oneCon in sortedConceptList:
                    theConcept = pcam.VSConcept()

                    if (tmp := oneCon.get_parentCodeSystemName()) and (tmp.startswith('http://') or tmp.startswith('https://')):
                        theConcept.system = tmp
                    else:
                        theConcept.system = self.globalUrl+"CodeSystem-"+ (re.sub(r'[^A-Za-z0-9\-]+', '', oneCon.get_parentCodeSystemName().replace(" ","-").replace("_","-").replace("--","-").replace("---","-").replace("--","-"))).strip("-").lower()

                    theConcept.code = oneCon.get_code()
                    theConcept.display = oneCon.get_displayName()

                    if oneCon.get_type() == "A":
                        theConcept.abstract = True
                    if (tmpDeutsch := oneCon.get_deutsch()) and tmpDeutsch.strip() != "" and tmpDeutsch != oneCon.get_displayName():
                        theDesig = pcam.ConceptDesignation()
                        theDesig.language = "de-AT"
                        theDesig.value = tmpDeutsch
                        theConcept.designation.append(theDesig)
                    if (tmpDisAlt := oneCon.get_displayNameAlt()) and tmpDisAlt.strip() != "" and tmpDisAlt != oneCon.get_displayName() and tmpDisAlt != tmpDeutsch:
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##alt#alt")
                        theDesig.value = tmpDisAlt
                        theConcept.designation.append(theDesig)
                    if (tmp := oneCon.get_concept_beschreibung()) and tmp.strip() != "":
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##concept_beschreibung#concept_beschreibung")
                        theDesig.value = tmp
                        theConcept.designation.append(theDesig)
                    if (tmp := oneCon.get_einheit_codiert()) and tmp.strip() != "":
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##einheit_codiert#einheit_codiert")
                        theDesig.value = tmp
                        theConcept.designation.append(theDesig)
                    if (tmp := oneCon.get_einheit_print()) and tmp.strip() != "":
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##einheit_print#einheit_print")
                        theDesig.value = tmp
                        theConcept.designation.append(theDesig)
                    if (tmp := oneCon.get_hinweise()) and tmp.strip() != "":
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##hinweise#hinweise")
                        theDesig.value = tmp
                        theConcept.designation.append(theDesig)
                    if (tmp := oneCon.get_relationships()) and tmp.strip() != "":
                        theDesig = pcam.ConceptDesignation()
                        theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##relationships#relationships")
                        theDesig.value = tmp
                        theConcept.designation.append(theDesig)

                    if 0 <= (tmpLevel := int(oneCon.get_level().strip())):
                        theConcept.level = tmpLevel
                        theMemberParent[tmpLevel] = theConcept
                        if tmpLevel > 0:
                            theMemberParent[tmpLevel-1].member.append(theConcept)

                    # read anyAttribute if version 2
                    if self.versionSVSextELGA == 2:
                        for oneAttrKey in oneCon.get_anyAttributes_():
                            theDesig = pcam.ConceptDesignation()
                            theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use##"+oneAttrKey+"#"+oneAttrKey)
                            theDesig.value = oneCon.get_anyAttributes_()[oneAttrKey]
                            theConcept.designation.append(theDesig)

                    retArr.append(theConcept)

            elif self.get_resource() == "CodeSystem":
                for oneCon in sortedConceptList:
                    theConcept = pcam.CSConcept()
                    theConcept.code = oneCon.get_code()
                    theConcept.display = oneCon.get_displayName()
                    retiredAlreadySet = False

                    if (theConcept.display.upper().startswith("DEPRECATED") and not retiredAlreadySet):
                        self.set_statusToRetired(theConcept)
                        retiredAlreadySet = True
                    if (oneCon.get_type() == "D" and not retiredAlreadySet):
                        self.set_statusToRetired(theConcept)
                        retiredAlreadySet = True
                    if oneCon.get_type() == "A":
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "notSelectable"
                        theProp.value = True
                        theProp.type = pcam.PropertyCodeType.boolean
                        theConcept.property.append(theProp)

                    if (tmpDeutsch := oneCon.get_deutsch()) and tmpDeutsch.strip() != "" and tmpDeutsch != oneCon.get_displayName():
                        theDesig = pcam.ConceptDesignation()
                        theDesig.language = "de-AT"
                        theDesig.value = tmpDeutsch
                        theConcept.designation.append(theDesig)
                    if (tmpDisAlt := oneCon.get_displayNameAlt()) and tmpDisAlt.strip() != "" and tmpDisAlt != oneCon.get_displayName() and tmpDisAlt != tmpDeutsch:
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "displayNameAlt"
                        theProp.value = tmpDisAlt
                        theProp.type = pcam.PropertyCodeType.string
                        theConcept.property.append(theProp)
                    if (tmp := oneCon.get_concept_beschreibung()) and tmp.strip() != "":
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "concept_beschreibung"
                        theProp.value = tmp
                        theProp.type = pcam.PropertyCodeType.string
                        theConcept.property.append(theProp)
                    if (tmp := oneCon.get_einheit_codiert()) and tmp.strip() != "":
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "einheit_codiert"
                        theProp.value = tmp
                        theProp.type = pcam.PropertyCodeType.string
                        theConcept.property.append(theProp)
                    if (tmp := oneCon.get_einheit_print()) and tmp.strip() != "":
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "einheit_print"
                        theProp.value = tmp
                        theProp.type = pcam.PropertyCodeType.string
                        theConcept.property.append(theProp)
                    if (tmp := oneCon.get_hinweise()) and tmp.strip() != "":
                        if (tmp.upper().startswith("DEPRECATED") or tmp.upper().startswith("INAKTIV")) and not retiredAlreadySet:
                            self.set_statusToRetired(theConcept)
                            retiredAlreadySet = True
                        else:
                            theProp = pcam.CSConcept.ConceptProperty()
                            theProp.code = "hinweise"
                            theProp.value = tmp
                            theProp.type = pcam.PropertyCodeType.string
                            theConcept.property.append(theProp)
                    if (tmp := oneCon.get_relationships()) and tmp.strip() != "":
                        theProp = pcam.CSConcept.ConceptProperty()
                        theProp.code = "relationships"
                        theProp.value = tmp
                        theProp.type = pcam.PropertyCodeType.string
                        theConcept.property.append(theProp)


                    if 0 <= (tmpLevel := int(oneCon.get_level().strip())):
                        theMemberParent[tmpLevel] = theConcept
                        if tmpLevel > 0:
                            theProperty = pcam.CSConcept.ConceptProperty()
                            theProperty.code = "child"
                            theProperty.value = oneCon.get_code()
                            theProperty.type = pcam.PropertyCodeType.code
                            theMemberParent[tmpLevel-1].property.append(theProperty)

                            theProperty = pcam.CSConcept.ConceptProperty()
                            theProperty.code = "parent"
                            theProperty.value = theMemberParent[tmpLevel-1].code
                            theProperty.type = pcam.PropertyCodeType.code
                            theConcept.property.append(theProperty)

                    # read anyAttribute if version 2
                    if self.versionSVSextELGA == 2:
                        for oneAttrKey in oneCon.get_anyAttributes_():
                            theProp = pcam.CSConcept.ConceptProperty()
                            theProp.code = oneAttrKey
                            theProp.value = oneCon.get_anyAttributes_()[oneAttrKey]
                            theProp.type = pcam.PropertyCodeType.string
                            theConcept.property.append(theProp)

                    retArr.append(theConcept)
            self.concept = retArr
            return retArr

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False, versionSVSextELGA=1):
        beschreibung = description = ""
        if (tmp := self.get_description()) and len(tmp := self.get_description().split("**")) >= 5:
            if "Beschreibung:" in tmp:
                beschreibung = tmp[tmp.index("Beschreibung:")+1].strip()
            if "Description:" in tmp:
                description = tmp[tmp.index("Description:")+1].strip()
        else:
            beschreibung = description = self.get_description()

        displayName = self.get_title()
        effectiveDate = last_change_date = status_date = self.get_date() or date.today() # TODO should here be the today date?
        gueltigkeitsbereich = "empfohlen"

        if (identifier := self.get_identifier()) and (tmp := identifier[0]) and (re.match('([0-9]+\.)+[0-9]+',tmp)):
            id = tmp
        else:
            id = self.gainOidFromName(self.get_resource()+"-"+self.get_name())

        name = self.get_name()
        statusCode = "1"
        verantw_Org = self.get_publisher() or ""
        version = self.get_version()

        foundIt = False
        for oneConcept in self.get_contact():
            if (tmp := oneConcept.telecom) and tmp[0].system == pcam.ContactDetail.ContactPoint.ContactPointSystem.url.value:
                website = oneConcept.telecom[0].value
                foundIt = True
        if not foundIt:
            website = ""

        concepts = []
        orderNumber = 0
        tmpDict = self.buildConceptDictWithAttr("code")
        for oneConcept in self.get_concept():
            # code can directly be appended, see concepts.append

            # creating codeSystem
            codeSystem = None
            if self.get_resource() == "CodeSystem":
                if (identifier := self.get_identifier()) and (tmp := identifier[0]):
                    codeSystem = tmp
                else:
                    codeSystem = ''
            elif self.get_resource() == "ValueSet":
                if oneConcept.system.startswith('http://') or oneConcept.system.startswith('https://'):
                    codeSystem = self.gainOidFromCanonical(oneConcept.system) or ""
                else:
                    codeSystem = self.gainOidFromName("CodeSystem-"+oneConcept.system) or ""

            # creating concept_beschreibung
            concept_beschreibung = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "concept_beschreibung":
                        concept_beschreibung = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "concept_beschreibung":
                        concept_beschreibung = oneDesig.value

            # creating deutsch
            deutsch = None
            foundIt = False
            for oneDesig in oneConcept.designation:
                if oneDesig.language == "de-AT":
                    deutsch = oneDesig.value
                    foundIt = True
            if not foundIt:
                deutsch = oneConcept.display

            # displayName can directly be appended, see concepts.append

            # creating displayNameAlt
            displayNameAlt = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "displayNameAlt":
                        displayNameAlt = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "alt":
                        displayNameAlt = oneDesig.value

            # creating einheit_codiert
            einheit_codiert = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "einheit_codiert":
                        einheit_codiert = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "einheit_codiert":
                        einheit_codiert = oneDesig.value

            # creating einheit_print
            einheit_print = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "einheit_print":
                        einheit_print = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "einheit_print":
                        einheit_print = oneDesig.value

            # creating hinweise
            hinweise = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "hinweise":
                        hinweise = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "hinweise":
                        hinweise = oneDesig.value

            # creating level
            level = None
            if self.get_resource() == "CodeSystem":
                level = 0
                key = oneConcept.code
                thereIsAParent = True
                while thereIsAParent:
                    # if there is a parent, than it will be set once to True
                    thereIsAParent = False
                    for oneProp in tmpDict[key].property:
                        if oneProp.code == "parent":
                            thereIsAParent = True
                            level = level+1
                            key = oneProp.value
            elif self.get_resource() == "ValueSet":
                level = oneConcept.level

            # creating orderNumber
            orderNumber += 1

            # creating parentCodeSystemName
            parentCodeSystemName = None
            if self.get_resource() == "ValueSet":
                parentCodeSystemName = oneConcept.system

            # creating relationships
            relationships = None
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "relationships":
                        relationships = oneProp.value
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if oneDesig.use.code == "relationships":
                        relationships = oneDesig.value

            # creating type
            type_ = None
            if self.get_resource() == "CodeSystem":
                foundIt = False
                for oneProp in oneConcept.property:
                    # overruled following # for same behaivor like termpub csv, deprecation status is never set in type
                    if oneProp.code == "status" and oneProp.value == "retired":
                        type_= "D"
                        foundIt = True
                        break
                    elif oneProp.code == "notSelectable" and oneProp.value == "true":
                        type_ = "A"
                        foundIt = True
                        break
                    elif oneProp.code == "child":
                        type_ = "S"
                        foundIt = True
                        break
                if foundIt == False:
                    type_ = "L"
            elif self.get_resource() == "ValueSet":
                if oneConcept.member != []:
                    type_ = "S"
                elif oneConcept.abstract:
                    type_ = "A"
                else:
                    type_ = "L"

            concepts.append(conceptSub(oneConcept.code or "",codeSystem or "", 1, self.get_date() or date.today(), # TODO should here be the today date?
              concept_beschreibung or "", deutsch or "", oneConcept.display or "", displayNameAlt,
              einheit_codiert, einheit_print, hinweise or "", level, orderNumber,
              parentCodeSystemName or "", relationships or "", type_ or ""))

            # create anyAttribute if version 2
            if versionSVSextELGA == 2:
                anyAttrDict = {}
                if self.get_resource() == "CodeSystem":
                    for oneProp in oneConcept.property:
                        if (oneProp.code != "status" and oneProp.code != "notSelectable" and oneProp.code != "child"
                        and oneProp.code != "relationships" and oneProp.code != "parent" and oneProp.code != "hinweise"
                        and oneProp.code != "einheit_print" and oneProp.code != "einheit_codiert"
                        and oneProp.code != "displayNameAlt" and oneProp.code != "concept_beschreibung"):
                            anyAttrDict.update({oneProp.code: oneProp.value})
                elif self.get_resource() == "ValueSet":
                    for oneDesig in oneConcept.designation:
                        if (oneDesig.use.code != "relationships" and oneDesig.use.code != "hinweise"
                        and oneDesig.use.code != "einheit_print" and oneDesig.use.code != "einheit_codiert"
                        and oneDesig.use.code != "alt" and oneDesig.language != "de-AT"
                        and oneDesig.use.code != "concept_beschreibung"):
                            anyAttrDict.update({oneDesig.use.code: oneDesig.value})
                concepts[-1].set_anyAttributes_(anyAttrDict)

        conceptList = conceptListSub(concepts)
        svsExtElga2 = SVSextELGA2Sub(beschreibung,description,displayName,effectiveDate,gueltigkeitsbereich,id,last_change_date,name,statusCode,status_date,verantw_Org,version,website,conceptList)
        svsExtElga2.export(outfile, 0)
supermod.SVSextELGA2.subclass = SVSextELGA1Sub
# end class valueSetSub

class SVSextELGA2Sub(SVSextELGA1Sub):
    def __init__(self, beschreibung=None, description=None, displayName=None, effectiveDate=None, gueltigkeitsbereich=None, id=None, last_change_date=None, name=None, statusCode=None, status_date=None, verantw_Org=None, version=None, website=None, conceptList=None, versionSVSextELGA=2, **kwargs_):
        SVSextELGA1Sub.__init__(self, beschreibung, description, displayName, effectiveDate, gueltigkeitsbereich, id, last_change_date, name, statusCode, status_date, verantw_Org, version, website, conceptList, versionSVSextELGA, **kwargs_)

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False, versionSVSextELGA=2):
        return SVSextELGA1Sub.exporto(self, outfile, outputClass, argsLang, incHierarchyExt4VS, versionSVSextELGA)
supermod.SVSextELGA2.subclass = SVSextELGA2Sub

class conceptListSub(supermod.conceptList):
    def __init__(self, concept=None, **kwargs_):
        super(conceptListSub, self).__init__(concept,  **kwargs_)
supermod.conceptList.subclass = conceptListSub
# end class conceptListSub


class conceptSub(supermod.concept):
    def __init__(self, code=None, codeSystem=None, conceptStatus=None, conceptStatusDate=None, concept_beschreibung=None, deutsch=None, displayName=None, displayNameAlt=None, einheit_codiert=None, einheit_print=None, hinweise=None, level=None, orderNumber=None, parentCodeSystemName=None, relationships=None, type_=None, **kwargs_):
        super(conceptSub, self).__init__(code, codeSystem, conceptStatus, conceptStatusDate, concept_beschreibung, deutsch, displayName, displayNameAlt, einheit_codiert, einheit_print, hinweise, level, orderNumber, parentCodeSystemName, relationships, type_,  **kwargs_)
supermod.concept.subclass = conceptSub
# end class conceptSub


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
        rootTag = 'valueSet'
        rootClass = supermod.SVSextELGA2
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
        rootTag = 'valueSet'
        rootClass = supermod.SVSextELGA2
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
        rootTag = 'valueSet'
        rootClass = supermod.SVSextELGA2
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
        rootTag = 'valueSet'
        rootClass = supermod.SVSextELGA2
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
