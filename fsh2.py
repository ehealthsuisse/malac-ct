from fsh1 import Fsh1, check_for_duplicates, writeSelfAndRecrCallMembers, exporto_extension
import sys
import prop_csv_and_master as pcam
import ext
import ext_aut

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
                                if 'userSelected' in splittedLine[0].split('.')[1].strip():
                                    theDesignation.use.userSelected = value
                                else:
                                    str4Coding = value
                                    if "|" in value:
                                        str4Coding = str4Coding.replace("|","^",1)
                                        str4Coding = str4Coding.replace("#","^",1)
                                    else:
                                        str4Coding = str4Coding.replace("#","^^",1)
                                    if " \"" in value:
                                        str4Coding = str4Coding.replace(" \"","^",1).replace("\"","")
                                    else:
                                        str4Coding += "^"
                                    str4Coding += "^"
                                    theDesignation.use = pcam.Coding(str4Coding)
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
                    check_for_duplicates(theConcept, dictConcept, "CS")
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
                    # space holder for duplicate check:
                    # check_for_duplicates(theConcept, dictConcept, "VS")
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
                                if 'userSelected' in line:
                                    theDesignation.use.userSelected = value
                                else:
                                    str4Coding = value
                                    if "|" in value:
                                        str4Coding = str4Coding.replace("|","^",1)
                                        str4Coding = str4Coding.replace("#","^",1)
                                    else:
                                        str4Coding = str4Coding.replace("#","^^",1)
                                    if " \"" in value:
                                        str4Coding = str4Coding.replace(" \"","^",1).replace("\"","")
                                    else:
                                        str4Coding += "^"
                                    str4Coding += "^"
                                    theDesignation.use = pcam.Coding(str4Coding)
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

            # look into the concepts and see if there are any members, so that these will be specially printed
            vsMemberAnywhere = False
            for oneConcept in conceptList:
                if hasattr(oneConcept,"member") and oneConcept.member != []:
                    vsMemberAnywhere = True

            # if there is a conceptSuppl, print them first
            if hasattr(self,"conceptSuppl") and self.conceptSuppl:
                tempList = self.conceptSuppl
            elif self.get_resource() == 'ValueSet':
                tempList = self.buildConceptDictWithAttr('code', 'system').values() # quickly remove duplicates
            elif self.get_resource() == 'CodeSystem':
                tempList = self.get_concept()

            j = -1
            k = -1
            for oneConcept in tempList:
                #for CodeSystems
                if self.get_resource() == 'CodeSystem':
                    if hasattr(oneConcept, 'display') and oneConcept.display:
                        outfile.write('* #%s "%s"\n' % (oneConcept.code, oneConcept.display.replace('"','\\"')))
                    else:
                        outfile.write('* #%s\n' % (oneConcept.code))
                    if hasattr(oneConcept, 'definition') and oneConcept.definition:
                        outfile.write('* #%s ^definition = %s\n' % (oneConcept.code, oneConcept.definition))
                    if hasattr(oneConcept, 'designation') and oneConcept.designation:
                        i = 0
                        for oneDesignation in oneConcept.designation:
                            if hasattr(oneDesignation, 'language') and oneDesignation.language: outfile.write('* #%s ^designation[%s].language = #%s \n' % (oneConcept.code, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use') and oneDesignation.use.code:
                                tmpCoding = oneDesignation.use.codesystem
                                if tmp := oneDesignation.use.version: tmpCoding += "|"+tmp
                                tmpCoding += "#"+oneDesignation.use.code
                                if tmp := oneDesignation.use.display: tmpCoding += " \""+tmp+"\""
                                outfile.write('* #%s ^designation[%s].use = %s \n' % (oneConcept.code, i, tmpCoding))
                                if tmp := oneDesignation.use.userSelected:
                                    outfile.write('* #%s ^designation[%s].use.userSelected = %s \n' % (oneConcept.code, i, tmp))
                            if hasattr(oneDesignation, 'value') and oneDesignation.value: outfile.write('* #%s ^designation[%s].value = "%s" \n' % (oneConcept.code, i, oneDesignation.value))
                            i += 1
                    if hasattr(oneConcept, 'property') and oneConcept.property:
                        i = 0
                        for oneProperty in oneConcept.property:
                            if hasattr(oneProperty, 'code'): outfile.write('* #%s ^property[%s].code = #%s \n' % (oneConcept.code, i, oneProperty.code))
                            if hasattr(oneProperty, 'value') and oneProperty.type.value == "string": outfile.write('* #%s ^property[%s].value%s = "%s" \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), oneProperty.value.replace('"','\\"')))
                            elif hasattr(oneProperty, 'value') and oneProperty.type.value == "code": outfile.write('* #%s ^property[%s].value%s = #%s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), oneProperty.value.replace('"','\\"')))
                            elif hasattr(oneProperty, 'value') and oneProperty.type.value == "boolean": outfile.write('* #%s ^property[%s].value%s = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value).lower().replace('"','\\"')))
                            elif hasattr(oneProperty, 'value') and oneProperty.type.value == "Coding":
                                if hasattr(oneProperty.value, 'codesystem') and oneProperty.value.codesystem: outfile.write('* #%s ^property[%s].value%s.system = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value.codesystem).replace('"','\\"')))
                                if hasattr(oneProperty.value, 'version') and oneProperty.value.version: outfile.write('* #%s ^property[%s].value%s.version = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value.version).replace('"','\\"')))
                                if hasattr(oneProperty.value, 'code') and oneProperty.value.code: outfile.write('* #%s ^property[%s].value%s.code = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value.code).replace('"','\\"')))
                                if hasattr(oneProperty.value, 'display') and oneProperty.value.display: outfile.write('* #%s ^property[%s].value%s.display = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value.display).replace('"','\\"')))
                                if hasattr(oneProperty.value, 'userSelected') and oneProperty.value.userSelected: outfile.write('* #%s ^property[%s].value%s.userSelected = %s \n' % (oneConcept.code, i, pcam.first_char_to_upper(oneProperty.type.value), str(oneProperty.value.userSelected).lower().replace('"','\\"')))

                            i += 1

                    # export extension
                    exporto_extension(outfile, '* #%s ^' % (oneConcept.code), oneConcept, 0, ext.ReplacedBy.extension_canonical)
                elif self.get_resource() == 'ValueSet': # e.g. ->* compose.include.concept[5].designation[4].language
                    if tempConcept == None or tempConcept.system != oneConcept.system:
                        j += 1
                        k = -1
                        tempConcept = oneConcept
                        exporto_extension(outfile, '* compose.include[%s].' % (j), oneConcept, 0, ext_aut.SystemOid.extension_canonical)
                        outfile.write('* compose.include[%s].system = "%s"\n' % (j, oneConcept.system))
                        # write the system version if existent
                        if hasattr(oneConcept, 'version') and oneConcept.version:
                            outfile.write('* compose.include[%s].version = "%s"\n' % (j, oneConcept.version))
                        else:
                            # retrieve version from metadata

                            # theoretically one_concept.system could be either canonical or OID in
                            # most cases, however, it would be the canonical
                            if tmp := self.gainVersionFromCanonical(oneConcept.system):
                                outfile.write('* compose.include[%s].version = "%s"\n' % (j, tmp))
                            elif tmp := self.gainVersionFromOid(oneConcept.system):
                                outfile.write('* compose.include[%s].version = "%s"\n' % (j, tmp))

                    if hasattr(oneConcept, 'code'):
                        k += 1
                        outfile.write('* compose.include[%s].concept[%s].code = "%s"\n' % (j, k, oneConcept.code))
                    if hasattr(oneConcept, 'display') and oneConcept.display:
                        outfile.write('* compose.include[%s].concept[%s].display = "%s"\n' % (j, k, oneConcept.display))
                    if hasattr(oneConcept, 'designation') and oneConcept.designation:
                        i = -1
                        for oneDesignation in oneConcept.designation:
                            i += 1
                            if hasattr(oneDesignation, 'language') and oneDesignation.language: outfile.write('* compose.include[%s].concept[%s].designation[%s].language = #%s \n' % (j, k, i, oneDesignation.language))
                            if hasattr(oneDesignation, 'use') and oneDesignation.use.code:
                                tmpCoding = oneDesignation.use.codesystem
                                if tmp := oneDesignation.use.version: tmpCoding += "|"+tmp
                                tmpCoding += "#"+oneDesignation.use.code
                                if tmp := oneDesignation.use.display: tmpCoding += " \""+tmp+"\""
                                outfile.write('* compose.include[%s].concept[%s].designation[%s].use = %s \n' % (j, k, i, tmpCoding))
                                if tmp := oneDesignation.use.userSelected:
                                    outfile.write('* compose.include[%s].concept[%s].designation[%s].use.userSelected = %s \n' % (j, k, i, tmp))
                            if hasattr(oneDesignation, 'value') and oneDesignation.value: outfile.write('* compose.include[%s].concept[%s].designation[%s].value = "%s" \n' % (j, k, i, oneDesignation.value))
                    exporto_extension(outfile, '* compose.include[%s].concept[%s].' % (j, k), oneConcept, 0, ext.ConceptOrder.extension_canonical)
                    if hasattr(oneConcept, 'filter') and oneConcept.filter:
                        k += 1
                        for oneFilter in oneConcept.filter:
                            if hasattr(oneFilter, 'property') and oneFilter.property: outfile.write('* compose.include[%s].filter[%s].property = #%s \n' % (j, k, oneConcept.filter.property))
                            if hasattr(oneFilter, 'op') and oneFilter.op: outfile.write('* compose.include[%s].filter[%s].op = #%s \n' % (j, k, oneConcept.filter.op))
                            if hasattr(oneFilter, 'value') and oneFilter.value: outfile.write('* compose.include[%s].filter[%s].value = "%s" \n' % (j, k, oneConcept.filter.value))
                    # ToDo: implement exclude similar to include
                    # ToDo: implement simple Hierarchie for Children with the member extension

            # look if a member definition in the valueset is used (* compose.include.extension.extension.url & valueCode) and the args param is set
            if vsMemberAnywhere and self.get_resource() == 'ValueSet' and incHierarchyExt4VS:
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
            if self.get_resource() == 'ValueSet':
                outfile.write('\n')
                outfile.write('* expansion.timestamp = "%s"\n' % self.metadata_change_timestamp)
                outfile.write('\n')
                containCnt = [-1]
                for oneConcept in conceptList:
                    if oneConcept.level == 0:
                        writeSelfAndRecrCallMembers(self, oneConcept, outfile, containCnt)