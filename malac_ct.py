import argparse
import sys
import xml.etree.ElementTree as ET

#The list of accepted input formats: ClaML-> claml, valueSet -> IHE SVS, CodeSystem -> FHIR CodeSystem, ValueSet -> FHIR ValueSet 
listClasses = ("propCsv","ClaML3","fsh1")# nice2have ,IHEsvs, ArtDecor)

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s -i INPUT-FILE-PATH -o OUTPUT-FILE-PATH -oclass OUTPUT-CLASSIFICATION",
        description="This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and possible output classes are right now ClaML 3.0.0, HL7 FHIR, FHIR Shorthand and a predefined CSV."
    )
    parser.add_argument(
        "-i", "--input", help='the input file, classification is detected automaticly', required=True
    )
    parser.add_argument(
        "-o", "--output", help='the output file', required=True
    )
    parser.add_argument(
        "-oclass", "--outputClassification", help='the output files classification', required=True
    )
    parser.add_argument(
        "-argsLang", "--argumentLanguage", help='the language for the output classification'
    )
    return parser

def detectInputClassByRootElement(root) -> str:
    for iclass in listClasses:
        if root.tag == iclass:
            return iclass

def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    
    #a short validation of oclass to exit before doing anything else
    if(args.outputClassification == "propCsv"):
        from prop_csv_and_master import PropCsvAndMaster as outputClass
    elif(args.outputClassification == "ClaML3"):
        from claml3 import ClaML3Sub as outputClass
    elif(args.outputClassification == "fsh1"):
        from fsh1 import Fsh1 as outputClass
    else:
        sys.exit("Your output classification is not a valid one. Please choose between propCsv, ClaML3 or fsh1.")

    #look into the input file and get the classification
    inputEnding = args.input.split('.')
    if(inputEnding[1] == "csv"):
        import prop_csv_and_master as inputClass
    elif(inputEnding[1] == "xml"):
        import claml3 as inputClass
    elif(inputEnding[1] == "fsh"):
        import fsh1 as inputClass
    else:
        sys.exit("Your input classification could not be detected from the input file. Please check your input file.")

    input = inputClass.parse(args.input)
    outfile = open(args.output, 'w', newline='', encoding='utf-8') 
    outputClass.exporto(input, outfile, args.argumentLanguage)
    
if __name__ == "__main__":
    main()