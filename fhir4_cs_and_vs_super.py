class FHIR4CsAndVsSuper:
    def __init__(self, inFile=None):
        super().__init__(inFile)

    def get_url(self):
        return super().get_url().get_value()

    def get_version(self):
        return super().get_version().get_value()

    def get_name(self):
        return super().get_name().get_value()

    def get_title(self):
        return super().get_title().get_value()

    def get_status(self):
        return super().get_status().get_value()

    def get_description(self):
        return super().get_description().get_value()

    def get_implicitrules(self):
        return super().get_implicitRules().get_value()

    def get_language(self):
        return super().get_language().get_value()

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
        f4_identifier_list = super().get_identifier()
        identifier_list = []
        for one_f4_identifier in f4_identifier_list:
            if one_f4_identifier.get_value():
                identifier_list.append(one_f4_identifier.get_value())
        return identifier_list

    def get_experimental(self):
        return super().get_experimental().get_value()

    def get_date(self):
        return super().get_date().get_value()

    def get_publisher(self):
        return super().get_publisher().get_value()

    def get_contact(self):
        return super().get_contact()

