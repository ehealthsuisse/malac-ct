import argparse
import subprocess
import sys
import time

# list of accepted input formats: ClaML-> claml, valueSet -> IHE SVS, CodeSystem -> FHIR CodeSystem, ValueSet -> FHIR ValueSet 
# dictionary with key as fileending, first element value with module and second element 
listClasses = {".1.propcsv.csv": ["prop_csv_and_master", "PropCsvAndMaster"],
    ".2.claml.xml":["claml2", "ClaML2Sub"],
    ".3.claml.xml":["claml3", "ClaML3Sub"],
    ".1.fsh":["fsh1", "Fsh1"],
    ".2.fsh":["fsh2", "Fsh2"],
    ".1.svsextelga.xml":["svsextelga1", "SVSextELGA1Sub"]
    #".4.fhir.json":["fhir4json", "FHIR4json"],
    #".4.fhir.xml":["fhir4xml", "FHIR4xml"]
    }# nice2have ,IHEsvs, ArtDecor)
descriptionText = "This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and output classes are right now ClaML 2.0.0 with a file ending \".2.claml.xml\", ClaML 3.0.0 with a file ending \".3.claml.xml\", HL7 FHIR Shorthand 1.3.0 with a file ending \".1.fsh\", HL7 FHIR Shorthand 2.0.0 with a file ending \".2.fsh\" and a predefined CSV a file ending \".1.csv\"."

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
        "-langArg", "--argumentLanguage", help='the language element for the output classification', required=False
    )
    parser.add_argument(
        "-sushi", "--sushiConvertingToJson", action="store_true", help='Directly run sushi after MaLaC-CT. Warning: sushi has to be installed!', required=False
    )
    parser.add_argument(
        "-gofsh", "--goFshConvertingToFsh", action="store_true", help='Directly run gofsh before MaLaC-CT. Warning: gofsh has to be installed!', required=False
    )
    parser.add_argument(
        "-j2xServer", "--json2xmlFHIRServer", help="Directly run a json2xml convert on a given FHIR server after sushi. "+
        "the FHIR Server adress including the base path wraped into quotation marks. e.g.:"+
        '--user fhiruser:fhiruserpassword "http://ibmfhir.quantumeconomy.org/fhir-server/api/v4/"'+
        "Warning: a json has to exists, that is usually generated via sushi!", required=False
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
        "-CSSuppl4VS", "--CodeSystemSupplement4Valueset", action="store_true", help="Creates a CodeSystem Supplement for a ValueSet", required=False
    )

    return parser

def detectClassByEnding(filename):
    for iclass in listClasses:
        if filename.endswith(iclass):
            return listClasses[iclass],iclass
    sys.exit("The classification could not be detected from the file name. \n %s" % descriptionText)

# todo: get all paths if fhir.json or xml is the output format
def main() -> None:
    start = time.time()
    print("-------------------- MaLaC-CT started --------------------")
    
    parser = init_argparse()
    args = parser.parse_args()

    print("converted "+args.input+" to")

    # if the input is a fhir xml or a fhir json, and the output any other classification, then do that
    if (args.goFshConvertingToFsh or ("fhir" in args.input and args.output == None) or ("fhir" in args.input and args.output != None and not "fhir" in args.output)):
        import os

        print("-------------------- start gofsh --------------------")
        startGoFsh = time.time()
        os.system("gofsh \""+os.path.dirname(args.input)+"\" -o \""+os.path.dirname(args.input)+"\\o\" -s file-per-definition")
        endGoFsh = time.time()
        print("-------------------- end gofsh --------------------")
        print("gofsh needed "+str(round(endGoFsh-startGoFsh,2))+" seconds.")

        # move gofsh fsh to root, delete createrd files afterwards and old file before
        if (os.path.exists(args.input.replace(".4.fhir.json",".1.fsh"))):
            os.remove(args.input.replace(".4.fhir.json",".1.fsh"))
        os.rename(os.path.join(os.path.dirname(args.input),"o","input","fsh",
            os.path.basename(args.input.replace(".4.fhir.json","-Instance.fsh"))),args.input.replace(".4.fhir.json",".1.fsh"))
        os.remove(os.path.join(os.path.dirname(args.input),"o","input","fsh","index.txt"))
        os.rmdir(os.path.join(os.path.dirname(args.input),"o","input","fsh"))
        os.rmdir(os.path.join(os.path.dirname(args.input),"o","input"))
        os.remove(os.path.join(os.path.dirname(args.input),"o","sushi-config.yaml"))
        os.rmdir(os.path.join(os.path.dirname(args.input),"o"))
        print("*.1.fsh")

        if (args.input.endswith(".4.fhir.json")):
            args.input = args.input.replace(".4.fhir.json",".1.fsh")
        elif (args.input.endswith(".4.fhir.xml")):
            args.input = args.input.replace(".4.fhir.xml",".1.fsh")

    # look at the name of the input file and load the classification, 
    iClassValue,iClass = detectClassByEnding(args.input)

    # if it is a fhir input and the output is also fhir, skip the true converting
    if not("fhir" in args.input and args.output != None and "fhir" in args.output):
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as inputClass]'
        
        iModule = __import__(iClassValue[0])
        inputClass = getattr(iModule, iClassValue[1])

        # serialize the input file
        inputClass.globalUrl = args.fhirIgUrl
        input = inputClass.parse(args.input)

        # look at the name of the output file and load the classification, 
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as outputClass]'
        if args.output != None:
            oClassValue,oClass = detectClassByEnding(args.output)
            oModule = __import__(oClassValue[0])
            outputClass = getattr(oModule, oClassValue[1])

            # open a new file and export to output file
            if not (args.CodeSystemSupplement4Valueset and "ValueSet-" in args.output and oClass == ".1.fsh"): 
                with open(args.output, 'w', newline='', encoding='utf-8') as outfile:
                    outputClass.exporto(input, outfile, outputClass, args.argumentLanguage)
                    print("*"+oClass)
            else:
                import os
                with open(args.output, 'w', newline='', encoding='utf-8') as outfileVS:
                    with open(os.path.join(os.path.dirname(args.output),"CodeSystem-zuppl-4-"+os.path.basename(args.output).lower()), 'w', newline='', encoding='utf-8') as outfileCSsuppl:
                        outputClass.exportoSuppl(input, outfileVS, outfileCSsuppl, outputClass, args.argumentLanguage)
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
                            outputClass.exporto(input, outfile, outputClass, argsLang=args.argumentLanguage)
                            print("*"+oClass)
                    else:
                        import os
                        with open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') as outfileVS:
                            with open(os.path.join(os.path.dirname(args.input.replace(iClass,oClass)),"CodeSystem-suppl-4-"+os.path.basename(args.input.replace(iClass,oClass).lower())), 'w', newline='', encoding='utf-8') as outfileCSsuppl:
                                outputClass.exportoSuppl(input, outfileVS, outfileCSsuppl, outputClass, args.argumentLanguage)
                                print("*"+oClass+" and CodeSystem-suppl-4-*"+oClass)
        # converting fsh to json with sushi
        if (args.sushiConvertingToJson):
            import os
            # TODO dirname has to be functional if a relative path is given
            # TODO sushi should only use one fsh-file, not all files in dir
            # TODO different file name to title could be supported
            with open(os.path.join(os.path.dirname(args.input),"sushi-config.yaml"), 'w', newline='', encoding='utf-8') as f:
                f.writelines("\n".join(["FSHOnly: true","canonical: https://gitlab.com/elga-gmbh/malac-ct","name: MaLaC-CT","status: active", "fhirVersion: 4.0.1"]))
            # run sushi, create json, rename .2.fsh file to escape sushi and rename back
            tmp = os.path.dirname(args.input) 
            for file_name in os.listdir(os.path.dirname(args.input)):
                if ".2.fsh" in file_name:
                    os.rename(os.path.join(os.path.dirname(args.input),file_name),os.path.join(os.path.dirname(args.input),file_name.replace(".2.fsh",".2.fshy")))
            print("-------------------- start sushi --------------------")
            startSushi = time.time()
            subprocess.Popen("sushi -v", shell=True).communicate()
            subprocess.Popen("sushi \""+os.path.dirname(args.input)+"\" -o \""+os.path.dirname(args.input)+"\"", shell=True).communicate()
            endSushi = time.time()
            print("-------------------- end sushi --------------------")
            print("sushi needed "+str(round(endSushi-startSushi,2))+" seconds.")
            for file_name in os.listdir(os.path.dirname(args.input)):
                if ".2.fshy" in file_name:
                    os.rename(os.path.join(os.path.dirname(args.input),file_name),os.path.join(os.path.dirname(args.input),file_name.replace(".2.fshy",".2.fsh")))
            
            # move fhir json to root, delete old file before
            file_names = os.listdir(os.path.join(os.path.dirname(args.input),"input","vocabulary"))
            for file_name in file_names:
                if ("CodeSystem-" in file_name) or ("ValueSet-" in file_name):
                    if os.path.exists(os.path.join(os.path.dirname(args.input),file_name.replace(".json",".4.fhir.json").replace("input","").replace("vocabulary",""))):
                        os.remove(os.path.join(os.path.dirname(args.input),file_name.replace(".json",".4.fhir.json").replace("input","").replace("vocabulary","")))
                    os.rename(os.path.join(os.path.dirname(args.input),"input","vocabulary",file_name),
                        os.path.join(os.path.dirname(args.input),file_name.replace(".json",".4.fhir.json").replace("input","").replace("vocabulary","")))
                else:
                    sys.exit("The FHIR Ressource Type could not be detected from the file name. \n %s" % descriptionText)

            os.rmdir(os.path.join(os.path.dirname(args.input),"input","vocabulary"))
            os.rmdir(os.path.join(os.path.dirname(args.input),"input"))
            os.remove(os.path.join(os.path.dirname(args.input),"sushi-config.yaml"))
            print("*.4.fhir.json")
    
    # TODO convert all .4.fhir.json to xml, not only main one
    # run converter, create from json a xml       
    if (url := args.json2xmlFHIRServer):
        import requests
        import xml.dom.minidom
         
        headers={ 'Content-Type' : 'application/fhir+json; charset=utf-8' ,  'Accept' : 'application/fhir+xml; charset=utf-8' }
        auth = None
        if (args.json2xmlFHIRServerUser and args.json2xmlFHIRServerUserPassword):
            auth = (args.json2xmlFHIRServerUser, args.json2xmlFHIRServerUserPassword) 

        with open(args.input.replace(iClass,".4.fhir.json"), 'rb') as json_format_file:
            if auth is None:
                res = requests.post(url+"$convert", headers=headers, data=json_format_file) # files={'upload_file': json_format_file})
            else:
                res = requests.post(url+"$convert", headers=headers, auth=auth, data=json_format_file) # files={'upload_file': json_format_file})
        
        import os
        if os.path.exists(args.input.replace(iClass,".4.fhir.xml")):
            os.remove(args.input.replace(iClass,".4.fhir.xml"))
        res.raise_for_status()
        with open(args.input.replace(iClass,".4.fhir.xml"), 'w', newline='', encoding='utf-8') as xml_format_file:
            xml_format_file.write(xml.dom.minidom.parseString(res.text).toprettyxml())
        print("*.4.fhir.xml")

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
