import enum
import time
from unittest import skip
from malac_ct import extensions_dict
import ext

class FileStyle(enum.Enum):
    propCSV = "propCSV"
    spreadCT = "spreadCT"

class ParentingBy(enum.Enum):
    conceptOrder = "conceptOrder"
    parentAndSystem = "parentAndSystem"

    def set_unchangeable_parenting_by(finalVariable, newValue):
        if finalVariable and finalVariable != newValue:
            import sys
            sys.exit('It is only allowed to use parentByConceptOrder or parent and parentSystem, not both, at the same time.')
        else:
            return newValue

class DuplicateConceptError(Exception):
    pass

class ShareableCSVSError(Exception):
    def __init__(self, keyword):
        super().__init__(f"Terminology is not compliant with the Profile ShareableCodeSystem/ShareableValueSet, missing element : '{keyword}'")

def get_full_path(concept):
    path = []
    current = concept
    while hasattr(current, 'parent') and current.parent:
        path.append((current.parent.code, getattr(current.parent, 'system', None)))
        current = current.parent
    return tuple(reversed(path))

# helper function to check for duplicate occurences of tempConcept in the conceptList on (code) for VS and (code, system) for VS
def check_for_duplicates(tempConcept, conceptList, check_parent_by="parent"):
    for concept in conceptList:
        if concept.code == tempConcept.code:
            concept_parent = getattr(concept, check_parent_by, None)
            tempConcept_parent = getattr(tempConcept, check_parent_by, None)
            if (concept_parent is None and tempConcept_parent is None) or (concept_parent is not None and tempConcept_parent is not None and concept_parent.code == tempConcept_parent.code):
                if not hasattr(tempConcept, "system"):
                    raise DuplicateConceptError(f"Duplicate concept code found: {tempConcept.code}")
                else:
                    if hasattr(tempConcept, "system") and hasattr(concept, "system") and concept.system == tempConcept.system:
                        raise DuplicateConceptError(f"Duplicate concept code found: {tempConcept.code}")

def trim_output(func):
    """strips/trims strings and list of strings"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, str):
            return result.strip() if result else ""
        elif isinstance(result, list):
            return [item.strip() if isinstance(item, str) else item 
                    for item in result]
        return result
    return wrapper

class PropCsvAndMaster():
    # following are use only in malac-ct
    parenting_by = None

    def __init__(self, inFile = None, encoding='cp1252', file_style=FileStyle.propCSV):
        self.resource = Resource
        self.id = None
        self.profiles = []
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
        self.experimental = False
        self.date = None
        self.publisher = "Not specified"
        self.contact = []
        self.usecontext = []
        self.jurisdiction = []
        self.purpose = None
        self.copyright = None
        self.concept = []
        # following are used only in ValueSets
        self.immutable = None
        self.lockeddate = None
        self.inactive = False
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
            try:
                import csv
                if file_style is FileStyle.spreadCT:
                    inFile = inFile.replace(".data.1.spreadct.csv",".meta.1.spreadct.csv")
                    encoding = "utf-8"

                # usally open file with special encoding because of Excel compatibility,
                # see https://stackoverflow.com/questions/6588068/which-encoding-opens-csv-files-correctly-with-excel-on-both-mac-and-windows
                with open(inFile, 'r', encoding=encoding) as csvfile:
                    # creating dictreader object
                    file = csv.reader(csvfile, quotechar='"', delimiter=';')

                    if file_style is FileStyle.propCSV:
                        # iterating over first two rows and append values to empty list
                        metaList = [file.__next__()]+[file.__next__()]
                        # iterating over a empty row
                        file.__next__()
                    elif file_style is FileStyle.spreadCT:
                        metaList = []
                        for metaLine in file:
                            metaList.append(metaLine)
                        metaList = list(zip(*metaList)) #transpose the list

                    #initializing the header/metadata
                    i = -1
                    for metaObj in metaList[0]:
                        i += 1
                        # change all ';' to ','
                        #metaList[1][i].replace(';',',')
                        metaList[1][i].strip("\"")

                        if 'resource' == metaObj: self.resource = Resource(metaList[1][i])
                        if 'id' == metaObj: self.id = metaList[1][i]
                        if metaObj.startswith('profile'): self.profiles.append(metaList[1][i])
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
                        if metaObj.startswith('identifier'): self.identifier.append(metaList[1][i])
                        if 'date' == metaObj:
                            import datetime
                            self.date = datetime.datetime.strptime(metaList[1][i][:10], '%Y-%m-%d').strftime('%Y-%m-%d')
                        if 'experimental' == metaObj: self.experimental = metaList[1][i]
                        if 'publisher' == metaObj: self.publisher = metaList[1][i]
                        if metaObj.startswith('contact'):
                            # append contact if not None
                            if tmp := ContactDetail.from_string(metaList[1][i]):
                                self.contact.append(tmp)
                        if metaObj.startswith('useContext'): self.usecontext.append(metaList[1][i])
                        if metaObj.startswith('jurisdiction'): self.jurisdiction.append(metaList[1][i])
                        if 'purpose' == metaObj: self.purpose = metaList[1][i]
                        if 'copyright' == metaObj: self.copyright = metaList[1][i]
                        if 'immutable' == metaObj: self.immutable = metaList[1][i]
                        if 'lockedDate' == metaObj: self.lockeddate = metaList[1][i]
                        if 'caseSensitive' == metaObj: self.casesensitive = metaList[1][i]
                        if 'valueSet' == metaObj: self.valueset = metaList[1][i]
                        if 'hierarchyMeaning' == metaObj and metaList[1][i]: self.hierarchymeaning = HierarchyMeaning(metaList[1][i])
                        if 'compositional' == metaObj: self.compositional = metaList[1][i]
                        if 'versionNeeded' == metaObj: self.versionneeded = metaList[1][i]
                        if 'supplements' == metaObj: self.supplements = metaList[1][i]
                        if 'count' == metaObj: self.count = metaList[1][i]
                        if metaObj.startswith('filter'):
                            filterElements = metaList[1][i].split('|')
                            tempFilter = Filter()
                            tempFilter.code = filterElements[0]
                            tempFilter.description = filterElements[1]
                            tempFilter.operator = filterElements[2]
                            tempFilter.value = filterElements[3]
                            self.filter.append(tempFilter)
                        if metaObj.startswith('property'):
                            propElements = metaList[1][i].split('|')
                            tempProperty = Property()
                            tempProperty.code = propElements[0]
                            tempProperty.uri = propElements[1]
                            tempProperty.description = propElements[2]
                            tempProperty.type = PropertyCodeType[propElements[3].lower()]
                            self.property.append(tempProperty)

                    # shareable profile compliance:
                    self.ensure_shareable_profile_compliance()

                    if file_style is FileStyle.spreadCT:
                        csvfile.close()
                        csvfile = open(inFile.replace(".meta.1.spreadct.csv",".data.1.spreadct.csv"), 'r', encoding=encoding)
                        file = csv.reader(csvfile, quotechar='"', delimiter=';')

                    # iterating over the next row with headings for concepts
                    headingList = file.__next__()

                    #initializing the body/content
                    for row in file:

                        if self.resource == self.resource.CodeSystem:
                            tempConcept = CSConcept()
                        elif self.resource == self.resource.ValueSet:
                            tempConcept = VSConcept()

                        # reading the content of the row
                        for i in range(0, len(row)):
                            if row[i].strip() != "":
                                row[i].strip("\"").strip("\'")

                                if self.resource == self.resource.CodeSystem:
                                    if 'code' == headingList[i]: tempConcept.code = row[i]
                                    elif 'display' == headingList[i]: tempConcept.display = row[i]
                                    elif 'definition' == headingList[i]: tempConcept.definition = row[i]
                                    elif 'designation' == headingList[i]:
                                        tempConcept.designation.append(ConceptDesignation(row[i]))
                                    elif 'property' == headingList[i]:
                                        tempConcept.property.append(CSConcept.ConceptProperty(row[i]))
                                    elif 'extension' == headingList[i]:
                                        tempConcept.extension.append(Extension(row[i]))
                                    else: # everything else should be a known extension or unknown property (aka easyProperties & easyExtensions)
                                        foundOneExt = False
                                        for extensionValueModule, extensionValueClass in extensions_dict.values():
                                            if extensionValueClass.lower() == headingList[i].lower():
                                                extModule = __import__(extensionValueModule)
                                                extClass = getattr(extModule, extensionValueClass)
                                                extClass.add_extension(tempConcept, row[i])
                                                #tempConcept.extension.append(Extension(row[i]))
                                                foundOneExt = True
                                                break
                                        if not foundOneExt:
                                            prop_type = "string" # default type if none found in meta
                                            for one_meta in metaList[1]:
                                                if (tmp := one_meta.split("|"))[0] == headingList[i]:
                                                    prop_type = tmp[3]
                                                    break
                                            tempConcept.property.append(CSConcept.ConceptProperty(headingList[i]+"|"+row[i]+"|"+prop_type))
                                elif self.resource == self.resource.ValueSet:
                                    if 'system' == headingList[i]: tempConcept.system = row[i]
                                    elif 'version' == headingList[i]: tempConcept.version = row[i]
                                    elif 'code' == headingList[i]: tempConcept.code = row[i]
                                    elif 'display' == headingList[i]: tempConcept.display = row[i]
                                    elif 'parent' == headingList[i]:
                                        tempConcept.parent = row[i]
                                        self.parenting_by = ParentingBy.set_unchangeable_parenting_by(self.parenting_by, ParentingBy.parentAndSystem)
                                    elif 'parentSystem' == headingList[i]:
                                        tempConcept.parentSystem = row[i]
                                        self.parenting_by = ParentingBy.set_unchangeable_parenting_by(self.parenting_by, ParentingBy.parentAndSystem)
                                    elif 'designation' == headingList[i]:
                                        tempConcept.designation.append(ConceptDesignation(row[i]))
                                    elif 'filter' == headingList[i]:
                                        filterElements = row[i].split('|')
                                        tempFilter = VSConcept.VSConceptFilter()
                                        tempFilter.property = filterElements[0]
                                        tempFilter.op = filterElements[1]
                                        tempFilter.value = filterElements[2]
                                        tempConcept.filter = tempFilter # this is not a list!
                                    elif 'abstract' == headingList[i]:
                                        if row[i].lower() == "true" or "yes" or "1":
                                            tempConcept.abstract = True
                                    elif 'inactive' == headingList[i]:
                                        if row[i].lower() == "true" or "yes" or "1":
                                            tempConcept.inactive = True
                                            self.inactive = True
                                    elif 'exclude' == headingList[i]:
                                        if row[i].lower() == "true" or "yes" or "1":
                                            tempConcept.exclude = True
                                    elif 'extension' == headingList[i]:
                                        tempConcept.extension.append(Extension(row[i]))
                                    elif 'parentByConceptOrder' == headingList[i]: # special handling of malac-ct addition if conceptOrder is used
                                        tempConcept.parentByConceptOrder = int(row[i])
                                        self.parenting_by = ParentingBy.set_unchangeable_parenting_by(self.parenting_by, ParentingBy.conceptOrder)
                                    else: # Everything else should be a known extension or unknown designation (aka easyDesignation & easyExtensions),
                                        # with a designation use inside https://termgit.elga.gv.at/CodeSystem/austrian-designation-use.
                                        # The valueset author should be aware that the CodeSystem should have that designations
                                        foundOneExt = False
                                        for extensionValueModule, extensionValueClass in extensions_dict.values():
                                            if extensionValueClass.lower() == headingList[i].lower():
                                                extModule = __import__(extensionValueModule)
                                                extClass = getattr(extModule, extensionValueClass)
                                                extClass.add_extension(tempConcept, row[i])
                                                #tempConcept.extension.append(Extension(row[i]))
                                                foundOneExt = True
                                                break
                                        if not foundOneExt:
                                            tempConcept.designation.append(ConceptDesignation("|https://termgit.elga.gv.at/CodeSystem/austrian-designation-use^^"+headingList[i]+"^"+headingList[i]+"^|"+row[i]))


                        # check for some invalid combinations on a concept level
                        if self.resource == self.resource.ValueSet:
                            # both, the parent and the parentSystem, have to exist together or do not
                            if bool(tempConcept.parent) != (hasattr(tempConcept,"parentSystem") and bool(tempConcept.parentSystem)):
                                import sys
                                sys.exit('Parent code and system should always be stated together. See concept with code: ' + tempConcept.code)
                        
                        self.concept.append(tempConcept)

                    # fill members of parents
                    if self.resource == self.resource.ValueSet:

                        if self.parenting_by == ParentingBy.conceptOrder:
                            # create a dict with the conceptOrder as key
                            # beware, some concept may do not have a conceptOrder, these can only be childs!
                            # beware, if a conceptOrder is using a already given value, only the last concept with the same conceptOrder can be a parent
                            # beware, if there are multiple conceptOrder extensions, only the first will be used
                            concept_dict_with_order_as_key = {}
                            for one_concept in self.concept:
                                for one_ext in one_concept.extension:
                                    if one_ext.url == ext.ConceptOrder.extension_canonical:
                                        concept_dict_with_order_as_key[one_ext.value] = one_concept
                                        break
                                else:
                                    # if parentByConceptOrder is used once, then every concept has to have a explicitly given conceptOrder
                                    import sys
                                    sys.exit('If parentByConceptOrder is used, then every concept needs a conceptOrder extension. See concept with code: ' + one_concept.code)
                            # now link all the parents using the dict
                            for one_concept in self.concept:
                                if hasattr(one_concept,"parentByConceptOrder"):
                                    parent = concept_dict_with_order_as_key[one_concept.parentByConceptOrder]
                                    # setting one_concept as child of the parent
                                    parent.member.append(one_concept)
                                    # setting the parent of one_concept
                                    one_concept.parent = parent

                        else: # fallback to parent + parentSystem
                            concept_dict = self.buildConceptDictWithAttr('code', 'system')
                            for one_concept in self.concept:
                                if one_concept.parent and one_concept.parentSystem:
                                    parent = concept_dict[one_concept.parent+one_concept.parentSystem]
                                    # setting one_concept as child of the parent
                                    parent.member.append(one_concept)
                                    # setting the parent of one_concept
                                    one_concept.parent = parent

                        # do level retrieving after definition, else if you have a child listed before a parent, that is also having a parent, there will be errors
                        for one_concept in self.concept:
                            # setting the hierarchy level
                            one_concept.level = self.retrieve_level_of_VS_concept(one_concept)
                    elif self.resource == self.resource.CodeSystem:
                        concept_dict = self.buildConceptDictWithAttr('code')

                        for one_concept in self.concept:
                            self.add_children_to_CS_concept(concept_dict, one_concept)
                    # check concept length for shareable profile compliance
                    if self.concept is None or len(self.concept) == 0:
                        raise ShareableCSVSError("concept")
            except UnicodeDecodeError:
                print(" (because of some DecodeError, this terminology will be read again in utf-8 instead of cp1252)")
                return PropCsvAndMaster.__init__(self, inFile, encoding='utf-8')
        if self.parenting_by == ParentingBy.conceptOrder:
            self.check_duplicate_codes_per_parent("parentByConceptOrder")
        else:
            self.check_duplicate_codes_per_parent()

    def check_duplicate_codes_per_parent(self, check_parent_by="parent"):
        if self.resource == self.resource.CodeSystem:
            seen_codes = set()
            duplicates = set()
            for concept in self.concept:
                if concept.code in seen_codes:
                    duplicates.add(concept.code)
                else:
                    seen_codes.add(concept.code)
        else:
            path_duplicates = {}
            for concept in self.concept:
                path = get_full_path(concept)
                key = (concept.code, concept.system, path)
                if key in path_duplicates:
                    raise DuplicateConceptError("Duplicate concept found: ", key)
                else:
                    path_duplicates[key] = concept.code

    # check metadata compliance for shareable profiles
    def ensure_shareable_profile_compliance(self):
        canonical_shareable_profile = None
        if self.resource == self.resource.CodeSystem:
            canonical_shareable_profile = "http://hl7.org/fhir/StructureDefinition/shareablecodesystem"
        else:
            canonical_shareable_profile = "http://hl7.org/fhir/StructureDefinition/shareablevalueset"
        if self.url is None: raise ShareableCSVSError("url")
        if self.version is None: raise ShareableCSVSError("version")
        if self.name is None: raise ShareableCSVSError("name")
        if self.status is None: raise ShareableCSVSError("status")
        if self.description is None: raise ShareableCSVSError("description")
        # experimental default False, publisher default "Not specified"
        if len(self.contact) == 0:
            self.contact.append(ContactDetail.from_string("|other^Not specified^^^^"))
        if canonical_shareable_profile not in self.profiles:
            self.profiles.append(canonical_shareable_profile)

    def retrieve_level_of_VS_concept(self, concept):
        if tmp_parent := concept.parent:
            level = self.retrieve_level_of_VS_concept(tmp_parent)
            return level + 1
        else:
            return 0

    def retrieve_level_of_CS_concept(self, concept_dict, concept):
        if hasattr(concept,'property') and concept.property:
            for oneProperty in concept.property:
                if oneProperty.code == "parent":
                    level = self.retrieve_level_of_CS_concept(concept_dict, concept_dict[oneProperty.value])
                    return level + 1
        return 0

    def add_children_to_CS_concept(self, concept_dict, concept):
        if hasattr(concept,'property') and concept.property:
            for oneProperty in concept.property:
                if oneProperty.code == "parent":
                    if not hasattr(concept_dict[oneProperty.value], "propChildDict"):
                        # there is no managing of the now added props in the dict, but a code cant exists twice in a CS, so that should be good
                        concept_dict[oneProperty.value].propChildDict = self.build_property_dict_on_code_with_value_as_key(concept_dict[oneProperty.value],"child")
                    if concept.code not in concept_dict[oneProperty.value].propChildDict.keys():
                        the_property_child = CSConcept.ConceptProperty()
                        the_property_child.code = "child"
                        the_property_child.value = concept.code
                        the_property_child.type = PropertyCodeType.code
                        concept_dict[oneProperty.value].property.append(the_property_child)

    def parse(inFilename):
        return PropCsvAndMaster(inFilename)

    @trim_output
    def get_resource(self):
        return self.resource.value if hasattr(self,"resource") and hasattr(self.resource,"value") else None

    @trim_output
    def get_id(self):
        return self.id if hasattr(self,"id") else None

    @trim_output
    def get_profiles(self):
        if not hasattr(self, 'profiles'):
            self.profiles = []
        return self.profiles

    @trim_output
    def get_url(self):
        return self.url if hasattr(self,"url") else None

    @trim_output
    def get_version(self):
        return self.version if hasattr(self,"version") else None

    @trim_output
    def get_name(self):
        return self.name if hasattr(self,"name") else None

    @trim_output
    def get_title(self):
        return self.title if hasattr(self,"title") else None

    @trim_output
    def get_status(self):
        return self.status.value if hasattr(self,"status") and hasattr(self.status,"value") else None

    @trim_output
    def get_description(self):
        return self.description if hasattr(self,"description") else None

    @trim_output
    def get_content(self):
        return self.content.value if hasattr(self,"content") and hasattr(self.content,"value") else None

    @trim_output
    def get_implicitrules(self):
        return self.implicitrules if hasattr(self,"implicitrules") else None

    @trim_output
    def get_language(self):
        return self.language if hasattr(self,"language") else None

    @trim_output
    def get_text(self):
        return self.text if hasattr(self,"text") else None

    @trim_output
    def get_contained(self):
        return self.contained if hasattr(self,"contained") else None

    @trim_output
    def get_extension(self):
        return self.extension if hasattr(self,"extension") else None

    @trim_output
    def get_modifierextension(self):
        return self.modifierextension if hasattr(self,"modifierextension") else None

    @trim_output
    def get_identifier(self):
        return self.identifier if hasattr(self,"identifier") else None

    @trim_output
    def get_experimental(self):
        return self.experimental if hasattr(self,"experimental") else None

    @trim_output
    def get_date(self):
        return self.date if hasattr(self,"date") else None

    @trim_output
    def get_publisher(self):
        return self.publisher if hasattr(self,"publisher") else None

    @trim_output
    def get_contact(self):
        return self.contact if hasattr(self,"contact") else None

    @trim_output
    def get_usecontext(self):
        return self.usecontext if hasattr(self,"usecontext") else None

    @trim_output
    def get_jurisdiction(self):
        return self.jurisdiction if hasattr(self,"jurisdiction") else None

    @trim_output
    def get_purpose(self):
        return self.purpose if hasattr(self,"purpose") else None

    @trim_output
    def get_copyright(self):
        return self.copyright if hasattr(self,"copyright") else None

    @trim_output
    def get_immutable(self):
        return self.immutable if hasattr(self,"immutable") else None

    @trim_output
    def get_lockeddate(self):
        return self.lockeddate if hasattr(self,"lockeddate") else None

    @trim_output
    def get_inactive(self):
        return self.inactive if hasattr(self,"inactive") else None

    @trim_output
    def get_casesensitive(self):
        return self.casesensitive if hasattr(self,"casesensitive") else None

    @trim_output
    def get_valueset(self):
        return self.valueset if hasattr(self,"valueset") else None

    @trim_output
    def get_hierarchymeaning(self):
        return self.hierarchymeaning if hasattr(self,"hierarchymeaning") else None

    @trim_output
    def get_compositional(self):
        return self.compositional if hasattr(self,"compositional") else None

    @trim_output
    def get_versionneeded(self):
        return self.versionneeded if hasattr(self,"versionneeded") else None

    @trim_output
    def get_supplements(self):
        return self.supplements if hasattr(self,"supplements") else None

    @trim_output
    def get_count(self):
        return len(self.get_concept())

    @trim_output
    def get_filter(self):
        return self.filter if hasattr(self,"filter") else None

    @trim_output
    def get_property(self):
        tmp = []
        if hasattr(self,"property"):
            tmp = self.property
        if self.get_resource() == "CodeSystem":
            tmp = self.appendAdditionalConceptProperties(tmp)
        return tmp

    @trim_output
    def get_concept(self):
        return self.concept if hasattr(self,"concept") else None

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

    def appendMetaDataTo(self, csvFilename, timestamp):
        terminology_metadata_csv_columns = ['name', 'canonical', 'oid', 'version', 'id', 'type', 'metadata-change-timestamp', '"description"', 'title', 'status']

        # if file is new, add headers
        try:
            f = open(csvFilename)
            f.close()
        except IOError:
            with open(csvFilename, 'a', encoding="utf8") as csvfile:
                csvfile.write(','.join(terminology_metadata_csv_columns)+'\n')

        # file is existent, open and read into a dict with the second column as key
        import csv
        reader = csv.reader(open(csvFilename), quoting=csv.QUOTE_NONE)
        mydict = {row[1]:row for row in reader}

        # overwrite the first row with the now valid columns stated here
        mydict["canonical"] = terminology_metadata_csv_columns

        # check if any value changed
        if (tmpTup := mydict.get(self.get_url())) and tmpTup == [self.get_resource() + "-" + self.get_id(), self.get_url() or "", (tmp[0] if (tmp := self.get_identifier()) else ""), self.get_version() or "", self.get_id() or "", self.get_resource() or "", tmpTup[6], '"'+(self.get_description() or "").replace('\n', '<br/>').replace('"', "''")+'"', (self.get_title() or ""), (self.get_status() or "")]:
            timestamp = tmpTup[6]
        else:
            # change the one row or add the row to the dictionary
            mydict[self.get_url()] = [self.get_resource() + "-" + self.get_id(), self.get_url() or "", (tmp[0] if (tmp := self.get_identifier()) else ""), self.get_version() or "", self.get_id() or "", self.get_resource() or "", timestamp, '"'+(self.get_description() or "").replace('\n', '<br/>').replace('"', "''")+'"', (self.get_title() or ""), (self.get_status() or "")]

        # if metadata_change_timestamp has not yet been set
        if not hasattr(self, 'metadata_change_timestamp') or not self.metadata_change_timestamp:
            self.metadata_change_timestamp = timestamp

        # sort the dict
        import collections
        mydict = collections.OrderedDict(sorted(mydict.items()))
        mydict.move_to_end("canonical",False)

        # wirte the whole dict
        with open(csvFilename, 'w', newline='', encoding='utf-8') as outfile:
            for line in mydict.values():
                outfile.write(','.join(line)+'\n')

        return self.metadata_change_timestamp

    def resolveTerminologyMapping(self, search_column, search_value, target_column, error_message=None, error_value=None):
        # check if the needed argument is given
        if not hasattr(self, "processedTerminologies"):
            import sys
            sys.exit('An outdated csv needs a terminologies list for gaining OIDs, given with "-appndProcTermTo".\n')

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
        if error_message:
            print(error_message)
        return error_value

    def gainOidFromName(self, name):
        error_message = 'Error: For "%s" as CodeSystem-Name or as canonical the CodeSystem OID was not found in the appndProcTermTo list. Some formats, like the outdatedCSV, need a appndProcTermTo list for gaining OIDs of the used CodeSystems, given with "-appndProcTermTo". In this case, the given value will be used instead.\n' % name
        return self.resolveTerminologyMapping('name', name, 'oid', error_message, name)

    def gainOidFromCanonical(self, canonical):
        error_message = 'Error: For "%s" as CodeSystem-Name or as canonical the CodeSystem OID was not found in the appndProcTermTo list. Some formats, like the outdatedCSV, need a appndProcTermTo list for gaining OIDs of the used CodeSystems, given with "-appndProcTermTo". In this case, the given value will be used instead.\n' % canonical
        return self.resolveTerminologyMapping('canonical', canonical, 'oid', error_message, canonical)

    def gainCanonicalFromOid(self, oid):
        error_message = 'Error: For "%s" as OID the canonical of the CodeSystem was not found in the appndProcTermTo list. Some formats, like FHIR or FSH, need a appndProcTermTo list for gaining canonicals of the used CodeSystems, given with "-appndProcTermTo". In this case, the given value will be used instead.\n' % oid
        return self.resolveTerminologyMapping('oid', oid, 'canonical', error_message, oid)

    def gainVersionFromCanonical(self, canonical):
        return self.resolveTerminologyMapping('canonical', canonical, 'version')

    def gainVersionFromOid(self, oid):
        return self.resolveTerminologyMapping('oid', oid, 'version')

    def buildConceptDictWithAttr(self, *stringAttrAsKeys):
        tmpDict = {}
        for oneCon in self.get_concept():
            key = ''
            for stringAttrAsKey in stringAttrAsKeys:
                tmp_pointer = oneCon
                for part in stringAttrAsKey.split("."):
                    tmpPointer = getattr(tmp_pointer,part)
                if tmpPointer is None:
                    key = None
                    break
                key += tmpPointer
            # check if key is already in the dict and if, add it as a reference inside the object
            if key is None:
                continue
            if key in tmpDict:
                # create list, if non existent, name will be generated, i.e. _same_code_same_system
                if not hasattr(tmpDict[key],"same_"+"_and_same_".join(stringAttrAsKeys)):
                    setattr(tmpDict[key],"same_"+"_and_same_".join(stringAttrAsKeys),[])
                # check if same object is already in list and add it if not
                if not oneCon in getattr(tmpDict[key],"same_"+"_and_same_".join(stringAttrAsKeys)):
                    (getattr(tmpDict[key],"same_"+"_and_same_".join(stringAttrAsKeys))).append(oneCon)
            else:
                tmpDict[key] = oneCon
        return tmpDict

    def build_property_dict_on_code_with_value_as_key(self, concept, propCode):
        tmpDict = {}
        for oneProp in concept.property:
            if oneProp.code == propCode:
                tmpDict[oneProp.value] = oneProp
        return tmpDict

    def sortConceptsExpandStyle(self, conDict=None):
        sortedConcepts = []

        # build up a dict with code as key, with valuesets add system for using the same concept-codes in different codesystems
        if not conDict:
            if self.get_resource() == "CodeSystem":
                conDict = self.buildConceptDictWithAttr("code")
            elif self.get_resource() == "ValueSet":
                conDict = self.buildConceptDictWithAttr("code", "system")

        # sort all the child properties inside the concepts (only for CS!)
        if self.get_resource() == "CodeSystem":
            for key in conDict:
                if hasattr(conDict[key],"property") and conDict[key].property:
                    conDict[key].property.sort(key=CSConcept.ConceptProperty.get_value_if_code_is_child)

        # find all the concepts with no parent, sorted after key
        allLvl0 = []
        for key in sorted(conDict):
            thereIsAPropertyParent = False
            if self.get_resource() == "CodeSystem":
                for oneProp in conDict[key].property:
                    if oneProp.code == "parent":
                        thereIsAPropertyParent = True
            if (self.get_resource() == "CodeSystem" and not thereIsAPropertyParent or
                    self.get_resource() == "ValueSet" and not conDict[key].parent):
                allLvl0.append(key)

        # call the recr for all elements with no parent
        for lvl0 in allLvl0:
            self.storeSelfAndRecrCallChildren(conDict[lvl0], conDict, sortedConcepts)

        # overwrite the concept list with the just sorted one
        self.concept = sortedConcepts

    def sort_VS_concepts_by_conceptOrder(self):
        return self.get_concept().sort(key=VSConcept.get_value_of_conceptOrder)

    def storeSelfAndRecrCallChildren(self, oneCon, conDict, sortedCons):
        sortedCons.append(oneCon)
        if self.get_resource() == "CodeSystem":
            for oneProp in oneCon.property:
                if oneProp.code == "child":
                    if popdCon := conDict.pop(oneProp.value, None): # This will return conDict[key] if key exists in the dictionary, and None otherwise.
                        self.storeSelfAndRecrCallChildren(popdCon, conDict, sortedCons)
        elif self.get_resource() == "ValueSet":
            for oneMember in oneCon.member:
                if popdCon := conDict.pop(oneMember.code+oneMember.system, None): # This will return conDict[key] if key exists in the dictionary, and None otherwise.
                    self.storeSelfAndRecrCallChildren(popdCon, conDict, sortedCons)

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False, file_style=FileStyle.propCSV):
        csv_meta = []
        # start list of metaelements
        csv_meta.append(("resource",self.get_resource()))
        csv_meta.append(("id",self.get_id()))
        csv_meta.append(("url",self.get_url()))
        csv_meta.append(("version",self.get_version()))
        csv_meta.append(("name",self.get_name()))
        csv_meta.append(("title",self.get_title()))
        csv_meta.append(("status",self.get_status()))
        if tmp := self.get_profiles():
            for one_profile in tmp:
                csv_meta.append(("profile", one_profile))
        if tmp := self.get_description(): csv_meta.append(("description", tmp))

        if self.get_resource() == "CodeSystem": csv_meta.append(("content",self.get_content()))

        if tmp := self.get_implicitrules(): csv_meta.append(("implicitRules",tmp))
        if tmp := self.get_language(): csv_meta.append(("language",tmp))
        if tmp := self.get_text(): csv_meta.append(("text",tmp))
        if tmp := self.get_contained(): csv_meta.append(("contained",tmp))
        if tmp := self.get_extension(): csv_meta.append(("extension",tmp))
        if tmp := self.get_modifierextension(): csv_meta.append(("modifierExtension",tmp))
        if tmp := self.get_identifier():
            for oneIdentifier in tmp:
                csv_meta.append(("identifier",oneIdentifier))
        if tmp := self.get_experimental(): csv_meta.append(("experimental",tmp))
        if tmp := self.get_date(): csv_meta.append(("date",tmp))
        if tmp := self.get_publisher(): csv_meta.append(("publisher",tmp))
        if tmp := self.get_contact():
            for oneContact in tmp:
                csv_meta.append(("contact", str(oneContact)))
        if tmp := self.get_usecontext():
            for oneUseContext in tmp:
                csv_meta.append(("useContext",oneUseContext))
        if tmp := self.get_jurisdiction():
            for oneJurisdiction in tmp:
                csv_meta.append(("jurisdiction",oneJurisdiction))
        if tmp := self.get_purpose(): csv_meta.append(("purpose",tmp))
        if tmp := self.get_copyright(): csv_meta.append(("copyright",tmp))
        if tmp := self.get_immutable(): csv_meta.append(("immutable",tmp))
        if tmp := self.get_lockeddate(): csv_meta.append(("lockedDate",tmp))
        if tmp := self.get_inactive(): csv_meta.append(("inactive",tmp))
        if tmp := self.get_casesensitive(): csv_meta.append(("caseSensitive",tmp))
        if tmp := self.get_valueset(): csv_meta.append(("valueSet",tmp))
        if tmp := self.get_hierarchymeaning(): csv_meta.append(("hierarchyMeaning",tmp.value))
        if tmp := self.get_compositional(): csv_meta.append(("compositional",tmp))
        if tmp := self.get_versionneeded(): csv_meta.append(("versionNeeded",tmp))
        if tmp := self.get_supplements(): csv_meta.append(("supplements",tmp))
        if tmp := self.get_count(): csv_meta.append(("count",tmp))
        if tmp := self.get_filter():
            for oneFilter in tmp:
                csv_meta.append(("filter",oneFilter.code+"|"+oneFilter.description+"|"+oneFilter.operator+"|"+oneFilter.value))
        if tmp := self.get_property():
            for oneProperty in tmp:
                csv_meta.append(("property",str(oneProperty)))
        # end list of metaelements

        csv_header = []
        csv_list = []
        conceptList = self.get_concept()

        # check if there are multiple concepts with the same code and system, so that parentingByConceptOrder is used
        # OR is the conceptOrder explicitly in use
        if self.get_resource() == 'ValueSet':
            if len(conceptList) > len(self.buildConceptDictWithAttr('code', 'system')) or next((concept for concept in conceptList if concept.has_extension(ext.ConceptOrder.extension_canonical)), False):
                self.parenting_by = ParentingBy.conceptOrder
            else:
                self.parenting_by = ParentingBy.parentAndSystem

        for oneConcept in conceptList:
            csv_line = []
            
            # Common initialization for CodeSystems and ValueSets
            headerIterator = 0
            headerDesignationIterator = 0
            headerExtensionIterator = 0
            
            # Common designation logic for both resource types
            if file_style is FileStyle.propCSV:
                easy_designations = []
                other_designations = oneConcept.designation
            elif file_style is FileStyle.spreadCT:
                easy_designations = [oneDesig for oneDesig in oneConcept.designation 
                                    if oneDesig.use.codesystem == 
                                    "https://termgit.elga.gv.at/CodeSystem/austrian-designation-use"]
                other_designations = [oneDesig for oneDesig in oneConcept.designation 
                                    if oneDesig.use.codesystem != 
                                    "https://termgit.elga.gv.at/CodeSystem/austrian-designation-use"]
            
            # for CodeSystems
            if self.get_resource() == 'CodeSystem':
                # adding values to already existing columns, if value empty then an empty string is added
                headerPropertyIterator = 0
                
                if file_style is FileStyle.propCSV:
                    easy_properties = []
                    other_properties = oneConcept.property
                elif file_style is FileStyle.spreadCT:
                    easy_properties = oneConcept.property
                    other_properties = []

                for csv_header_element in csv_header:

                    if csv_header_element == "designation":
                        if headerDesignationIterator < len(other_designations):
                            csv_line.append(other_designations[headerDesignationIterator])
                        else:
                            csv_line.append('')
                        headerDesignationIterator += 1

                    elif csv_header_element == "extension":
                        if headerExtensionIterator < len(oneConcept.extension):
                            csv_line.append(oneConcept.extension[headerExtensionIterator])
                        else:
                            csv_line.append('')
                        headerExtensionIterator += 1

                    elif csv_header_element == "property":
                        if headerPropertyIterator < len(other_properties):
                            csv_line.append(other_properties[headerPropertyIterator])
                        else:
                            csv_line.append('')
                        headerPropertyIterator += 1

                    elif hasattr(oneConcept, csv_header_element) and (tmp := getattr(oneConcept,csv_header_element)):
                        csv_line.append(tmp)
                    
                    elif easy_designations and (fitting_easy_desigs := [oneDesig for oneDesig in easy_designations if oneDesig.use.code == csv_header_element]):
                        header_easy_desig_iteratior = csv_header[:headerIterator].count(csv_header_element)
                        if header_easy_desig_iteratior < len(fitting_easy_desigs) and (tmp := fitting_easy_desigs[header_easy_desig_iteratior]):
                            csv_line.append(tmp.value)
                        else:
                            csv_line.append('')

                    elif easy_properties and (fitting_easy_props := [oneProp for oneProp in easy_properties if oneProp.code == csv_header_element]):
                        header_easy_prop_iteratior = csv_header[:headerIterator].count(csv_header_element)
                        if header_easy_prop_iteratior < len(fitting_easy_props) and (tmp := fitting_easy_props[header_easy_prop_iteratior]):
                            csv_line.append(tmp.value)
                        else:
                            csv_line.append('')

                    else:
                        csv_line.append('')

                    headerIterator += 1

                # adding not existing columns because we just got some values
                if 'code' not in csv_header and (tmp := oneConcept.code):
                    csv_header.append('code')
                    csv_line.append(tmp)
                if 'display' not in csv_header and (tmp := oneConcept.display):
                    csv_header.append('display')
                    csv_line.append(tmp)
                if 'definition' not in csv_header and (tmp := oneConcept.definition):
                    csv_header.append('definition')
                    csv_line.append(tmp)
                while other_designations and headerDesignationIterator < len(other_designations):
                    csv_header.append('designation')
                    csv_line.append(other_designations[headerDesignationIterator])
                    headerDesignationIterator += 1
                while (conceptExtension := oneConcept.extension) and headerExtensionIterator < len(conceptExtension):
                    csv_header.append('extension')
                    csv_line.append(conceptExtension[headerExtensionIterator])
                    headerExtensionIterator += 1
                while other_properties and headerPropertyIterator < len(other_properties):
                    csv_header.append('property')
                    csv_line.append(other_properties[headerPropertyIterator])
                    headerPropertyIterator += 1
                
                for one_easy_design in easy_designations:
                    while csv_header.count(one_easy_design.use.code) < len(fitting_easy_desigs := [one_desig for one_desig in easy_designations if one_desig.use.code == one_easy_design.use.code]):
                        csv_line.append(fitting_easy_desigs[csv_header.count(one_easy_design.use.code)].value)
                        csv_header.append(one_easy_design.use.code) 
                        
                for one_easy_prop in easy_properties:
                    while csv_header.count(one_easy_prop.code) < len(fitting_easy_props := [one_prop for one_prop in easy_properties if one_prop.code == one_easy_prop.code]):
                        csv_line.append(fitting_easy_props[csv_header.count(one_easy_prop.code)].value)
                        csv_header.append(one_easy_prop.code)

            # for ValueSets
            elif self.get_resource() == 'ValueSet':
                # adding values to already existing columns, if value empty then an empty string is added
                headerFilterIterator = 0
                
                for csv_header_element in csv_header:

                    if csv_header_element == "designation":
                        if headerDesignationIterator < len(other_designations):
                            csv_line.append(other_designations[headerDesignationIterator])
                        else:
                            csv_line.append('')
                        headerDesignationIterator += 1

                    elif csv_header_element == "filter":
                        if headerFilterIterator < len(oneConcept.filter):
                            csv_line.append(oneConcept.filter[headerFilterIterator])
                        else:
                            csv_line.append('')
                        headerFilterIterator += 1

                    elif csv_header_element == "extension":
                        extension_found = False
                        while (conceptExtension := oneConcept.extension) and headerExtensionIterator < len(conceptExtension) and not extension_found:
                            # skip conceptOrder if in extensions
                            if not conceptExtension[headerExtensionIterator].url == ext.ConceptOrder.extension_canonical:
                                csv_line.append(conceptExtension[headerExtensionIterator])
                                extension_found = True
                            headerExtensionIterator += 1

                        if not extension_found:
                            csv_line.append('')

                    elif self.parenting_by == ParentingBy.conceptOrder and csv_header_element == 'conceptOrder' and (tmp := oneConcept):
                        for one_ext in tmp.extension:
                            if one_ext.url == ext.ConceptOrder.extension_canonical:
                                if one_ext.value:
                                    csv_line.append(one_ext.value)
                                break
                        else:
                            # Use index of current concept when generating conceptOrder from scratch.
                            # Add +1 in order to prevent conceptOrder of value '0' as this will be interpreted as 'False' in if-statements
                            csv_line.append(conceptList.index(oneConcept) + 1)
                    elif self.parenting_by == ParentingBy.conceptOrder and csv_header_element == 'parentByConceptOrder' and (tmp := oneConcept.parent):
                        for one_ext in tmp.extension:
                            if one_ext.url == ext.ConceptOrder.extension_canonical:
                                if one_ext.value:
                                    csv_line.append(one_ext.value)
                                    break
                                else:
                                    # if parentByConceptOrder is used and the parent concept has got the extension a proper value is required
                                    import sys
                                    sys.exit('If parentByConceptOrder is used and the parent concept uses the extension a proper value is required. See concept with code: ' + tmp.code)
                        else:
                            # Use index of current concept when generating conceptOrder from scratch.
                            # Add +1 in order to prevent conceptOrder of value '0' as this will be interpreted as 'False' in if-statements
                            csv_line.append(conceptList.index(tmp) + 1)
                    elif self.parenting_by == ParentingBy.parentAndSystem and csv_header_element == 'parent' and (tmp := oneConcept.parent):
                        if tmp.code:
                            csv_line.append(tmp.code)
                        else:
                            csv_line.append('')
                    elif self.parenting_by == ParentingBy.parentAndSystem and csv_header_element == 'parentSystem' and (tmp := oneConcept.parent):
                        if tmp.system:
                            csv_line.append(tmp.system)
                        else:
                            csv_line.append('')

                    elif csv_header_element == 'version':
                        # write the system version if existent
                        if  tmp := oneConcept.version:
                            csv_line.append(tmp)
                        else:
                            # retrieve version from metadata

                            # theoretically one_concept.system could be either canonical or OID in
                            # most cases, however, it would be the canonical
                            if tmp := self.gainVersionFromCanonical(oneConcept.system):
                                csv_line.append(tmp)
                            elif tmp := self.gainVersionFromOid(oneConcept.system):
                                csv_line.append(tmp)
                            else: # in case no version for the codesystem is available
                                csv_line.append('')

                    elif hasattr(oneConcept, csv_header_element) and (tmp := getattr(oneConcept,csv_header_element)):
                        csv_line.append(tmp)
                    
                    elif easy_designations and (fitting_easy_desigs := [oneDesig for oneDesig in easy_designations if oneDesig.use.code == csv_header_element]):
                        header_easy_desig_iteratior = csv_header[:headerIterator].count(csv_header_element)
                        if header_easy_desig_iteratior < len(fitting_easy_desigs) and (tmp := fitting_easy_desigs[header_easy_desig_iteratior]):
                            csv_line.append(tmp.value)
                        else:
                            csv_line.append('')
                    
                    else:
                        csv_line.append('')
                    
                    headerIterator += 1

                # adding not existing columns because we just got some values
                if 'system' not in csv_header and (tmp := oneConcept.system):
                    csv_header.append('system')
                    csv_line.append(tmp)
                if 'version' not in csv_header:
                    # create 'version' header in any case
                    csv_header.append('version')
                    # write the system version if existent
                    if  tmp := oneConcept.version:
                        csv_line.append(tmp)
                    else:
                        # retrieve version from metadata

                        # theoretically one_concept.system could be either canonical or OID in
                        # most cases, however, it would be the canonical
                        if tmp := self.gainVersionFromCanonical(oneConcept.system):
                            csv_line.append(tmp)
                        elif tmp := self.gainVersionFromOid(oneConcept.system):
                            csv_line.append(tmp)
                        else: # in case no version for the codesystem is available
                            csv_line.append('')
                if 'code' not in csv_header and (tmp := oneConcept.code):
                    csv_header.append('code')
                    csv_line.append(tmp)
                if 'display' not in csv_header and (tmp := oneConcept.display):
                    csv_header.append('display')
                    csv_line.append(tmp)
                while other_designations and headerDesignationIterator < len(other_designations):
                    csv_header.append('designation')
                    csv_line.append(other_designations[headerDesignationIterator])
                    headerDesignationIterator += 1

                if self.parenting_by == ParentingBy.conceptOrder and 'conceptOrder' not in csv_header and oneConcept:
                    csv_header.append('conceptOrder')
                    for one_ext in oneConcept.extension:
                        if one_ext.url == ext.ConceptOrder.extension_canonical:
                            if one_ext.value:
                                csv_line.append(one_ext.value)
                            break
                    else:
                        # Use index of current concept when generating conceptOrder from scratch.
                        # Add +1 in order to prevent conceptOrder of value '0' as this will be interpreted as 'False' in if-statements
                        csv_line.append(conceptList.index(oneConcept) + 1)
                if self.parenting_by == ParentingBy.conceptOrder and 'parentByConceptOrder' not in csv_header and (tmp := oneConcept.parent):
                    csv_header.append('parentByConceptOrder')
                    for one_ext in tmp.extension:
                        if one_ext.url == ext.ConceptOrder.extension_canonical:
                            if one_ext.value:
                                csv_line.append(one_ext.value)
                                break
                            else:
                                # if parentByConceptOrder is used and the parent concept has got the extension a proper value is required
                                import sys
                                sys.exit('If parentByConceptOrder is used and the parent concept uses the extension a proper value is required. See concept with code: ' + tmp.code)
                    else:
                        # Use index of current concept when generating conceptOrder from scratch.
                        # Add +1 in order to prevent conceptOrder of value '0' as this will be interpreted as 'False' in if-statements
                        csv_line.append(conceptList.index(tmp) + 1)
                if self.parenting_by == ParentingBy.parentAndSystem and 'parent' not in csv_header and (tmp := oneConcept.parent):
                    csv_header.append('parent')
                    if tmp.code:
                        csv_line.append(tmp.code)
                    else:
                        csv_line.append('')
                if self.parenting_by == ParentingBy.parentAndSystem and 'parentSystem' not in csv_header and (tmp := oneConcept.parent):
                    csv_header.append('parentSystem')
                    if tmp.system:
                        csv_line.append(tmp.system)
                    else:
                        csv_line.append('')

                while (conceptFilter := oneConcept.filter) and headerFilterIterator < len(conceptFilter):
                    csv_header.append('filter')
                    csv_line.append(conceptFilter[headerFilterIterator])
                    headerFilterIterator += 1
                while (conceptExtension := oneConcept.extension) and headerExtensionIterator < len(conceptExtension):
                    # skip conceptOrder if in extensions and parentingByConceptOrder is actived, because of possible redundancy
                    if not conceptExtension[headerExtensionIterator].url == ext.ConceptOrder.extension_canonical:
                        csv_header.append('extension')
                        csv_line.append(conceptExtension[headerExtensionIterator])
                    headerExtensionIterator += 1
                
                # Common easy_designations completion for ValueSets
                for one_easy_design in easy_designations:
                    while csv_header.count(one_easy_design.use.code) < len(fitting_easy_desigs := [one_desig for one_desig in easy_designations if one_desig.use.code == one_easy_design.use.code]):
                        csv_line.append(fitting_easy_desigs[csv_header.count(one_easy_design.use.code)].value)
                        csv_header.append(one_easy_design.use.code)
                
                if 'abstract' not in csv_header and (tmp := oneConcept.abstract):
                    csv_header.append('abstract')
                    csv_line.append(tmp)
                if 'inactive' not in csv_header and (tmp := oneConcept.inactive):
                    csv_header.append('inactive')
                    csv_line.append(tmp)
                if 'exclude' not in csv_header and (tmp := oneConcept.exclude):
                    csv_header.append('exclude')
                    csv_line.append(tmp)

            csv_list.append(csv_line)

        csv_list.insert(0,csv_header)

        if outfile.name.endswith('.csv'):
            # special encoding because of Excel compatibility, see https://stackoverflow.com/questions/6588068/which-encoding-opens-csv-files-correctly-with-excel-on-both-mac-and-windows
            try:
                writeCSV(outfile, csv_meta, csv_list, file_style=file_style)
            except UnicodeEncodeError:
                print(" (because of some EncodeError, this terminologys *.1.propcsv.csv will be written in utf-8 instead of cp1252)")
                writeCSV(outfile, csv_meta, csv_list, encoding="utf-8")

        elif outfile.name.endswith('.xlsx'):
            writeXLSX(outfile, csv_meta, csv_list, file_style=file_style)

def writeCSV(outfile, csv_meta, csv_list, encoding="cp1252", file_style=FileStyle.propCSV):
    outfile_path = outfile.name
    if file_style is FileStyle.spreadCT:
        outfile_path = outfile_path.replace(".data.1.spreadct.csv", ".meta.1.spreadct.csv")
        encoding = "utf-8"

    with open(outfile_path, 'wb') as outfile:
        first_line_of_file = True

        if file_style is FileStyle.propCSV:
            csv_meta = list(zip(*csv_meta)) #transpose the list
        for csvline in csv_meta:
            first_line_of_file = write_csv_line(outfile, encoding, first_line_of_file, csvline)

        if file_style is FileStyle.propCSV:
            outfile.write(("\n").encode(encoding))
        elif file_style is FileStyle.spreadCT:
            outfile.close() # closing and opening with the same name, so that the with is still active, see https://www.geeksforgeeks.org/with-statement-in-python/
            outfile = open(outfile_path.replace(".meta.1.spreadct.csv",".data.1.spreadct.csv"), 'wb')
            first_line_of_file = True
        for csvline in csv_list:
            first_line_of_file = write_csv_line(outfile, encoding, first_line_of_file, csvline)

def write_csv_line(outfile, encoding, first_line_of_file, csvline):
    if first_line_of_file:
        first_line_of_file = False
    else:
        outfile.write(("\n").encode(encoding))
    newline = True
    for csvelement in csvline:
        outfile.write(((";" if not newline else "") + "\"" + str(csvelement).replace("\"",'""') + "\"").encode(encoding))
        newline = False
    return first_line_of_file

def writeXLSX(outfile, csv_meta, csv_list, file_style=FileStyle.propCSV):
    import xlsxwriter
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(outfile.name)
    if file_style is FileStyle.propCSV:
        worksheet = workbook.add_worksheet()
        csv_meta = list(zip(*csv_meta))
    elif file_style is FileStyle.spreadCT:
        worksheet_data = workbook.add_worksheet(name="data")
        worksheet_meta = workbook.add_worksheet(name="meta")
        worksheet = worksheet_meta

    # fill with meta
    x = -1
    for csvline in csv_meta: #transpose the list
        x += 1
        y = -1
        for csvelement in csvline:
            y += 1
            """
            based on https://stackoverflow.com/questions/71574319/how-to-remove-newline-characters-so-it-doesnt-produce-x000d-when-reading-exce
            all ocurrences of \r\n will be replaced with a single \n in order to guarantee that reading from xlsx does not produce _x000D_ instead
            of \r
            """
            worksheet.write_string(x,y,str(csvelement).replace('\r\n', '\n'))#.encode(encoding).decode(encoding))

    # for the empty row between meta and data
    x += 1

    if file_style is FileStyle.spreadCT:
        worksheet = worksheet_data
        x = -1 #start from first row

    # fill with data
    for csvline in csv_list:
        x += 1
        y = -1
        for csvelement in csvline:
            y += 1
            """
            based on https://stackoverflow.com/questions/71574319/how-to-remove-newline-characters-so-it-doesnt-produce-x000d-when-reading-exce
            all ocurrences of \r\n will be replaced with a single \n in order to guarantee that reading from xlsx does not produce _x000D_ instead
            of \r
            """
            worksheet.write_string(x,y,str(csvelement).replace('\r\n', '\n'))#.encode(encoding).decode(encoding))

    workbook.close()

class PropCsvAsXLSX():
    def parse(inFilename):
        import pandas as pd

        read_file = pd.read_excel(inFilename, keep_default_na=False, header=None, names=None)
        try:
            read_file.to_csv(inFilename.replace('.1.propcsv.xlsx', '.1.propcsv.csv'), index = None, header=False, sep=';', quoting=1, quotechar='"', encoding='cp1252')
            return PropCsvAndMaster(inFilename.replace('.1.propcsv.xlsx', '.1.propcsv.csv'))
        except UnicodeEncodeError:
            read_file.to_csv(inFilename.replace('.1.propcsv.xlsx', '.1.propcsv.csv'), index = None, header=False, sep=';', quoting=1, quotechar='"', encoding='utf-8')
            return PropCsvAndMaster(inFilename.replace('.1.propcsv.xlsx', '.1.propcsv.csv'), encoding='utf-8')

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        PropCsvAndMaster.exporto(self, outfile, outputClass, argsLang, incHierarchyExt4VS)

class SpreadCT(PropCsvAndMaster):
    def parse(inFilename):
        return PropCsvAndMaster(inFilename, encoding='utf-8', file_style=FileStyle.spreadCT)

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        PropCsvAndMaster.exporto(self, outfile, outputClass, argsLang, incHierarchyExt4VS, file_style=FileStyle.spreadCT)

class SpreadCTasXLSX():
    def parse(inFilename):
        import pandas as pd

        read_meta = pd.read_excel(inFilename, keep_default_na=False, sheet_name="meta", header=None, names=None)
        read_data = pd.read_excel(inFilename, keep_default_na=False, sheet_name="data", header=None, names=None)

        read_meta.to_csv(inFilename.replace('.1.spreadct.xlsx', '.meta.1.spreadct.csv'), index = None, header=False, sep=';', quoting=1, quotechar='"', encoding='utf-8')
        read_data.to_csv(inFilename.replace('.1.spreadct.xlsx', '.data.1.spreadct.csv'), index = None, header=False, sep=';', quoting=1, quotechar='"', encoding='utf-8')
        ret = SpreadCT.parse(inFilename.replace('.1.spreadct.xlsx', '.data.1.spreadct.csv'))
        # management decision: no spreadct csvs
        import os
        os.remove(inFilename.replace('.1.spreadct.xlsx', '.data.1.spreadct.csv'))
        os.remove(inFilename.replace('.1.spreadct.xlsx', '.meta.1.spreadct.csv'))
        return ret

    def exporto(self, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        SpreadCT.exporto(self, outfile, outputClass, argsLang, incHierarchyExt4VS)

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

class ExtensionType(enum.Enum):
    oid = "oid"
    coding = "Coding"
    integer = "integer"
    # TODO more to be defined

class ContactDetail():
    def __init__(self, name=None, telecom=None):
        self.name = name
        # see https://stackoverflow.com/questions/73714169/why-are-there-two-elements-in-the-collection
        #     https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
        #     https://web.archive.org/web/20200221224620id_/http://effbot.org/zone/default-values.htm
        #     https://docs.python.org/3/reference/compound_stmts.html#function-definitions
        if telecom is None:
            telecom = []
        self.telecom = telecom

    @classmethod
    def from_string(cls, str):
        # str is None or empty return None
        if not str:
            return None

        telecom_list = []

        splitted_contact = str.split('|',2)
        name = splitted_contact[0]

        splitted_telecom = splitted_contact[1].split('~')
        for telecom in splitted_telecom:
            if telecom:
                telecom_list.append(cls.ContactPoint.from_string(telecom))

        return cls(name, telecom_list)

    def __str__(self) -> str:
        tmp_str = ""
        if temp := self.name:
            tmp_str += temp
        tmp_str += "|"
        telecom_list = []
        for telecom in self.telecom:
            telecom_list.append(str(telecom))
        tmp_str += "~".join(telecom_list)
        return tmp_str

    class ContactPoint():
        def __init__(self, system=None, value=None, use=None, rank=None, period_start=None, period_end=None):
            self.system = system # ContactPointSystem
            self.value = value
            self.use = use # ContactPointUse
            self.rank = rank
            self.period_start = period_start
            self.period_end = period_end

        @classmethod
        def from_string(cls, str):
            splitted_contact_point = str.split('^',6)
            return cls(cls.ContactPointSystem(splitted_contact_point[0]) if splitted_contact_point[0] else None, splitted_contact_point[1], cls.ContactPointUse(splitted_contact_point[2]) if splitted_contact_point[2] else None, splitted_contact_point[3], splitted_contact_point[4], splitted_contact_point[5])

        def __str__(self) -> str:
            tmp_str = ""
            if tmp := self.system:
                tmp_str += tmp.value
            tmp_str += "^"
            if tmp := self.value:
                tmp_str += tmp
            tmp_str += "^"
            if tmp := self.use:
                tmp_str += tmp.value
            tmp_str += "^"
            if tmp := self.rank:
                tmp_str += tmp
            tmp_str += "^"
            if tmp := self.period_start:
                tmp_str += tmp
            tmp_str += "^"
            if tmp := self.period_end:
                tmp_str += tmp
            return tmp_str

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
        self.extension = []

    class ConceptProperty():
        def __init__(self, str=None):
            if not str:
                self.code = None
                self.value = None
                self.type = PropertyCodeType
            else:
                propertyElements = str.split('|')
                self.code = propertyElements[0]
                self.type = PropertyCodeType[propertyElements[2].lower()]
                if self.type == PropertyCodeType.coding:
                    self.value = Coding(propertyElements[1])
                else:
                    self.value = propertyElements[1]

        # only used for sort
        @trim_output
        def get_value_if_code_is_child(self):
            if self.code == "child":
                return str(self.value)
            else:
                return str(0)

        # only used for sort
        @trim_output
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
        self.parent = None
        self.member = [] # simple hirarchie that stores all children, needs a extension
        self.level = 0 # Additional information in what level the concept can be found.
                       # The default value implies that this concept is a top level concept.
                       # For concepts in hierarchies this value would have to be set explicitly.
        self.abstract = False
        self.inactive = False
        self.extension = []

    # created only for sorting, shouldn't be used for anything else
    @trim_output
    def get_system(self):
        return self.system

    # created only for sorting, shouldn't be used for anything else
    @trim_output
    def get_code(self):
        return self.code

    # created only for sorting, shouldn't be used for anything else
    @trim_output
    def get_value_of_conceptOrder(self):
        for one_ext in self.extension:
            if one_ext.url == ext.ConceptOrder.extension_canonical:
                return one_ext.value
        else: return 0

    def has_extension(self, extension_canonical):
        return True if next((extension_item for extension_item in self.extension if extension_item.url == extension_canonical), False) else False

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
        if not str:
            self.codesystem = None
            self.version = None
            self.code = None
            self.display = None
            self.userSelected = None
        else:
            splittedValue = str.split('^',4)
            self.codesystem = splittedValue[0] or None
            self.version = splittedValue[1] or None
            self.code = splittedValue[2] or None
            self.display = splittedValue[3] or None
            self.userSelected = splittedValue[4] or None

    def __str__(self) -> str:
        buildStr = ""
        if self.codesystem: buildStr += self.codesystem
        buildStr += "^"
        if self.version: buildStr += self.version
        buildStr += "^"
        if self.code: buildStr += self.code
        buildStr += "^"
        if self.display: buildStr += self.display
        buildStr += "^"
        if self.userSelected: buildStr += str(self.userSelected)
        return buildStr

class Extension():
    def __init__(self, str=None):
        if not str:
            self.url = None
            self.value = None
            self.type = ExtensionType
        else:
            extension_elements = str.split('|')
            self.url = extension_elements[0]
            self.type = ExtensionType(extension_elements[2])
            if self.type == ExtensionType.coding:
                self.value = Coding(extension_elements[1])
            elif self.type == ExtensionType.integer:
                self.value = int(extension_elements[1])
            else:
                self.value = extension_elements[1]

    def __str__(self) -> str:
        return self.url + "|" + (str(self.value) if self.value else "") + "|" + self.type.value

# upper case first character: https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
first_char_to_upper = lambda s: s[:1].upper() + s[1:] if s else ''
# lower case first character: https://stackoverflow.com/questions/3840843/how-to-downcase-the-first-character-of-a-string
first_char_to_lower = lambda s: s[:1].lower() + s[1:] if s else ''
