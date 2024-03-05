import prop_csv_and_master as pcam

# TODO check if this class could get removed
class ReplacedBy():
    extension_canonical = 'http://hl7.org/fhir/StructureDefinition/codesystem-replacedby'

    def add_extension(the_element, string):
        if not hasattr(the_element, 'extension'):
            the_element.extension = []

        the_extension = pcam.Extension()
        the_extension.url = ConceptOrder.extension_canonical
        the_extension.value = pcam.Coding(string)
        the_extension.type = pcam.ExtensionType.coding

        the_element.extension.append(the_extension)

class ConceptOrder():
    extension_canonical = 'http://hl7.org/fhir/StructureDefinition/valueset-conceptOrder'

    def add_extension(the_element, number):
        if not hasattr(the_element, 'extension'):
            the_element.extension = []

        the_extension = pcam.Extension()
        the_extension.url = ConceptOrder.extension_canonical
        the_extension.value = int(number)
        the_extension.type = pcam.ExtensionType.integer

        the_element.extension.append(the_extension)