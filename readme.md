# MaLaC-CT - Markup Language Converter for Clinical Terminologies
This is the MArkup LAnguage Converter for Clinical Terminologies, short MaLaC-CT. Accepted and automaticly detected input and possible output classes are right now ClaML 3.0.0 with param "claml3", HL7 FHIR Shorthand 1.1.0 with param "fsh1" and a predefined CSV with param "propCsv1".
## How to use
* malac_ct.py -i INPUT-FILE-PATH -o OUTPUT-FILE-PATH -oclass OUTPUT-CLASSIFICATION [-argsLang OUTPUT-LANGUAGE]
  * "-i", "--input", help='the input file, classification is detected automaticly', required=True
  * "-o", "--output", help='the output file', required=True
  * "-oclass", "--outputClassification", help='the output files classification', required=True
  * "-argsLang", "--argumentLanguage", help='the language for the output classification', required=False
## How to expand
The easy expandability is given by descending from the prop_csv_and_master.py . All the getter, the parse and the exporto function should be implemented, to convert your new classification. Don't forget to add the new classification to the malac_ct.py argument handling!
## Class Diagramm
![Class Diagramm](class_diagramm.png "Class_Diagramm")
