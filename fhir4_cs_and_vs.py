import sys
import prop_csv_and_master as pcam
import fhir4_codesystem as f4cs
import fhir4_valueset as f4vs

####################################################################################
#
# GETTER
#
# The following getter-methods are used for retrieving the corresponding information
# of the underlying FHIR resource. These getter-methods may be used for CodeSystem
# and ValueSet resources alike.
#
####################################################################################

def get_id(self):
    """Return CodeSystem.id or ValueSet.id
    """
    if tmp := self.get_id():
        return tmp.get_value()
    return None

# NOT SUPPORTED:
#   CodeSystem.meta or ValueSet.meta in general
# def get_meta(resource):
def get_profiles(self):
    """Return CodeSytem.meta.profile or ValueSet.meta.profile.
    """
    the_profile_list = []

    if meta := self.get_meta():
        if profiles := meta.get_profile():
            for one_profile in profiles:
                if tmp := one_profile.get_value():
                    the_profile_list.append(tmp)

    return the_profile_list

def get_implicitrules(self):
    """Return CodeSytem.implicitRules or ValueSet.implicitRules.
    """
    if tmp := self.get_implicitRules():
        return tmp.get_value()
    return None

def get_language(self):
    """Return CodeSystem.language or ValueSet.language.
    """
    if tmp := self.get_language():
        return tmp.get_value()
    return None

def get_text(self):
    """NOT SUPPORTED: Return CodeSystem.text or ValueSet.text.

    Within fhir-base.xsd "text" has been removed from DomainResource.

    DomainResource.text is of type Narrative which itself allows a lot
    of further tags which eventually would result in two "class code()" definitions
    in the generated python files by generateDS.

    As DomainResource.text is not required it will not be supported
    by MaLaC-CT.
    """
    return None

def get_contained(self):
    """NOT SUPPORTED: Return CodeSystem.contained or ValueSet.contained.

    Within fhir-base.xsd "contained" has been removed from DomainResource.

    DomainResource.contained results in circular references which makes it
    difficult to create proper python classes with generateDS.

    As a result it has been decided that "contained" resources will not
    be supported by MaLaC-CT.
    """
    return None

def get_extension(self):
    """NOT SUPPORTED: Return CodeSystem.extension or ValueSet.extension.

    Extension is a complex datatype (http://www.hl7.org/fhir/extensibility.html#Extension), and there may be 0..*
    see http://www.hl7.org/fhir/domainresource.html

    Has to be implemented specifically for each extension. For converting resources MaLaC-CT would have to understand/interpret extensions
    accordingly.
    """
    return None

def get_modifierextension(self):
    """NOT SUPPORTED: Return CodeSystem.modifierExtension or ValueSet.modifierExtension.

    Extension is a complex datatype (http://www.hl7.org/fhir/extensibility.html#Extension), and there may be 0..*
    see http://www.hl7.org/fhir/domainresource.html

    Has to be implemented specifically for each extension. For converting resources MaLaC-CT would have to understand/interpret extensions
    accordingly.
    """
    return None

def get_url(self):
    """Return CodeSystem.url or ValueSet.url.
    """
    if tmp := self.get_url():
        return tmp.get_value()
    return None

def get_identifier(self):
    """Return CodeSystem.identifier or ValueSet.identifier.

    Currently, only urn:oid: is supported. As a result only Identifier.value will be retrieved -
    even if there is more information available. See http://www.hl7.org/fhir/datatypes.html#Identifier
    """
    identifier_list = self.get_identifier()
    the_identifier_list = []
    for one_identifier in identifier_list:
        # NOT SUPPORTED one_identifier.get_use()

        # NOT SUPPORTED one_identifier.get_type()

        # NOT SUPPORTED one_identifier.get_system()

        # TODO same for FSH
        if (tmp := one_identifier.get_value()) and 'urn:oid:' in tmp.get_value():
            the_identifier_list.append(tmp.get_value().replace('urn:oid:', ''))

        # NOT SUPPORTED one_identifier.get_period()

        # NOT SUPPORTED one_identifier.get_assigner()

    return the_identifier_list

def get_version(self):
    """Return CodeSystem.version or ValueSet.version.
    """
    if tmp := self.get_version():
        return tmp.get_value()
    return None

def get_name(self):
    """Return CodeSystem.name or ValueSet.name.
    """
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
    """Return CodeSystem.title or ValueSet.title.
    """
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
    """Return CodeSystem.status or ValueSet.status.
    """
    if tmp := self.get_status():
        return tmp.get_value()
    return None

def get_experimental(self):
    """Return CodeSystem.experimental or ValueSet.experimental.
    """
    if tmp := self.get_experimental():
        return tmp.get_value()
    return None

def get_date(self):
    """Return CodeSystem.date or ValueSet.date.
    """
    if tmp := self.get_date():
        return tmp.get_value()
    return None

def get_publisher(self):
    """Return CodeSystem.publisher or ValueSet.publisher.
    """
    if (tmp := self.get_publisher()) and tmp.get_value() != 'see':
        return tmp.get_value()
    return None

def get_contact(self):
    """Return CodeSystem.contact or ValueSet.contact.
    """
    contact_list = self.get_contact()
    the_contact_list = []
    for one_contact in contact_list:
        the_contact_detail = pcam.ContactDetail()

        if tmp := one_contact.get_name():
            the_contact_detail.name = tmp.get_value()

        for one_contact_point in one_contact.get_telecom():
            the_contact_point = pcam.ContactDetail.ContactPoint()

            if tmp := one_contact_point.get_system():
                the_contact_point.system = pcam.ContactDetail.ContactPoint.ContactPointSystem(tmp.get_value())

            if tmp := one_contact_point.get_value():
                the_contact_point.value = tmp.get_value()

            if tmp := one_contact_point.get_use():
                the_contact_point.use = pcam.ContactDetail.ContactPoint.ContactPointUse(tmp.get_value())

            if tmp := one_contact_point.get_rank():
                the_contact_point.value = tmp.get_value()

            if period := one_contact_point.get_period():
                if tmp := period.get_start():
                    the_contact_point.period_start = tmp.get_value()

                if tmp := period.get_end():
                    the_contact_point.period_end = tmp.get_value()

            the_contact_detail.telecom.append(the_contact_point)

        the_contact_list.append(the_contact_detail)

    return the_contact_list

def get_description(self):
    """Return CodeSystem.description or ValueSet.description.
    """
    if tmp := self.get_description():
        """A XML having &#10; will be loaded correctly by generateDS transforming the
        &#10; into \n.

        For the correct interpretation in all other formats it was assumed that \n would
        have to be replaced by \\n in order to be written properly. The return statement
        would have been as follows:

        return tmp.get_value().replace('\n', '\\n')

        However, code analysis revealed that this was not necessary. FSH for example handles
        real line feeds as well as \n in the description. Furthermore, if the FSH was subsequently
        processed by SUSHI the correct result was delivered in either cases. Hence the
        replace was found to be not necessary.
        """

        return tmp.get_value()
    return None

def get_usecontext(self):
    """NOT SUPPORTED: Return CodeSystem.useContext or ValueSet.useContext.

    UsageContext is a complex datatype, and there may be 0..*.
    Not clear, how the elements should be processed.
    See http://www.hl7.org/fhir/metadatatypes.html#UsageContext
    """
    return []

def get_jurisdiction(self):
    """NOT SUPPORTED: Return CodeSystem.jurisdiction or ValueSet.jurisdiction.

    CodeableConcept is a complex datatype, and there may be 0..*.
    Not clear, how the elements should be processed.
    See http://www.hl7.org/fhir/datatypes.html#CodeableConcept
    """
    return []

def get_purpose(self):
    """Return CodeSystem.purpose or ValueSet.purpose.
    """
    if tmp := self.get_purpose():
        return tmp.get_value()
    return None

def get_copyright(self):
    """Return CodeSystem.copyright or ValueSet.copyright.
    """
    if tmp := self.get_copyright():
        return tmp.get_value()
    return None

####################################################################################
#
# PARSER
#
# The following parser-methods are used for retrieving the corresponding information
# of the underlying FHIR resource. These parser-methods may be used for CodeSystem
# and ValueSet resources alike.
#
####################################################################################

def parse_concept_designation(designation_list):
    """Parse list of CodeSystem_Designations or ValueSet_Designations and transform them to pcam.ConceptDesignations.

    designation_list -- List of CodeSystem_Designations or ValueSet_Designations
    """
    the_designation_list = []

    for one_designation in designation_list:
        the_designation = pcam.ConceptDesignation()

        if tmp := one_designation.get_language():
            the_designation.language = tmp.get_value()

        if one_use := one_designation.get_use():
            the_use = pcam.Coding()

            if tmp := one_use.get_system():
                the_use.codesystem = tmp.get_value()

            if tmp := one_use.get_version():
                the_use.version = tmp.get_value()

            if tmp := one_use.get_code():
                the_use.code = tmp.get_value()

            if tmp := one_use.get_display():
                the_use.display = tmp.get_value()

            if tmp := one_use.get_userSelected():
                the_use.userSelected = tmp.get_value()

            the_designation.use = the_use

        if tmp := one_designation.get_value():
            the_designation.value = tmp.get_value()

        the_designation_list.append(the_designation)

    return the_designation_list

####################################################################################
#
# EXPORTO
#
# The following exporto-methods are used for writing the corresponding information
# into a FHIR resource. These exporto-methods may be used for CodeSystem
# and ValueSet resources alike.
#
####################################################################################

def exporto(self, globals, fhir_resource):
    """Write information to a FHIR resource (CodeSystem or ValueSet) that is independent
    of the resource type.

    self -- Object holding the information that should be written to the FHIR resource.

    globals -- Dictionary implementing the calling module namespace.

    fhir_resource -- The FHIR resource the information will be written to.
    """

    if tmp := self.get_id():
        fhir_resource.set_id(globals.get('idSub')(value=tmp))

    # NOT SUPPORTED CodeSystem.meta or ValueSet.meta in general
    # CodeSystem.meta.profile or ValueSet.meta.profile
    if one_profile_list := self.get_profiles():
        the_profile_list = []
        for one_profile in one_profile_list:
            the_profile_list.append(globals.get('canonicalSub')(value=one_profile))
        fhir_resource.set_meta(globals.get('MetaSub')(profile=the_profile_list))

    if tmp := self.get_implicitrules():
        fhir_resource.set_implicitRules(globals.get('uriSub')(value=tmp))

    if tmp := self.get_language():
        fhir_resource.set_language(globals.get('codeSub')(value=tmp))

    # NOT SUPPORTED CodeSystem.text or ValueSet.text

    # NOT SUPPORTED CodeSystem.contained or ValueSet.contained

    # NOT SUPPORTED CodeSystem.extension or ValueSet.extension

    # NOT SUPPORTED CodeSystem.modifierExtension or ValueSet.modifierExtension

    if tmp := self.get_url():
        fhir_resource.set_url(globals.get('uriSub')(value=tmp))

    if tmp := self.get_identifier():
        for one_identifier in tmp:
            the_identifier = globals.get('IdentifierSub')()

            # As only urn:oid: is supported the use will set to a fixed value
            the_identifier.set_use(globals.get('IdentifierUseSub')(value='official'))

            # NOT SUPPORTED the_identifier.set_type()

            # As only urn:oid: is supported the system will set to a fixed value
            the_identifier.set_system(globals.get('uriSub')(value='urn:ietf:rfc:3986'))

            # currently only urn:oid: supported
            the_identifier.set_value(globals.get('stringSub')(value='urn:oid:'+one_identifier))

            # NOT SUPPORTED the_identifier.set_period()

            # NOT SUPPORTED the_identifier.set_assigner()

            fhir_resource.add_identifier(the_identifier)

    if tmp := self.get_version():
        fhir_resource.set_version(globals.get('stringSub')(value=tmp))

    if tmp := self.get_name():
        fhir_resource.set_name(globals.get('stringSub')(value=tmp))

    if tmp := self.get_title():
        fhir_resource.set_title(globals.get('stringSub')(value=tmp))

    if tmp := self.get_status():
        fhir_resource.set_status(globals.get('PublicationStatusSub')(value=tmp))

    if tmp := self.get_experimental():
        fhir_resource.set_experimental(globals.get('booleanSub')(value=tmp))

    if tmp := self.get_date():
        fhir_resource.set_date(globals.get('dateTimeSub')(value=tmp))

    if tmp := self.get_publisher():
        fhir_resource.set_publisher(globals.get('stringSub')(value=tmp))
    # for the case, that there is no publisher but one or many contacts available, put in a default value
    elif (tmp := self.get_contact()) and len(tmp) > 0:
        fhir_resource.set_publisher(globals.get('stringSub')(value="see"))

    if tmp := self.get_contact():
        contact_list = tmp
        for one_contact in contact_list:
            the_contact = globals.get('ContactDetailSub')()

            if tmpConctactName := one_contact.name:
                the_contact.set_name(globals.get('stringSub')(value=tmpConctactName))

            if tmp := one_contact.telecom:
                contact_point_list = tmp
                for one_contact_point in contact_point_list:
                    the_contact_point = globals.get('ContactPointSub')()

                    if tmp := one_contact_point.system:
                        the_contact_point.set_system(globals.get('ContactPointSystemSub')(value=tmp.value))

                    if tmp := one_contact_point.value:
                        the_contact_point.set_value(globals.get('stringSub')(value=tmp))
                        # for the case, that there is no name in the contact but one or many telecom available, use first telecom value element as name
                        if not tmpConctactName:
                            the_contact.set_name(globals.get('stringSub')(value=tmp))
                            tmpConctactName = tmp

                    if tmp := one_contact_point.use:
                        the_contact_point.set_use(globals.get('ContactPointUseSub')(value=tmp.value))

                    if tmp := one_contact_point.rank:
                        the_contact_point.set_rank(globals.get('positiveIntSub')(value=tmp))

                    if (period_start := one_contact_point.period_start) or (period_end := one_contact_point.period_end):
                        the_period = globals.get('PeriodSub')()

                        if period_start:
                            the_period.set_start(globals.get('dateTimeSub')(value=period_start))

                        if period_end:
                            the_period.set_end(globals.get('dateTimeSub')(value=period_end))

                        one_contact_point.set_period(the_period)

                    the_contact.add_telecom(the_contact_point)

            fhir_resource.add_contact(the_contact)

    if tmp := self.get_description():
        fhir_resource.set_description(globals.get('markdownSub')(value=tmp))

    # NOT SUPPORTED CodeSystem.useContext or ValueSet.useContext

    # NOT SUPPORTED CodeSystem.jurisdiction or ValueSet.jurisdiction

    if tmp := self.get_purpose():
        fhir_resource.set_purpose(globals.get('markdownSub')(value=tmp))

    if tmp := self.get_copyright():
        fhir_resource.set_copyright(globals.get('markdownSub')(value=tmp))

def exporto_concept_designation(globals, designation_class, designation_list):
    """Transform list of pcam.ConceptDesignations to list of CodeSystem_Designations or ValueSet_Designations depending on designation_class.

    globals -- Dictionary implementing the calling module namespace.

    designation_class -- Either CodeSystem_Designation or ValueSet_Designation.

    designation_list -- list of pcam.ConceptDesignations
    """
    the_designation_list = []

    for one_designation in designation_list:
        the_designation = designation_class()

        if tmp := one_designation.language:
            the_designation.set_language(globals.get('codeSub')(value=tmp))

        if (one_use := one_designation.use) and one_use.code:
            the_use = globals.get('CodingSub')()

            if tmp := one_use.codesystem:
                the_use.set_system(globals.get('uriSub')(value=tmp))

            if tmp := one_use.version:
                the_use.set_version(globals.get('stringSub')(value=tmp))

            if tmp := one_use.code:
                the_use.set_code(globals.get('codeSub')(value=tmp))

            if tmp := one_use.display:
                the_use.set_display(globals.get('stringSub')(value=tmp))

            if tmp := one_use.userSelected:
                the_use.set_userSelected(globals.get('booleanSub')(value=tmp))

            the_designation.set_use(the_use)

        if tmp := one_designation.value:
            the_designation.set_value(globals.get('stringSub')(value=tmp))

        the_designation_list.append(the_designation)

    return the_designation_list

def parse_extension(pcam_target, fhir_source):
    """Retrieve all extensions from the fhir_source and store them in the pcam_target.
    Open question: can the same extension (same url) be used on one fhir_source more than once (with differing values)?
    Attention: The pcam_target might collect extensions of different fhir_source elements. Beware, that currently only one value per extension url will be stored!

    pcam_target -- the object according to pcam that will store all extensions read from the fhir_source.

    fhir_source -- the element from the FHIR resource whose extensions are being retrieved.
    """

    # depends on where this method is used
    # currently only used on VSConcept which provides 'extension_list'
    if not hasattr(pcam_target, 'extension_list'):
        pcam_target.extension_list = []

    if extension_list := fhir_source.get_extension():
        for one_extension in extension_list:
            if one_url := one_extension.get_url():
                # check if extension already has been retrieved
                extension_exists = [index for (index, item) in enumerate(pcam_target.extension_list) if item.uri == one_url]

                if not extension_exists:
                    the_extension = pcam.Extension()
                    the_extension.url = one_url

                    if (one_value := one_extension.get_valueOid()): #TODO support of further types
                        the_extension.value = one_value.get_value()
                        the_extension.type = pcam.ExtensionType(pcam.first_char_to_lower(one_value.original_tagname_.replace('value','')))
                    # TODO support Coding

                    pcam_target.extension_list.append(the_extension)

def exporto_extension(globals, fhir_target, pcam_source, extension_url):
    """Write the extension with the given extenstion_url from the pcam_source to the fhir_target.

    fhir_target -- the element from the FHIR resource where the extension will be written to.

    pcam_source -- the object whose extension according to the extension_url will be written to the fhir_target.

    extension_url -- identification of the extension to be written.
    """
    for one_extension in pcam_source.extension_list:
        if one_extension.url == extension_url:
            the_extension = globals.get('ExtensionSub')(url=one_extension.url)

            if (value := one_extension.value) and (value_type := one_extension.type):
                if value_type == pcam.ExtensionType.coding:
                    # the if else inside of params are checking, if ther string value is empty, else there would be e.g. <version/> elements
                    the_extension.set_valueCoding(globals.get('CodingSub')(
                            system=globals.get('urlSub')(value=value.codesystem) if value.codesystem else None,
                            version=globals.get('stringSub')(value=value.version) if value.version else None,
                            code=globals.get('codeSub')(value=value.code) if value.code else None,
                            display=globals.get('stringSub')(value=value.display) if value.display else None,
                            userSelected=globals.get('booleanSub')(value=value.userSelected) if value.userSelected else None))
                else:
                    # determine class name (e.g. string -> stringSub)
                    value_type_class_name = value_type.value + 'Sub'
                    # determine proper setter method name (e.g. set_valueString)
                    setter_name = 'set_value' + pcam.first_char_to_upper(value_type.value)

                    # check if the_property has got a setter according to setter_name
                    #       if this module has got a datatype (i.e. class definition) according to value_type_class_name
                    if hasattr(the_extension, setter_name) and globals.get(value_type_class_name):
                        # for setter_name = 'set_valueString' and value_type_class_anme = 'stringSub' the following
                        # line could be rewritten as:
                        #
                        # the_property.set_valueString(stringSub(value=tmp))
                        getattr(the_extension, setter_name)(globals.get(value_type_class_name)(value=value))

            fhir_target.add_extension(the_extension)
            # return true and break the loop once the extension has been written to the fhir_target
            return True
    # return false in case the extension with the given extension_url was not written to the fhir_target
    return False

class FHIR4CsAndVs:
    """Class serves as entrypoint for properly parsing and writing
    FHIR CodeSystem and ValueSet resources.
    """

    def __init__(self) -> None:
        pass

    # just for calling the outer method (within )
    def parse(filename):
        """Parse given file. Depending on file's name either a CodeSystem
        or ValueSet is expected.

        filename -- Name of the file to be parsed.
        """
        if 'CodeSystem-' in filename:
            return f4cs.parse(filename)
        elif 'ValueSet-' in filename:
            return f4vs.parse(filename)
        else:
            sys.exit('Filename does not comply with convention: either "CodeSystem-" or "ValueSet-"')

    def exporto(input, outfile, output_class, args_lang=None, include_hierarchy_extension_4_valueset=False):
        """Exports the given input and writes it to output file.

        input -- Object holding all the information that should be written to the output file.

        outfile -- File the information will be written to.

        output_class -- not required

        args_lang -- NOT SUPPORTED CLI parameter containing default language for resource.

        include_hierarchy_extension_4_valueset -- NOT SUPPORTED If true, extensions within ValueSet.compose will be included for specifying hierarchical ValueSets.
        """
        outfile.write('<?xml version="1.0" ?>\n')

        resource = input.get_resource()
        if resource == 'CodeSystem':
            f4cs.CodeSystemSub.exporto(input, outfile)
        elif resource == 'ValueSet':
            f4vs.ValueSetSub.exporto(input, outfile)
