import prop_csv_and_master as pcam
import pyodbc

# database has been downloaded from
# https://www.sozialministerium.at/Themen/Gesundheit/Gesundheitssystem/Krankenanstalten/LKF-Modell-2022/Programme-(XDok,-C-Files,-Stammdaten,-Intensiv-Scoring)-f%C3%BCr-landesgesundheitsfondsfinanzierte-Krankenanstalten-2022.html
# https://www.sozialministerium.at/dam/jcr:8dfa64f6-fe02-4f1a-924c-6d082388865b/Stammdaten_2022_SP2.zip


# python environment and Acces ODBC need the same bit rate either 64 - 64 or 32 - 32
# for checking python version, start python by typing "python" in a console and see if the MSC Version in the info text is 32 or 64 bit
# for checking the MS Access Driver loaded be pyodbc, type following into the console with the already started python:
# first "import pyodbc" and then "[i for i in pyodbc.drivers() if i.startswith('Microsoft Access Driver')]".
# If there is any output, a functioning driver has been found, the name there is the driver name that should be used for the connect string!
# If there is no output, try installing from here the driver for your bit rate: https://www.microsoft.com/en-US/download/details.aspx?id=13255

# If above does not help, here are other usefull links for adjusting your Microsoft Access Driver:
# How to connect to Microsoft Access with ODBC from Windows 10 https://help.interfaceware.com/v6/connect-to-microsoft-access-odbc

class BMGICD(pcam.PropCsvAndMaster):
    def __init__(self, inFile):
        super().__init__()
        # if you have an ODBC Driver Manager Error here, look into the comments above
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + inFile + ';')
        # https://github.com/mkleehammer/pyodbc/wiki/Cursor#attributes
        cursor = conn.cursor()
        # jointable between "DIAGLIST", "DIAGLIST- 3 STELLER", "DIAGLIST - UNTERKAPITEL", "DIAGLIST-KAPITEL"
        cursor.execute(
            "SELECT [D].Diagnose AS [DDiagnose], [D].Kennzeichen AS [DKennzeichen],[D].Gruppe AS [DGruppe], [D].HD_Gruppe AS [DHDGruppe], [D].ZD_Gruppe AS [DZDGruppe], [D].Geschlecht AS [DGeschlecht], [D].Mindestalter AS [DMindestalter], [D].Höchstalter AS [DHöchstalter], [D].Unwahrscheinlich AS [DUnwahrscheinlich], [D].HD_ambulant AS [DHDambulant], [D].[HD_>0_Tage] AS [DHDZTage], [D].Bezeichnung AS [DBezeichnung],[D].Meldepflicht AS [DMeldepflicht], [D].Stationär_erworben AS [DStationärerworben],[D].Kurzbezeichnung AS [DKurzbezeichnung],[D3S].Diagnose AS [D3SDiagnose], [D3S].Bezeichnung AS [D3SBezeichnung], [DUK].Unterkapitel AS [DUKUnterkapitel], [DUK].Beschreibung AS [DUKBeschreibung], [DK].Beschreibung AS [DKBeschreibung], [DK].Kapitel AS [DKKapitel]"
            "FROM [DIAGLIST] AS [D], [DIAGLIST - 3STELLER] AS [D3S], [DIAGLIST - UNTERKAPITEL] AS [DUK], [DIAGLIST - KAPITEL] AS [DK]"
            "WHERE [D].Diagnose LIKE [D3S].Diagnose + '%' "
            "AND [D3S].Diagnose BETWEEN [DUK].Diagnose_von AND [DUK].Diagnose_bis "
            "AND [DUK].Diagnose_von AND [DUK].Diagnose_bis BETWEEN [DK].Diagnose_von AND [DK].Diagnose_bis ")#.fetchall() #this could help if you have odbc errors

        #metadata
        self.resource = pcam.Resource.CodeSystem
        self.url = "https://termgit.elga.gv.at/CodeSystem/bmg-icd-10-2024"
        self.id = "bmg-icd-10-2024"
        self.name = "bmg-icd-10-2024"
        self.title = "ICD-10 BMSGPK 2024"
        self.status = pcam.Status.active
        self.content = pcam.Content.complete
        self.version = "1.0.1+20240205"
        self.identifier.append("1.2.40.0.34.5.222")
        self.contact.append(pcam.ContactDetail.from_string("Sozialministerium LKF Modell 2023|url^https://www.sozialministerium.at/Themen/Gesundheit/Gesundheitssystem/Krankenanstalten/LKF-Modell-2024/Programme-(XDok,-C-Files,-Stammdaten,-Intensiv-Scoring)-f%C3%BCr-landesgesundheitsfondsfinanzierte-Krankenanstalten-2024.html^^^^"))
        self.description = """Seit 1. Jänner 1989 sind in Österreichs Krankenanstalten die Entlassungsdiagnosen der in stationärer Behandlung befindlichen Patienten bundeseinheitlich nach der von der Weltgesundheitsorganisation veröffentlichten Internationalen Klassifikation der Krankheiten (ICD) in der jeweils aktuellen Fassung des für Gesundheit zuständigen Bundesministeriums zu erfassen. 
Nach über 10-jähriger Verwendung der ICD-10 Version ICD-10 BMSG 2001 in unveränderter Form wurde eine Aktualisierung des Diagnosenschlüssels erforderlich. 
Dabei sollte der bekannte Diagnosenschlüssel unter Berücksichtigung der seither erfolgten Updates der WHO in möglichst unveränderter Form beibehalten werden.<br/>
In der Sitzung der Bundesgesundheitskommision vom 29. Juni 2012 wurde daher der Beschluss gefasst, die seit 1.1.2001 verwendete Version ICD-10 BMSG 2001 durch die seit dem 1.1.2013 geltende ICD-10 BMG 2013 zu ersetzen.<br/>
In die seit dem 1.1.2014 verwendete ICD-10 BMG 2014 wurden zusätzlich die im Herbst 2012 publizierten Aktualisierungen der WHO eingearbeitet.
Die seit 1.1.2017 verwendete ICD-10 BMGF 2017 beinhaltet alle Aktualisierungen der WHO 2016, gefolgt von der seit 1.1.2020 geltenden ICD-10 BMASGK 2020 mit allen Aktualisierungen der WHO 2019.<br/>
Die aktuelle, ab 1.1.2024 geltende Version ICD-10 BMSGPK 2024 beinhaltet alle von der WHO zur Verfügung gestellten Updates sowie einzelne 5-stellige Codes, die aus der vom Bundesinstitut für Arzneimittel und Medizinprodukte (BfArM) in Deutschland herausgegebenen ICD-10-GM übernommen wurden. 
Besonderer Dank gilt allen, die in den österreichischen Krankenanstalten mit der Diagnosencodierung und der Datenqualitätssicherung befasst sind und durch ihr Zutun und ihr Engagement die Erstellung der Diagnosen- und Leistungsberichte ermöglichen, sowie all jenen, die zur Weiterentwicklung der Dokumentationsgrundlagen beitragen."""

        self.parseConcepts(cursor)

    def parseConcepts(self, cursor):
        row = cursor.fetchone()
        dictParents = {}

        while row:
            theDKCode = row.DKBeschreibung.split("(")[1].replace(")","") #row.DKKapitel
            theDUKCode = row.DUKBeschreibung.split("(")[1].replace(")","") #row.DUKUnterkapitel

            if row.D3SDiagnose == "Z21":
                pass

            unequalDKAndDUK, unequalDUKAndD3S, unequalD3SAndD = False, False, False
            if theDKCode != theDUKCode:
                unequalDKAndDUK = True
                if theDKCode not in dictParents:
                    theParentConcept = pcam.CSConcept()
                    theParentConcept.code = theDKCode
                    theParentConcept.display = row.DKBeschreibung
                    parseProp(theParentConcept.property, True, "notSelectable", pcam.PropertyCodeType.boolean)
                    dictParents[theDKCode] = theParentConcept

            if theDUKCode != row.D3SDiagnose:
                unequalDUKAndD3S = True
                if theDUKCode not in dictParents:
                    theParentConcept = pcam.CSConcept()
                    theParentConcept.code = theDUKCode
                    theParentConcept.display = row.DUKBeschreibung
                    parseProp(theParentConcept.property, True, "notSelectable", pcam.PropertyCodeType.boolean)
                    dictParents[theDUKCode] = theParentConcept
                    if unequalDKAndDUK:
                        parseChild(dictParents,theDKCode,theDUKCode)
                        parseParent(dictParents,theDUKCode,theDKCode)

            if row.D3SDiagnose != row.DDiagnose:
                unequalD3SAndD = True
                if row.D3SDiagnose not in dictParents:
                    theParentConcept = pcam.CSConcept()
                    theParentConcept.code = row.D3SDiagnose
                    theParentConcept.display = row.D3SBezeichnung
                    # D3S codes are not abstract/notselectable!
                    #parseProp(theParentConcept.property, True, "notSelectable", pcam.PropertyCodeType.boolean)
                    dictParents[row.D3SDiagnose] = theParentConcept
                    if unequalDUKAndD3S:
                        parseChild(dictParents,theDUKCode,row.D3SDiagnose)
                        parseParent(dictParents,row.D3SDiagnose,theDUKCode)
                    elif unequalDKAndDUK:
                        parseChild(dictParents,theDKCode,row.D3SDiagnose)
                        parseParent(dictParents,row.D3SDiagnose,theDKCode)

            theConcept = pcam.CSConcept()
            theConcept.code = row.DDiagnose
            theConcept.display = row.DKurzbezeichnung
            if row.DKurzbezeichnung != row.DBezeichnung:
                theConcept.definition = row.DBezeichnung
            # parsing respective properties to one concept
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
            parseProp(theConcept.property, row.DStationärerworben, "Stationär_erworben")
            dictParents[row.DDiagnose] = theConcept
            # adding parent-property to the concept
            if unequalD3SAndD:
                parseChild(dictParents,row.D3SDiagnose,row.DDiagnose)
                parseParent(dictParents,row.DDiagnose,row.D3SDiagnose)
            # if the D3S and D was equal, but the DUK and D3S unequal, than the DUK is the parent of D
            elif unequalDUKAndD3S:
                parseChild(dictParents,theDUKCode,row.DDiagnose)
                parseParent(dictParents,row.DDiagnose,theDUKCode)
            # if the D3S and D and DUK was equal, but the DK and DUK unequal, than the DK is the parent of D
            elif unequalDKAndDUK:
                parseChild(dictParents,theDKCode,row.DDiagnose)
                parseParent(dictParents,row.DDiagnose,theDKCode)

            row = cursor.fetchone()

        # adding the dictParents to all concepts
        self.concept = dictParents.values()

        # adding the LKF reference to icd10 per property -> Ontologie
        cursor.execute("SELECT * FROM DIAGMEL")
        row = cursor.fetchone()
        conDict = self.buildConceptDictWithAttr("code")
        while row:
            parseProp(conDict[row.Diagnose].property, row.Leistung, "LKF-Code", pcam.PropertyCodeType.coding,
                "https://termgit.elga.gv.at/CodeSystem-bmg-lkf-2023")
            row = cursor.fetchone()

    # just for calling the outer method
    def parse(inFilename):
        return BMGICD(inFilename)

class BMGLKF(pcam.PropCsvAndMaster):
    def __init__(self, inFile):
        super().__init__()
        # if you have an ODBC Driver Manager Error here, look into the comments above
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + inFile + ';')
        # https://github.com/mkleehammer/pyodbc/wiki/Cursor#attributes
        cursor = conn.cursor()
        # jointable between "DIAGLIST", "DIAGLIST- 3 STELLER", "DIAGLIST - UNTERKAPITEL", "DIAGLIST-KAPITEL"
        cursor.execute(
            "SELECT [M].Leistung, [MAG].Anatomie_Text AS [AnatomieGrob], [MAF].AnatomieFein_Text AS [AnatomieFein], [MLA].Leistungsart_Text AS [Leistungsart], [MZ].Zugang_Text AS [Zugang], [MLE].Leistungseinheit_Text AS [Leistungseinheit], "
            "[M].Gruppe, [M].LGR, [M].Geschlecht, [M].Mindestalter, [M].Höchstalter, [M].WarninganzahlAufenthalt, [M].ErroranzahlAufenthalt, [M].WarninganzahlTag, [M].ErroranzahlTag, [M].MEL_ambulant, [M].[MEL>0_Tage] AS [MEL0_Tage], [M].MEL_TKL, [M].MEL_OP, [M].Kurztext, "
            "[M].Langtext, [M].Beschreibung, [M].Codierhinweis, [M].Nichtinhalt, [M].Quelle, [M].ErfassungStationär, [M].GruppeAmbulant, [M].LGRAmbulant, [M].WarninganzahlAmbulant, [M].ErroranzahlAmbulant, [M].DiagnoseAmbulant, [M].ErfassungAmbulant, [M].BettenführenderFuco, [M].PhysischeAnwesenheit, "
            "[MUK].Unterkapitel AS [MUKUnterkapitel], [MUK].Beschreibung AS [MUKBeschreibung], [MK].Beschreibung AS [MKBeschreibung], [MK].Kapitel AS [MKKapitel], [MD].DiagnoseVon AS [MDDiagnoseVon], [MD].DiagnoseBis AS [MDDiagnoseBis] "
            "FROM ((((((( [MELLIST] AS [M] LEFT JOIN [MELLIST - UNTERKAPITEL] AS [MUK] ON [M].Unterkapitel = [MUK].Unterkapitel)"
            "LEFT JOIN [MELLIST - KAPITEL] AS [MK] ON [M].Kapitel = [MK].Kapitel )"
            "LEFT JOIN [MELLIST - ANATOMIE GROB] AS [MAG] ON [M].AnatomieGrob = [MAG].Anatomie_Grob )"
            "LEFT JOIN [MELLIST - ANATOMIE FEIN] AS [MAF] ON [M].AnatomieFein = [MAF].AnatomieFein_Code )"
            "LEFT JOIN [MELLIST - LEISTUNGSART] AS [MLA] ON [M].Leistungsart = [MLA].Leistungsart_Code )"
            "LEFT JOIN [MELLIST - ZUGANG] AS [MZ] ON [M].Zugang = [MZ].Zugang_Code )"
            "LEFT JOIN [MELLIST - LEISTUNGSEINHEIT] AS [MLE] ON [M].Zugang = [MLE].Leistungseinheit_Code )"
            "LEFT JOIN [MELDIAG] AS [MD] ON [M].Leistung = [MD].LeistungVon ")


        #metadata
        self.resource = pcam.Resource.CodeSystem
        self.url = "https://termgit.elga.gv.at/CodeSystem/bmg-lkf-2024"
        self.id = "bmg-lkf-2024"
        self.name = "bmg-lkf-2024"
        self.title = "BMG Leistungskatalog Gesamt 2024"
        self.status = pcam.Status.active
        self.content = pcam.Content.complete
        self.version = "1.0.1+20240205"
        self.identifier.append("1.2.40.0.34.5.223")
        self.contact.append(pcam.ContactDetail.from_string("Sozialministerium LKF Modell 2023|url^https://www.sozialministerium.at/Themen/Gesundheit/Gesundheitssystem/Krankenanstalten/LKF-Modell-2024/Programme-(XDok,-C-Files,-Stammdaten,-Intensiv-Scoring)-f%C3%BCr-landesgesundheitsfondsfinanzierte-Krankenanstalten-2024.html^^^^"))
        self.description = """Der Leistungskatalog BMSGPK 2024 bildet die verbindliche Grundlage für die bundesweite inheitliche Leistungsdokumentation in Österreich ab 1. Jänner 2024. Der Leistungskatalog umfasst stationäre und ambulante Prozeduren:<br/>
* 889 stationäre Leistungen (große Operationen etc.)<br/>
* 893 Leistungen, die sowohl ambulant als auch stationär zu erfassen sind (CT, MR, kleine Operationen etc.)<br/>
* 347 Leistungen, die nur bei ambulanten Besuchen zu erfassen sind (EKG, Sonographie, ambulante Untersuchungen etc."""

        self.parseConcepts(cursor)

    def parseConcepts(self, cursor):
        row = cursor.fetchone()
        dictParents = {}

        while row:
            ### we are working on the lvl 1 parent (unterkapitel) ###

            new_mukunterkapitel = False
            if row.MUKUnterkapitel not in dictParents:
                new_mukunterkapitel = True

                theParentConcept = pcam.CSConcept()
                theParentConcept.code = row.MUKUnterkapitel
                theParentConcept.display = row.MUKUnterkapitel
                dictParents[row.MUKUnterkapitel] = theParentConcept
                self.concept.append(theParentConcept)
                # setting the parent upon creation of the concept
                parseParent(dictParents,row.MUKUnterkapitel,row.MKKapitel)

            parseChild(dictParents,row.MUKUnterkapitel,row.Leistung)

            ### we are working on the lvl 2 parent (kapitel) ###

            if row.MKKapitel not in dictParents:
                theParentConcept = pcam.CSConcept()
                theParentConcept.code = row.MKKapitel
                theParentConcept.display = row.MKBeschreibung
                dictParents[row.MKKapitel] = theParentConcept
                self.concept.append(theParentConcept)

            # adding child only if it is a new child
            if new_mukunterkapitel:
                parseChild(dictParents,row.MKKapitel,row.MUKUnterkapitel)
                conceptparent = row.MUKUnterkapitel

            theConcept = pcam.CSConcept()
            theConcept.code = row.Leistung
            theConcept.display = row.Kurztext
            theConcept.definition = row.Beschreibung

            # adding parent-property to the concept
            theProperty = pcam.CSConcept.ConceptProperty()
            theProperty.code = "parent"
            theProperty.value = conceptparent
            theProperty.type = pcam.PropertyCodeType.code
            theConcept.property.append(theProperty)
            # parsing respective properties to one concept
            if row.AnatomieGrob: parseProp(theConcept.property, row.AnatomieGrob, "AnatomieGrob")
            if row.AnatomieFein: parseProp(theConcept.property, row.AnatomieFein, "AnatomieFein")
            if row.Leistungsart: parseProp(theConcept.property, row.Leistungsart, "Leistungsart")
            if row.Zugang: parseProp(theConcept.property, row.Zugang, "Zugang")
            if row.Leistungseinheit: parseProp(theConcept.property, row.Leistungseinheit, "Leistungseinheit")
            if row.Gruppe: parseProp(theConcept.property, row.Gruppe, "Gruppe")
            if row.LGR: parseProp(theConcept.property, row.LGR, "LGR")
            if row.Geschlecht: parseProp(theConcept.property, row.Geschlecht, "Geschlecht")
            if row.Mindestalter: parseProp(theConcept.property, row.Mindestalter, "Mindestalter")
            if row.Höchstalter: parseProp(theConcept.property, row.Höchstalter, "Höchstalter")
            if row.WarninganzahlAufenthalt: parseProp(theConcept.property, row.WarninganzahlAufenthalt, "WarninganzahlAufenthalt")
            if row.ErroranzahlAufenthalt: parseProp(theConcept.property, row.ErroranzahlAufenthalt, "ErroranzahlAufenthalt")
            if row.WarninganzahlTag: parseProp(theConcept.property, row.WarninganzahlTag, "WarninganzahlTag")
            if row.ErroranzahlTag: parseProp(theConcept.property, row.ErroranzahlTag, "ErroranzahlTag")
            if row.MEL_ambulant: parseProp(theConcept.property, row.MEL_ambulant, "MEL_ambulant")
            if row.MEL0_Tage: parseProp(theConcept.property, row.MEL0_Tage, "MEL>0_Tage")
            if row.MEL_TKL: parseProp(theConcept.property, row.MEL_TKL, "MEL_TKL")
            if row.MEL_OP: parseProp(theConcept.property, row.MEL_OP, "MEL_OP")
            if row.Langtext: parseProp(theConcept.property, row.Langtext, "Langtext")
            if row.Codierhinweis: parseProp(theConcept.property, row.Codierhinweis, "Codierhinweis")
            if row.Nichtinhalt: parseProp(theConcept.property, row.Nichtinhalt, "Nichtinhalt")
            if row.Quelle: parseProp(theConcept.property, row.Quelle, "Quelle")
            if row.ErfassungStationär: parseProp(theConcept.property, row.ErfassungStationär, "ErfassungStationär")
            if row.GruppeAmbulant: parseProp(theConcept.property, row.GruppeAmbulant, "GruppeAmbulant")
            if row.LGRAmbulant: parseProp(theConcept.property, row.LGRAmbulant, "LGRAmbulant")
            if row.WarninganzahlAmbulant: parseProp(theConcept.property, row.WarninganzahlAmbulant, "WarninganzahlAmbulant")
            if row.ErroranzahlAmbulant: parseProp(theConcept.property, row.ErroranzahlAmbulant, "ErroranzahlAmbulant")
            if row.DiagnoseAmbulant: parseProp(theConcept.property, row.DiagnoseAmbulant, "DiagnoseAmbulant")
            if row.ErfassungAmbulant: parseProp(theConcept.property, row.ErfassungAmbulant, "ErfassungAmbulant")
            if row.BettenführenderFuco: parseProp(theConcept.property, row.BettenführenderFuco, "BettenführenderFuco")
            if row.PhysischeAnwesenheit: parseProp(theConcept.property, row.PhysischeAnwesenheit, "PhysischeAnwesenheit")

            parseProp(theConcept.property, row.MDDiagnoseVon, "MDDiagnoseVon", pcam.PropertyCodeType.coding,
                "https://termgit.elga.gv.at/CodeSystem-bmg-icd-10-2023")
            parseProp(theConcept.property, row.MDDiagnoseBis, "MDDiagnoseBis", pcam.PropertyCodeType.coding,
                "https://termgit.elga.gv.at/CodeSystem-bmg-icd-10-2023")

            self.concept.append(theConcept)
            row = cursor.fetchone()

    # just for calling the outer method
    def parse(inFilename):
        return BMGLKF(inFilename)

# checks if a certain property is filled and adds to the propertylist accordingly
def parseProp(conceptPropList, propertyInRow, nameOfProperty, typeOfProperty=pcam.PropertyCodeType.string, codeSystemOfProp=None):
    if propertyInRow != " ":
        theProperty = pcam.CSConcept.ConceptProperty()
        theProperty.code = nameOfProperty
        if typeOfProperty is pcam.PropertyCodeType.coding:
            theCoding = pcam.Coding()
            theCoding.code = propertyInRow
            theCoding.codesystem = codeSystemOfProp
            theProperty.value = theCoding
        else:
            theProperty.value = propertyInRow
        theProperty.type = typeOfProperty
        conceptPropList.append(theProperty)

def parseChild(dictConceptParents,propertyOfConcept,nameOfChildProperty):
    # create new child link to Parent
    thePropertyofParent = pcam.CSConcept.ConceptProperty()
    thePropertyofParent.code = "child"
    thePropertyofParent.value = nameOfChildProperty
    thePropertyofParent.type = pcam.PropertyCodeType.code
    dictConceptParents[propertyOfConcept].property.append(thePropertyofParent)

def parseParent(dictConceptParents, propertyOfConcept, nameOfParentProperty):
    # create new parent link to parent of parent
    thePropertyofParent = pcam.CSConcept.ConceptProperty()
    thePropertyofParent.code = "parent"
    thePropertyofParent.value = nameOfParentProperty
    thePropertyofParent.type = pcam.PropertyCodeType.code
    dictConceptParents[propertyOfConcept].property.append(thePropertyofParent)



#https://www.sozialministerium.at/Themen/Gesundheit/Gesundheitssystem/Krankenanstalten/LKF-Modell-2022/Programme-(XDok,-C-Files,-Stammdaten,-Intensiv-Scoring)-f%C3%BCr-landesgesundheitsfondsfinanzierte-Krankenanstalten-2022.html
# inFile = "C:\\Users\\gralf\\OneDrive\\Desktop\\FH Technikum\\Bachelor\\SYSTEMDATEN2022.mdb"
# ICDBMG(inFile)

class SystemOid():
    profile_canonical = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-valueset'
    extension_canonical = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-valueset-systemoid'

    def add_extension(the_element, oid):
        if not hasattr(the_element, 'extension'):
            the_element.extension = []

        the_extension = pcam.Extension()
        the_extension.url = SystemOid.extension_canonical
        the_extension.value = 'urn:oid:' + oid
        the_extension.type = pcam.ExtensionType.oid

        the_element.extension.append(the_extension)