import argparse
import sys
import time

# malac directly convertable classes as dictionary with fileending as key, first element value with module and second element with official name
listClasses = {".1.propcsv.csv": ["prop_csv_and_master", "PropCsvAndMaster"],
    ".1.propcsv.xlsx": ["prop_csv_and_master", "PropCsvAsXLSX"],
    ".1.outdatedcsv.csv": ["outdated_csv", "OutdatedCsv1"],
    ".2.outdatedcsv.csv": ["outdated_csv", "OutdatedCsv2"],
    ".2.claml.xml":["claml2", "ClaML2Sub"],
    ".3.claml.xml":["claml3", "ClaML3Sub"],
    ".1.fsh":["fsh1", "Fsh1"],
    ".2.fsh":["fsh2", "Fsh2"],
    ".1.svsextelga.xml":["svsextelga", "SVSextELGA1Sub"],
    ".2.svsextelga.xml":["svsextelga", "SVSextELGA2Sub"],
    ".4.fhir.xml":["fhir4_cs_and_vs", "FHIR4CsAndVs"],
    #".4.fhir.json":["fhir4_cs_and_vs", "FHIR4xml69json"] # create FHIR4xml69json inside of fhir4_cs_and_vs.py for json to xml and xml to json
    }
descriptionText = "This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and output classes are right now ClaML 2.0.0 with a file ending \".2.claml.xml\", ClaML 3.0.0 with a file ending \".3.claml.xml\", HL7 FHIR Shorthand 1.3.0 with a file ending \".1.fsh\", HL7 FHIR Shorthand 2.0.0 with a file ending \".2.fsh\", a predefined CSV with a file ending \".1.csv\" and a extended SVS with a file ending \".1.svsextelga.xml\". Additionally gofsh and sushi can be used to convert from and to a \".4.fhir.json\" or \".4.fhir.xml\", see arguments. Also, FHIR server credentials can be given, to directly convert json to xml or xml to json and to directly upload the result, see arguments."
versionNumber = "3.0.1+20221018"

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s -i INPUT-FILE-PATH [-o OUTPUT-FILE-PATH] [-argsLang OUTPUT-LANGUAGE] [-s]",
        description=descriptionText
    )
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
        "-j2xServer", "--json2xmlFHIRServer", help="Directly run a json2xml convert on a given FHIR server after sushi. "+
        "the FHIR Server adress including the base path wraped into quotation marks. e.g.:"+
        '--user fhiruser:fhiruserpassword "http://ibmfhir.quantumeconomy.org/fhir-server/api/v4/"'+
        "Warning: a fhir json has to exists, that is usually generated via sushi!", required=False
    )
    parser.add_argument(
        "-j2xUser", "--json2xmlFHIRServerUser", help="the FHIR server user password if needed"+
        '"FHIRServerUser" "FHIRServerPassword""', required=False
    )
    parser.add_argument(
        "-j2xPw", "--json2xmlFHIRServerUserPassword", help="the FHIR server user password if needed"+
        '"FHIRServerUser" "FHIRServerPassword""', required=False
    )
    parser.add_argument(
        "-ttt", "--tergiTunnelToken", help='A HTTP header token that may be required in order to access the FHIR server', required=False
    )
    parser.add_argument(
        "-up", "--upload2FhirServer", action="store_true", help='Directly upload the converted FHIR json to the given FHIR Server. Can only be run if all the j2x argument(s) are given.', required=False
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
    return parser

def detectClassByEnding(filename):
    for iclass in listClasses:
        if filename.endswith(iclass):
            return listClasses[iclass],iclass
    sys.exit("The classification could not be detected from the file name. \n %s" % descriptionText)

def convert_fhir_resource(input_filename, input_filename_extension, source_format, target_format, fhir_server_url, fhir_server_user=None, fhir_server_password=None, tergi_tunnel_token=None):
    import os
    import requests
    import json
    import xml.dom.minidom

    headers={'Content-Type':'application/fhir+' + source_format + '; charset=utf-8',
             'Accept':'application/fhir+' + target_format + '; charset=utf-8'}
    if (tergi_tunnel_token):
        headers['tergi-tunnel-token'] = tergi_tunnel_token

    auth = None
    if (fhir_server_user and fhir_server_password):
        auth = (fhir_server_user, fhir_server_password)

    source_filename = input_filename.replace(input_filename_extension, '.4.fhir.' + source_format)
    target_filename = input_filename.replace(input_filename_extension, '.4.fhir.' + target_format)

    with open(source_filename, 'rb') as source_file:
        if auth is None:
            res = requests.post(fhir_server_url+"$convert", headers=headers, data=source_file)
        else:
            res = requests.post(fhir_server_url+"$convert", headers=headers, auth=auth, data=source_file)

    # remove old target file if it has existed
    if os.path.exists(target_filename):
        os.remove(target_filename)

    try:
        res.raise_for_status()
    except:
        print("ERROR: " + res.text)
        res.raise_for_status()

    with open(target_filename, 'w', newline='', encoding='utf-8') as target_file:
        startRequest = time.time()
        if target_format == 'json':
            target_file.write(json.dumps(json.loads(res.text), indent=2))
            print("*.4.fhir.json (in "+str(round(time.time()-startRequest,3))+" seconds)")
        elif target_format == 'xml':
            target_file.write(xml.dom.minidom.parseString(res.text).toprettyxml())
            print("*.4.fhir.xml (in "+str(round(time.time()-startRequest,3))+" seconds)")
        else:
            sys.exit('Target format ' + target_format + ' not supported. Either xml or json.')


def main() -> None:
    start = time.time()
    print("-------------------- MaLaC-CT "+versionNumber+" started --------------------")

    parser = init_argparse()
    args = parser.parse_args()

    print("converted "+args.input+" to")

    # if input is a FHIR JSON file a FHIR server has to be specified in all cases
    if '.4.fhir.json' in args.input and not args.json2xmlFHIRServer:
        sys.exit("A FHIR JSON file as input requires a FHIR server with $convert capabilities. \n %s" % descriptionText)

    do_fhir_server_conversion = True
    if '.4.fhir.json' in args.input:
        do_fhir_server_conversion = False
        convert_fhir_resource(args.input, '.4.fhir.json', 'json', 'xml', args.json2xmlFHIRServer, args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword, args.tergiTunnelToken)
        args.input = args.input.replace('.4.fhir.json', '.4.fhir.xml')

    # look at the name of the input file and load the classification,
    iClassValue,iClass = detectClassByEnding(args.input)

    # if it is a fhir input and the output is also fhir, skip the real malac-ct converting
    if not(".4.fhir." in args.input and args.output != None and ".4.fhir." in args.output):
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as inputClass]'
        iModule = __import__(iClassValue[0])
        inputClass = getattr(iModule, iClassValue[1])

        # add globalUrl as class variable for outdatedcsv - would not be able to access it otherwise
        inputClass.globalUrl = args.fhirIgUrl
        # serialize the input file
        input = inputClass.parse(args.input)
        input.globalUrl = args.fhirIgUrl
        input.filename = args.input
        # sort the input
        if "CodeSystem-" in args.input:
            input.sortConceptsExpandStyle()

        # append to all processedTerminology lists
        if args.appendProcessedTerminologyTo:
            input.processedTerminologies = args.appendProcessedTerminologyTo[0]
            for csv2AppendTo in args.appendProcessedTerminologyTo:
                input.appendMetaDataTo(csv2AppendTo)

        # do the converting for every class known, or if fixed in output, once and break out the loop
        for oClass in listClasses:
            if not args.input.endswith(oClass):
                oClassValue = listClasses[oClass]
                if args.output != None: # overwrite output variables if there is an fixed output
                    oClassValue,oClass = detectClassByEnding(args.output)
                # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as outputClass]'
                oModule = __import__(oClassValue[0])
                outputClass = getattr(oModule, oClassValue[1])

                # open a new file and export to output file
                with open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') as outfile:
                    startFormat = time.time()
                    outputClass.exporto(input, outfile, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                    print("*"+oClass+" (in "+str(round(time.time()-startFormat,3))+" seconds)")

                if args.output != None: # if there is an fixed output, do the loop just once
                    break

    # run converter for only main file, create from xml the json, it doesn't convert the supplement!
    if (url := args.json2xmlFHIRServer):
        if do_fhir_server_conversion:
            convert_fhir_resource(args.input, iClass, 'xml', 'json', args.json2xmlFHIRServer, args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword, args.tergiTunnelToken)

        if (args.upload2FhirServer):
            import requests
            import os

            headers={ 'Content-Type' : 'application/fhir+json; charset=utf-8' }
            if (args.tergiTunnelToken):
                headers['tergi-tunnel-token'] = args.tergiTunnelToken

            auth = None
            if (args.json2xmlFHIRServerUser and args.json2xmlFHIRServerUserPassword):
                auth = (args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword)

            if ("CodeSystem-" in args.input):
                url += "CodeSystem/"+os.path.basename(args.input.replace(iClass,"").replace("CodeSystem-","")).lower()
            elif ("ValueSet-" in args.input):
                url += "ValueSet/"+os.path.basename(args.input.replace(iClass,"").replace("ValueSet-","")).lower()
            else:
                sys.exit("The FHIR Ressource Type could not be detected from the file name. \n %s" % descriptionText)

            with open(args.input.replace(iClass,".4.fhir.json"), 'rb') as json_format_file:
                if auth is None:
                    res = requests.put(url, headers=headers, data=json_format_file) # files={'upload_file': json_format_file})
                else:
                    res = requests.put(url, headers=headers, auth=auth, data=json_format_file) # files={'upload_file': json_format_file})

            print(res.text)
            res.raise_for_status()
            print("& uploaded to given fhir server")

    print("altogether in "+str(round(time.time()-start,2))+" seconds.")
    print("-------------------- MaLaC-CT ended --------------------")

if __name__ == "__main__":
    main()
