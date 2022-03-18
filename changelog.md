# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
