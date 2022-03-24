import sys
import prop_csv_and_master as pcam
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
        return self.f4superclass.get_resource()

    def get_url(self):
        if tmp := super(self.f4superclass, self).get_url():
            return tmp.get_value()
        else:
            return None

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
        if tmp := super(self.f4superclass, self).get_implicitRules():
            return tmp.get_value()
        else:
            return None

    def get_language(self):
        if tmp := super(self.f4superclass, self).get_language():
            return tmp.get_value()
        return None

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
            if tmp := one_f4_identifier.get_value():
                identifier_list.append(tmp.get_value())
        return identifier_list

    def get_experimental(self):
        if tmp := super(self.f4superclass, self).get_experimental():
            return tmp.get_value()
        return None

    def get_date(self):
        return super(self.f4superclass, self).get_date().get_value()

    def get_publisher(self):
        if tmp := super(self.f4superclass, self).get_publisher():
            return tmp.get_value()
        return None

    def get_contact(self):
        f4_contact_list = super(self.f4superclass, self).get_contact()
        contact_list = []
        for one_contact in f4_contact_list:
            the_contact_detail = pcam.ContactDetail()
            if tmp := one_contact.get_name():
                the_contact_detail.name = tmp.get_value()
            for one_contact_point in one_contact.get_telecom():
                the_contact_point = pcam.ContactDetail.ConcactPoint()
                if tmp := one_contact_point.get_system():
                    the_contact_point.system = tmp.get_value()
                if tmp := one_contact_point.get_value():
                    the_contact_point.value = tmp.get_value()
                if tmp := one_contact_point.get_use():
                    the_contact_point.use = tmp.get_value()
                if tmp := one_contact_point.get_rank():
                    the_contact_point.value = tmp.get_value()
                if tmp := one_contact_point.get_period():
                    the_contact_point.value = tmp.get_value()
                the_contact_detail.telecom.append(the_contact_point)
            contact_list.append(the_contact_detail)
        return contact_list

    # TODO not fully supported yet, UsageContext is a complex datatype, and there may be 0..*
    #
    # right now it is not clear, how the elements should be processed
    #
    # see http://www.hl7.org/fhir/metadatatypes.html#UsageContext
    def get_usecontext(self):
        return []

    # TODO not fully supported yet, CodeableConcept is a complex datatype
    #
    # right now it is not clear, how the elements should be processed
    #
    # see http://www.hl7.org/fhir/datatypes.html#CodeableConcept
    def get_jurisdiction(self):
        return []

    def get_purpose(self):
        if tmp := super(self.f4superclass, self).get_purpose():
            return tmp.get_value()
        return None

    def get_copyright(self):
        if tmp := super(self.f4superclass, self).get_copyright():
            return tmp.get_value()
        return None

    def get_immutable(self):
        if tmp := super(self.f4superclass, self).get_immutable():
            return tmp.get_value()
        return None

    def get_lockeddate(self):
        return self.f4superclass.get_lockeddate(self)



f4cs.supermod.CodeSystem.subclass = FHIR4CsAndVs
f4vs.supermod.ValueSet.subclass = FHIR4CsAndVs
