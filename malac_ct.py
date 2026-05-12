import argparse
from datetime import datetime
import sys
import time

# malac directly convertable classes as dictionary with fileending as key, first element value with module and second element with official name
listOClasses = {
    ".1.propcsv.csv": ["prop_csv_and_master", "PropCsvAndMaster"],
    ".1.propcsv.xlsx": ["prop_csv_and_master", "PropCsvAsXLSX"],
    # management decision: no spreadct csvs
    #".data.1.spreadct.csv": ["prop_csv_and_master", "SpreadCT"], # additionally a special check is beeing made, if the mandatory .meta.1.spreadct.csv file does exist
    ".1.spreadct.xlsx": ["prop_csv_and_master", "SpreadCTasXLSX"],
    ".1.outdatedcsv.csv": ["outdated_csv", "OutdatedCsv1"],
    ".2.outdatedcsv.csv": ["outdated_csv", "OutdatedCsv2"],
    ".2.claml.xml":["claml2", "ClaML2Sub"],
    ".3.claml.xml":["claml3", "ClaML3Sub"],
    ".1.fsh":["fsh1", "Fsh1"],
    ".2.fsh":["fsh2", "Fsh2"],
    ".1.svsextelga.xml":["svsextelga", "SVSextELGA1Sub"],
    ".2.svsextelga.xml":["svsextelga", "SVSextELGA2Sub"],
    ".4.fhir.xml":["fhir4_cs_and_vs", "FHIR4CsAndVs"],
    ".4.fhir.json":["fhir4_cs_and_vs", "FHIR4CsAndVsJson"]
    }
listIClasses = listOClasses | {
    ".icd.mdb":["ext_aut", "BMGICD"],
    ".lkf.mdb":["ext_aut", "BMGLKF"]
    }

# dictionary of extensions that may be activated by using the "-ext" parameter and specifying the corresponding canonical URL
extensions_dict = {
    "http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-valueset-systemoid":["ext_aut", "SystemOid"],
    "http://hl7.org/fhir/StructureDefinition/codesystem-replacedby":["ext","ReplacedBy"], #TODO specific FHIR version?
    "http://hl7.org/fhir/StructureDefinition/valueset-conceptOrder":["ext","ConceptOrder"]
    }

descriptionText = "This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. See arguments for more details."
versionNumber = "5.0.0+20260331"

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=descriptionText)
    parser.add_argument(
        "-i", "--input", help='the input file, classification is detected automaticly', required=True
    )
    parser.add_argument(
        "-o", "--output", help='the output file, if none is given MaLaC-CT will convert into all other known formats.', required=False
    )
    parser.add_argument(
        "-langArg", "--argumentLanguage", help='a fixed language for the output classification ClaML v3, use offical language codes only, see http://www.ietf.org/rfc/rfc3066.txt.', required=False
    )
    parser.add_argument(
        "-up2addlServer", "--uploadToAdditionalFHIRServer", action='append', help="Upload the FHIR JSON to an additional FHIR Server", required=False
    )
    parser.add_argument(
        "-url", "--fhirIgUrl", help="the home adress of the FHIR IG Publisher URL, to fill a predefined url in the resource", required=False
    )
    parser.add_argument(
        "-appndProcTermTo", "--appendProcessedTerminologyTo", action='append', help="Appends the processed terminology to a given csv", required=False
    )
    parser.add_argument(
        "-incHierarchyExt4VS", "--includeHierarchyExtension4ValueSet", action='store_true', help="Includes the hierarchy extension wenn creating ValueSets", required=False
    )
    parser.add_argument(
        "-turnOffVerif", "--turnOffVerification", action="store_false", help='Do not use this argument, if you dont know what it does! Only for private networks! Turns of the verification of the certificate. There will also be ssl-warnings from urllib3.', required=False
    )
    parser.add_argument(
        "-convTs", "--conversionTimestamp", help="Specify the conversion timestamp which is also used as expansion timestamp in case of value set resources.", required=False
    )
    parser.add_argument(
        '-ext', '--extension', action='append', help='Specify the canonical URL of the FHIR extension that shall be activated.', required=False
    )
    return parser

def detectClassByEnding(filename):
    for iclass in listIClasses:
        if filename.endswith(iclass):
            return listIClasses[iclass],iclass
    sys.exit("The classification could not be detected from the file name. \n %s" % descriptionText)

def upload_to_fhir_server(input, iClass, FHIRServer, FHIRServerUser, FHIRServerUserPassword, FHIRServerTergiTunnelToken, verification, failIfUploadGoesWrong=False):
    import requests
    import os
    import time

    headers={ 'Content-Type' : 'application/fhir+json; charset=utf-8' }
    if (FHIRServerTergiTunnelToken):
        headers['tergi-tunnel-token'] = FHIRServerTergiTunnelToken

    auth = None
    if (FHIRServerUser and FHIRServerUserPassword):
        auth = (FHIRServerUser, FHIRServerUserPassword)

    if ("CodeSystem-" in input):
        FHIRServer += "CodeSystem/"+os.path.basename(input.replace(iClass,"").replace("CodeSystem-","")).lower()
    elif ("ValueSet-" in input):
        FHIRServer += "ValueSet/"+os.path.basename(input.replace(iClass,"").replace("ValueSet-","")).lower()
    else:
        sys.exit("The FHIR Ressource Type could not be detected from the file name. \n %s" % descriptionText)

    with open(input.replace(iClass,".4.fhir.json"), 'rb') as json_format_file:
        # retry 3 times
        for attempt in range(3):
            try:
                json_format_file.seek(0)  # reset file pointer for retry
                if auth is None:
                    res = requests.put(FHIRServer, headers=headers, data=json_format_file, verify=verification, timeout=(30, 900))  # timeout(connect, read/response)
                else:
                    res = requests.put(FHIRServer, headers=headers, auth=auth, data=json_format_file, verify=verification, timeout=(30, 900))  # timeout(connect, read/response)
                break

            except requests.exceptions.ConnectionError as e:
                if attempt < 2:  # still some retries left
                    print(f"Connection error (attempt {attempt + 1}/3), retrying in 60 seconds...")
                    time.sleep(60)
                    
                    continue
                else:  # last try failed
                    print(f"Connection failed after 3 attempts: {e}")
                    raise
            
            except requests.exceptions.Timeout as e:
                print(f"Timeout after 900 seconds: {e}")
                raise  # no retry for a timeout (server is too slow)


    if failIfUploadGoesWrong:
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"ERROR: HTTP {res.status_code} - {res.text}")
            raise

def main() -> None:
    start = time.time()
    print("-------------------- MaLaC-CT "+versionNumber+" started --------------------")

    parser = init_argparse()
    args = parser.parse_args()

    print("converted "+args.input+" to")

    # look at the name of the input file and load the classification,
    iClassValue,iClass = detectClassByEnding(args.input)

    # management decision: no spreadct csvs
    # special handling of .data.1.spreadct.csv, check if *.meta.1.spreadct.csv exists
    #if iClass == ".data.1.spreadct.csv":
    #    import os
    #    if not os.path.exists(args.input.replace(".data.1.spreadct.csv",".meta.1.spreadct.csv")):
    #        sys.exit("The spreadCT format requires beside the *.data.1.spreadct.csv a mandatory *.meta.1.spreadct.csv in the same folder! \n %s" % descriptionText)

    # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as inputClass]'
    iModule = __import__(iClassValue[0])
    inputClass = getattr(iModule, iClassValue[1])

    # add globalUrl as class variable for outdatedcsv - would not be able to access it otherwise
    inputClass.globalUrl = args.fhirIgUrl
    # serialize the input file
    input = inputClass.parse(args.input)
    input.globalUrl = args.fhirIgUrl
    input.filename = args.input

    # read activated extensions
    input.activated_extension_dict = {}
    input.applied_extension_list = []
    if args.extension:
        for extension in args.extension:
            if extension in extensions_dict:
                input.activated_extension_dict[extension] = extensions_dict[extension]

    # append to all processedTerminology lists
    if args.appendProcessedTerminologyTo:
        input.processedTerminologies = args.appendProcessedTerminologyTo[0]
        timestamp = args.conversionTimestamp if args.conversionTimestamp else datetime.now().strftime("%Y-%m-%dT%X.0000Z")
        for csv2AppendTo in args.appendProcessedTerminologyTo:
            timestamp = input.appendMetaDataTo(csv2AppendTo, timestamp)

    # sort the input
    if 'CodeSystem-' in input.filename:
        input.sortConceptsExpandStyle()
    elif 'ValueSet-' in input.filename:
        input.sort_VS_concepts_by_conceptOrder()

    # do the converting for every class known, or if fixed in output, once and break out the loop
    for oClass in listOClasses:
        if not args.input.endswith(oClass):
            oClassValue = listOClasses[oClass]
            if args.output != None: # overwrite output variables if there is an fixed output
                oClassValue,oClass = detectClassByEnding(args.output)
            # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as outputClass]'
            oModule = __import__(oClassValue[0])
            outputClass = getattr(oModule, oClassValue[1])

            # open a new file and export to output file
            with open(args.output if args.output else args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') as outfile:
                startFormat = time.time()
                outputClass.exporto(input, outfile, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                print("*"+oClass+" (in "+str(round(time.time()-startFormat,3))+" seconds)")

            if args.output != None: # if there is an fixed output, do the loop just once
                break

    if args.uploadToAdditionalFHIRServer:
        for addlServer in args.uploadToAdditionalFHIRServer:
            startUpload = time.time()
            import json
            addlServerDict = json.loads(addlServer)
            upload_to_fhir_server(args.input, iClass, addlServerDict["FHIRServer"], addlServerDict["FHIRServerUser"], addlServerDict["FHIRServerUserPassword"], addlServerDict["FHIRServerTergiTunnelToken"], args.turnOffVerification)
            print("uploaded to additional FHIR server named "+ addlServerDict["FHIRServer"]+" (in "+str(round(time.time()-startUpload,3))+" seconds)")

    print("altogether in "+str(round(time.time()-start,2))+" seconds.")
    print("-------------------- MaLaC-CT ended --------------------")

if __name__ == "__main__":
    main()
