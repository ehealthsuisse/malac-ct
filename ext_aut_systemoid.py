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