import enum
from unittest import skip

class PropCsvAndMaster():
    def __init__(self, inFile = None):
        self.resource = Resource
        self.url = None
        self.version = None
        self.name = None
        self.title = None
        self.status = Status
        self.description = None
        self.content = Content
        self.implicitrules = None
        self.language = None
        self.text = None
        self.contained = None
        self.extension = None
        self.modifierextension = None
        self.identifier = []
        self.experimental = None
        self.date = None
        self.publisher = None
        self.contact = []
        self.usecontext = []
        self.jurisdiction = []
        self.purpose = None
        self.copyright = None
        self.concept = []
        # following are used only in ValueSets
        self.immutable = None
        self.lockeddate = None
        self.inactive = None
        # following are used only in CodeSystems
        self.casesensitive = None
        self.valueset = None
        self.hierarchymeaning = None #HierarchyMeaning
        self.compositional = None
        self.versionneeded = None
        self.supplements = None
        self.count = None
        self.filter = []
        self.property = []

        if inFile is not None:
            # open the file in read mode, special encoding because of Excel compatibility, see https://stackoverflow.com/questions/6588068/which-encoding-opens-csv-files-correctly-with-excel-on-both-mac-and-windows
            with open(inFile, 'r', encoding="cp1252") as csvfile:
                import csv
                # creating dictreader object
                file = csv.reader(csvfile, quotechar='\"', delimiter=';')
                # iterating over first two rows and append values to empty list
                metaList = [file.__next__()]+[file.__next__()]
                # iterating over a empty row
                file.__next__()
                # iterating over the next row with headings for concepts
                headingList = file.__next__()

                #initializing the header/metadata
                i = -1
                for metaObj in metaList[0]:
                    i += 1
                    # change all ';' to ','
                    #metaList[1][i].replace(';',',')
                    metaList[1][i].strip("\"")

                    if 'resource' == metaObj: self.resource = Resource(metaList[1][i])
                    if 'url' == metaObj: self.url = metaList[1][i]
                    if 'version' == metaObj: self.version = metaList[1][i]
                    if 'name' == metaObj: self.name = metaList[1][i]
                    if 'title' == metaObj: self.title = metaList[1][i]
                    if 'status' == metaObj: self.status = Status(metaList[1][i])
                    if 'description' == metaObj: self.description = metaList[1][i]
                    if 'content' == metaObj: self.content = Content(metaList[1][i])
                    if 'implicitRules' == metaObj: self.implicitrules = metaList[1][i]
                    if 'language' == metaObj: self.language = metaList[1][i]
                    if 'text' == metaObj: self.text = metaList[1][i]
                    if 'contained' == metaObj: self.contained = metaList[1][i]
                    if 'extension' == metaObj: self.extension = metaList[1][i]
                    if 'modifierExtension' == metaObj: self.modifierextension = metaList[1][i]
                    if 'identifier' == metaObj: self.identifier.append(metaList[1][i])
                    if 'date' == metaObj: self.date = metaList[1][i]
                    if 'experimental' == metaObj: self.experimental = metaList[1][i]
                    if 'publisher' == metaObj: self.publisher = metaList[1][i]
                    if 'contact' == metaObj: self.contact.append(metaList[1][i])
                    if 'useContext' == metaObj: self.usecontext.append(metaList[1][i])
                    if 'jurisdiction' == metaObj: self.jurisdiction.append(metaList[1][i])
                    if 'purpose' == metaObj: self.purpose = metaList[1][i]
                    if 'copyright' == metaObj: self.copyright = metaList[1][i]
                    if 'immutable' == metaObj: self.immutable = metaList[1][i]
                    if 'lockedDate' == metaObj: self.lockeddate = metaList[1][i]
                    if 'caseSensitive' == metaObj: self.casesensitive = metaList[1][i]
                    if 'valueSet' == metaObj: self.valueset = metaList[1][i]
                    if 'hierarchyMeaning' == metaObj: self.hierarchymeaning = HierarchyMeaning(metaList[1][i])
                    if 'compositional' == metaObj: self.compositional = metaList[1][i]
                    if 'versionNeeded' == metaObj: self.versionneeded = metaList[1][i]
                    if 'supplements' == metaObj: self.supplements = metaList[1][i]
                    if 'count' == metaObj: self.count = metaList[1][i]
                    if 'filter' == metaObj:
                        filterElements = metaList[1][i].split('|')
                        tempFilter = Filter()
                        tempFilter.code = filterElements[0]
                        tempFilter.description = filterElements[1]
                        tempFilter.operator = filterElements[2]
                        tempFilter.value = filterElements[3]
                        self.filter.append(tempFilter)
                    if 'property' == metaObj:
                        propElements = metaList[1][i].split('|')
                        tempProperty = Property()
                        tempProperty.code = propElements[0]
                        tempProperty.uri = propElements[1]
                        tempProperty.description = propElements[2]
                        tempProperty.type = PropertyCodeType(propElements[3].lower())
                        self.property.append(tempProperty)

                #initializing the body/content
                for row in file:

                    if self.resource == self.resource.CodeSystem:
                        tempConcept = CSConcept()
                    elif self.resource == self.resource.ValueSet:
                        tempConcept = VSConcept()

                    for i in range(0, len(row)):
                        if row[i].strip() != "":
                            row[i].strip("\"").strip("\'")

                            if self.resource == self.resource.CodeSystem:
                                if 'code' == headingList[i]: tempConcept.code = row[i]
                                if 'display' == headingList[i]: tempConcept.display = row[i]
                                if 'definition' == headingList[i]: tempConcept.definition = row[i]
                                if 'designation' == headingList[i]:
                                    tempConcept.designation.append(ConceptDesignation(row[i]))
                                if 'property' == headingList[i]:
                                    propertyElements = row[i].split('|')
                                    tempProperty = CSConcept.ConceptProperty()
                                    tempProperty.code = propertyElements[0]
                                    tempProperty.value = propertyElements[1]
                                    tempProperty.type = PropertyCodeType(propertyElements[2].lower())
                                    tempConcept.property.append(tempProperty)

                            elif self.resource == self.resource.ValueSet:
                                if 'system' == headingList[i]: tempConcept.system = row[i]
                                if 'version' == headingList[i]: tempConcept.version = row[i]
                                if 'code' == headingList[i]: tempConcept.code = row[i]
                                if 'display' == headingList[i]: tempConcept.display = row[i]
                                if 'designation' == headingList[i]:
                                    tempConcept.designation.append(ConceptDesignation(row[i]))
                                if 'filter' == headingList[i]:
                                    filterElements = row[i].split('|')
                                    tempFilter = VSConcept.VSConceptFilter()
                                    tempFilter.property = filterElements[0]
                                    tempFilter.op = filterElements[1]
                                    tempFilter.value = filterElements[2]
                                    tempConcept.filter = tempFilter # this is not a list!
                                if 'abstract' == headingList[i]:
                                    if row[i].lower() == "true" or "yes" or "1":
                                        tempConcept.abstract = True
                                if 'exclude' == headingList[i]:
                                    if row[i].lower() == "true" or "yes" or "1":
                                        tempConcept.exclude = True

                    self.concept.append(tempConcept)

    def parse(inFilename):
        return PropCsvAndMaster(inFilename)

    def get_resource(self):
        return self.resource.value

    def get_url(self):
        return self.url

    def get_version(self):
        return self.version

    # TODO build in a recognition if CodeSystem oder ValueSet is already in name
    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def get_status(self):
        return self.status.value

    def get_description(self):
        return self.description

    def get_content(self):
        return self.content.value

    def get_implicitrules(self):
        return self.implicitrules

    def get_language(self):
        return self.language

    def get_text(self):
        return self.text

    def get_contained(self):
        return self.contained

    def get_extension(self):
        return self.extension

    def get_modifierextension(self):
        return self.modifierextension

    def get_identifier(self):
        return self.identifier

    def get_experimental(self):
        return self.experimental

    def get_date(self):
        return self.date

    def get_publisher(self):
        return self.publisher

    def get_contact(self):
        return self.contact

    def get_usecontext(self):
        return self.usecontext

    def get_jurisdiction(self):
        return self.jurisdiction

    def get_purpose(self):
        return self.purpose

    def get_copyright(self):
        return self.copyright

    def get_immutable(self):
        return self.immutable

    def get_lockeddate(self):
        return self.lockeddate

    def get_inactive(self):
        return self.inactive

    def get_casesensitive(self):
        return self.casesensitive

    def get_valueset(self):
        return self.valueset

    def get_hierarchymeaning(self):
        return self.hierarchymeaning

    def get_compositional(self):
        return self.compositional

    def get_versionneeded(self):
        return self.versionneeded

    def get_supplements(self):
        return self.supplements

    def get_count(self):
        return len(self.get_concept())

    def get_filter(self):
        return self.filter

    def get_property(self):
        tmp = []
        if hasattr(self,"property"):
            tmp = self.property
        if self.get_resource() == "CodeSystem":
            tmp = self.appendAdditionalConceptProperties(tmp)
        return tmp

    def get_concept(self):
        return self.concept

    def set_statusToRetired(self, theCSConcept):
        theProp = CSConcept.ConceptProperty()
        theProp.code = "status"
        theProp.value = "retired"
        theProp.type = PropertyCodeType.code
        theCSConcept.property.append(theProp)

    def appendAdditionalConceptProperties(self, retArr):
        # look into the concepts and add missing properties
        for oneConcept in self.get_concept():
            if hasattr(oneConcept,"property"):
                for oneCProperty in oneConcept.property:
                    foundFullMatch = False
                    #foundTypeMismatch = False # if needed in the future
                    for oneProperty in retArr:
                        if oneCProperty.code == oneProperty.code and oneCProperty.type == oneProperty.type:
                            foundFullMatch = True
                        #elif oneCProperty.code == oneProperty.code and oneCProperty.type != oneProperty.type:
                        #    foundTypeMismatch = True
                    if not foundFullMatch:# and not foundTypeMismatch:
                        retArr.append(Property(code=oneCProperty.code,type=oneCProperty.type))
                    #elif not foundFullMatch and foundTypeMismatch:
                    #    retArr.append(Property(code=oneCProperty.code,type=oneCProperty.type))
        return retArr

    def appendMetaDataTo(self, csvFilename):
        # if file is new, add headers
        try:
            f = open(csvFilename)
            f.close()
        except IOError:
            TERMINOLOGY_METADATA_CSV_COLUMNS = ['name', 'canonical', 'oid', 'version']
            with open(csvFilename, 'a', encoding="utf8") as csvfile:
                csvfile.write(','.join(TERMINOLOGY_METADATA_CSV_COLUMNS)+'\n')

        # write the one processed terminology
        with open(csvFilename, 'a', encoding="utf8") as csvfile:
            csvfile.write(self.get_resource()+"-"+self.get_name()+","+self.globalUrl + self.get_resource()+"-"+self.get_name()+"," + (tmp[0] if (tmp := self.get_identifier()) else "") + ","+self.get_version()+"\n")

        # remove duplicates, remaining the newer/below entry
        csvlist = []
        with open(csvFilename, "r", encoding="utf8") as csvfile:
            for line in csvfile:
                for listline in csvlist:
                    if line.split(',')[0] == listline.split(',')[0]:
                        csvlist.remove(listline)
                csvlist.append(line)

        with open(csvFilename, 'w', newline='', encoding='utf-8') as outfile:
            for line in csvlist:
                outfile.write(line)

    def resolveTerminologyMapping(self, search_column, search_value, target_column):
        # check if the needed argument is given
        if not hasattr(self, "processedTerminologies"):
            import sys
            sys.exit('A outdated csv needs a terminologies list for gaining OIDs, given with "-appndProcTermTo".\n')

        # import the csv when its the first time used
        if type(self.processedTerminologies) is not list:
            import csv
            with open(self.processedTerminologies, 'r', newline='') as file:
                csvFile = csv.DictReader(file, delimiter=',')
                self.processedTerminologies = []
                # displaying the contents of the CSV file
                for csv_line in csvFile:
                    self.processedTerminologies.append(csv_line)

        # search for the Name in the list and return oid
        for line_dict in self.processedTerminologies:
            if line_dict[search_column] == search_value:
                if line_dict[target_column]:
                    return line_dict[target_column]
        print('Error: For "%s" as CodeSystem-Name or as canonical the CodeSystem OID was not found in the appndProcTermTo list. Some formats, like the outdated csv, needs a appndProcTermTo list for gaining OIDs of the used CodeSystems, given with "-appndProcTermTo". In this case, the given value will be used instead.\n' % search_value)
        return search_value

    def gainOidFromName(self, name):
        return self.resolveTerminologyMapping('name', name, 'oid')

    def gainOidFromCanonical(self, canonical):
        return self.resolveTerminologyMapping('canonical', canonical, 'oid')

    def gainCanonicalFromOid(self, oid):
        return self.resolveTerminologyMapping('oid', oid, 'canonical')

    def buildConceptDictWithAttr(self, stringAttrAsKey):
        tmpDict = {}
        for oneCon in self.get_concept():
            tmpPointer = oneCon
            for part in stringAttrAsKey.split("."):
                tmpPointer = getattr(tmpPointer,part)
            tmpDict[tmpPointer] = oneCon
        return tmpDict

    def sortConceptsExpandStyle(self):
        sortedConcepts = []

        # build up a dict with code as key
        conDict = self.buildConceptDictWithAttr("code")

        # sort all the child properties inside the concepts
        for key in conDict:
            if hasattr(conDict[key],"property") and conDict[key].property:
                conDict[key].property.sort(key=CSConcept.ConceptProperty.get_value_if_code_is_child)

        # find all the concepts with no parent, sorted after key
        allLvl0 = []
        for key in sorted(conDict):
            thereIsAParent = False
            for oneProp in conDict[key].property:
                if oneProp.code == "parent":
                    thereIsAParent = True
            if thereIsAParent == False:
                allLvl0.append(key)

        # call the recr for all elements with no parent
        for lvl0 in allLvl0:
            self.storeSelfAndRecrCallChildren(conDict[lvl0], conDict, sortedConcepts)

        # overwrite the concept list with the just sorted one
        self.concept = sortedConcepts

    def storeSelfAndRecrCallChildren(self, oneCon, conDict, sortedCons):
        sortedCons.append(oneCon)
        for oneProp in oneCon.property:
            if oneProp.code == "child":
                if popdCon := conDict.pop(oneProp.value, None): # This will return conDict[key] if key exists in the dictionary, and None otherwise.
                    self.storeSelfAndRecrCallChildren(popdCon, conDict, sortedCons)


    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        # special encoding because of Excel compatibility, see https://stackoverflow.com/questions/6588068/which-encoding-opens-csv-files-correctly-with-excel-on-both-mac-and-windows
        with open(outfile.name, 'wb') as outfile:

            csv_list = []
            # start list of metaelements
            csv_list.append(("resource",self.get_resource()))
            csv_list.append(("url",self.get_url()))
            csv_list.append(("version",self.get_version()))
            csv_list.append(("name",self.get_name()))
            csv_list.append(("title",self.get_title()))
            csv_list.append(("status",self.get_status()))
            csv_list.append(("description",self.get_description()))

            if self.get_resource() == "CodeSystem": csv_list.append(("content",self.get_content()))

            if tmp := self.get_implicitrules(): csv_list.append(("implicitRules",tmp))
            if tmp := self.get_language(): csv_list.append(("language",tmp))
            if tmp := self.get_text(): csv_list.append(("text",tmp))
            if tmp := self.get_contained(): csv_list.append(("contained",tmp))
            if tmp := self.get_extension(): csv_list.append(("extension",tmp))
            if tmp := self.get_modifierextension(): csv_list.append(("modifierExtension",tmp))
            if tmp := self.get_identifier():
                for oneIdentifier in tmp:
                    csv_list.append(("identifier",oneIdentifier))
            if tmp := self.get_experimental(): csv_list.append(("experimental",tmp))
            if tmp := self.get_date(): csv_list.append(("date",tmp))
            if tmp := self.get_publisher(): csv_list.append(("publisher",tmp))
            if tmp := self.get_contact():
                for oneContact in tmp:
                    csv_list.append(("contact", str(oneContact)))
            if tmp := self.get_usecontext():
                for oneUseContext in tmp:
                    csv_list.append(("useContext",oneUseContext))
            if tmp := self.get_jurisdiction():
                for oneJurisdiction in tmp:
                    csv_list.append(("jurisdiction",oneJurisdiction))
            if tmp := self.get_purpose(): csv_list.append(("purpose",tmp))
            if tmp := self.get_copyright(): csv_list.append(("copyright",tmp))
            if tmp := self.get_immutable(): csv_list.append(("immutable",tmp))
            if tmp := self.get_lockeddate(): csv_list.append(("lockedDate",tmp))
            if tmp := self.get_inactive(): csv_list.append(("inactive",tmp))
            if tmp := self.get_casesensitive(): csv_list.append(("caseSensitive",tmp))
            if tmp := self.get_valueset(): csv_list.append(("valueSet",tmp))
            if tmp := self.get_hierarchymeaning(): csv_list.append(("hierarchyMeaning",tmp))
            if tmp := self.get_compositional(): csv_list.append(("compositional",tmp))
            if tmp := self.get_versionneeded(): csv_list.append(("versionNeeded",tmp))
            if tmp := self.get_supplements(): csv_list.append(("supplements",tmp))
            if tmp := self.get_count(): csv_list.append(("count",tmp))
            if tmp := self.get_filter():
                for oneFilter in tmp:
                    csv_list.append(("filter",oneFilter.code+"|"+oneFilter.description+"|"+oneFilter.operator+"|"+oneFilter.value))
            if tmp := self.get_property():
                for oneProperty in tmp:
                    csv_list.append(("property",str(oneProperty)))
            # end list of metaelements
            for csvline in zip(*csv_list): #transpose the list
                newline = True
                for csvelement in csvline:
                    # write and change all ',' to ';'
                    #outfile.write(("," if not newline else "") + "\'" + str(csvelement).replace("'","´") + "\'")
                    outfile.write(((";" if not newline else "") + "\"" + str(csvelement).replace("\"","´") + "\"").encode('cp1252',errors='replace'))
                    newline = False
                outfile.write(("\n").encode('cp1252',errors='replace'))

            csv_header = []

            #csv_header_designation_count = 0
            csv_list = []

            conceptList = self.get_concept()
            if len(conceptList) > 0:
                for oneConcept in conceptList:

                    csv_line = []

                    #for CodeSystems
                    if self.get_resource() == 'CodeSystem':
                        #adding values to already existing columns, if value empty than a empty string is added
                        headerDesignationIterator = 0
                        headerPropertyIterator = 0
                        for csv_header_element in csv_header:

                            if csv_header_element == "designation":
                                if headerDesignationIterator < len(oneConcept.designation):
                                    csv_line.append(oneConcept.designation[headerDesignationIterator])
                                else:
                                    csv_line.append('')
                                headerDesignationIterator += 1

                            elif csv_header_element == "property":
                                if headerPropertyIterator < len(oneConcept.property):
                                    csv_line.append(oneConcept.property[headerPropertyIterator])
                                else:
                                    csv_line.append('')
                                headerPropertyIterator += 1
                            elif hasattr(oneConcept, csv_header_element) and (tmp := getattr(oneConcept,csv_header_element)):
                                csv_line.append(tmp)#getattr(oneConcept,csv_header_element))
                            else:
                                csv_line.append('')

                        #adding not existing columns because we just got some values
                        if 'code' not in csv_header and (tmp := oneConcept.code):#hasattr(oneConcept,'code'):
                            csv_header.append('code')
                            csv_line.append(tmp)
                        if 'display' not in csv_header and (tmp := oneConcept.display):#hasattr(oneConcept,'display'):
                            csv_header.append('display')
                            csv_line.append(tmp)
                        if 'definition' not in csv_header and (tmp := oneConcept.definition):#hasattr(oneConcept,'definition'):
                            csv_header.append('definition')
                            csv_line.append(tmp)
                        while (conceptDesig := oneConcept.designation) and headerDesignationIterator < len(conceptDesig):
                            csv_header.append('designation')
                            csv_line.append(conceptDesig[headerDesignationIterator])
                            headerDesignationIterator += 1
                        while (conceptProps := oneConcept.property) and headerPropertyIterator < len(conceptProps):
                            csv_header.append('property')
                            csv_line.append(conceptProps[headerPropertyIterator])
                            headerPropertyIterator += 1

                    #for ValueSets
                    elif self.get_resource() == 'ValueSet':
                        #adding values to already existing columns, if value empty than a empty string is added
                        headerDesignationIterator = 0
                        headerFilterIterator = 0
                        for csv_header_element in csv_header:

                            if csv_header_element == "designation":
                                if headerDesignationIterator < len(oneConcept.designation):
                                    csv_line.append(oneConcept.designation[headerDesignationIterator])
                                else:
                                    csv_line.append('')
                                headerDesignationIterator += 1

                            elif csv_header_element == "filter":
                                if headerFilterIterator < len(oneConcept.filter):
                                    csv_line.append(oneConcept.filter[headerFilterIterator])
                                else:
                                    csv_line.append('')
                                headerFilterIterator += 1

                            elif hasattr(oneConcept, csv_header_element) and (tmp := getattr(oneConcept,csv_header_element)):
                                csv_line.append(tmp)#getattr(oneConcept,csv_header_element))
                            else:
                                csv_line.append('')

                        #adding not existing columns because we just got some values
                        if 'system' not in csv_header and (tmp := oneConcept.system):# hasattr(oneConcept,'system'):
                            csv_header.append('system')
                            csv_line.append(tmp)
                        if 'version' not in csv_header and (tmp := oneConcept.version):#hasattr(oneConcept,'version'):
                            csv_header.append('version')
                            csv_line.append(tmp)
                        if 'code' not in csv_header and (tmp := oneConcept.code):#hasattr(oneConcept,'code'):
                            csv_header.append('code')
                            csv_line.append(tmp)
                        if 'display' not in csv_header and (tmp := oneConcept.display):#hasattr(oneConcept,'display'):
                            csv_header.append('display')
                            csv_line.append(tmp)
                        while (conceptDesig := oneConcept.designation) and headerDesignationIterator < len(conceptDesig):
                            csv_header.append('designation')
                            csv_line.append(conceptDesig[headerDesignationIterator])
                            headerDesignationIterator += 1
                        while (conceptFilter := oneConcept.filter) and headerFilterIterator < len(conceptFilter):
                            csv_header.append('filter')
                            csv_line.append(conceptFilter[headerFilterIterator])
                            headerFilterIterator += 1
                        if 'abstract' not in csv_header and (tmp := oneConcept.abstract):
                            csv_header.append('abstract')
                            csv_line.append(tmp)
                        if 'exclude' not in csv_header and (tmp := oneConcept.exclude):
                            csv_header.append('exclude')
                            csv_line.append(tmp)

                    csv_list.append(csv_line)

            csv_list.insert(0,csv_header)

            for csvline in csv_list:
                outfile.write(("\n").encode('cp1252',errors='replace'))
                newline = True
                for csvelement in csvline:
                    #outfile.write(("," if not newline else "") + "\'" + str(csvelement).replace("'","´") + "\'")
                    outfile.write(((";" if not newline else "") + "\"" + str(csvelement).replace("\"","´") + "\"").encode('cp1252',errors='replace'))
                    newline = False

class Resource(enum.Enum):
    ValueSet = 'ValueSet'
    CodeSystem = 'CodeSystem'

class Status(enum.Enum):
    draft = 'draft'
    active = 'active'
    retired = 'retired'
    unknown = 'unknown'

class Content(enum.Enum):
    notpresent = 'not-present'
    example = 'example'
    fragment = 'fragment'
    complete = 'complete'
    supplement = 'supplement'

class HierarchyMeaning(enum.Enum):
    groupedby = "grouped-by"
    isa = "is-a"
    partof = "part-of"
    classifiedwith = "classified-with"

class PropertyCodeType(enum.Enum):
    code = "code"
    coding = "Coding"
    string = "string"
    integer = "integer"
    boolean = "boolean"
    datetime = "dateTime"
    decimal = "decimal"

class ContactDetail():
    def __init__(self):
        self.name = None
        self.telecom = []

    def __str__(self) -> str:
        tempStr = ""
        if temp := self.name:
            tempStr += temp
        tempStr += "|"
        if (temp := self.telecom) and (temp := self.telecom[0]) and (temp := self.telecom[0].system):
            tempStr += temp
        tempStr += "|"
        if (temp := self.telecom) and (temp := self.telecom[0]) and (temp := self.telecom[0].value):
            tempStr += temp
        return tempStr

    class ContactPoint():
        def __init__(self):
            self.system = None # ContactPointSystem
            self.value = None
            self.use = None # ContactPointUse
            self.rank = None
            self.period_start = None
            self.period_end = None

        class ContactPointSystem(enum.Enum):
            phone = "phone"
            fax = "fax"
            email = "email"
            pager = "pager"
            url = "url"
            sms = "sms"
            other = "other"

        class ContactPointUse(enum.Enum):
            home = "home"
            work = "work"
            temp = "temp"
            old = "old"
            mobile = "mobile"

class Filter():
    def __init__(self):
        self.code = None
        self.description = None
        self.operator = None
        self.value = None

class Property():
    def __init__(self, code=None, uri=None, description=None, type=PropertyCodeType, idInFsh=None):
        self.code = code
        self.uri = uri
        self.description = description
        self.type = type
        self.idInFsh = idInFsh

    def __str__(self) -> str:
        return self.code+"|"+(self.uri or "")+"|"+(self.description or "")+"|"+self.type.value

class CSConcept():
    def __init__(self):
        self.code = None
        self.display = None
        self.definition = None
        self.designation = []
        self.property = []

    class ConceptProperty():
        def __init__(self):
            self.code = None
            self.value = None
            self.type = PropertyCodeType

        # only used for sort
        def get_value_if_code_is_child(self):
            if self.code == "child":
                return str(self.value)
            else:
                return str(0)

        # only used for sort
        def get_code(self):
            return self.code

        def __str__(self) -> str:
            buildStr = ""
            buildStr = self.code
            buildStr += "|"+ str(self.value)
            buildStr += "|"+ self.type.value
            return buildStr

class VSConcept():
    def __init__(self) -> None:
        self.system = None
        self.version = None
        self.code = None
        self.display = None
        self.designation = [] # ConceptDesignation
        self.filter = [] # VSConceptFilter
        self.exclude = False
        self.member = [] # simple hirarchie that stores all children, needs a extension
        self.level = -1 # additional information in what level the concept can be found, just for easier writing concepts
        self.abstract = False

    # created only for sorting, shouldn't be used for anything else
    def get_system(self):
        return self.system

    # created only for sorting, shouldn't be used for anything else
    def get_code(self):
        return self.code

    class VSConceptFilter():
        def __init__(self):
            self.property = None
            self.op = None
            self.value = None

        def __str__(self) -> str:
            buildStr = ""
            if hasattr(self, 'property'): buildStr = self.property
            if hasattr(self, 'op'):
                if buildStr != "":
                    buildStr += "|"
                buildStr += self.op
            if hasattr(self, 'value'):
                if buildStr != "":
                    buildStr += "|"
                buildStr += self.value
            return buildStr

class ConceptDesignation():
    def __init__(self, str=None):
        if str is None:
            self.language = None
            self.use = Coding()
            self.value = None
        else:
            splittedValue = str.split('|',2)
            self.language = splittedValue[0]
            self.use = Coding(splittedValue[1])
            self.value = splittedValue[2]

    def __str__(self) -> str:
        buildStr = ""
        if self.language: buildStr += self.language
        buildStr += "|"
        if self.use: buildStr += str(self.use)
        buildStr += "|"
        if self.value: buildStr += self.value
        return buildStr

class Coding():
    def __init__(self, str=None):
        if str is None:
            self.codesystem = None
            self.version = None
            self.code = None
            self.display = None
        else:
            splittedValue = str.split('#',3)
            self.codesystem = splittedValue[0]
            self.version = splittedValue[1]
            self.code = splittedValue[2]
            self.display = splittedValue[3]

    def __str__(self) -> str:
        buildStr = ""
        if self.codesystem: buildStr += self.codesystem
        buildStr += "#"
        if self.version: buildStr += self.version
        buildStr += "#"
        if self.code: buildStr += self.code
        buildStr += "#"
        if self.display: buildStr += self.display
        return buildStr

# upper case first character: https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
first_char_to_upper = lambda s: s[:1].upper() + s[1:] if s else ''
# lower case first character: https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
first_char_to_lower = lambda s: s[:1].lower() + s[1:] if s else ''
