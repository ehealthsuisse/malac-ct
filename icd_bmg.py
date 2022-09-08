import prop_csv_and_master as pcam
import pyodbc
import math
import argparse
# #python 64 bit
# #python environment and Acces ODBC need the same bit rate either 64 - 64 or 32 - 32
# #usefull links for adjusting your Microsoft Access Driver:
# #find bit rate of your python https://stackoverflow.com/questions/32662123/pyodbc-error-data-source-name-not-found-and-no-default-driver-specified-paradox
# #How to connect to Microsoft Access with ODBC from Windows 10 https://help.interfaceware.com/v6/connect-to-microsoft-access-odbc

class ICDBMG(pcam.PropCsvAndMaster):
    def __init__(self, inFile):
        super().__init__()
        # jointabelle between "DIAGLIST", "DIAGLIST- 3 STELLER", "DIAGLIST - UNTERKAPITEL", "DIAGLIST-KAPITEL"
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + inFile + ';')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT [D].Diagnose AS [DDiagnose], [D].Kennzeichen AS [DKennzeichen],[D].Gruppe AS [DGruppe], [D].HD_Gruppe AS [DHDGruppe], [D].ZD_Gruppe AS [DZDGruppe], [D].Geschlecht AS [DGeschlecht], [D].Mindestalter AS [DMindestalter], [D].Höchstalter AS [DHöchstalter], [D].Unwahrscheinlich AS [DUnwahrscheinlich], [D].HD_ambulant AS [DHDambulant], [D].[HD_>0_Tage] AS [DHDZTage], [D].Bezeichnung AS [DBezeichnung],[D].Meldepflicht AS [DMeldepflicht], [D].Stationär_erworben AS [DStationärerworben],[D].Kurzbezeichnung AS [DKurzbezeichnung],[D3S].Diagnose AS [D3SDiagnose], [DUK].Unterkapitel AS [DUKUnterkapitel], [DUK].Beschreibung AS [DUKBeschreibung], [DK].Beschreibung AS [DKBeschreibung], [DK].Kapitel AS [DKKapitel]"
            "FROM [DIAGLIST] AS [D], [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
            "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
            "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
            "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")

        # cursor.execute(
        #     "SELECT [D].*,[D3S].Diagnose AS [D3SDiagnose], [DUK].Unterkapitel AS [DUKUnterkapitel], [DUK].Beschreibung AS [DUKBeschreibung], [DK].Beschreibung AS [DKBeschreibung], [DK].Kapitel AS [DKKapitel]"
        #     "FROM [DIAGLIST] AS [D], [DIAGLIST - 3 STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
        #     "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
        #     "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
        #     "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")

        self.url = "https://termgit.elga.gv.at/CodeSystem-icd-10-bmg-2022"
        self.name = "icd-10-bmg-2022"
        self.title = "ICD-10 BMG 2022"
        self.status = "draft"
        self.content = "complete"
        self.version = "Version 2022"
        self.count = "13166"
        self.resource = pcam.Resource.CodeSystem.value
        print(self.name,self.title,self.status,self.content, self.version, self.count,self.resource)

        lstProperty = []
        pcdict = {}
        dictConcept = {}
        theProperty = pcam.Property()
        theProperty.code = "child"
        theProperty.type = pcam.PropertyCodeType.code
        lstProperty.append(theProperty)

        theProperty = pcam.Property()
        theProperty.code = "parent"
        theProperty.type = pcam.PropertyCodeType.code
        lstProperty.append(theProperty)
        #https://stackoverflow.com/questions/12704305/return-column-names-from-pyodbc-execute-statement
        columns = [column[0] for column in cursor.description]
        # https://github.com/mkleehammer/pyodbc/wiki/Cursor#attributes
        #for column in cursor.columns("Diaglist"):
            # if column.column_name != "Diagnose": #or column != 'Bezeichnung' or column != 'Kapitel' or column != 'Unterkapitel' or column != 'Kurzbezeichnung':
            #     if column.column_name != "Bezeichnung":
            #         if column.column_name != "Kapitel":
            #             if column.column_name != "Unterkapitel":
            #                 if column.column_name != "Kurzbezeichnung":
            #                     theProperty = pcam.Property()
            #                     theProperty.code = column.column_name
            #                     theProperty.type = pcam.PropertyCodeType.string
            #                     lstProperty.append(theProperty)

        for column in columns:
            if column == 'DDiagnose' or column == 'DBezeichnung' or column == 'DKapitel' or column == 'DUnterkapitel' or column == 'DKurzbezeichnung' or column == 'D3SDiagnose' or column == "DUKUnterkapitel" or column == "DUKBeschreibung" or column == "DKBeschreibung" or column == "DKKapitel":
                continue
            else:
                theProperty = pcam.Property()
                theProperty.code = column
                theProperty.type = pcam.PropertyCodeType.string
                lstProperty.append(theProperty)
                print(column)

        self.parseConcepts(cursor)

        if lstProperty != []:
            self.property = lstProperty
        # if dictConcept != {}:
        #     self.concept = list(dictConcept.values())

    def parseConcepts(self, cursor):
        row = cursor.fetchone()
        dictParents = {}
        #pcdict[row.D3SDiagnose] = "parent"
        #dictConcept[row.DDiagnose] = 0
        while row:

            theConcept = pcam.CSConcept()
            #theConcept = pcam.VSConcept.__new__(pcam.VSConcept)
            #theConcept.definition =

            #oneConcept = dictConcept[row.DDiagnose]
            #theConcept.code = row.DDiagnose
            #dictConcept[row.DDiagnose] = theConcept
            #dictConcept[row.DDiagnose] = 0

            #if oneConcept := dictConcept[row.DDiagnose]:
            theConcept.code = row.DDiagnose
            theConcept.display = row.DKurzbezeichnung
            #dictConcept[row.DDiagnose] = theConcept

                #oneConcept.code = row.DDiagnose
                #oneConcept.display = row.DKurzbezeichnung

                #for oneProperty in oneConcept.property:
                #    theProperty = oneProperty

            #if theProperty is None:
            theProperty = pcam.CSConcept.ConceptProperty()

            #if row.DDiagnose is row.D3SDiagnose + '*':
            theProperty.code = "parent"
            theProperty.value = row.D3SDiagnose
            theProperty.type = pcam.PropertyCodeType.code
            theConcept.property.append(theProperty)

            ### we are working on the lvl 1 parent (drei steller) ###

            # if the parent cant be fount in the dict, create it
            if row.D3SDiagnose not in dictParents:
                theParentConcept = pcam.CSConcept()
                theParentConcept.code = row.D3SDiagnose
                theParentConcept.display = row.D3SBeschreibung
                dictParents[row.D3SDiagnose] = theParentConcept
                self.concept.append(theParentConcept)

            # create new child link to Parent
            thePropertyofParent = pcam.CSConcept.ConceptProperty()
            thePropertyofParent.code = "child"
            thePropertyofParent.value = row.DDiagnose
            thePropertyofParent.type = pcam.PropertyCodeType.code
            dictParents[row.D3SDiagnose].property.append(thePropertyofParent)

            # create new parent link to parent of parent
            thePropertyofParent = pcam.CSConcept.ConceptProperty()
            thePropertyofParent.code = "parent"
            thePropertyofParent.value = row.DUKUnterkapitel
            thePropertyofParent.type = pcam.PropertyCodeType.code
            dictParents[row.D3SDiagnose].property.append(thePropertyofParent)

            ### we are working on the lvl 2 parent (unterkapitel) ###

            if row.DUKUnterkapitel not in dictParents:
                theParentConcept = pcam.CSConcept()
                theParentConcept.code = row.DUKUnterkapitel
                theParentConcept.display = row.DUKBeschreibung
                dictParents[row.DUKUnterkapitel] = theParentConcept
                self.concept.append(theParentConcept)

            # create new child link to Parent
            thePropertyofParent = pcam.CSConcept.ConceptProperty()
            thePropertyofParent.code = "child"
            thePropertyofParent.value = row.D3SDiagnose
            thePropertyofParent.type = pcam.PropertyCodeType.code
            dictParents[row.DUKUnterkapitel].property.append(thePropertyofParent)

            # create new parent link to parent of parent
            thePropertyofParent = pcam.CSConcept.ConceptProperty()
            thePropertyofParent.code = "parent"
            thePropertyofParent.value = row.DKKapitel
            thePropertyofParent.type = pcam.PropertyCodeType.code
            dictParents[row.DUKUnterkapitel].property.append(thePropertyofParent)

            ### we are working on the lvl 3 parent (kapitel) ###

            if row.DKKapitel not in dictParents:
                theParentConcept = pcam.CSConcept()
                theParentConcept.code = row.DKKapitel
                theParentConcept.display = row.DKBeschreibung
                dictParents[row.DKKapitel] = theParentConcept
                self.concept.append(theParentConcept)

            # create new child link to Parent
            thePropertyofParent = pcam.CSConcept.ConceptProperty()
            thePropertyofParent.code = "child"
            thePropertyofParent.value = row.DUKUnterkapitel
            thePropertyofParent.type = pcam.PropertyCodeType.code
            dictParents[row.DKKapitel].property.append(thePropertyofParent)


            parseProp(theConcept.property, row.DKennzeichen, "Kennzeichen")
            parseProp(theConcept.property, row.DGruppe, "Gruppe")
            parseProp(theConcept.property, row.DHDGruppe, "HD_Gruppe")
            parseProp(theConcept.property, row.DZDGruppe, "ZD_Gruppe")
            parseProp(theConcept.property, row.DGeschlecht, "Geschlecht")
            parseProp(theConcept.property, row.DMindestalter, "Mindestalter")
            parseProp(theConcept.property, row.DHöchstalter, "Höchstalter")
            parseProp(theConcept.property, row.DUnwahrscheinlich, "Unwahrscheinlich")
            parseProp(theConcept.property, row.DHDambulant, "HD_ambulant")
            parseProp(theConcept.property, row.DHDZTage, "HDZ_Tage")
            parseProp(theConcept.property, row.DMeldepflicht, "Meldepflicht")
            parseProp(theConcept.property, row.DDStationärerworben, "Stationär_erworben")

            #print("hi")

            # if row.HD_Gruppe != " ":
            #     theProperty = pcam.CSConcept.ConceptProperty()
            #     theProperty.code = "Gruppe"
            #     theProperty.value = row.HD_Gruppe
            #     theProperty.type = pcam.PropertyCodeType.string
            #     theConcept.property.append(theProperty)
        # print("hi")
            #if row.

            # if row.D3SDiagnose != list(pcdict)[-1]:
            #     #pcdict[row.D3SDiagnose] = "parent"
            #     theProperty.code = "parent"
            #     theProperty.value = row.D3SDiagnose
            #     theProperty.type = pcam.PropertyCodeType.code
            #     theConcept.property.append(theProperty)
            #
            # elif row.DDiagnose != list(pcdict)[-1]:
            #     #pcdict[row.DDiagnose] = "child"
            #     theProperty.code = "child"
            #     theProperty.value = row.D3SDiagnose
            #     theProperty.type = pcam.PropetyCodeType.code
            #     theConcept.property.append(theProperty)

    #('101.0', 'Revisionsgrund: Pfannenlockerung', '!', ' ', 'Revisionsgrund: Pfannenlockerung', '101', 'A1.01', 'Revisionsgründe in der Endoprothetik (101-199)', 'Revisionsgründe in der Endoprothetik (101-199)', 'A1')
            # if row.DKennzeichen != " ":
            #      print(row.DDiagnose, row.DKennzeichen)
            # else:
            #     print(row.DDiagnose, "haha")
            #if row.DGruppe == None:
            #   print (row.DDiagnose)

            #dictConcept[row.DDiagnose] = theConcept



                #check through all properties and add them to the property
                #if

                #theConcept.property.
            # theConcept.designation = []
            # theConcept.property = []
            # dictConcept[tempindex] = theConcept
            #dictConcept[row.DUKUnterkapitel] = theConcept
            #dictConcept['Kapitel'] = row.KKapitel
            # self.name = row.DDiagnose
            # self.title = row.DBezeichnung
            # self.status = "draft"
            # self.description=row.DKurzbezeichnung
            # self.resource = pcam.Resource.CodeSystem.value
            #print(self.name,self.title,self.status,self.description,self.resource)
            # for x in range(len(theConcept.property)):
            #      print (theConcept.property[x])


            #print(row.D3SDiagnose, theConcept.code, theConcept.display, theConcept.property)
            #print(row.DDiagnose, pcdict)


            self.concept.append(theConcept)
            row = cursor.fetchone()


    # just for calling the outer method
    def parse(inFilename):
        return ICDBMG(inFilename)
    # name-title-url-status
    # infile:C:

def parseProp(conceptPropList, propertyInRow, nameOfProperty):
    if propertyInRow != " ":
        theProperty = pcam.CSConcept.ConceptProperty()
        theProperty.code = nameOfProperty
        theProperty.value = propertyInRow
        theProperty.type = pcam.PropertyCodeType.string
        conceptPropList.append(theProperty)

inFile = "C:\\Users\\gralf\\OneDrive\\Desktop\\FH Technikum\\Bachelor\\SYSTEMDATEN2022.mdb"
ICDBMG(inFile)
