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
    return parser

def detectClassByEnding(filename):
    for iclass in listClasses:
        if filename.endswith(iclass):
            return listClasses[iclass],iclass
    sys.exit("The classification could not be detected from the file name. \n %s" % descriptionText)

# todo: get all paths if fhir.json or xml is the output format
def main() -> None:
    start = time.time()
    sys.stdout.write("MaLaC-CT converted\n")
    
    parser = init_argparse()
    args = parser.parse_args()

    sys.stdout.write(args.input+" to\n")

    # if the input is a fhir xml or a fhir json, and the output any other classification, then do that
    if (args.goFshConvertingToFsh or ("fhir" in args.input and args.output == None) or ("fhir" in args.input and args.output != None and not "fhir" in args.output)):
        import os

        sys.stdout.write("-------------------- start gofsh --------------------\n")
        startGoFsh = time.time()
        os.system("gofsh \""+os.path.dirname(args.input)+"\" -o \""+os.path.dirname(args.input)+"\\o\" -s file-per-definition")
        endGoFsh = time.time()
        sys.stdout.write("-------------------- end gofsh --------------------\n")
        sys.stdout.write("gofsh needed "+str(round(endGoFsh-startGoFsh,2))+" seconds.\n")

        # move gofsh fsh to root, delete createrd files afterwards and old file before
        if (os.path.exists(args.input.replace(".4.fhir.json",".1.fsh"))):
            os.remove(args.input.replace(".4.fhir.json",".1.fsh"))
        os.rename(os.path.dirname(args.input)+"\\o\\input\\fsh\\"+
            os.path.basename(args.input.replace(".4.fhir.json","-Instance.fsh")),args.input.replace(".4.fhir.json",".1.fsh"))
        os.remove(os.path.dirname(args.input)+"\\o\\input\\fsh\\index.txt")
        os.rmdir(os.path.dirname(args.input)+"\\o\\input\\fsh")
        os.rmdir(os.path.dirname(args.input)+"\\o\\input")
        os.remove(os.path.dirname(args.input)+"\\o\\sushi-config.yaml")
        os.rmdir(os.path.dirname(args.input)+"\\o")
        sys.stdout.write("*.1.fsh\n")

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

        # serialize the input file,
        input = inputClass.parse(args.input)

        # look at the name of the output file and load the classification, 
        # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as outputClass]'
        if args.output != None:
            oClassValue,oClass = detectClassByEnding(args.output)
            oModule = __import__(oClassValue[0])
            outputClass = getattr(oModule, oClassValue[1])

            # open a new file and export to output file
            outfile = open(args.output, 'w', newline='', encoding='utf-8') 
            outputClass.exporto(input, outfile, outputClass, args.argumentLanguage)
            sys.stdout.write("*"+oClass+"\n")
        # if no output class is given, than convert to all known formats
        else:
            for oClass in listClasses:
                if not args.input.endswith(oClass):
                    oModule = __import__(listClasses[oClass][0])
                    outputClass = getattr(oModule, listClasses[oClass][1])

                    # open a new file and export to output file
                    outfile = open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') 
                    outputClass.exporto(input, outfile, outputClass, argsLang=args.argumentLanguage)
                    sys.stdout.write("*"+oClass+"\n")
        # converting fsh to json with sushi
        if (args.sushiConvertingToJson):
            import os
            # TODO dirname has to be functional if a relative path is given
            # TODO sushi should only use one fsh-file, not all files in dir
            # TODO different file name to title could be supported
            with open(os.path.dirname(args.input)+"/sushi-config.yaml", 'w', newline='', encoding='utf-8') as f:
                f.writelines("\n".join(["FSHOnly: true","canonical: https://gitlab.com/elga-gmbh/malac-ct","name: MaLaC-CT","status: active", "fhirVersion: 4.0.1"]))
            # run sushi, create json, rename .2.fsh file to escape sushi and rename back
            #os.rename(args.input.replace(iClass,".2.fsh"),args.input.replace(iClass,".2.fshy"))
            sys.stdout.write("-------------------- start sushi --------------------\n")
            startSushi = time.time()
            subprocess.call(["sushi","-v"], shell=True)
            subprocess.call(["sushi",os.path.dirname(args.input),"-o",os.path.dirname(args.input)], shell=True)
            endSushi = time.time()
            sys.stdout.write("-------------------- end sushi --------------------\n")
            sys.stdout.write("sushi needed "+str(round(endSushi-startSushi,2))+" seconds.\n")
            #os.rename(args.input.replace(iClass,".2.fshy"),args.input.replace(iClass,".2.fsh"))
            
            # move fhir json to root, delete old file before
            if (os.path.exists(args.input.replace(iClass,".4.fhir.json"))):
                os.remove(args.input.replace(iClass,".4.fhir.json"))
            if ("/CS-" in args.input):
                os.rename(os.path.dirname(args.input)+"/input/vocabulary/CodeSystem-"+
                    os.path.basename(args.input.replace(iClass,".json")),args.input.replace(iClass,".4.fhir.json"))
            elif ("/VS-" in args.input):
                os.rename(os.path.dirname(args.input)+"/input/vocabulary/ValueSet-"+
                    os.path.basename(args.input.replace(iClass,".json")),args.input.replace(iClass,".4.fhir.json"))
            else:
                sys.exit("The FHIR Ressource Type could not be detected from the file name. \n %s" % descriptionText)
            os.rmdir(os.path.dirname(args.input)+"/input/vocabulary")
            os.rmdir(os.path.dirname(args.input)+"/input")
            os.remove(os.path.dirname(args.input)+"/sushi-config.yaml")
            sys.stdout.write("*.4.fhir.json\n")
            
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
                res = requests. post(url+"$convert", headers=headers, data=json_format_file) # files={'upload_file': json_format_file})
            else:
                res = requests.post(url+"$convert", headers=headers, auth=auth, data=json_format_file) # files={'upload_file': json_format_file})
        
        import os
        if os.path.exists(args.input.replace(iClass,".4.fhir.xml")):
            os.remove(args.input.replace(iClass,".4.fhir.xml"))
        res.raise_for_status()
        with open(args.input.replace(iClass,".4.fhir.xml"), 'w', newline='', encoding='utf-8') as xml_format_file:
            xml_format_file.write(xml.dom.minidom.parseString(res.text).toprettyxml())
        sys.stdout.write("*.4.fhir.xml\n")

    sys.stdout.write("in "+str(round(time.time()-start,2))+" seconds.")

if __name__ == "__main__":
    main()