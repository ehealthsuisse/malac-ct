import sys
import prop_csv_and_master as pcam

class Fsh1(pcam.PropCsvAndMaster):

    def __init__(self, inFile):
        super(pcam.PropCsvAndMaster, self).__init__()
        # open the file in read mode
        with open(inFile, 'r', encoding="utf8") as file:
            self.name = file.readline().split(':')[1].strip().strip('"')
            self.resource = pcam.Resource[file.readline().split(':')[1].strip().strip('"')]
            file.readline()
            self.url = file.readline().split('=')[1].strip().strip('"')
            self.version = file.readline().split('=')[1].strip().strip('"')
            file.readline()
            self.title = file.readline().split('=')[1].strip().strip('"')
            self.status = pcam.Status[file.readline().split('=')[1].strip().strip('#')]
            self.description = file.readline().split('=')[1].strip().strip('"')
            
            if self.resource == self.resource.CodeSystem:
                self.content = pcam.Content[file.readline().split('=')[1].strip().strip('#')]

            lstFilter =  []
            lstProperty = []
            lstConcept = []

            finalVSSystem = None
            finalVSVersion = None

            for line in file:
                splittedLine = line.split('=')
                if '//' in splittedLine[0].strip() or len(splittedLine[0].strip()) == 0:
                    continue
                if '=' in splittedLine:
                    value = splittedLine[1].split('//')[0].strip().strip('"').strip('#')
                if splittedLine[0] == '* implicitRules ': self.implicitrules = value
                if splittedLine[0] == '* language ': self.language = value
                if splittedLine[0] == '* text ': self.text = value
                if splittedLine[0] == '* contained ': self.contained = value
                if splittedLine[0] == '* extension ': self.extension = value
                if splittedLine[0] == '* modifierExtension ': self.modifierextension = value
                if splittedLine[0] == '* identifier ': 
                    if not hasattr(self, 'identifier'):
                        self.identifier = []
                    self.identifier.append(value)
                if splittedLine[0] == '* experimental ': self.experimental = value
                if splittedLine[0] == '* date ': self.date = value
                if splittedLine[0] == '* publisher ': self.publisher = value
                if splittedLine[0] == '* contact ': 
                    if not hasattr(self, 'contact'):
                        self.contact = []
                    self.contact.append(value)
                if splittedLine[0] == '* useContext ': 
                    if not hasattr(self, 'useContext'):
                        self.usecontext = []
                    self.usecontext.append(value)
                if splittedLine[0] == '* jurisdiction ': 
                    if not hasattr(self, 'jurisdiction'):
                        self.jurisdiction = []
                    self.jurisdiction.append(value)
                if splittedLine[0] == '* purpose ': self.purpose = value
                if splittedLine[0] == '* copyright ': self.copyright = value
                if splittedLine[0] == '* immutable ': self.immutable = value
                if splittedLine[0] == '* lockedDate ': self.lockeddate = value
                if splittedLine[0] == '* inactive ': self.inactive = value
                if splittedLine[0] == '* caseSensitive ': self.casesensitive = value
                if splittedLine[0] == '* valueSet ': self.valueset = value
                if splittedLine[0] == '* hierarchyMeaning ': self.hierarchymeaning = value
                if splittedLine[0] == '* compositional ': self.compositional = value
                if splittedLine[0] == '* versionNeeded ': self.versionneeded = value
                if splittedLine[0] == '* supplements ': self.supplements = value
                if splittedLine[0] == '* count ': self.count = value

                if '* filter' in splittedLine[0]:
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

                if '* property' in splittedLine[0]:
                    theProperty = None
                    # look with idInFsh for Property in the Property list
                    for oneProperty in lstProperty:
                        if oneProperty.idInFsh == splittedLine[0].split(']')[0]:
                            theProperty = oneProperty
                    # if none is found in the list, make one
                    if theProperty is None:
                        theProperty.idInFsh = splittedLine[0].split(']')[0]
                        lstProperty.append(theProperty)
                    # add the data to the Property
                    if splittedLine[0].split('.')[1].strip() == 'code':
                        theProperty.code = value
                    elif splittedLine[0].split('.')[1].strip() == 'description':
                        theProperty.description = value
                    elif splittedLine[0].split('.')[1].strip() == 'uri':
                        theProperty.uri = value
                    elif splittedLine[0].split('.')[1].strip() == 'type':
                        theProperty.type = value

                #processing the body with the concepts
                if '* #' in splittedLine[0]:
                    theConcept = None
                    #split here for CS and VS
                    if self.resource == self.resource.CodeSystem:
                        theConcept = pcam.CSConcept.__new__(pcam.CSConcept) #alternative construktor to create an new object without calling __init__, for minimal memory allocation
                        if '^' in line:
                            for oneConcept in lstConcept:
                                if oneConcept.code is line.split(' ')[1].strip('#'):
                                    if 'definition' in line:
                                        oneConcept.definition = line.split['"'][1]
                                    elif 'designation' in line:
                                        theDesignation = None
                                        # look with idInFsh for designation in the designation list
                                        for oneDesignation in oneConcept.designation:
                                            if oneDesignation.idInFsh == line.split(']')[0]:
                                                theDesignation = oneDesignation
                                        # if none is found in the list, make one
                                        if theDesignation is None:
                                            theDesignation.idInFsh = line.split(']')[0]
                                            oneConcept.designation.append(theDesignation)
                                        # split the line properly
                                        if line.split('#') > 2:
                                            value = line.split[' '][-1:][0].strip('#')
                                        else:
                                            value = line.split['"'][1]
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
                                            if oneProperty.idInFsh == line.split(']')[0]:
                                                theProperty = oneProperty
                                        # if none is found in the list, make one
                                        if theProperty is None:
                                            theProperty.idInFsh = line.split(']')[0]
                                            oneConcept.property.append(theProperty)
                                        # split the line properly
                                        if line.split('#') > 2:
                                            value = line.split[' '][-1:][0].strip('#')
                                        else:
                                            value = line.split['"'][1]
                                        # add the data to the Property
                                        if 'code' in splittedLine[0].split('.')[1].strip():
                                            theProperty.code = value
                                        elif 'value' in splittedLine[0].split('.')[1].strip():
                                            theProperty.value = value
                        else:
                            # a detection of two # (without a ^) in a line to give a syserr that nested hierarchy is not supported 
                            if len(line.split('#')) > 2:
                                sys.exit('nested hierarchy per "* #this #that" is not supported, only the use of a multiparent hierarchy per propertys is supported.')
                            # go on with parsing main data of the concept 
                            theConcept.code = line.split(' ')[1].strip('#')
                            if '"' in line:
                                theConcept.display = line.split('"')[1]
                            theConcept.designation = []
                            theConcept.property = []
                            lstConcept.append(theConcept)
                       
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
                            lstConcept.append(theConcept)
                        if '.display' in line:
                            for oneConcept in lstConcept:
                                if oneConcept.idInFsh == line.split('.display')[0]:
                                    theConcept = oneConcept
                                    theConcept.display = line.split('"')[1].strip()
                        if '.designation' in line:
                            theDesignation = None
                            for oneConcept in lstConcept:
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
                            for oneConcept in lstConcept:
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

            if lstFilter != []:
                self.filter = lstFilter
            if lstProperty != []:
                self.property = lstProperty
            if lstConcept != []:
                self.concept = lstConcept

    def exporto(self, outfile, argsLang=None):
        outfile.write('Instance: %s \n' % self.get_name())
        outfile.write('InstanceOf: %s \n' % self.get_resource())
        outfile.write('Usage: #definition \n')
        outfile.write('* url = "%s" \n' % self.get_url())
        outfile.write('* version = "%s" \n' % self.get_version())
        outfile.write('* name = "%s" \n' % self.get_name())
        outfile.write('* title = "%s" \n' % self.get_title())
        outfile.write('* status = #%s \n' % self.get_status())
        outfile.write('* description = "%s" \n' % self.description)
        
        if self.resource == self.resource.CodeSystem: outfile.write('* content = #%s \n' % self.get_content())
        
        if hasattr(self, 'implicitrules'): outfile.write('* implicitRules = "%s" \n' % self.get_implicitrules())
        if hasattr(self, 'language'): outfile.write('* language = "%s" \n' % self.get_language())
        elif argsLang is not None: outfile.write('* language = "%s" \n' % argsLang)
        if hasattr(self, 'text'): outfile.write('* text = "%s" \n' % self.get_text())
        if hasattr(self, 'contained'): outfile.write('* contained = "%s" \n' % self.get_contained())
        if hasattr(self, 'extension'): outfile.write('* extension = "%s" \n' % self.get_implicitrules())
        if hasattr(self, 'modifierextension'): outfile.write('* modifierExtension = "%s" \n' % self.get_modifierextension())
        if hasattr(self, 'identifier'): 
            i = 0
            for oneIdentifier in self.get_identifier():
                outfile.write('* identifier[%s] = "%s" \n' % (i,oneIdentifier))
                i += 1
        if hasattr(self, 'experimental'): outfile.write('* experimental = "%s" \n' % self.get_experimental())
        if hasattr(self, 'date'): outfile.write('* date = "%s" \n' % self.get_date())
        if hasattr(self, 'publisher'): outfile.write('* publisher = "%s" \n' % self.get_publisher())
        if hasattr(self, 'contact'):
            i = 0 
            for oneContact in self.get_contact():
                outfile.write('* contact[%s] = "%s" \n' % (i,oneContact))
                i += 1
        if hasattr(self, 'usecontext'): 
            i = 0
            for oneUseContext in self.get_usecontext():
                outfile.write('* useContext[%s] = "%s" \n' % (i,oneUseContext))
                i += 1
        if hasattr(self, 'jurisdiction'):
            i = 0
            for oneJurisdiction in self.get_jurisdiction():
                outfile.write('* jurisdiction[%s] = "%s" \n' % (i,oneJurisdiction))
                i += 1
        if hasattr(self, 'purpose'): outfile.write('* purpose = "%s" \n' % self.get_purpose())
        if hasattr(self, 'copyright'): outfile.write('* copyright = "%s" \n' % self.get_copyright())
        
        if hasattr(self, 'immutable'): outfile.write('* publisher = "%s" \n' % self.get_immutable())
        if hasattr(self, 'lockeddate'): outfile.write('* lockedDate = "%s" \n' % self.get_lockeddate())
        if hasattr(self, 'inactive'): outfile.write('* inactive = "%s" \n' % self.get_inactive())
        
        if hasattr(self, 'casesensitive'): outfile.write('* caseSensitive = "%s" \n' % self.get_casesensitive())
        if hasattr(self, 'valueset'): outfile.write('* valueSet = "%s" \n' % self.get_valueset())
        if hasattr(self, 'hierarchymeaning'): outfile.write('* hierarchyMeaning = "%s" \n' % self.get_hierarchymeaning())
        if hasattr(self, 'compositional'): outfile.write('* compositional = "%s" \n' % self.get_compositional())
        if hasattr(self, 'versionneeded'): outfile.write('* versionNeeded = "%s" \n' % self.get_versionneeded())
        if hasattr(self, 'supplements'): outfile.write('* supplements = "%s" \n' % self.get_supplements())
        if hasattr(self, 'count'): outfile.write('* count = "%s" \n' % self.get_count())
        if hasattr(self, 'filter'): 
            i = 0
            for oneFilter in self.get_filter():
                if hasattr(oneFilter, 'code'): outfile.write('* filter[%s].code = #%s \n' % (i, oneFilter.code))
                if hasattr(oneFilter, 'description'): outfile.write('* filter[%s].description = "%s" \n' % (i, oneFilter.description))
                if hasattr(oneFilter, 'operator'): outfile.write('* filter[%s].operator = #%s \n' % (i, oneFilter.operator))
                if hasattr(oneFilter, 'value'): outfile.write('* filter[%s].value = #%s \n' % (i, oneFilter.value))
                i += 1
        if hasattr(self, 'property'): 
            i = 0
            for oneProperty in self.get_property():
                if hasattr(oneProperty, 'code'): outfile.write('* property[%s].code = #%s \n' % (i, oneProperty.code))
                if hasattr(oneProperty, 'uri'): outfile.write('* property[%s].uri = "%s" \n' % (i, oneProperty.uri))
                if hasattr(oneProperty, 'description'): outfile.write('* property[%s].description = "%s" \n' % (i, oneProperty.description))
                if hasattr(oneProperty, 'type'): outfile.write('* property[%s].type = #%s \n' % (i, oneProperty.type))
                i += 1
        
        if hasattr(self, 'concept'):
            tempConcept = None
            j = -1
            k = -1
            for oneConcept in self.get_concept():
                #for CodeSystems
                if self.resource.name == 'CodeSystem':
                    if hasattr(oneConcept, 'displayName'): 
                        outfile.write('* #%s "%s"\n' % (oneConcept.code, oneConcept.displayName))
                    else:
                        outfile.write('* #%s\n' % (oneConcept.code))
                    if hasattr(oneConcept, 'definition'):
                        outfile.write('* #%s ^definition = %s\n' % (oneConcept.code, oneConcept.definition))
                    if hasattr(oneConcept, 'designation'): 
                        i = 0
                        for oneDesignation in oneConcept.designation:
                            if hasattr(oneDesignation, 'language'): outfile.write('* #%s ^designation[%s].language = #%s \n' % (oneConcept.code, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use'): outfile.write('* #%s ^designation[%s].use = #%s \n' % (oneConcept.code, i, oneDesignation.use))
                            if hasattr(oneDesignation, 'value'): outfile.write('* #%s ^designation[%s].value = "%s" \n' % (oneConcept.code, i, oneDesignation.value))
                            i += 1
                    if hasattr(oneConcept, 'property'): 
                        i = 0
                        for oneProperty in oneConcept.property:
                            if hasattr(oneProperty, 'code'): outfile.write('* #%s ^property[%s].code = #%s \n' % (oneConcept.code, i, oneProperty.code))
                            if hasattr(oneProperty, 'value'): outfile.write('* #%s ^property[%s].valueString = "%s" \n' % (oneConcept.code, i, oneProperty.value))
                            i += 1
                elif self.resource.name == 'ValueSet': # e.g. ->* compose.include.concept[5].designation[4].language
                    if tempConcept == None or tempConcept.system != oneConcept.system:
                        j += 1
                        k = -1
                        tempConcept = oneConcept
                        outfile.write('* compose.include[%s].system = "%s"\n' % (j, oneConcept.system))
                        if hasattr(oneConcept, 'version'):
                            outfile.write('* compose.include[%s].version = "%s"\n' % (j, oneConcept.version))
                    
                    if hasattr(oneConcept, 'code'):
                        k += 1
                        outfile.write('* compose.include[%s].concept[%s].code = "%s"\n' % (j, k, oneConcept.code))
                    if hasattr(oneConcept, 'display'):
                        outfile.write('* compose.include[%s].concept[%s].display = "%s"\n' % (j, k, oneConcept.display))
                    if hasattr(oneConcept, 'designation'):
                        i = -1
                        for oneDesignation in oneConcept.designation:
                            i += 1
                            if hasattr(oneDesignation, 'language'): outfile.write('* compose.include[%s].concept[%s].designation[%s].language = #%s \n' % (j, k, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use'): outfile.write('* compose.include[%s].concept[%s].designation[%s].use = #%s \n' % (j, k, i, oneDesignation.use))
                            if hasattr(oneDesignation, 'value'): outfile.write('* compose.include[%s].concept[%s].designation[%s].value = "%s" \n' % (j, k, i, oneDesignation.value))
                    if hasattr(oneConcept, 'filter'):
                        k += 1
                        if hasattr(oneDesignation.filter, 'property'): outfile.write('* compose.include[%s].filter[%s].property = #%s \n' % (j, k, oneConcept.filter.property))
                        if hasattr(oneDesignation.filter, 'op'): outfile.write('* compose.include[%s].filter[%s].op = #%s \n' % (j, k, oneConcept.filter.op))
                        if hasattr(oneDesignation.filter, 'value'): outfile.write('* compose.include[%s].filter[%s].value = "%s" \n' % (j, k, oneConcept.filter.value))
                        
                    # ToDo: implement exclude similar to include
                    # ToDo: implement simple Hierarchie for Children with the member extension
                    

        outfile.close()

def parse(inFilename):
    return Fsh1(inFilename)

class Filter(pcam.Filter):
    def __init__(self, idInFsh):
        super().__init__()
        self.idInFsh = idInFsh # this is a temporary ID for reading in fsh files

class Property(pcam.Property):
    def __init__(self, idInFsh):
        super().__init__()
        self.idInFsh = idInFsh # this is a temporary ID for reading in fsh files