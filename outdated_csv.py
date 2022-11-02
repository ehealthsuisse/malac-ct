import csv
import re
import os
import prop_csv_and_master as pcam

class OutdatedCsv1(pcam.PropCsvAndMaster):
    def __init__(self, inFile=None, versionOfOutdatedCsv=1):
        super().__init__()
        self.versionOfOutdatedCsv = versionOfOutdatedCsv

        # open the file in read mode
        if inFile is not None:
            with open(inFile, 'r', encoding="utf8") as csvfile:
                # creating dictreader object
                file = csv.reader(csvfile, quotechar='\'', delimiter=';')
                # iterating over the next row with headings for concepts
                headingList = file.__next__()

                # initializing header/metadata with mandatory fields from fhir
                if "parentCodeSystemName" in headingList:
                    self.resource = pcam.Resource["ValueSet"]
                else:
                    self.resource = pcam.Resource["CodeSystem"]
                self.version = "unknown due to outdated csv"
                self.name = (re.sub(r'[^A-Za-z0-9\-]+', '', os.path.basename(csvfile.name).replace("CodeSystem-","").replace("ValueSet-","").split('.')[0].replace(" ","-").replace("_","-").replace("--","-").replace("---","-").replace("--","-"))).strip("-").lower()
                self.title = csvfile.name.split('\\')[-1].replace("CodeSystem-","").replace("ValueSet-","").split('.')[0]
                self.status = pcam.Status['active']
                self.description = "unknown due to outdated csv"
                if self.get_resource() == "CodeSystem": self.content = pcam.Content['complete']
                self.concept = []

                # initializing the body/content
                for row in file:
                    if self.resource == self.resource.CodeSystem:
                        theConcept = pcam.CSConcept()
                    elif self.resource == self.resource.ValueSet:
                        theConcept = VSConcept()
                    for i in range(0, len(row)):
                        if row[i].strip() != "":
                            row[i].strip("\"").strip("\'")
                            retiredAlreadySet = False

                            if self.resource == self.resource.CodeSystem:
                                if 'code' == headingList[i]: theConcept.code = row[i]
                                elif 'codeSystem' == headingList[i]: pass
                                elif 'displayName' == headingList[i] and row[i] != "": theConcept.display = row[i]
                                # codesystem and parentCodeSystem columns are beeing ignored, because they doesn't make sense
                                elif 'concept_Beschreibung' == headingList[i] and row[i] != "": theConcept.definition = row[i]
                                elif 'meaning' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.language = "de-AT"
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'hints' == headingList[i] and row[i] != "":
                                    if row[i].startswith("DEPRECATED") or row[i].startswith("inaktiv") and not retiredAlreadySet:
                                        self.set_statusToRetired(theConcept)
                                        retiredAlreadySet = True
                                    elif row[i] != "DEPRECATED" or row[i] != "inaktiv" and not retiredAlreadySet:
                                        theProp = pcam.CSConcept.ConceptProperty()
                                        theProp.code = "hints"
                                        theProp.value = row[i]
                                        theProp.type = pcam.PropertyCodeType.string
                                        theConcept.property.append(theProp)
                                elif 'level' == headingList[i] and row[i] != "" and row[i].strip().isnumeric(): theConcept.level = int(row[i].strip())
                                elif 'type' == headingList[i] and row[i] == "D" and not retiredAlreadySet:
                                    self.set_statusToRetired(theConcept)
                                    retiredAlreadySet = True
                                elif 'type' == headingList[i] and row[i] == "A":
                                    theProp = pcam.CSConcept.ConceptProperty()
                                    theProp.code = "notSelectable"
                                    theProp.value = True
                                    theProp.type = pcam.PropertyCodeType.boolean
                                    theConcept.property.append(theProp)
                                elif 'relationships' == headingList[i] and row[i] != "":
                                    theProp = pcam.CSConcept.ConceptProperty()
                                    theProp.code = "relationships"
                                    theProp.value = row[i]
                                    theProp.type = pcam.PropertyCodeType.string
                                    theConcept.property.append(theProp)
                                # following "parentCode" cant come from the termpub csv, because this column is never filled there, only as a malac export it is filled
                                #if 'parentCode' == headingList[i] and row[i] != "":
                                #    for partOfRow in row[i].split(","):
                                #        theProp = pcam.CSConcept.ConceptProperty()
                                #        theProp.code = "parent"
                                #        theProp.value = partOfRow.strip()
                                #        theProp.type = pcam.PropertyCodeType.code
                                #        theConcept.property.append(theProp)

                                # read all the other properties/designations, if this is a outdated csv v2
                                elif self.versionOfOutdatedCsv == 2 and headingList[i] != "" and row[i] != "":
                                    theProp = pcam.CSConcept.ConceptProperty()
                                    theProp.code = headingList[i]
                                    theProp.value = row[i]
                                    theProp.type = pcam.PropertyCodeType.string
                                    theConcept.property.append(theProp)

                            elif self.resource == self.resource.ValueSet:
                                if 'parentCodeSystemName' == headingList[i]: theConcept.system = row[i]
                                # unknown due to outdated csv
                                #if 'version' == headingList[i]: theConcept.version = row[i]
                                elif 'code' == headingList[i]: theConcept.code = row[i]
                                elif 'displayName' == headingList[i] and row[i] != "": theConcept.display = row[i]
                                elif 'concept_Beschreibung' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^concept_beschreibung^concept_beschreibung^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'meaning' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.language = "de-AT"
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'hints' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^hinweise^hinweise^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'orderNumber' == headingList[i]: theConcept.orderNumber = row[i]
                                elif 'level' == headingList[i] and row[i] != "" and (tmpLevel := int(row[i].strip())): theConcept.level = tmpLevel
                                elif 'type' == headingList[i] and row[i] == "A":
                                    theConcept.abstract = True
                                elif 'relationships' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^relationships^relationships^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'einheit codiert' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^einheit_codiert^einheit_codiert^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)
                                elif 'einheit print' == headingList[i] and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^einheit_print^einheit_print^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)

                                # read the codeSystemVersion, if this is a outdated csv v2
                                elif self.versionOfOutdatedCsv == 2 and 'codeSystemVersion' == headingList[i] and row[i] != "":
                                    theConcept.version = row[i]
                                # read all the other properties/designations, if this is a outdated csv v2
                                elif self.versionOfOutdatedCsv == 2 and headingList[i] != "" and row[i] != "":
                                    theDesig = pcam.ConceptDesignation()
                                    theDesig.use = pcam.Coding(self.globalUrl+"CodeSystem-"+"austrian-designation-use^^"+headingList[i]+"^"+headingList[i]+"^")
                                    theDesig.value = row[i]
                                    theConcept.designation.append(theDesig)

                    self.concept.append(theConcept)

                # close file and return obj
                csvfile.close()

                if self.resource == self.resource.ValueSet:
                    # sort after everthing is read, if there is a orderNumber
                    if self.concept[0].get_orderNumber() is not None:
                        self.concept.sort(key=VSConcept.get_orderNumber)
                    # set members after it is sort and everything is read
                    theMemberParent = [None]*9
                    for oneConcept in self.concept:
                        theMemberParent[oneConcept.level] = oneConcept
                        if oneConcept.level > 0:
                            parent = theMemberParent[oneConcept.level-1]
                            # setting oneConcept as child of the parent
                            parent.member.append(oneConcept)
                            # setting the parent of oneConcept
                            oneConcept.parent = parent

                if self.resource == self.resource.CodeSystem:
                    # set parent and child after everything is read
                    theParent = [None]*9
                    for oneConcept in self.concept:
                        theParent[oneConcept.level] = oneConcept
                        if oneConcept.level > 0:
                            theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                            theProperty.code = "child"
                            theProperty.value = oneConcept.get_code()
                            theProperty.type = pcam.PropertyCodeType.code
                            theParent[oneConcept.level-1].property.append(theProperty)

                            theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                            theProperty.code = "parent"
                            theProperty.value = theParent[oneConcept.level-1].get_code()
                            theProperty.type = pcam.PropertyCodeType.code
                            oneConcept.property.append(theProperty)

    def parse(inFilename):
        return OutdatedCsv1(inFilename)

    def get_url(self):
        if tempUrl := self.globalUrl:
            return tempUrl+self.get_resource()+"-"+self.get_name()
        else:
            return self.get_resource()+"-"+self.get_name()

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False, versionOfOutdatedCsv=1):
        # to stay fully backwards compatible, don't do an other coding of file
        # do an new opening of the file, because of other coding
        #filePath = outfile.name
        #outfile.close()
        #with open(filePath, 'w', newline='', encoding='utf-8') as outfile:

        csv_list = []
        csv_list.append(['code','codeSystem','displayName'])
        if self.get_resource() == "CodeSystem":
            csv_list[0].append('parentCode')
        elif self.get_resource() == "ValueSet":
            csv_list[0].append('parentCodeSystemName')
        csv_list[0].append('concept_Beschreibung')
        csv_list[0].append('meaning')
        csv_list[0].append('hints')
        if self.get_resource() == "ValueSet":
            csv_list[0].append('orderNumber')
        csv_list[0].append('level')
        csv_list[0].append('type')
        csv_list[0].append('relationships')
        if self.get_resource() == "ValueSet":
            csv_list[0].append('einheit print')
            csv_list[0].append('einheit codiert')

        # needed for writing the orderNuber if its a valueset
        runningOrderNumber = 0
        tmpDict = self.buildConceptDictWithAttr("code")
        for oneConcept in self.get_concept():
            # writing csv-code
            conceptRow = [oneConcept.code or ""]

            # writing csv-codeSystem
            if self.get_resource() == "CodeSystem":
                if (identifier := self.get_identifier()) and (tmp := identifier[0]):
                    conceptRow.append(tmp)
                else:
                    conceptRow.append('')
            elif self.get_resource() == "ValueSet":
                if oneConcept.system.startswith('http://') or oneConcept.system.startswith('https://'):
                    conceptRow.append(self.gainOidFromCanonical(oneConcept.system) or "")
                else:
                    conceptRow.append(self.gainOidFromName("CodeSystem-"+oneConcept.system) or "")

            # writing csv-displayName
            conceptRow.append(oneConcept.display or "")

            # writing csv-parentCode as empty in CS / csv-parentCodeSystemName in VS
            if self.get_resource() == "CodeSystem":
                #tmpString = ""
                #for oneProp in oneConcept.property:
                #    if oneProp.code == "parent":
                #        if tmpString != "":
                #            tmpString += ", "
                #        tmpString += oneProp.value
                #conceptRow.append(tmpString)
                conceptRow.append("")
            elif self.get_resource() == "ValueSet":
                conceptRow.append(oneConcept.system or "")

            # writing csv-concept_beschreibung
            if self.get_resource() == "CodeSystem":
                conceptRow.append(oneConcept.definition or "")
            elif self.get_resource() == "ValueSet":
                foundIt = False
                for oneDesig in oneConcept.designation:
                    if hasattr(oneDesig,"use") and oneDesig.use.code == "concept_beschreibung":
                        conceptRow.append(oneDesig.value)
                        foundIt = True
                if foundIt == False:
                    conceptRow.append("")

            # writing csv-meaning
            foundIt = False
            for oneDesig in oneConcept.designation:
                if hasattr(oneDesig,'language') and oneDesig.language == "de-AT":
                    conceptRow.append(oneDesig.value or "")
                    foundIt = True
            if foundIt == False:
                conceptRow.append("")

            # writing csv-hints
            tmpString = ""
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "status" and oneProp.value == "retired":
                        if tmpString != "":
                            tmpString += ", "
                        tmpString += "DEPRECATED"
                    if oneProp.code == "hints":
                        if tmpString != "":
                            tmpString += ", "
                        tmpString += oneProp.value.replace(";",",")
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if hasattr(oneDesig,"use") and oneDesig.use.code == "hinweise":
                        if tmpString != "":
                            tmpString += ", "
                        tmpString += oneDesig.value
            conceptRow.append(tmpString)

            # writing csv-orderNumber (only VS)
            if self.get_resource() == "ValueSet":
                runningOrderNumber += 1
                conceptRow.append(runningOrderNumber)

            # writing csv-level
            if self.get_resource() == "CodeSystem":
                lvl = 0
                key = oneConcept.code
                thereIsAParent = True
                while thereIsAParent:
                    # if there is a parent, than it will be set once to True
                    thereIsAParent = False
                    for oneProp in tmpDict[key].property:
                        if oneProp.code == "parent":
                            thereIsAParent = True
                            lvl = lvl+1
                            key = oneProp.value
                conceptRow.append(lvl)
            elif self.get_resource() == "ValueSet":
                conceptRow.append(oneConcept.level)

            # writing csv-type
            if self.get_resource() == "CodeSystem":
                foundIt = False
                for oneProp in oneConcept.property:
                    # overruled following # for same behaivor like termpub csv, deprecation status is never set in type
                    if oneProp.code == "status" and oneProp.value == "retired":
                        conceptRow.append("D")
                        foundIt = True
                        break
                    elif oneProp.code == "notSelectable" and oneProp.value == "true":
                        conceptRow.append("A")
                        foundIt = True
                        break
                    elif oneProp.code == "child":
                        conceptRow.append("S")
                        foundIt = True
                        break
                if foundIt == False:
                    conceptRow.append("L")
            elif self.get_resource() == "ValueSet":
                if oneConcept.abstract:
                    conceptRow.append("A")
                elif oneConcept.member != []:
                    conceptRow.append("S")
                else:
                    conceptRow.append("L")

            # writing csv-relationships
            foundIt = False
            if self.get_resource() == "CodeSystem":
                for oneProp in oneConcept.property:
                    if oneProp.code == "relationships":
                        conceptRow.append(oneProp.value or "")
                        foundIt = True
                        break
            elif self.get_resource() == "ValueSet":
                for oneDesig in oneConcept.designation:
                    if hasattr(oneDesig,"use") and oneDesig.use.code == "relationships":
                        conceptRow.append(oneDesig.value)
                        foundIt = True
                        break
            if foundIt == False:
                conceptRow.append("")

            # writing csv-einheit print (only VS)
            if self.get_resource() == "ValueSet":
                foundIt = False
                for oneDesig in oneConcept.designation:
                    if hasattr(oneDesig,"use") and oneDesig.use.code == "einheit_print":
                        conceptRow.append(oneDesig.value or "")
                        foundIt = True
                        break
                if foundIt == False:
                    conceptRow.append("")

            # writing csv-einheit codiert (only VS)
            if self.get_resource() == "ValueSet":
                foundIt = False
                for oneDesig in oneConcept.designation:
                    if hasattr(oneDesig,"use") and oneDesig.use.code == "einheit_codiert":
                        conceptRow.append(oneDesig.value or "")
                        foundIt = True
                        break
                if foundIt == False:
                    conceptRow.append("")

            # write all the other properties/designations, if this is a outdated csv v2
            if versionOfOutdatedCsv == 2:
                if self.get_resource() == "ValueSet":
                    # write the system version if existent
                    if hasattr(oneConcept, 'version') and oneConcept.version:
                        # look up if there is already one column we could use
                        if 'codeSystemVersion' not in csv_list[0]:
                            csv_list[0].append('codeSystemVersion')

                        # add "" for not existing props in this concept to conceptRow
                        while len(conceptRow) <= csv_list[0].index('codeSystemVersion'):
                            conceptRow.append("")

                        conceptRow[csv_list[0].index('codeSystemVersion')] = oneConcept.version
                    else:
                        # retrieve version from metadata

                        # theoretically one_concept.system could be either canonical or OID in
                        # most cases, however, it would be the canonical
                        if tmp := self.gainVersionFromCanonical(oneConcept.system):
                            # look up if there is already one column we could use
                            if 'codeSystemVersion' not in csv_list[0]:
                                csv_list[0].append('codeSystemVersion')

                            # add "" for not existing props in this concept to conceptRow
                            while len(conceptRow) <= csv_list[0].index('codeSystemVersion'):
                                conceptRow.append("")

                            conceptRow[csv_list[0].index('codeSystemVersion')] = tmp
                        elif tmp := self.gainVersionFromOid(oneConcept.system):
                            # look up if there is already one column we could use
                            if 'codeSystemVersion' not in csv_list[0]:
                                csv_list[0].append('codeSystemVersion')

                            # add "" for not existing props in this concept to conceptRow
                            while len(conceptRow) <= csv_list[0].index('codeSystemVersion'):
                                conceptRow.append("")

                            conceptRow[csv_list[0].index('codeSystemVersion')] = tmp

                if hasattr(oneConcept,"property"):
                    #oneConcept.property.sort(key=pcam.CSConcept.ConceptProperty.get_code) # TODO discuss if sort should be done for properties
                    for oneProp in oneConcept.property:
                        if oneProp.code != "relationships" and oneProp.code != "child" and oneProp.code != "parent" and oneProp.code != "hints":
                            # look up if there is already one column we could use
                            if oneProp.code not in csv_list[0]:
                                csv_list[0].append(oneProp.code)

                            # add "" for not existing props in this concept to conceptRow
                            while len(conceptRow) <= csv_list[0].index(oneProp.code):
                                conceptRow.append("")

                            conceptRow[csv_list[0].index(oneProp.code)] = oneProp.value
                            #conceptRow.append(oneProp.value)

                            csv_list[0][csv_list[0].index(oneProp.code)]
                if hasattr(oneConcept,"designation"):
                    for oneDesig in oneConcept.designation:
                        if (hasattr(oneDesig,"use") and oneDesig.use.code != "einheit_codiert" and oneDesig.use.code != "einheit_print" and
                                oneDesig.language != "de-AT" and oneDesig.use.code != "relationships" and
                                oneDesig.use.code != "hinweise" and oneDesig.use.code != "concept_beschreibung"):
                            # look up if there is already one column we could use
                            if oneDesig.use.code not in csv_list[0]:
                                csv_list[0].append(oneDesig.use.code)

                            # add "" for not existing props in this concept to conceptRow
                            while len(conceptRow) <= csv_list[0].index(oneDesig.use.code):
                                conceptRow.append("")

                            conceptRow[csv_list[0].index(oneDesig.use.code)] = oneDesig.value


            # add conceptRow to csv list
            csv_list.append(conceptRow)

        for csvline in csv_list:
            newline = True
            for csvelement in csvline:
                if versionOfOutdatedCsv == 2 and csvelement == "":
                    outfile.write((";" if not newline else ""))
                else:
                    outfile.write((";" if not newline else "") + "\'" + str(csvelement).replace("'","´").replace(";",",") + "\'")
                newline = False
            outfile.write("\n")

class OutdatedCsv2(OutdatedCsv1):
    def __init__(self, inFile=None, versionOfOutdatedCsv=2):
        OutdatedCsv1.__init__(self, inFile, versionOfOutdatedCsv)

    def parse(inFilename):
        return OutdatedCsv2(inFilename)

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False, versionOfOutdatedCsv=2):
        return OutdatedCsv1.exporto(self, outfile, outputClass, argsLang, incHierarchyExt4VS, versionOfOutdatedCsv)

class VSConcept(pcam.VSConcept):
    def __init__(self) -> None:
        super().__init__()
        self.orderNumber = None

    # used only for sorting mechanism
    def get_orderNumber(self):
        return self.orderNumber