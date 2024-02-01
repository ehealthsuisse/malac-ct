PROFILE_CANONICAL = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-valueset'
EXTENSION_CANONICAL = 'http://hl7.at/fhir/HL7ATCoreProfiles/4.0.1/StructureDefinition/at-core-ext-valueset-systemoid'

def fhir_4_vs_add_profile(globals, valueset):
    """ TODO
        - introduce parameter
        - support profiles in general
    """
    valueset.set_meta(globals.get('MetaSub')(profile=[globals.get('canonicalSub')(value=PROFILE_CANONICAL)]))

def fhir_4_vs_add_extension(self, globals, system, element):
    """ TODO
    - introduce parameter
    - support extensions in general
    """
    if tmp := self.gainOidFromCanonical(system):
        element.add_extension(globals.get('ExtensionSub')(url=EXTENSION_CANONICAL, valueOid=globals.get('oidSub')(value='urn:oid:' + tmp)))