import prop_csv_and_master as pcam

PROFILE_CANONICAL = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-valueset'
EXTENSION_CANONICAL = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-valueset-systemoid'

# TODO: introduce functionality to activate/deactivate extension

########## propCSV & propXLSX

##### reading

# profile of value set is read automatically in fhir4_cs_and_vs.py

##### writing

# profile of value set is written automatically if fhir4_cs_and_vs.py

# writing of this extension is carried out automatically in prop_csv_and_master.py

########## FHIR 4 XML & JSON

##### reading

# profile of value set is read automatically in fhir4_cs_and_vs.py

# read value of extension
#
# Question: kann ein und dieselbe extension bei einem element öfter vorkommen mit jeweils anderem value?
#
# Attention: The target might collect extensions of different source. Beware, that only one value per extension url will be stored!
#
def fhir4_vs_get_extension(target, source):
    # depends on where this method is used
    # currently only used on VSConcept which provides 'extension'
    if not hasattr(target, 'extension_list'):
        target.extension_list = []

    if extension_list := source.get_extension():
        for one_extension in extension_list:
            if one_url := one_extension.get_url():
                # check if extension already has been retrieved
                extension_exists = [index for (index, item) in enumerate(target.extension_list) if item.uri == one_url]

                if not extension_exists:
                    the_extension = pcam.Extension()
                    the_extension.url = one_url

                    if (one_value := one_extension.get_valueOid()): #TODO support of further types
                        the_extension.value = one_value.get_value()
                        the_extension.type = pcam.ExtensionType(pcam.first_char_to_lower(one_value.original_tagname_.replace('value','')))
                    # TODO support Coding

                    target.extension_list.append(the_extension)

##### writing

# profile of value set is written automatically if fhir4_cs_and_vs.py

# add profile to terminology if it does not yet exist
def fhir4_vs_add_profile(self):
    # TODO: introduce functionality to activate/deactivate this method
    if PROFILE_CANONICAL not in self.get_profiles():
        self.get_profiles().append(PROFILE_CANONICAL)

# add extension to element if it does not yet exist
def fhir4_vs_add_extension(self, globals, system, element):
    if tmp := self.gainOidFromCanonical(system):
        element.add_extension(globals.get('ExtensionSub')(url=EXTENSION_CANONICAL, valueOid=globals.get('oidSub')(value='urn:oid:' + tmp)))

def fhir4_vs_exporto_extension(globals, target, source, extension_url):
    for one_extension in source.extension_list:
        if one_extension.url == extension_url:
            the_extension = globals.get('ExtensionSub')(url=one_extension.url)

            if (value := one_extension.value) and (value_type := one_extension.type):
                if value_type == pcam.ExtensionType.coding:
                    # TODO
                    pass
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

            target.add_extension(the_extension)
            return True

    return False