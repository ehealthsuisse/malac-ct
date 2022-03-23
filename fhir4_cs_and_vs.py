import sys
import fhir4_codesystem as f4cs
import fhir4_valueset as f4vs

class FHIR4CsAndVs:
    def __init__(self, *args_, **kwargs_):
        super(FHIR4CsAndVs, self).__init__(*args_, **kwargs_)

    # just for calling the outer method (within )
    def parse(inFilename):
        if 'CodeSystem-' in inFilename:
            return f4cs.parse(inFilename)
        elif 'ValueSet-' in inFilename:
            return f4vs.parse(inFilename)
        else:
            sys.exit('Filename does not comply with convention: either "CodeSystem-" or "ValueSet-"')

    # def build(self, rootNode):
    #     if 'CodeSystem' in rootNode.tag:
    #         self.f4superclass = f4cs.CodeSystemSub
    #         super(self.f4superclass, self).build(rootNode)
    #     elif 'ValueSet' in rootNode.tag:
    #         self.f4superclass = f4vs.ValueSetSub
    #         super(self.f4superclass, self).build(rootNode)
    #     else:
    #         sys.exit('Filename does not comply with convention: either "CodeSystem" or "ValueSet"')



# f4cs.supermod.CodeSystem.subclass = FHIR4CsAndVs
# f4vs.supermod.ValueSet.subclass = FHIR4CsAndVs
