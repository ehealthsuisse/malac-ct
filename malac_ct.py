import argparse
import subprocess
import sys
import time

# malac directly convertable classes as dictionary with fileending as key, first element value with module and second element with official name
# TODO check if fhir.json and fhir.xml has to be in listClasses for input check
listClasses = {".1.propcsv.csv": ["prop_csv_and_master", "PropCsvAndMaster"],
    ".1.outdatedcsv.csv": ["outdated_csv", "OutdatedCsv"],
    ".2.claml.xml":["claml2", "ClaML2Sub"],
    ".3.claml.xml":["claml3", "ClaML3Sub"],
    ".1.fsh":["fsh1", "Fsh1"],
    ".2.fsh":["fsh2", "Fsh2"],
    ".1.svsextelga.xml":["svsextelga1", "SVSextELGA1Sub"],
    ".4.fhir.xml":["fhir4_cs_and_vs", "FHIR4CsAndVs"]
    }
descriptionText = "This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and output classes are right now ClaML 2.0.0 with a file ending \".2.claml.xml\", ClaML 3.0.0 with a file ending \".3.claml.xml\", HL7 FHIR Shorthand 1.3.0 with a file ending \".1.fsh\", HL7 FHIR Shorthand 2.0.0 with a file ending \".2.fsh\", a predefined CSV with a file ending \".1.csv\" and a extended SVS with a file ending \".1.svsextelga.xml\". Additionally gofsh and sushi can be used to convert from and to a \".4.fhir.json\" or \".4.fhir.xml\", see arguments. Also, FHIR server credentials can be given, to directly convert json to xml or xml to json and to directly upload the result, see arguments."
versionNumber = "1.1.0+20220310-beta"

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
        "-langArg", "--argumentLanguage", help='a fixed language for the output classification, use offical language codes only, see http://www.ietf.org/rfc/rfc3066.txt.', required=False
    )
    # parser.add_argument(
    #     "-sushi", "--sushiConvertingToJson", action="store_true", help='Directly run sushi after MaLaC-CT. Warning: sushi has to be installed!', required=False
    # )
    # parser.add_argument(
    #     "-gofsh", "--goFshConvertingToFsh", action="store_true", help='Directly runs gofsh before MaLaC-CT. Warning: gofsh has to be installed!', required=False
    # )
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
        "-up", "--upload2FhirServer", action="store_true", help='Directly upload the converted FHIR json to the given FHIR Server. Can only be run if all the j2x argument(s) are given.', required=False
    )
    parser.add_argument(
        "-url", "--fhirIgUrl", help="the home adress of the FHIR IG Publisher URL, to fill a predefined url in the resource", required=False
    )
    parser.add_argument(
        "-CSSuppl4VS", "--CodeSystemSupplement4Valueset", action="store_true", help="Creates a CodeSystem supplement for a ValueSet", required=False
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

def convert_fhir_resource(input_filename, input_filename_extension, source_format, target_format, fhir_server_url, fhir_server_user=None, fhir_server_password=None):
    import os
    import requests
    import json
    import xml.dom.minidom

    headers={'Content-Type':'application/fhir+' + source_format + '; charset=utf-8',
             'Accept':'application/fhir+' + target_format + '; charset=utf-8'}

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

    res.raise_for_status()

    with open(target_filename, 'w', newline='', encoding='utf-8') as target_file:
        if target_format == 'json':
            target_file.write(json.dumps(json.loads(res.text), indent=2))
            print("*.4.fhir.json")
        elif target_format == 'xml':
            target_file.write(xml.dom.minidom.parseString(res.text).toprettyxml())
            print("*.4.fhir.xml")
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
        convert_fhir_resource(args.input, '.4.fhir.json', 'json', 'xml', args.json2xmlFHIRServer, args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword)
        args.input = args.input.replace('.4.fhir.json', '.4.fhir.xml')

    # # if the input is a fhir xml or a fhir json, and the output any other classification, than gofsh should be active
    # if ".4.fhir." in args.input and not ".4.fhir." in args.output and not args.goFshConvertingToFsh:
    #     sys.exit("A fhir file as input needs gofsh. Exception: fhir as output. \n %s" % descriptionText)

    # if args.goFshConvertingToFsh and ".4.fhir." in args.input:
    #     import os

    #     print("-------------------- start gofsh --------------------")
    #     startGoFsh = time.time()
    #     os.system("gofsh \""+os.path.dirname(args.input)+"\" -o \""+os.path.dirname(args.input)+"\\o\" -s file-per-definition")
    #     endGoFsh = time.time()
    #     print("-------------------- end gofsh --------------------")
    #     print("gofsh needed "+str(round(endGoFsh-startGoFsh,2))+" seconds.")

    #     # move gofsh fsh to root, delete createrd files afterwards and old file before
    #     if (os.path.exists(args.input.replace(".4.fhir.json",".1.fsh"))):
    #         os.remove(args.input.replace(".4.fhir.json",".1.fsh"))
    #     os.rename(os.path.join(os.path.dirname(args.input),"o","input","fsh",
    #         os.path.basename(args.input.replace(".4.fhir.json","-Instance.fsh"))),args.input.replace(".4.fhir.json",".1.fsh"))
    #     os.remove(os.path.join(os.path.dirname(args.input),"o","input","fsh","index.txt"))
    #     os.rmdir(os.path.join(os.path.dirname(args.input),"o","input","fsh"))
    #     os.rmdir(os.path.join(os.path.dirname(args.input),"o","input"))
    #     os.remove(os.path.join(os.path.dirname(args.input),"o","sushi-config.yaml"))
    #     os.rmdir(os.path.join(os.path.dirname(args.input),"o"))
    #     print("*.1.fsh")

    #     if (args.input.endswith(".4.fhir.json")):
    #         args.input = args.input.replace(".4.fhir.json",".1.fsh")
    #     elif (args.input.endswith(".4.fhir.xml")):
    #         args.input = args.input.replace(".4.fhir.xml",".1.fsh")

    # look at the name of the input file and load the classification,
    iClassValue,iClass = detectClassByEnding(args.input)

    # if it is a fhir input and the output is also fhir, skip the real malac-ct converting
    if not(".4.fhir." in args.input and args.output != None and ".4.fhir." in args.output):
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as inputClass]'

        iModule = __import__(iClassValue[0])
        inputClass = getattr(iModule, iClassValue[1])

        # serialize the input file
        input = inputClass.parse(args.input)
        input.globalUrl = args.fhirIgUrl
        # sort the input
        if "CodeSystem-" in args.input:
            input.sortConceptsExpandStyle()

        # append to all processedTerminology lists
        if args.appendProcessedTerminologyTo:
            input.processedTerminologies = args.appendProcessedTerminologyTo[0]
            for csv2AppendTo in args.appendProcessedTerminologyTo:
                input.appendMetaDataTo(csv2AppendTo)

        # look at the name of the output file and load the classification,
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as outputClass]'
        if args.output != None:
            oClassValue,oClass = detectClassByEnding(args.output)
            oModule = __import__(oClassValue[0])
            outputClass = getattr(oModule, oClassValue[1])

            # open a new file and export to output file
            if not (args.CodeSystemSupplement4Valueset and "ValueSet-" in args.output and oClass == ".1.fsh"):
                with open(args.output, 'w', newline='', encoding='utf-8') as outfile:
                    outputClass.exporto(input, outfile, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                    print("*"+oClass)
            else:
                import os
                with open(args.output, 'w', newline='', encoding='utf-8') as outfileVS:
                    with open(os.path.join(os.path.dirname(args.output),"CodeSystem-zuppl-4-"+os.path.basename(args.output).lower()), 'w', newline='', encoding='utf-8') as outfileCSsuppl:
                        outputClass.exportoSuppl(input, outfileVS, outfileCSsuppl, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                        print("*"+oClass+" and CodeSystem-zuppl-4-*"+oClass)
        # if no output class is given, than convert to all known formats
        else:
            for oClass in listClasses:
                if not args.input.endswith(oClass) or oClass == "svsextelga1": #for the beta there is this exception that svs is no indirect export format!
                    oModule = __import__(listClasses[oClass][0])
                    outputClass = getattr(oModule, listClasses[oClass][1])

                    # open a new file and export to output file
                    if not (args.CodeSystemSupplement4Valueset and "ValueSet-" in args.input and oClass == ".1.fsh"):
                        with open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') as outfile:
                            outputClass.exporto(input, outfile, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                            print("*"+oClass)
                    else:
                        import os
                        with open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') as outfileVS:
                            with open(os.path.join(os.path.dirname(args.input.replace(iClass,oClass)),"CodeSystem-zuppl-4-"+os.path.basename(args.input.replace(iClass,oClass).lower())), 'w', newline='', encoding='utf-8') as outfileCSsuppl:
                                outputClass.exportoZuppl(input, outfileVS, outfileCSsuppl, outputClass, args.argumentLanguage, args.includeHierarchyExtension4ValueSet)
                                print("*"+oClass+" and CodeSystem-zuppl-4-*"+oClass)
        # # converting fsh to json with sushi
        # if (args.sushiConvertingToJson):
        #     import os
        #     import shutil
        #     from pathlib import Path

        #     # directory where sushi will be executed
        #     sushi_base_dir = os.path.dirname(args.input)

        #     # write sushi-config-yml required for sushi conversion
        #     with open(os.path.join(sushi_base_dir,"sushi-config.yaml"), 'w', newline='', encoding='utf-8') as f:
        #         f.writelines("\n".join(["FSHOnly: true","canonical: https://gitlab.com/elga-gmbh/malac-ct","name: MaLaC-CT","status: active", "fhirVersion: 4.0.1"]))

        #     # input directory containing fsh files as expected / required by sushi
        #     # input/fsh within sushi_base_dir
        #     sushi_input_dir = os.path.join(sushi_base_dir, 'input', 'fsh')
        #     # create directories if they do not yet exist
        #     Path(sushi_input_dir).mkdir(parents=True, exist_ok=True)
        #     # copy *.1.fsh to input/fsh
        #     for created_file_name in os.listdir(sushi_base_dir):
        #         if ".1.fsh" in created_file_name:
        #             shutil.copy(os.path.join(sushi_base_dir,created_file_name), sushi_input_dir)

        #     # execute sushi
        #     print("-------------------- start sushi --------------------")
        #     startSushi = time.time()
        #     subprocess.Popen("sushi -v", shell=True).communicate()
        #     subprocess.Popen("sushi \"" + sushi_base_dir + "\" -o \"" + sushi_base_dir + "\"", shell=True).communicate()
        #     endSushi = time.time()
        #     print("-------------------- end sushi --------------------")
        #     print("sushi needed "+str(round(endSushi-startSushi,2))+" seconds.")

        #     # output directory containing json files converted by sushi
        #     # fsh-generated/resources within sushi_base_dir
        #     sushi_output_dir = os.path.join(sushi_base_dir, 'fsh-generated', 'resources')
        #     # copy fhir json created by sushi to sushi_base_dir
        #     created_file_names = os.listdir(sushi_output_dir)
        #     for created_file_name in created_file_names:
        #         if "CodeSystem-" in created_file_name or "ValueSet-" in created_file_name:
        #             # file name with adapted file extension
        #             new_file_name = created_file_name.replace('.json', '.4.fhir.json')
        #             # rename the created json
        #             os.rename(os.path.join(sushi_output_dir, created_file_name), os.path.join(sushi_output_dir, new_file_name))

        #             shutil.copy(os.path.join(sushi_output_dir, new_file_name), sushi_base_dir)
        #         else:
        #             sys.exit("The FHIR Ressource Type could not be detected from the file name. \n %s")

        #     # remove "input" and "fsh-generated" directories as well as sushi-config-yaml
        #     shutil.rmtree(os.path.join(sushi_base_dir,"input"), ignore_errors=True)
        #     shutil.rmtree(os.path.join(sushi_base_dir,"fsh-generated"), ignore_errors=True)
        #     os.remove(os.path.join(sushi_base_dir,"sushi-config.yaml"))

        #     # in case of a ValueSet and the creation of zuppl-files the corresponding FSH-file will be deleted
        #     if (args.CodeSystemSupplement4Valueset and "ValueSet-" in args.input):
        #         # remove the corresponding zuppl-codesystem: CodeSystem-zuppl-4-[NAME-OF-THE-VALUESET-IN-LOWER-CASE].1.fsh
        #         os.remove(os.path.join(sushi_base_dir, "CodeSystem-zuppl-4-" + os.path.basename(args.input).replace(iClass,".1.fsh").lower()))

        #     print("*.4.fhir.json")

    # run converter for only main file, create from xml the json, it doesn't convert the supplement!
    if (url := args.json2xmlFHIRServer):
        if do_fhir_server_conversion:
            convert_fhir_resource(args.input, iClass, 'xml', 'json', args.json2xmlFHIRServer, args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword)

        if (args.upload2FhirServer):
            headers={ 'Content-Type' : 'application/fhir+json; charset=utf-8' }

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

    print("in "+str(round(time.time()-start,2))+" seconds.")
    print("-------------------- MaLaC-CT ended --------------------")

if __name__ == "__main__":
    main()
