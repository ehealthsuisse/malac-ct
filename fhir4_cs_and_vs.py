import sys
import fhir4_codesystem as f4cs
import fhir4_valueset as f4vs

class FHIR4CsAndVs(f4cs.CodeSystemSub, f4vs.ValueSetSub):
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

    def build(self, rootNode):
        if 'CodeSystem' in rootNode.tag:
            self.f4superclass = f4cs.CodeSystemSub
            super(self.f4superclass, self).build(rootNode)
        elif 'ValueSet' in rootNode.tag:
            self.f4superclass = f4vs.ValueSetSub
            super(self.f4superclass, self).build(rootNode)
        else:
            sys.exit('Filename does not comply with convention: either "CodeSystem" or "ValueSet"')

    def get_resource(self):
        return super(self.f4superclass, self).get_resource()

    def get_url(self):
        return super(self.f4superclass, self).get_url().get_value()

    def get_version(self):
        return super(self.f4superclass, self).get_version().get_value()

    def get_name(self):
        return super(self.f4superclass, self).get_name().get_value()

    def get_title(self):
        return super(self.f4superclass, self).get_title().get_value()

    def get_status(self):
        return super(self.f4superclass, self).get_status().get_value()

    def get_description(self):
        return super(self.f4superclass, self).get_description().get_value()

    def get_implicitrules(self):
        return super(self.f4superclass, self).get_implicitRules().get_value()

    def get_language(self):
        return super(self.f4superclass, self).get_language().get_value()

    # within fhir-base.xsd "text" has been removed from DomainResource
    #
    # DomainResource/text is of type Narrative which itself allows a lot
    # of further tags which eventually would result in two "Class code()" in
    # the generated python files by generateDS.
    # As DomainResource/text is not required it will no longer be supported
    # by MaLaC-CT.
    def get_text(self):
        return None

    # within fhir-base.xsd "contained" has been removed from DomainResource
    #
    # DomainResource/contained results in circular imports which makes it
    # difficult to create proper python classes with generateDS.
    # As a result it has been decided that "contained" resources will not
    # be supported by MaLaC-CT.
    def get_contained(self):
        return None

    # TODO not fully supported yet, supermod.Extension is a complex datatype, and there may be 0..*
    # see http://www.hl7.org/fhir/domainresource.html
    def get_extension(self):
        return None

    # TODO not fully supported yet, supermod.Extension is a complex datatype, and there may be 0..*
    # see http://www.hl7.org/fhir/domainresource.html
    def get_modifierextension(self):
        return None

    # TODO currently, only value may be retrieved - even if there is more information available
    def get_identifier(self):
        f4_identifier_list = super(self.f4superclass, self).get_identifier()
        identifier_list = []
        for one_f4_identifier in f4_identifier_list:
            if one_f4_identifier.get_value():
                identifier_list.append(one_f4_identifier.get_value())
        return identifier_list

    def get_experimental(self):
        return super(self.f4superclass, self).get_experimental().get_value()

    def get_date(self):
        return super(self.f4superclass, self).get_date().get_value()

    def get_publisher(self):
        return super(self.f4superclass, self).get_publisher().get_value()

    def get_contact(self):
        return super(self.f4superclass, self).get_contact()

f4cs.supermod.CodeSystem.subclass = FHIR4CsAndVs
f4vs.supermod.ValueSet.subclass = FHIR4CsAndVs
