from datetime import datetime
import prop_csv_and_master as pcam
import re
import copy

tempindex = None

class Fsh1(pcam.PropCsvAndMaster):

    def __init__(self, inFile):
        super().__init__()
        # open the file in read mode
        with open(inFile, 'r', encoding="utf8") as file:
            # first mandatory fields, using the instance way of fsh
            self.name = file.readline().split(':')[1].strip().strip('"')
            self.resource = pcam.Resource[file.readline().split(':')[1].strip().strip('"')]
            file.readline()
            
            # preparing lists and some variables 
            lstFilter =  []
            lstProperty = []
            dictConcept = {}

            finalVSSystem = None
            finalVSVersion = None

            for line in file:
                # preprocessing of value
                splittedLine = line.split('=',1)
                if '//' in splittedLine[0].strip() or len(splittedLine[0].strip()) == 0:
                    continue
                if '=' in line:
                    value = splittedLine[1].split("////")[0].strip()
                if value[:1] == '"' or value[:1] == '#':
                    value = value[1:]
                if value[-1:] == '"':
                    value = value[:-1]
                if "\\\"" in value:
                    value = value.replace("\\\"",'"')

                # more mandatory fields
                if splittedLine[0] == '* status ':self.status = pcam.Status[value]
                
                #self.content = file.readline().split('=')[1].strip().strip('#')

                elif splittedLine[0] == '* content ' and self.resource == self.resource.CodeSystem:
                    self.content = pcam.Content[value]

                # optional fields
                elif splittedLine[0] == '* url ': self.url = value
                elif splittedLine[0] == '* version ':self.version = value
                elif splittedLine[0] == '* title ':self.title = value
                elif splittedLine[0] == '* description ':self.description = value
                elif splittedLine[0] == '* implicitRules ': self.implicitrules = value
                elif splittedLine[0] == '* language ': self.language = value
                
                #self.__getattribute__(splittedLine[0]) = value
                
                elif splittedLine[0] == '* text ': self.text = value
                elif splittedLine[0] == '* contained ': self.contained = value
                elif splittedLine[0] == '* extension ': self.extension = value
                elif splittedLine[0] == '* modifierExtension ': self.modifierextension = value
                elif '* identifier' in splittedLine[0] and 'value' in splittedLine[0]: 
                    if not hasattr(self,'identifier'):
                        self.identifier = []
                    self.identifier.append(value)
                elif splittedLine[0] == '* experimental ': self.experimental = value
                elif splittedLine[0] == '* date ': self.date = value
                elif splittedLine[0] == '* publisher ': self.publisher = value
                elif '* contact' in splittedLine[0]: 
                    if not hasattr(self,'contact'):
                        self.contact = []
                    self.contact.append(value)
                elif '* useContext' in splittedLine[0]: 
                    if not hasattr(self,'useContext'):
                        self.usecontext = []
                    self.usecontext.append(value)
                elif '* jurisdiction' in splittedLine[0]: 
                    if not hasattr(self,'jurisdiction'):
                        self.jurisdiction = []
                    self.jurisdiction.append(value)
                elif splittedLine[0] == '* purpose ': self.purpose = value
                elif splittedLine[0] == '* copyright ': self.copyright = value
                elif splittedLine[0] == '* immutable ': self.immutable = value
                elif splittedLine[0] == '* lockedDate ': self.lockeddate = value
                elif splittedLine[0] == '* inactive ': self.inactive = value
                elif splittedLine[0] == '* caseSensitive ': self.casesensitive = value
                elif splittedLine[0] == '* valueSet ': self.valueset = value
                elif splittedLine[0] == '* hierarchyMeaning ': self.hierarchymeaning = value
                elif splittedLine[0] == '* compositional ': self.compositional = value
                elif splittedLine[0] == '* versionNeeded ': self.versionneeded = value
                elif splittedLine[0] == '* supplements ': self.supplements = value
                elif splittedLine[0] == '* count ': self.count = value

                elif '* filter' in splittedLine[0]:
                    theFilter = None
                    # look with idInFsh for Filter in the Filter list
                    for oneFilter in lstFilter:
                        if oneFilter.idInFsh == splittedLine[0].split(']')[0]:
                            theFilter = oneFilter
                    # if none is found in the list, make one
                    if theFilter is None:
                        theFilter = Filter(splittedLine[0].split(']')[0])
                        lstFilter.append(theFilter)
                    # add the data to the Filter
                    if splittedLine[0].split('.')[1].strip() == 'code':
                        theFilter.code = value
                    elif splittedLine[0].split('.')[1].strip() == 'description':
                        theFilter.description = value
                    elif splittedLine[0].split('.')[1].strip() == 'operator':
                        theFilter.operator = value
                    elif splittedLine[0].split('.')[1].strip() == 'value':
                        theFilter.value = value

                elif '* property' in splittedLine[0]:
                    theProperty = None
                    # look with idInFsh for Property in the Property list
                    for oneProperty in lstProperty:
                        if oneProperty.idInFsh == splittedLine[0].split('.')[0]:
                            theProperty = oneProperty
                    # if none is found in the list, make one
                    if theProperty is None:
                        theProperty = pcam.Property()
                        theProperty.idInFsh = splittedLine[0].split('.')[0]
                        lstProperty.append(theProperty)
                    # add the data to the Property
                    if splittedLine[0].split('.')[1].strip() == 'code':
                        theProperty.code = value
                    elif splittedLine[0].split('.')[1].strip() == 'description':
                        theProperty.description = value
                    elif splittedLine[0].split('.')[1].strip() == 'uri':
                        theProperty.uri = value
                    elif splittedLine[0].split('.')[1].strip() == 'type':
                        theProperty.type = pcam.PropertyCodeType[value]

                #processing the body with the concepts
                else: 
                    self.parseConcepts(dictConcept, line, splittedLine, value)

            if lstFilter != []:
                self.filter = lstFilter
            if lstProperty != []:
                self.property = lstProperty
            if dictConcept != {}:
                self.concept = list(dictConcept.values())

    def parseConcepts(self, dictConcept, line, splittedLine, value):
        if '* concept' in splittedLine[0]:
            theConcept = None
            #split here for CS and VS
            if self.resource == self.resource.CodeSystem:
                theConcept = pcam.CSConcept() #alternative construktor to create an new object without calling __init__, for minimal memory allocation
                
                # parsing index if the = and + notation is used
                index = line.split(']')[0].split('[')[1]#.strip("'")
                global tempindex
                if index == "=":
                    index = tempindex
                elif index == "+": 
                    tempindex = int(tempindex)+1
                    index = tempindex
                else:
                    tempindex = index
                if not re.match('\* concept\[(\d+|\+|=)+\]\.code .*', line):
                    if oneConcept := dictConcept[index]:
                        if 'display' in line:
                            oneConcept.display = value
                        elif 'definition' in line:
                            oneConcept.definition = value #line.split('"')[1]
                        elif 'designation' in line:
                            theDesignation = None
                                        # look with idInFsh for designation in the designation list
                            for oneDesignation in oneConcept.designation:
                                if oneDesignation.idInFsh == line.split('.')[1]:
                                    theDesignation = oneDesignation
                                        # if none is found in the list, make one
                            if theDesignation is None:
                                theDesignation.idInFsh = line.split('.')[1]
                                oneConcept.designation.append(theDesignation)
                                        # split the line properly
                            if line.split('#') > 2:
                                value = line.strip().split[' '][-1:][0].strip('#')
                            else:
                                value = line.strip().split['"'][1]
                                        # add the data to the designation
                            if 'language' in splittedLine[0].split('.')[1].strip():
                                theDesignation.language = value
                            elif 'use' in splittedLine[0].split('.')[1].strip():
                                theDesignation.use = value
                            elif 'value' in splittedLine[0].split('.')[1].strip():
                                theDesignation.value = value
                        elif 'property' in line:
                                        #line.split('^')[1]
                            theProperty = None
                                        # look with idInFsh for Property in the Property list
                            for oneProperty in oneConcept.property:
                                if oneProperty.idInFsh == line.split('.')[1]:
                                    theProperty = oneProperty
                                        # if none is found in the list, make one
                            if theProperty is None:
                                theProperty = pcam.CSConcept.ConceptProperty()
                                theProperty.idInFsh = line.split('.')[1]
                                oneConcept.property.append(theProperty)
                                        # split the line properly
                            #if len(line.split('#')) > 2:
                            #    value = line.strip().split(' ')[-1:][0].strip('#')
                            #else:
                            #    value = line.strip().split('"')[1]
                                        # add the data to the Property
                            if 'code' in splittedLine[0].split('.')[-1].strip():
                                theProperty.code = value
                            elif 'value' in splittedLine[0].split('.')[-1].strip():
                                theProperty.value = value
                                theProperty.type = pcam.PropertyCodeType(splittedLine[0].split('.')[-1].strip().replace("value",""))
                else:
                    # parsing main data of the concept 
                    theConcept.code = value
                    theConcept.designation = []
                    theConcept.property = []
                    dictConcept[tempindex] = theConcept
                    
            elif self.resource == self.resource.ValueSet:
                theConcept = pcam.VSConcept.__new__(pcam.VSConcept) #alternative construktor to create an new object without calling __init__, for minimal memory allocation
                if 'compose.include.system' in line:
                    finalVSSystem = line.split('"')[1].strip()
                if 'compose.include.version' in line:
                    finalVSVersion = line.split('"')[1].strip()
                if '.code' in line:
                    theConcept.idInFsh = line.split('.code')[0]
                    theConcept.code = line.split('#')[1].strip()
                    theConcept.system = finalVSSystem
                    theConcept.version = finalVSVersion
                    theConcept.designation = []
                    theConcept.filter = []
                    dictConcept[theConcept.code] = theConcept
                if '.display' in line:
                    for oneConcept in dictConcept:
                        if oneConcept.idInFsh == line.split('.display')[0]:
                            theConcept = oneConcept
                            theConcept.display = line.split('"')[1].strip()
                if '.designation' in line:
                    theDesignation = None
                    for oneConcept in dictConcept:
                        if oneConcept.idInFsh == line.split('.designation')[0]:
                                        # look with idInFsh for designation in the designation list of the concept
                            for oneDesignation in oneConcept.designation: # e.g. ->* compose.include.concept[5].designation[4].language
                                if oneDesignation.idInFsh == line.split(']')[0]+line.split(']')[1]:
                                    theDesignation = oneDesignation
                                        # if none is found in the list, make one
                            if theDesignation is None:
                                theDesignation.idInFsh = line.split(']')[0]+line.split(']')[1]
                                oneConcept.designation.append(theDesignation)
                                        # add the data to the designation
                            if '.language' in line:
                                theDesignation.language = value
                            elif '.use' in line:
                                theDesignation.use = value
                            elif '.value' in line:
                                theDesignation.value = value
                if '.filter' in line:
                    theFilter = None
                                # look with idInFsh for filter in the filter list of the concept
                    for oneConcept in dictConcept:
                        if oneConcept.idInFsh == line.split(']')[0]:
                            theFilter = oneConcept
                                # if none is found in the list, make one
                    if theFilter is None:
                        theFilter.idInFsh = line.split(']')[0]
                        oneConcept.filter = theFilter
                                # add the data to the designation
                    if '.property' in line:
                        theFilter.property = value
                    elif '.op' in line:
                        theFilter.op = value
                    elif '.value' in line:
                        theFilter.value = value

    def parse(inFilename):
        return Fsh1(inFilename)

    def exporto(self, outfile, outputClass, argsLang=None):
        # mandatory fields
        outfile.write('Instance: %s \n' % self.get_name())
        outfile.write('InstanceOf: %s \n' % self.get_resource())
        outfile.write('Usage: #definition \n')
        outfile.write('* url = "%s" \n' % self.get_url())
        outfile.write('* name = "%s" \n' % self.get_name())
        outfile.write('* title = "%s" \n' % self.get_title())
        outfile.write('* status = #%s \n' % self.get_status())
        
        if self.get_resource() == "CodeSystem": 
            outfile.write('* content = #%s \n' % self.get_content())
        
        # optional fields
        if tmp := self.get_version(): outfile.write('* version = "%s" \n' % tmp)
        if tmp := self.get_description(): outfile.write('* description = "%s" \n' % tmp)
        if tmp := self.get_implicitrules(): outfile.write('* implicitRules = "%s" \n' % tmp)
        if tmp := self.get_language(): outfile.write('* language = #%s \n' % tmp)
        elif argsLang is not None: outfile.write('* language = #%s \n' % argsLang)
        if tmp := self.get_text(): outfile.write('* text = "%s" \n' % tmp)
        if tmp := self.get_contained(): outfile.write('* contained = "%s" \n' % tmp)
        if tmp := self.get_extension(): outfile.write('* extension = "%s" \n' % tmp)
        if tmp := self.get_modifierextension(): outfile.write('* modifierExtension = "%s" \n' % tmp)
        if tmp := self.get_identifier(): 
            i = 0
            for oneIdentifier in self.get_identifier():
                outfile.write('* identifier[%s].use = #official \n' % (i))
                outfile.write('* identifier[%s].system = "urn:ietf:rfc:3986" \n' % (i))
                outfile.write('* identifier[%s].value = "urn:oid:%s" \n' % (i,oneIdentifier))
                i += 1
        if tmp := self.get_experimental(): outfile.write('* experimental = "%s" \n' % tmp)
        if tmp := self.get_date(): outfile.write('* date = "%s" \n' % tmp)
        if tmp := self.get_publisher(): outfile.write('* publisher = "%s" \n' % tmp)
        # todo make the contact write also possible for claml2&3
        if tmp := self.get_contact():
            i = 0 
            for oneContact in tmp:
                if tmpName := oneContact.name:
                    outfile.write('* contact[%s].name = "%s" \n' % (i,tmpName))
                if tmpSystem := oneContact.telecom[0].system:
                    outfile.write('* contact[%s].telecom[0].system = #%s \n' % (i,tmpSystem))
                if tmpValue := oneContact.telecom[0].value:
                    outfile.write('* contact[%s].telecom[0].value = "%s" \n' % (i,tmpValue))
                i += 1
        if tmp := self.get_usecontext(): 
            i = 0
            for oneUseContext in tmp:
                outfile.write('* useContext[%s] = "%s" \n' % (i,oneUseContext))
                i += 1
        if tmp := self.get_jurisdiction():
            i = 0
            for oneJurisdiction in tmp:
                outfile.write('* jurisdiction[%s] = "%s" \n' % (i,oneJurisdiction))
                i += 1
        if tmp := self.get_purpose(): outfile.write('* purpose = "%s" \n' % tmp)
        if tmp := self.get_copyright(): outfile.write('* copyright = "%s" \n' % tmp)
        
        if tmp := self.get_immutable(): outfile.write('* immutable = "%s" \n' % tmp)
        if tmp := self.get_lockeddate(): outfile.write('* lockedDate = "%s" \n' % tmp)
        if tmp := self.get_inactive(): outfile.write('* inactive = "%s" \n' % tmp)
        
        if tmp := self.get_casesensitive(): outfile.write('* caseSensitive = "%s" \n' % tmp)
        # TODO how should we work with references like valueset
        #if tmp := self.get_valueset(): outfile.write('* valueSet = "%s" \n' % tmp)
        if tmp := self.get_hierarchymeaning(): outfile.write('* hierarchyMeaning = "%s" \n' % tmp)
        if tmp := self.get_compositional(): outfile.write('* compositional = "%s" \n' % tmp)
        if tmp := self.get_versionneeded(): outfile.write('* versionNeeded = "%s" \n' % tmp)
        if tmp := self.get_supplements(): outfile.write('* supplements = "%s" \n' % (tmp))
        if self.get_resource() == "CodeSystem":
            if tmp := self.get_count(): outfile.write('* count = %s \n' % tmp)
        if tmp := self.get_filter(): 
            i = 0
            for oneFilter in tmp:
                if hasattr(oneFilter, 'code') and oneFilter.code: outfile.write('* filter[%s].code = #%s \n' % (i, oneFilter.code))
                if hasattr(oneFilter, 'description') and oneFilter.description: outfile.write('* filter[%s].description = "%s" \n' % (i, oneFilter.description))
                if hasattr(oneFilter, 'operator') and oneFilter.operator: outfile.write('* filter[%s].operator = #%s \n' % (i, oneFilter.operator))
                if hasattr(oneFilter, 'value') and oneFilter.value: outfile.write('* filter[%s].value = #%s \n' % (i, oneFilter.value))
                i += 1
        if tmp := self.get_property(): 
            i = 0
            for oneProperty in tmp:
                if hasattr(oneProperty, 'code'): outfile.write('* property[%s].code = #%s \n' % (i, oneProperty.code or "None") )
                if hasattr(oneProperty, 'uri') and oneProperty.uri: outfile.write('* property[%s].uri = "%s" \n' % (i, oneProperty.uri))
                if hasattr(oneProperty, 'description') and oneProperty.description: outfile.write('* property[%s].description = "%s" \n' % (i, oneProperty.description))
                if hasattr(oneProperty, 'type') and oneProperty.type: outfile.write('* property[%s].type = #%s \n' % (i, oneProperty.type.name))
                i += 1
        
        
        outputClass.exportoConcepto(self, outfile)           
        # ToDo: implement exclude similar to include
        # ToDo: implement simple Hierarchie for Children with the member extension      

    def exportoConcepto(self, outfile):
        conceptList = self.get_concept()
        if len(conceptList) > 0:
            tempConcept = None
            cntCSConcept = -1
            cntIncAndExclude = -1
            cntVSConcept = -1

            # look into the concepts and see if there are any members, so that these will be specially printed
            vsMemberAnywhere = False
            for oneConcept in conceptList:    
                if hasattr(oneConcept,"member") and oneConcept.member != []:
                    vsMemberAnywhere = True

            # if there is a conceptSuppl, print them first
            if hasattr(self,"conceptSuppl"):
                tempList = self.conceptSuppl
            else:
                tempList = conceptList

            for oneConcept in tempList:               
                cntCSConcept += 1
                # for CodeSystems
                if self.get_resource() == 'CodeSystem':
                    if hasattr(oneConcept, 'code') and oneConcept.code:
                        outfile.write('* concept[%s].code = #%s\n' % (cntCSConcept,oneConcept.code))
                    if hasattr(oneConcept, 'display') and oneConcept.display: 
                        outfile.write('* concept[%s].display = "%s"\n' % (cntCSConcept, oneConcept.display.replace('"','\\"')))
                    if hasattr(oneConcept, 'definition') and oneConcept.definition:
                        outfile.write('* concept[%s].definition = "%s"\n' % (cntCSConcept, oneConcept.definition.replace('"','\\"')))
                    if hasattr(oneConcept, 'designation') and oneConcept.designation != []: 
                        i = 0
                        for oneDesignation in oneConcept.designation:
                            if hasattr(oneDesignation, 'language'): outfile.write('* concept[%s].designation[%s].language = #%s \n' % (cntCSConcept, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use'): outfile.write('* concept[%s].designation[%s].use = #%s \n' % (cntCSConcept, i, oneDesignation.use))
                            if hasattr(oneDesignation, 'value'): outfile.write('* concept[%s].designation[%s].value = "%s" \n' % (cntCSConcept, i, oneDesignation.value.replace('"','\\"')))
                            i += 1
                    if hasattr(oneConcept, 'property') and oneConcept.property != []: 
                        i = 0
                        for oneProperty in oneConcept.property:
                            if hasattr(oneProperty, 'code'): outfile.write('* concept[%s].property[%s].code = #%s \n' % (cntCSConcept, i, oneProperty.code or "None"))
                            if hasattr(oneProperty, 'value') and oneProperty.type.value == "String": outfile.write('* concept[%s].property[%s].value%s = "%s" \n' % (cntCSConcept, i, oneProperty.type.value, oneProperty.value.replace('"','\\"')))
                            elif hasattr(oneProperty, 'value') and oneProperty.type.value == "Code": outfile.write('* concept[%s].property[%s].value%s = #%s \n' % (cntCSConcept, i, oneProperty.type.value, oneProperty.value.replace('"','\\"')))
                            i += 1
                # for ValueSets
                elif self.get_resource() == 'ValueSet': # e.g. ->* compose.include.concept[5].designation[4].language
                    if tempConcept == None or tempConcept.system != oneConcept.system or tempConcept.exclude != oneConcept.exclude:
                        cntIncAndExclude += 1
                        cntVSConcept = -1
                        tempConcept = oneConcept
                        if oneConcept.exclude: 
                            incOrExclude = "exclude" 
                        else: 
                            incOrExclude = "include"

                        outfile.write('* compose.%s[%s].system = "%s"\n' % (incOrExclude, cntIncAndExclude, oneConcept.system))
                        if hasattr(oneConcept, 'version') and oneConcept.version:
                            outfile.write('* compose.%s[%s].version = "%s"\n' % (incOrExclude, cntIncAndExclude, oneConcept.version))
                    cntVSConcept += 1

                    if hasattr(oneConcept, 'code') and oneConcept.code:
                        outfile.write('* compose.%s[%s].concept[%s].code = #%s\n' % (incOrExclude, cntIncAndExclude, cntVSConcept, oneConcept.code))
                    if hasattr(oneConcept, 'display') and oneConcept.display:
                        outfile.write('* compose.%s[%s].concept[%s].display = "%s"\n' % (incOrExclude, cntIncAndExclude, cntVSConcept, oneConcept.display))
                    if hasattr(oneConcept, 'designation') and oneConcept.designation != []:
                        i = -1
                        for oneDesignation in oneConcept.designation:
                            i += 1
                            if hasattr(oneDesignation, 'language'): outfile.write('* compose.%s[%s].concept[%s].designation[%s].language = #%s \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use'): outfile.write('* compose.%s[%s].concept[%s].designation[%s].use = #%s \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, i, oneDesignation.use))
                            if hasattr(oneDesignation, 'value'): outfile.write('* compose.%s[%s].concept[%s].designation[%s].value = "%s" \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, i, oneDesignation.value))
                    if hasattr(oneConcept, 'filter') and oneConcept.filter != []:
                        if hasattr(oneConcept.filter, 'property'): outfile.write('* compose.%s[%s].filter[%s].property = #%s \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, oneConcept.filter.property))
                        if hasattr(oneConcept.filter, 'op'): outfile.write('* compose.%s[%s].filter[%s].op = #%s \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, oneConcept.filter.op))
                        if hasattr(oneConcept.filter, 'value'): outfile.write('* compose.%s[%s].filter[%s].value = "%s" \n' % (incOrExclude, cntIncAndExclude, cntVSConcept, oneConcept.filter.value))
                    # look if a member definition in the valueset is used (* compose.include.extension.extension.url & valueCode)
                    
                    if vsMemberAnywhere:
                        # write the extension
                        outerExtensionCnt = 0
                        outfile.write('\n')
                        outfile.write('* compose.include.extension[0].url = "http://hl7.org/fhir/StructureDefinition/valueset-expand-rules"\n')
                        outfile.write('* compose.include.extension[0].valueCode = #all-codes\n')
                        outfile.write('\n')
                        for oneConcept in conceptList:
                            if hasattr(oneConcept,"member") and oneConcept.member != []:
                                outerExtensionCnt += 1
                                outfile.write('* compose.include.extension[%s].url = "http://hl7.org/fhir/StructureDefinition/valueset-expand-group"\n' % (outerExtensionCnt))
                                outfile.write('* compose.include.extension[%s].extension[0].url = "code"\n' % (outerExtensionCnt))
                                outfile.write('* compose.include.extension[%s].extension[0].valueCode = #%s\n' % (outerExtensionCnt, oneConcept.code))
                                innerExtensionCnt = 0
                                for oneMember in oneConcept.member:
                                    innerExtensionCnt += 1
                                    outfile.write('* compose.include.extension[%s].extension[%s].url = "member"\n' % (outerExtensionCnt, innerExtensionCnt))
                                    outfile.write('* compose.include.extension[%s].extension[%s].valueCode = #%s\n' % (outerExtensionCnt, innerExtensionCnt, oneMember.code))
                    
                    # write the expansion
                    outfile.write('\n')
                    outfile.write('* expansion.parameter.name = "excludeNotForUI"\n')
                    outfile.write('* expansion.parameter.valueUri = "false"\n')
                    outfile.write('* expansion.timestamp = "%s"\n' % (datetime.now().strftime("%Y-%m-%dT%X.0000Z")))
                    outfile.write('\n')
                    containCnt = [-1]
                    for oneConcept in conceptList:
                        if oneConcept.level == 0:
                            writeSelfAndRecrCallMembers(oneConcept, outfile, containCnt)
                           

                        

    def exportoSuppl(self, outfileVS, outfileCSsuppl, outputClass, argsLang=None):
        # looking into the concepts, split to every codesystems that is used
        csUsedinVSinklConceptsOrClassi = {}
        for oneCon in self.get_concept():
            if tmp := oneCon.system:
                if tmp not in csUsedinVSinklConceptsOrClassi.keys():
                    csUsedinVSinklConceptsOrClassi[tmp] = []                    
                csUsedinVSinklConceptsOrClassi[tmp].append(oneCon)
        
        # for every codesystem, do a instance in the SAME suppl file
        for oneCS in csUsedinVSinklConceptsOrClassi.keys():
            # creating a deepcopy of self
            supplSelf = copy.deepcopy(self)
            # creating a suppl CodeSystem
            supplSelf.name = "zuppl-"+oneCS[:28]+"-4-"+self.get_name()[:27] # fsh instance names can only be 64 chars long
            supplSelf.title = "Zuppl "+oneCS+" 4 "+supplSelf.get_title()
            supplSelf.resource = pcam.Resource.CodeSystem.value
            supplSelf.identifier = []
            supplSelf.content = pcam.Content.supplement.value
            supplSelf.supplements = "CodeSystem-"+oneCS
            supplSelf.concept = csUsedinVSinklConceptsOrClassi[oneCS]
            csUsedinVSinklConceptsOrClassi[oneCS] = supplSelf
            outputClass.exporto(supplSelf, outfileCSsuppl, outputClass, argsLang)

        # state only the suppl-CodeSystem in the first ValueSet-concepts
        self.conceptSuppl = []
        for oneCS in csUsedinVSinklConceptsOrClassi.keys():
            tempCon = pcam.VSConcept()
            tempCon.system = ""
            if tempUrl := self.globalUrl:
                tempCon.system += tempUrl
            tempCon.system += "CodeSystem-"+csUsedinVSinklConceptsOrClassi[oneCS].get_name()
            self.conceptSuppl.append(tempCon)
        # exporting the changed ValueSet
        outputClass.exporto(self, outfileVS, outputClass, argsLang)

def writeSelfAndRecrCallMembers(oneConcept, outfile, containCnt):
    containCnt[oneConcept.level] += 1
    outfile.write('* expansion%s.system = "%s"\n' % (strContainsAsLevels(oneConcept.level,containCnt),oneConcept.system))
    outfile.write('* expansion%s.code = #%s\n' % (strContainsAsLevels(oneConcept.level,containCnt),oneConcept.code))
    outfile.write('* expansion%s.display = "%s"\n' % (strContainsAsLevels(oneConcept.level,containCnt),oneConcept.display))    

    if hasattr(oneConcept,"member") and oneConcept.member != []:
        containCnt+=[-1]
        for oneMember in oneConcept.member:
            writeSelfAndRecrCallMembers(oneMember, outfile, containCnt)
        containCnt.pop(oneConcept.level+1)

def strContainsAsLevels (level, containCnt):
    ret = ""
    for x in range(0,level+1):
        ret += ".contains["+ str(containCnt[x]) +"]"
    return ret

class Filter(pcam.Filter):
    def __init__(self, idInFsh):
        super().__init__()
        self.idInFsh = idInFsh # this is a temporary ID for reading in fsh files

class Property(pcam.Property):
    def __init__(self, idInFsh):
        super().__init__()
        self.idInFsh = idInFsh # this is a temporary ID for reading in fsh files