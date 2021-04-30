from os import write
import csv
import enum

class PropCsvAndMaster(object):
    def __init__(self):
        super(PropCsvAndMaster, self).__init__()
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
        self.immutable = None
        self.lockeddate = None
        self.inactive = None
        self.casesensitive = None
        self.valueset = None
        self.hierarchymeaning = HierarchyMeaning
        self.compositional = None
        self.versionneeded = None
        self.supplements = None
        self.count = None
        self.filter = []
        self.property = []

    def __init__(self, inFile):
        super(PropCsvAndMaster, self).__init__()
        # open the file in read mode
        with open(inFile, 'r') as csvfile:
            # creating dictreader object
            file = csv.reader(csvfile)
            # iterating over each row and append values to empty list
            metaList = [file.__next__()]+[file.__next__()]
            # close file and return obj
            csvfile.close()

            # lists have to get initialized
            self.identifier = []
            self.contact = []
            self.usecontext = []
            self.jurisdiction = []
            self.filter = []
            self.property = []

            i = -1
            for metaObj in metaList[0]:
                i += 1
                if 'resource' == metaObj: #todo
                    self.resource = Resource
                    self.resource.name = metaList[1][i]
                if 'url' == metaObj: self.url = metaList[1][i]
                if 'version' == metaObj: self.version = metaList[1][i]
                if 'name' == metaObj: self.name = metaList[1][i]
                if 'title' == metaObj: self.title = metaList[1][i]
                if 'status' == metaObj: self.status = metaList[1][i]
                if 'description' == metaObj: self.description = metaList[1][i]
                if 'content' == metaObj: self.content = metaList[1][i]
                if 'implicitRules' == metaObj: self.implicitrules = metaList[1][i]
                if 'language' == metaObj: self.language = metaList[1][i]
                if 'text' == metaObj: self.text = metaList[1][i]
                if 'contained' == metaObj: self.contained = metaList[1][i]
                if 'extension' == metaObj: self.extension = metaList[1][i]
                if 'modifierExtension' == metaObj: self.modifierextension = metaList[1][i]
                if 'identifier' == metaObj: self.identifier.append(metaList[1][i])
                if 'experimental' == metaObj: self.experimental = metaList[1][i]
                if 'publisher' == metaObj: self.publisher = metaList[1][i]
                if 'contact' == metaObj: self.contact.append(metaList[1][i])
                if 'useContext' == metaObj: self.usecontext.append(metaList[1][i])
                if 'jurisdiction' == metaObj: self.jurisdiction.append(metaList[1][i])
                if 'purpose' == metaObj: self.purpose = metaList[1][i]
                if 'copyright' == metaObj: self.copyright = metaList[1][i]
                if 'immutable' == metaObj: self.immutable = cmetaList[1][i]
                if 'lockedDate' == metaObj: self.lockeddate = metaList[1][i]
                if 'caseSensitive' == metaObj: self.casesensitive = metaList[1][i]
                if 'valueSet' == metaObj: self.valueset = metaList[1][i]
                if 'hierarchyMeaning' == metaObj: self.hierarchymeaning = metaList[1][i]
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
                    tempProperty.type = propElements[3]
                    self.property.append(tempProperty)

    def get_resource(self):
        return self.resource.name

    def get_url(self):
        return self.url

    def get_version(self):
        return self.version

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def get_status(self):
        return self.status

    def get_description(self):
        return self.description

    def get_content(self):
        if self.content == Content.notpresent:
            return "not-present"
        return self.content

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
        if self.hierarchymeaning == groupedby:
            return "grouped-by"
        if self.hierarchymeaning == isa:
            return "is-a"
        if self.hierarchymeaning == partof:
            return "part-of"
        if self.hierarchymeaning == classifiedwith:
            return "classified-with"
        return self.hierarchymeaning

    def get_compositional(self):
        return self.compositional

    def get_versionneeded(self):
        return self.versionneeded

    def get_supplements(self):
        return self.supplements

    def get_count(self):
        return self.count

    def get_filter(self):
        return self.filter

    def get_property(self):
        return self.property

    def exporto(self, outfile):
        csv_list = []
        # start list of metaelements
        csv_list.append(("resource",self.get_resource()))#todo
        csv_list.append(("url",self.get_url()))
        csv_list.append(("version",self.get_version()))
        csv_list.append(("name",self.get_name()))
        csv_list.append(("title",self.get_title()))
        csv_list.append(("status",self.get_status()))
        csv_list.append(("description",self.get_description()))
        
        if self.resource == Resource.CodeSystem: csv_list.append(("content",self.get_content()))
        
        if hasattr(self,'implicitrules'): csv_list.append(("implicitRules",self.get_implicitrules()))
        if hasattr(self,'language'): csv_list.append(("language",self.get_language()))
        if hasattr(self,'text'): csv_list.append(("text",self.get_text()))
        if hasattr(self,'contained'): csv_list.append(("contained",self.get_contained()))
        if hasattr(self,'extension'): csv_list.append(("extension",self.get_extension()))
        if hasattr(self,'modifierextension'): csv_list.append(("modifierExtension",self.get_modifierextension()))
        if hasattr(self,'identifier'): 
            for oneIdentifier in self.get_identifier():
                csv_list.append(("identifier",oneIdentifier))
        if hasattr(self,'experimental'): csv_list.append(("experimental",self.get_experimental()))
        if hasattr(self,'date'): csv_list.append(("date",self.get_date()))
        if hasattr(self,'publisher'): csv_list.append(("publisher",self.get_publisher()))
        if hasattr(self,'contact'): 
            for oneContact in self.get_contact():
                csv_list.append(("contact",oneContact))
        if hasattr(self,'usecontext'): 
            for oneUseContext in self.get_usecontext():
                csv_list.append(("useContext",oneUseContext))
        if hasattr(self,'jurisdiction'): 
            for oneJurisdiction in self.get_jurisdiction():
                csv_list.append(("jurisdiction",oneJurisdiction))
        if hasattr(self,'purpose'): csv_list.append(("purpose",self.get_purpose()))
        if hasattr(self,'copyright'): csv_list.append(("copyright",self.get_copyright()))
        if hasattr(self,'immutable'): csv_list.append(("immutable",self.get_immutable()))
        if hasattr(self,'lockeddate'): csv_list.append(("lockedDate",self.get_lockeddate()))
        if hasattr(self,'inactive'): csv_list.append(("inactive",self.get_inactive()))
        if hasattr(self,'casesensitive'): csv_list.append(("caseSensitive",self.get_casesensitive()))
        if hasattr(self,'valueset'): csv_list.append(("valueSet",self.get_valueset()))
        if hasattr(self,'hierarchymeaning'): csv_list.append(("hierarchyMeaning",self.get_hierarchymeaning()))
        if hasattr(self,'compositional'): csv_list.append(("compositional",self.get_compositional()))
        if hasattr(self,'versionneeded'): csv_list.append(("versionNeeded",self.get_versionneeded()))
        if hasattr(self,'supplements'): csv_list.append(("supplements",self.get_supplements()))
        if hasattr(self,'count'): csv_list.append(("count",self.get_count()))
        if hasattr(self,'filter'): 
            for oneFilter in self.get_filter():
                csv_list.append(("filter",onefilter.code+"|"+onefilter.description+"|"+onefilter.operator+"|"+onefilter.value))
        if hasattr(self,'property'): 
            for oneProperty in self.get_property():
                csv_list.append(("property",oneProperty.code+"|"+oneProperty.uri+"|"+oneProperty.description+"|"+oneProperty.type))
        # end list of metaelements
        for csvline in zip(*csv_list): #transpose the list
            newline = True
            for csvelement in csvline:
                outfile.write(("," if not newline else "") + csvelement)
                newline = False
            outfile.write("\n")
        outfile.close()

class Resource(enum.Enum):
    ValueSet = 1
    CodeSystem = 2

class Status(enum.Enum):
    draft = 1
    active = 2
    retired = 3
    unknown = 4

class Content(enum.Enum):
    notpresent = 1
    example = 2
    fragment = 3
    complete = 4
    supplement = 5

class HierarchyMeaning(enum.Enum):
    groupedby = 1
    isa = 2
    partof = 3
    classifiedwith = 4

class Filter():
    def __init__(self):
        self.code = None
        self.description = None
        self.operator = None
        self.value = None

class Property():
    def __init__(self):
        self.code = None
        self.uri = None
        self.description = None
        self.type = None

def parse(inFilename):
    return PropCsvAndMaster(inFilename)