import prop_csv_and_master as pcam

class Fsh1(pcam.PropCsvAndMaster):

    def __init__(self, inFile):
        super(pcam.PropCsvAndMaster, self).__init__()
        # open the file in read mode
        with open(inFile, 'r') as file:
            self.name = file.readline().split(':')[1].strip().strip('"')
            self.resource = pcam.Resource[file.readline().split(':')[1].strip().strip('"')]
            file.readline()
            self.url = file.readline().split('=')[1].strip().strip('"')
            self.version = file.readline().split('=')[1].strip().strip('"')
            file.readline()
            self.title = file.readline().split('=')[1].strip().strip('"')
            self.status = file.readline().split('=')[1].strip().strip('#')
            self.description = file.readline().split('=')[1].strip().strip('"')
            
            if self.resource == self.resource.CodeSystem:
                self.content = file.readline().split('=')[1].strip().strip('#')

            lstFilter =  []
            lstProperty = []

            for line in file:
                splittedLine = line.split('=')
                if '//' in splittedLine[0].strip():
                    continue
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
                        theProperty = Property(splittedLine[0].split(']')[0])
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
            
            if lstFilter != []:
                self.filter = lstFilter
            if lstProperty != []:
                self.property = lstProperty


    def exporto(self, outfile):
        outfile.write('Instance: %s \n' % self.get_name())
        outfile.write('InstanceOf: %s \n' % self.get_resource().name)#todo
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
                outfile.write('* filter[%s].code = #%s \n' % (i, oneFilter.code))
                outfile.write('* filter[%s].description = "%s" \n' % (i, oneFilter.description))
                outfile.write('* filter[%s].operator = #%s \n' % (i, oneFilter.operator))
                outfile.write('* filter[%s].value = #%s \n' % (i, oneFilter.value))
                i += 1
        if hasattr(self, 'property'): 
            i = 0
            for oneProperty in self.get_property():
                outfile.write('* property[%s].code = #%s \n' % (i, oneProperty.code))
                outfile.write('* property[%s].uri = "%s" \n' % (i, oneProperty.uri))
                outfile.write('* property[%s].description = "%s" \n' % (i, oneProperty.description))
                outfile.write('* property[%s].type = #%s \n' % (i, oneProperty.type))
                i += 1
        #if self.property is not None: outfile.write('* property = "%s" \n' % self.property)
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