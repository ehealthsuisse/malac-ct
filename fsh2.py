from fsh1 import Fsh1
import sys
import prop_csv_and_master as pcam

class Fsh2(Fsh1):

    def parse(inFilename):
        return Fsh2(inFilename)

    def parseConcepts(self, dictConcept, line, splittedLine, value):
        if '* #' in splittedLine[0]:
            theConcept = None
                        #split here for CS and VS
            if self.resource == self.resource.CodeSystem:
                theConcept = pcam.CSConcept() #alternative construktor to create an new object without calling __init__, for minimal memory allocation
                if '^' in line:
                    if oneConcept := dictConcept[line.split(' ')[1].strip('#')]:
                        if 'definition' in line:
                            oneConcept.definition = value #line.split('"')[1]
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
                                if oneProperty.idInFsh == line.split(']')[0]:
                                    theProperty = oneProperty
                                        # if none is found in the list, make one
                            if theProperty is None:
                                theProperty = pcam.CSConcept.ConceptProperty.__new__(pcam.CSConcept.ConceptProperty)
                                theProperty.idInFsh = line.split(']')[0]
                                oneConcept.property.append(theProperty)
                                        # split the line properly
                            #if len(line.split('#')) > 2:
                            #    value = line.strip().split(' ')[-1:][0].strip('#')
                            #else:
                            #    value = line.strip().split('"')[1]
                                        # add the data to the Property
                            if 'code' in splittedLine[0].strip().split('.')[-1].strip():
                                theProperty.code = value
                            elif 'value' in splittedLine[0].split('.')[-1].strip():
                                theProperty.value = value
                                theProperty.type = pcam.PropertyCodeType(splittedLine[0].split('.')[-1].strip()[5:].lower())
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
                    dictConcept[theConcept.code] = theConcept

                        # todo get to version 2
            elif self.resource == self.resource.ValueSet:
                theConcept = pcam.VSConcept()#.__new__(pcam.VSConcept) #alternative construktor to create an new object without calling __init__, for minimal memory allocation
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

    def exportoConcepto(self, outfile, incHierarchyExt4VS):
        conceptList = self.get_concept()
        if len(conceptList) > 0:
            tempConcept = None
            j = -1
            k = -1
            for oneConcept in conceptList:
                #for CodeSystems
                if self.get_resource() == 'CodeSystem':
                    if hasattr(oneConcept, 'display'):
                        outfile.write('* #%s "%s"\n' % (oneConcept.code, oneConcept.display.replace('"','\\"')))
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
                            # TODO has to be adapted according to fsh1.py
                            if hasattr(oneProperty, 'value'): outfile.write('* #%s ^property[%s].value%s = "%s" \n' % (oneConcept.code, i, oneProperty.type.value, oneProperty.value))
                            i += 1
                elif self.get_resource() == 'ValueSet': # e.g. ->* compose.include.concept[5].designation[4].language
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
                        for oneFilter in oneConcept.filter:
                            if hasattr(oneFilter, 'property'): outfile.write('* compose.include[%s].filter[%s].property = #%s \n' % (j, k, oneConcept.filter.property))
                            if hasattr(oneFilter, 'op'): outfile.write('* compose.include[%s].filter[%s].op = #%s \n' % (j, k, oneConcept.filter.op))
                            if hasattr(oneFilter, 'value'): outfile.write('* compose.include[%s].filter[%s].value = "%s" \n' % (j, k, oneConcept.filter.value))

                    # ToDo: implement exclude similar to include
                    # ToDo: implement simple Hierarchie for Children with the member extension