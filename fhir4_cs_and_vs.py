import sys
import fhir4_codesystem as f4cs
import fhir4_valueset as f4vs

class FHIR4CsAndVs:
    def __init__(self) -> None:
        pass

    # just for calling the outer method (within )
    def parse(inFilename):
        if 'CodeSystem-' in inFilename:
            return f4cs.parse(inFilename)
        elif 'ValueSet-' in inFilename:
            return f4vs.parse(inFilename)
        else:
            sys.exit('Filename does not comply with convention: either "CodeSystem-" or "ValueSet-"')