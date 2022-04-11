import sys
import prop_csv_and_master as pcam
import fhir4_codesystem as f4cs
import fhir4_valueset as f4vs

# get_id() is not supported

# get_meta() is not supported

def get_implicitrules(self):
    if tmp := self.get_implicitRules():
        return tmp.get_value()
    return None

def get_language(self):
    if tmp := self.get_language():
        return tmp.get_value()
    return None

# NOT SUPPORTED
#
# within fhir-base.xsd "text" has been removed from DomainResource
#
# DomainResource/text is of type Narrative which itself allows a lot
# of further tags which eventually would result in two "Class code()" in
# the generated python files by generateDS.
# As DomainResource/text is not required it will no longer be supported
# by MaLaC-CT.
def get_text(self):
    return None

# NOT SUPPORTED
#
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

def get_url(self):
    if tmp := self.get_url():
        return tmp.get_value()
    return None

# TODO currently, only value may be retrieved - even if there is more information available
# see http://www.hl7.org/fhir/datatypes.html#Identifier
def get_identifier(self):
    identifier_list = self.get_identifier()
    the_identifier_list = []
    for one_f4_identifier in identifier_list:
        if tmp := one_f4_identifier.get_value():
            the_identifier_list.append(tmp.get_value().replace('urn:oid:', ''))
    return the_identifier_list

def get_version(self):
    if tmp := self.get_version():
        return tmp.get_value()
    return None

def get_name(self):
    if tmp := self.get_name():
        # In case of FHIR CodeSystem or ValueSet get_name() returns an object which
        # has got a 'get_value' attribute.
        # In case of zuppl-creation self.name will be set within fsh1.py#exportoSuppl()
        # and will not have the 'get_value' attribute as it is a simple str object.
        if hasattr(tmp, 'get_value'):
            return tmp.get_value()
        else:
            return tmp
    return None

def get_title(self):
    if tmp := self.get_title():
        # In case of FHIR CodeSystem or ValueSet get_title() returns an object which
        # has got a 'get_value' attribute.
        # In case of zuppl-creation self.title will be set within fsh1.py#exportoSuppl()
        # and will not have the 'get_value' attribute as it is a simple str object.
        if hasattr(tmp, 'get_value'):
            return tmp.get_value()
        else:
            return tmp
    return None

def get_status(self):
    if tmp := self.get_status():
        return tmp.get_value()
    return None

def get_experimental(self):
    if tmp := self.get_experimental():
        return tmp.get_value()
    return None

def get_date(self):
    if tmp := self.get_date():
        return tmp.get_value()
    return None

def get_publisher(self):
    if tmp := self.get_publisher():
        return tmp.get_value()
    return None

def get_contact(self):
    contact_list = self.get_contact()
    the_contact_list = []
    for one_contact in contact_list:
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

            # TODO FHIR ContactPoint.period consists of start and end.
            #      pcam.ContactDetail.ContactPoint however has got a single value for 'period'
            #      Not clear how to transform.

            the_contact_detail.telecom.append(the_contact_point)
        the_contact_list.append(the_contact_detail)
    return the_contact_list

def get_description(self):
    if tmp := self.get_description():
        return tmp.get_value()
    return None

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
    if tmp := self.get_purpose():
        return tmp.get_value()
    return None

def get_copyright(self):
    if tmp := self.get_copyright():
        return tmp.get_value()
    return None

def parse_concept_designation(designation_list):
    the_designation_list = []

    for one_designation in designation_list:
        the_designation = pcam.ConceptDesignation()

        if tmp := one_designation.get_language():
            the_designation.language = tmp.get_value()

        if tmp := one_designation.get_use():
            if tmp := tmp.get_code():
                the_designation.use = tmp.get_value()

        if tmp := one_designation.get_value():
            the_designation.value = tmp.get_value()

        the_designation_list.append(the_designation)

    return the_designation_list

def exporto_concept_designation(supermod, designation_class, designation_list):
    the_designation_list = []

    for one_designation in designation_list:
        the_designation = designation_class()

        if tmp := one_designation.language:
            the_designation.set_language(supermod.code(value=tmp))

        if tmp := one_designation.use:
            the_designation.set_use(supermod.Coding(code=supermod.code(value=tmp)))

        if tmp := one_designation.value:
            the_designation.set_value(supermod.string(value=tmp))

        the_designation_list.append(the_designation)

    return the_designation_list

def exporto(self, supermod, fhir_resource, args_lang):
    # TODO id is not supported

    # TODO meta is not supported

    if tmp := self.get_implicitrules():
        fhir_resource.set_implicitRules(supermod.uri(value=tmp))

    if tmp := self.get_language():
        fhir_resource.set_language(supermod.code(value=tmp))

    # TODO text is not supported

    # TODO contained is not supported

    # TODO extension is not supported

    # TODO modifierextension is not supported

    if tmp := self.get_url():
        fhir_resource.set_url(supermod.uri(value=tmp))

    if tmp := self.get_identifier():
        for one_identifier in tmp:
            the_identifier = supermod.Identifier()
            the_identifier.set_use(supermod.IdentifierUse(value='official'))
            the_identifier.set_system(supermod.uri(value='urn:ietf:rfc:3986'))
            the_identifier.set_value(supermod.string(value='urn:oid:' + one_identifier))
            fhir_resource.add_identifier(the_identifier)

    if tmp := self.get_version():
        fhir_resource.set_version(supermod.string(value=tmp))

    if tmp := self.get_name():
        fhir_resource.set_name(supermod.string(value=tmp))

    if tmp := self.get_title():
        fhir_resource.set_title(supermod.string(value=tmp))

    if tmp := self.get_status():
        fhir_resource.set_status(supermod.PublicationStatus(value=tmp))

    if tmp := self.get_experimental():
        fhir_resource.set_experimental(supermod.boolean(value=tmp))

    if tmp := self.get_date():
        fhir_resource.set_date(supermod.dateTime(value=tmp))

    if tmp := self.get_publisher():
        fhir_resource.set_publisher(supermod.string(value=tmp))

    if tmp := self.get_contact():
        contact_list = tmp
        for one_contact in contact_list:
            the_contact = supermod.ContactDetail()

            if tmp := one_contact.name:
                the_contact.set_name(supermod.string(tmp))

            if tmp := one_contact.telecom:
                contact_point_list = tmp
                for one_contact_point in contact_point_list:
                    the_contact_point = supermod.ContactPoint()

                    if tmp := one_contact_point.system:
                        the_contact_point.set_system(supermod.ContactPointSystem(value=tmp))

                    if tmp := one_contact_point.value:
                        the_contact_point.set_value(supermod.string(value=tmp))

                    if tmp := one_contact_point.use:
                        the_contact_point.set_use(supermod.ContactPointUse(value=tmp))

                    if tmp := one_contact_point.rank:
                        the_contact_point.set_rank(supermod.positiveInt(value=tmp))

                    # TODO FHIR ContactPoint.period consists of start and end.
                    #      pcam.ContactDetail.ContactPoint however has got a single value for 'period'
                    #      Not clear how to transform.

                    the_contact.add_telecom(the_contact_point)

            fhir_resource.add_contact(the_contact)

    if tmp := self.get_description():
        fhir_resource.set_description(supermod.markdown(value=tmp))

    # TODO not fully supported yet, UsageContext is a complex datatype, and there may be 0..*
    #
    # right now it is not clear, how the elements should be processed
    #
    # see http://www.hl7.org/fhir/metadatatypes.html#UsageContext

    # TODO not fully supported yet, CodeableConcept is a complex datatype
    #
    # right now it is not clear, how the elements should be processed
    #
    # see http://www.hl7.org/fhir/datatypes.html#CodeableConcept

    if tmp := self.get_immutable():
        fhir_resource.set_immutable(supermod.boolean(value=tmp))

    if tmp := self.get_purpose():
        fhir_resource.set_purpose(supermod.markdown(value=tmp))

    if tmp := self.get_copyright():
        fhir_resource.set_copyright(supermod.markdown(value=tmp))

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

    def exporto(input, outfile, outputClass, argsLang=None, incHierarchyExt4VS=False):
        outfile.write('<?xml version="1.0" ?>\n')

        resource = input.get_resource()
        if resource == 'CodeSystem':
            f4cs.CodeSystemSub.exporto(input, outfile, outputClass, argsLang, incHierarchyExt4VS)
        elif resource == 'ValueSet':
            f4vs.ValueSetSub.exporto(input, outfile, outputClass, argsLang, incHierarchyExt4VS)
