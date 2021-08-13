import argparse
import sys

# list of accepted input formats: ClaML-> claml, valueSet -> IHE SVS, CodeSystem -> FHIR CodeSystem, ValueSet -> FHIR ValueSet 
# dictionary with key as fileending, first element value with module and second element 
listClasses = {".1.propcsv.csv": ["prop_csv_and_master", "PropCsvAndMaster"],
    ".2.claml.xml":["claml2", "ClaML2Sub"],
    ".3.claml.xml":["claml3", "ClaML3Sub"],
    ".1.fsh":["fsh1", "Fsh1"],
    ".2.fsh":["fsh2", "Fsh2"]}# nice2have ,IHEsvs, ArtDecor)
descriptionText = "This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and output classes are right now ClaML 2.0.0 with a file ending \".2.claml.xml\", ClaML 3.0.0 with a file ending \".3.claml.xml\", HL7 FHIR Shorthand 1.3.0 with a file ending \".1.fsh\", HL7 FHIR Shorthand 2.0.0 with a file ending \".2.fsh\" and a predefined CSV a file ending \".1.csv\"."

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s -i INPUT-FILE-PATH [-o OUTPUT-FILE-PATH] [-argsLang OUTPUT-LANGUAGE]",
        description=descriptionText
    )
    parser.add_argument(
        "-i", "--input", help='the input file, classification is detected automaticly', required=True
    )
    parser.add_argument(
        "-o", "--output", help='the output file, if none is given MaLaC-CT will convert into all other known formats.'
    )
    parser.add_argument(
        "-argsLang", "--argumentLanguage", help='the language element for the output classification', required=False
    )
    return parser

def detectClassByEnding(filename):
    for iclass in listClasses:
        if filename.endswith(iclass):
            return listClasses[iclass],iclass
    sys.exit("The classification could not be detected from the file name. \n %s", descriptionText)

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()

    # look at the name of the input file and load the classification, 
    # does the same as 'from [modulename/iClass[0]] import [classname/iClass[1]] as inputClass]'
    iClassValue,iClass = detectClassByEnding(args.input)
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
    # if no output class is given, than convert to all known formats
    else:
        for oClass in listClasses:
            if not args.input.endswith(oClass):
                oModule = __import__(listClasses[oClass][0])
                outputClass = getattr(oModule, listClasses[oClass][1])

                # open a new file and export to output file
                outfile = open(args.input.replace(iClass,oClass), 'w', newline='', encoding='utf-8') 
                outputClass.exporto(input, outfile, outputClass, argsLang=args.argumentLanguage)
    
    
if __name__ == "__main__":
    main()