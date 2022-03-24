import prop_csv_and_master as pcam

# see https://realpython.com/python-super/#multiple-inheritance-alternatives
class FHIR4CsAndVsMixin:
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
        identifier_list = super().get_identifier()
        the_identifier_list = []
        for one_f4_identifier in identifier_list:
            if tmp := one_f4_identifier.get_value():
                the_identifier_list.append(tmp.get_value())
        return the_identifier_list

    def get_version(self):
        if tmp := super().get_version():
            return tmp.get_value()
        return None

    def get_name(self):
        if tmp := super().get_name():
            return tmp.get_value()
        return None

    def get_title(self):
        if tmp := self.get_title():
            return tmp.get_value()
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
                if tmp := one_contact_point.get_period():
                    the_contact_point.value = tmp.get_value()
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
