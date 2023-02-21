# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Sort metadatacsv by first column when writing.

## [4.0.4+20230210]

### Fixed

- elga-gmbh/malac-ct#8 Fix type in VS within `.1.svsextelga.xml`, `.2.svsextelga.xml`, `.2.claml.xml`, and `.3.claml.xml`.

## [4.0.3+20230207]

### Fixed

- When reading concepts from ValueSet same concepts codes will be distinguished by their corresponding URL in order to correctly determine hierarchies.
- Add column `parentSystem` to `.1.propcsv.csv` and `.1.propcsv.xlsx` in order to have a clear correlation between parent code and its corresponding system.

## [4.0.2+20230207]

### Fixed

- elga-gmbh/malac-ct#7 Fix sort order of concepts when reading `.4.fhir.xml` or `.4.fhir.json`.

## [4.0.1+20230202]

### Fixed

- Fix use of `hierarchyMeaning`.

## [4.0.0+20230201]

### Added

- [TERGI-107](https://jira-neu.elga.gv.at/browse/TERGI-107) Support `CodeSystem.id` and `ValueSet.id`.

### Changed

- [TERGI-73](https://jira-neu.elga.gv.at/browse/TERGI-73) Upload possibility per args to multiple FHIR server
- [TERGI-107](https://jira-neu.elga.gv.at/browse/TERGI-107) Change canonical URLs from the scheme `BASE/RESOURCETYPE-ID` to `BASE/RESOURCETYPE/ID`.

### Fixed

- elga-gmbh/malac-ct#5 Read `ValueSet.expansion.contains.abstract` properly if `.4.fhir.xml` or `.4.fhir.json` is the input format.
- Fix reading of contact without telecom fails when reading `.1.propcsv.xlsx`.
- Fix use of `hierarchyMeaning`.
- Fix reading of `description` results if it contains `&#xD;&#xA;` when reading `.4.fhir.xml`.

## [3.1.4+20230118]

### Fixed

- Fix using name in enum of propcsv, not value

## [3.1.3+20221121]

### Fixed

- [CSD-2448](https://jira-neu.elga.gv.at/browse/CSD-2448) Fix superfluous line break in `Label` tags of `.2.claml.xml`.
- [TERGI-124](https://jira-neu.elga.gv.at/browse/TERGI-124) Fix handling of empty ClaML2 metas.
- Support reading repeating meta information (e.g. `identifier`, `contact`, etc.) in `.1.propcsv.xlsx`.

## [3.1.2+20221117]

### Fixed

- Fix handling of hints/hinweise and meaning/de-at

## [3.1.1+20221116]

### Fixed

- [TERGI-129](https://jira-neu.elga.gv.at/browse/TERGI-129) Converting from claml rubric `note` to fhir is going into the fhir element `definition`, so the other way around is now implemented

## [3.1.0+20221115]

### Added

- [TERGI-120](https://jira-neu.elga.gv.at/browse/TERGI-120) Support reading/writing of CodeSystem version in ValueSets.
- [TERGI-119](https://jira-neu.elga.gv.at/browse/TERGI-119) Add `.1.propcsv.xlsx` with same content as `.1.propcsv.csv` into an Excel. This format is specifically for authoring and has no focus on machine readability.

### Fixed

- [TERGI-118](https://jira-neu.elga.gv.at/browse/TERGI-118) Change quoting within fields within propCSV from `´` to `""` and within outdatedCSV from `´` to `''`.
- Fix reading of author in `.2.claml.xml`.
- Fix writing of concept status in `.2.claml.xml`.
- Fix using `&#10` instead of `\n` in all XML formats besides `.4.fhir.xml`.
- Fix handling of Beschreibung, Description and Version-Description in `.*.svsextelga.xml` and `.2.claml.xml`.
- Fix handling of contact and hints in `.2.claml.xml`.
- Fix handling of same content in prefereedLong, preferred, designation and note

## [3.0.1+20221018]

### Fixed

- Fix writing of author in `.2.claml.xml`.
- Fix the export of `.2.claml.xml` to comply with the standard.
- Fix handling of empty contact column in `.1.propcsv.csv`.

## [3.0.0+20221014]

### Added

- [TERGI-102](https://jira-neu.elga.gv.at/browse/TERGI-102) Allow definition of hierarchies in `.1.propcsv.csv` by using a `parent` column.

### Fixed

- [TERGI-60](https://jira-neu.elga.gv.at/browse/TERGI-60) Update split char from `#` to `^` for designations, also add support for `designation.use.userSelected`.
- [TERGI-118](https://jira-neu.elga.gv.at/browse/TERGI-118) Fix conversion between different file formats - especially `description`, `date`.
- [TERGI-102](https://jira-neu.elga.gv.at/browse/TERGI-102) Fix reading and writing of `contact` information within `.1.propcsv.csv`.

## [2.2.0+20220929]

### Added

- [TERGI-73](https://jira-neu.elga.gv.at/browse/TERGI-73) Add parameter `tergiTunnelToken` which allows access to all API endpoints of a tergi.

### Fixed

- [TERGI-111](https://jira-neu.elga.gv.at/browse/TERGI-111) Support `.1.svsextelga.xml` and `.2.svsextelga.xml` if concepts do not have `parentCodeSytemName` property.

## [2.1.2+20220913]

### Fixed
- [TERGI-98](https://jira-neu.elga.gv.at/browse/TERGI-98) Fix errors that came up reading HL7 International CodeSystems per *.4.fhir.xml
- [CSD-2288](https://jira-neu.elga.gv.at/browse/CSD-2288) Escape special XML characters for ClaML v2, ClaML v3, and for SVSextELGA v2 files.

## [2.1.1+20220726]

### Fixed
- [TERGI-99](https://jira-neu.elga.gv.at/browse/TERGI-99) Fix sort 4 concepts with multiple parents, like there is in ucum

## [2.1.0+20220602]

### Added

- [TERGI-64](https://jira-neu.elga.gv.at/browse/TERGI-64) Add `.2.outdatedcsv.xml` and `.2.svsextelga.xml` both of which will provide all concept properties.

## [2.0.3+20220516]

### Changed

- [TERGI-75](https://jira-neu.elga.gv.at/browse/TERGI-75) MaLaC-CT will not set a resource's language if language is missing (parameter `-langArg`). However, CLI parameter `-langArg` will affect ClaML v3 as language is required there.

### Fixed

- [TERGI-66](https://jira-neu.elga.gv.at/browse/TERGI-66) Fix not lowering first letter of property names
- [TERGI-81](https://jira-neu.elga.gv.at/browse/TERGI-81) Fix using whole url for references to codesystems

## [2.0.2+20220421]

### Fixed

- Fix invocation of methods.
- Fix handling of Rubrics without `@kind`.

## [2.0.1+20220420]

### Fixed

- Import missing module `os`.

## [2.0.0+20220420]

### Added

- [TERGI-16](https://jira-neu.elga.gv.at/browse/TERGI-16) Direct support of FHIR XML without the need for SUSHI.
- [TERGI-23](https://jira-neu.elga.gv.at/browse/TERGI-23) Support external CodeSystems as source for ValueSet concepts (e.g. `http://loinc.org`).
- Enhance `ConceptDesignation.use` in order to properly parse/write `Coding` values.
- Write `ValueSet.expansion.contains.designation` for FSH v1.
- Print error message from FHIR server if file conversion fails.
- Write properties according to FSH v1 in FSH v2.
- Support fragment CodeSystems when reading ClaML v2.

### Changed

- Only read identifies of type `urn:oid:` when parsing FSH v1.
- Correct `__str__` method for `Property` and `CSConcept.ConceptProperty`.
- Rename some existing methods.
- Correct typos.

### Removed

- [TERGI-16](https://jira-neu.elga.gv.at/browse/TERGI-16) Remove CLI parameters `-sushi` and `-gofsh` as they have been replaced by custom implementation.
- Remove support for automatic Zuppl-creation by specifying `-CSSuppl4VS` as CLI parameter.
- Remove `excludeNotForUI` as expansion parameter.

### Fixed

- Fix structure of `ValueSet.compose.lockedDate` and `ValueSet.compose.inactive` for FSH v1.
- Fix support of CodeSystems without identifier.
- Fix writing of designations in ClaML v3.
- Fix use of languages when writing ClaML v2.

## [1.1.0+20220315-beta]

### Added

- detection of retired concepts/codes
- manual integration test with a gilab ci/cd
- outdatedCsv v1 support
- function for oid gain from resource cannonical name

### Changed

- execution of sushi for newest sushi version
- encoding of propCsv and delimeters to excel friendly variant
- argument handling

### Fixed

- Zuppl generation
- gofsh trigger
- using python standard libraries only
- publisher & author handling
- empty description handling
- date management

## [1.0.1+20220131-beta]

### Fixed

- Zuppl management
- fsh1 hierarchy using all-codes instead of groups-only
- svsextelga1 returning status active

## [1.0.0+20211231-beta]

### Added

- Zuppl (codesystem supplement for valuesets, to save all attributes) handling
- SVSextELGA1 support

### Changed

- claml2 with facts from german claml experts
- sysout to print
- argument handling

### Fixed

- handling of empty and none values
- handling of paths for unix and windows machines

## [0.4.0+20211130-alpha]

### Changed

- args handling with empty or null output (convert to all known formats)
- args handling for fhir xml or json as in or out
- file prefixes from CS- and VS- to ValueSet- and CodeSystem-, to comply with IG publisher's naming convention
- argument handling

### Fixed

- handling of tables in claml (by igoring them at first)
- sushi's needed folder structure
- subprocesses calling

## [0.3.0+20211103-alpha]

### Added

- sushi support for converting from fsh to fhir json
- gofsh support for converting from fhir json to fsh
- fhirserver support for converting from fhir json to fhir xml and the possibility to upload fhir to a given server

## [0.2.0+20210813-alpha]

### Added

- fsh2 support
- claml2 support

### Changed

- malac_ct with simplified argument parsing and new dynamic module/class loading
- argument handling

### Fixed

- fsh1 with bugfixes
- claml3 with bugfixes

## [0.1.0+20210617-alpha]

### Added

- argument-handling with -i, -o, -oclass & -argsLang
- baseclass as a proprietary csv with all attributes of fhir and additional needed ones
- support for fsh v1 (fsh1)
- support for ClaMl v3 (claml3)
