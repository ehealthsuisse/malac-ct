#!/usr/bin/env python

#
# Generated Thu Mar  3 11:31:09 2022 by generateDS.py version 2.40.8.
# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'FHIR4ValueSetSuper.py')
#   ('-s', 'FHIR4ValueSet.py')
#
# Command line arguments:
#   valueset.xsd
#
# Command line:
#   C:/Dokumente und Einstellungen/gkleinoscheg/Downloads/generateDS-2.40.8/generateDS.py -o "FHIR4ValueSetSuper.py" -s "FHIR4ValueSet.py" valueset.xsd
#
# Current working directory (os.getcwd()):
#   FHIR
#

import os
import sys
from xml.etree.ElementInclude import include
from lxml import etree as etree_

import fhir4_valueset_super as supermod
import prop_csv_and_master as pcam
import fhir4_cs_and_vs as f4csvs
import ext_aut_systemoid as systemoid

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#

class ValueSetSub(supermod.ValueSet, pcam.PropCsvAndMaster):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extension=None, modifierExtension=None, url=None, identifier=None, version=None, name=None, title=None, status=None, experimental=None, date=None, publisher=None, contact=None, description=None, useContext=None, jurisdiction=None, immutable=None, purpose=None, copyright=None, compose=None, expansion=None, **kwargs_):
        super(ValueSetSub, self).__init__(id, meta, implicitRules, language, extension, modifierExtension, url, identifier, version, name, title, status, experimental, date, publisher, contact, description, useContext, jurisdiction, immutable, purpose, copyright, compose, expansion,  **kwargs_)

    def get_resource(self):
        """Return resource type.

        In case of zuppl-creation self.resource will be set within fsh1.py#exportoSuppl()
        and that value should then be returned instead.
        """
        if hasattr(self,"resource") and (tmp := self.resource):
            return tmp
        else:
            return pcam.Resource.ValueSet.value

    def get_id(self):
        return f4csvs.get_id(super())

    def get_profiles(self):
        return f4csvs.get_profiles(super())

    def get_implicitrules(self):
        return f4csvs.get_implicitrules(super())

    def get_language(self):
        return f4csvs.get_language(super())

    def get_text(self):
        return f4csvs.get_text(super())

    def get_contained(self):
        return f4csvs.get_contained(super())

    def get_extension(self):
        return f4csvs.get_extension(super())

    def get_modifierextension(self):
        return f4csvs.get_modifierextension(super())

    def get_url(self):
        return f4csvs.get_url(super())

    def get_identifier(self):
        return f4csvs.get_identifier(super())

    def get_version(self):
        return f4csvs.get_version(super())

    def get_name(self):
        return f4csvs.get_name(super())

    def get_title(self):
        return f4csvs.get_title(super())

    def get_status(self):
        return f4csvs.get_status(super())

    def get_experimental(self):
        return f4csvs.get_experimental(super())

    def get_date(self):
        return f4csvs.get_date(super())

    def get_publisher(self):
        return f4csvs.get_publisher(super())

    def get_contact(self):
        return f4csvs.get_contact(super())

    def get_description(self):
        return f4csvs.get_description(super())

    def get_usecontext(self):
        return f4csvs.get_usecontext(super())

    def get_jurisdiction(self):
        return f4csvs.get_jurisdiction(super())

    def get_immutable(self):
        """Return ValueSet.immutable.
        """
        if tmp := super().get_immutable():
            return tmp.get_value()
        return None

    def get_purpose(self):
        return f4csvs.get_purpose(super())

    def get_copyright(self):
        return f4csvs.get_copyright(super())

    def get_casesensitive(self):
        """Return CodeSystem.caseSensitive. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_valueset(self):
        """Return CodeSystem.valueSet. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_hierarchymeaning(self):
        """Return CodeSystem.hierarchyMeaning. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_compositional(self):
        """Return CodeSystem.compositional. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_versionneeded(self):
        """Return CodeSystem.versionNeeded. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_content(self):
        """Return CodeSystem.content. Field from CodeSystem.
        """
        # In case of zuppl-creation self.content will be set within fsh1.py#exportoSuppl()
        if hasattr(self,"content") and (tmp := self.content):
            return tmp
        else:
            # Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
            return None

    def get_supplements(self):
        """Return CodeSystem.supplements. Field from CodeSystem.
        """
        # In case of zuppl-creation self.supplements will be set within fsh1.py#exportoSuppl()
        if hasattr(self,"supplements") and (tmp := self.supplements):
            return tmp
        else:
            # Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
            return None

    def get_count(self):
        """Return CodeSystem.count. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return None

    def get_filter(self):
        """Return CodeSystem.filter. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return []

    def get_property(self):
        """Return CodeSystem.property. Field from CodeSystem.

        Required because some exporto() (e.g. in prop_csv_and_master.py) do not check if resource is a CodeSystem or ValueSet.
        """
        return []

    def get_lockeddate(self):
        """Return ValueSet.compose.lockedDate.
        """
        if tmp := super().get_compose():
            if tmp := tmp.get_lockedDate():
                return tmp.get_value()
        return None

    def get_inactive(self):
        """Return ValueSet.compose.inactive.
        """
        if tmp := super().get_compose():
            if tmp := tmp.get_inactive():
                return tmp.get_value()
        return None

    def get_concept(self):
        """Processes ValueSet.compose.include, ValueSet.compose.exclude, and ValueSet.expansion.contains and
        returns a list of pcam.VSConcept.
        """

        # Once the concepts of the underlying ValueSet have been parsed, the result
        # will be accessible in self.concept (improve performance).
        if hasattr(self,"concept") and (tmp := self.concept):
            return tmp
        else:
            self.concept = []

            if tmp := super().get_compose():
                compose = tmp
                # parse ValueSet.compose.include
                if tmp := compose.get_include():
                    self.concept.extend(ValueSetSub.parse_include_information(tmp))

                # parse ValueSet.compose.exclude
                if tmp := compose.get_exclude():
                    self.concept.extend(ValueSetSub.parse_include_information(tmp, True))

            # based on the concepts processed so far, a dictionary with the
            # concept's code as key will be created in order to add information
            # which will be retrieved from ValueSet.expansion.contains
            concept_code_dict = self.buildConceptDictWithAttr('code', 'system')

            # parse ValueSet.expansion.contains for retrieving information about
            # possible hierarchies
            if tmp := super().get_expansion():
                if tmp := tmp.get_contains():
                    # create a new list that sorts the concepts exactly like the expand does
                    the_from_expand_sorted_list = []
                    # recrusivly parse the information in the contains
                    self.parse_expansion_contains_information(0, tmp, concept_code_dict, the_from_expand_sorted_list)
                    # subtract/delete all concepts from self.concept that are in the expand and add these concepts on the end of the list
                    # this is only done for the case, that an (invalid) fhir xml got more concepts in the include than in the expansion
                    self.concept = the_from_expand_sorted_list + list(set(self.concept) - set(the_from_expand_sorted_list))

            return self.concept

    def parse_include_information(include_list, exclude=False):
        """Parse the given include_list (of type ValueSet_Include, i.e. ValueSet.compose.include or ValueSet.compose.exclude)
        and transforms the information into pcam.VSConcepts.

        include_list -- List of ValueSet_Includes that should be transformed to pcam.VSConcepts().

        exclude -- If true all VSConcepts will represent exculde information.
        """
        the_concept_list = []

        for one_include in include_list:
            the_include_system = None
            the_include_version = None

            # retrieve ValueSet_Include.system
            if tmp := one_include.get_system():
                the_include_system = tmp.get_value()

            # retrieve ValueSet_Include.version
            if tmp := one_include.get_version():
                the_include_version = tmp.get_value()

            # check if either concepts or filters have been present for one_include
            include_all_valueset = True

            # retrieve ValueSet_Include.concept
            if tmp := one_include.get_concept():
                # at least one concept is present, hence, it is not a include all valueset
                include_all_valueset = False

                concept_list = tmp
                # for each concept within ValueSet_Include a pcam.VSConcept will be created
                for one_concept in concept_list:
                    the_concept = pcam.VSConcept()

                    # read extensions
                    f4csvs.fhir4_get_extension(the_concept, one_include)

                    the_concept.system = the_include_system
                    the_concept.version = the_include_version
                    the_concept.exclude = exclude

                    if tmp := one_concept.get_code():
                        the_concept.code = tmp.get_value()

                    if tmp := one_concept.get_display():
                        the_concept.display = tmp.get_value()

                    if tmp := one_concept.get_designation():
                        the_concept.designation = f4csvs.parse_concept_designation(tmp)

                    the_concept_list.append(the_concept)

            # retrieve ValueSet_Include.filter
            if tmp := one_include.get_filter():
                # at least one filter is present, hence, it is not a include all valueset
                include_all_valueset = False

                filter_list = tmp

                the_concept = pcam.VSConcept()
                the_concept.system = the_include_system
                the_concept.version = the_include_version
                the_concept.exclude = exclude

                # all filters that belong to this ValueSet_Include will be part
                # of one pcam.VSConcept
                for one_filter in filter_list:
                    the_filter = pcam.VSConcept.VSConceptFilter()

                    if tmp := one_filter.get_property():
                        the_filter.property = tmp.get_value()

                    if tmp := one_filter.get_op():
                        the_filter.op = tmp.get_value()

                    if tmp := one_filter.get_value():
                        the_filter.value = tmp.get_value()

                    the_concept.filter.append(the_filter)

                the_concept_list.append(the_concept)

            # NOT SUPPORTED ValueSet_Include.valueSet

            # if it is an "include all valueset" create a dummy VSConcept
            if include_all_valueset:
                the_concept = pcam.VSConcept()
                the_concept.system = the_include_system
                the_concept.version = the_include_version
                the_concept.exclude = exclude

                the_concept_list.append(the_concept)

        return the_concept_list

    def parse_expansion_contains_information(self, level, contains_list, concept_code_dict, the_from_expand_sorted_list, parent=None):
        """Parse the given contains_list (of type ValueSet_Contains, i.e. ValueSet.expansion.contains) and add
        information regarding possible hierarchies to the pcam.VSConcepts which are part of concept_code_dict.

        level -- the current level of hierarchy. Top level should have level=0.

        contains_list -- List of ValueSet_Contains of the current level.

        concept_code_dict -- Dictionary of all concepts (retrieved from ValueSet.compose.include and ValueSet.compose.exclude) with their code as key.

        the_from_expand_sorted_list -- the recrusivly build up list of concepts, occured in order of the expand

        parent -- the parent of the concepts within the contains_list.

        Currently, only information about a possible hierarchical ValueSet definition is being
        retrieved from the expansion. No other information - if available - will be processed.
        """
        for one_contains in contains_list:
            if (tmp_code := one_contains.get_code()) and (tmp_system := one_contains.get_system()):
                key = tmp_code.get_value() + tmp_system.get_value()
                # retrieve the concept from the dictionary
                if key in concept_code_dict.keys() and (the_concept := concept_code_dict[key]):
                    # set the concept's level
                    the_concept.level = level

                    # parse ValueSet.expansion.contains.abstract
                    if tmp := one_contains.get_abstract():
                        the_concept.abstract = tmp.get_value()

                    # parse ValueSet.expansion.contains.inactive
                    if tmp := one_contains.get_inactive():
                        the_concept.inactive = tmp.get_value()
                        if the_concept.inactive:
                            self.inactive = True

                    # if a parent has been specified add the_concept to the parent's member
                    if parent:
                        # setting theConcept as child of the parent
                        parent.member.append(the_concept)
                        # setting the parent of one_concept
                        the_concept.parent = parent

                    the_from_expand_sorted_list.append(the_concept)
                    # if one_contains contains a list of contains go into recursion
                    if tmp := one_contains.get_contains():
                        self.parse_expansion_contains_information(level+1, tmp, concept_code_dict, the_from_expand_sorted_list, the_concept)

    def exporto(self, outfile):
        """Write information to a FHIR ValueSet.

        self -- Object holding the information that should be written to the FHIR ValueSet.

        outfile -- File the information will be written to.
        """

        # Create new FHIR ValueSet
        valueset = ValueSetSub()

        # TODO: introduce functionality to activate/deactivate extension
        # make sure the profile is being added
        systemoid.fhir4_vs_add_profile(self)

        # export general metadata
        f4csvs.exporto(self, globals(), valueset)

        if tmp := self.get_immutable():
            valueset.set_immutable(booleanSub(value = tmp))

        the_compose = None

        if tmp := self.get_lockeddate():
            the_compose = ValueSetSub.create_compose_if_not_existent(valueset)
            the_compose.set_lockedDate(dateSub(value=tmp))

        if tmp := self.get_inactive():
            the_compose = ValueSetSub.create_compose_if_not_existent(valueset)
            the_compose.set_inactive(booleanSub(value=tmp))

        if tmp := self.get_concept():
            the_compose = ValueSetSub.create_compose_if_not_existent(valueset)

            # create ValueSet.compose.include and/or ValueSet.compose.exclude
            do_expansion = ValueSetSub.exporto_include_exclude(self, the_compose, tmp)

            # if an expansion shall be appended to the ValueSet definition
            if do_expansion:
                the_expansion = ValueSet_ExpansionSub()

                # NOT SUPPORTED ValueSet_Expansion.identifier

                # set timestamp accordingly (required)
                the_expansion.set_timestamp(dateTimeSub(value=self.metadata_change_timestamp))

                # NOT SUPPORTED ValueSet_Expansion.total

                # NOT SUPPORTED ValueSet_Expansion.offset

                # NOT SUPPORTED ValueSet_Expansion.parameter

                # the expansion will be created starting with those concepts which are at level=0 of a possible hierarchy
                the_expansion.set_contains(ValueSetSub.exporto_expansion(self, list(filter(lambda concept: concept.level is not None and concept.level == 0, tmp))))

                valueset.set_expansion(the_expansion)

        # export the FHIR ValueSet resource to the outfile
        valueset.export(outfile=outfile, level=0, namespacedef_='xmlns="http://hl7.org/fhir"')

    def create_compose_if_not_existent(valueset):
        """Create ValueSet.compose if it does not yet exist.

        valueset -- the ValueSet object
        """
        compose = None

        if not (compose := valueset.get_compose()):
            compose = ValueSet_ComposeSub()
            valueset.set_compose(compose)

        return compose

    def exporto_include_exclude(self, the_compose, concept_list):
        """Export information from the given concept_list to the_compose and create
        ValueSet.compose.include and/or ValueSet.compose.exclude if necessary.

        the_compose -- Represents ValueSet.compose.
        concept_list -- List of pcam.VSConcepts which will be processed.
        """
        do_expansion = False

        # dictionaries containing the concepts for each system + version
        system_include_dict = {}
        system_exclude_dict = {}
        # dummy system + version if a VSConcept has got neither system nor version
        no_system_no_version = 'NO_SYSTEM_NO_VERSION'

        for one_concept in concept_list:
            exclude = one_concept.exclude

            # check if exclude is a valid value
            if exclude != True and exclude != False:
                sys.exit('Cannot determine if concept should be part of ValueSet.compose.include or ValueSet.compose.exclude')

            # based on exclude decide if the information within one_concept should be
            # added to ValueSet.compose.include ore ValueSet.compose.exclude
            the_system_dict = None
            if exclude:
                the_system_dict = system_exclude_dict
            else:
                the_system_dict = system_include_dict

            # retrieve system + version from one_concept
            the_system = one_concept.system
            # explicitly set the_version to None - otherwise it might occur that it has the value of a preceding loop-run
            the_version = None
            # write the system version if existent
            if tmp := one_concept.version:
                the_version = one_concept.version
            else:
                # retrieve version from metadata

                # theoretically one_concept.system could be either canonical or OID in
                # most cases, however, it would be the canonical
                if tmp := self.gainVersionFromCanonical(the_system):
                    the_version = tmp
                elif tmp := self.gainVersionFromOid(the_system):
                    the_version = tmp
            # create key for the dictionary entry
            system_key = None
            if the_system or the_version:
                system_key = (the_system or 'None') + '#' + (the_version or 'None')
            else:
                system_key = no_system_no_version

            the_include = None
            # if the key does not yet exist in the dictionary a new ValueSet_Include
            # with the current system + version will be created
            if system_key not in the_system_dict:
                the_include = ValueSet_IncludeSub()
                if the_system:
                    the_include.set_system(uriSub(value=the_system))

                    # add the extension to the include
                    if not f4csvs.fhir4_exporto_extension(globals(), the_include, one_concept, systemoid.EXTENSION_CANONICAL):
                        pass
                        # TODO: introduce functionality to activate/deactivate extension
                        #systemoid.fhir4_vs_add_extension(self, globals(), the_system, the_include)
                if the_version:
                    the_include.set_version(stringSub(value=the_version))
                the_system_dict[system_key] = the_include
            else:
                the_include = the_system_dict[system_key]

            # if one_concept has got a code it will be transformed into a ValueSet_Concept (i.e. ValueSet.compose.include.concept or ValueSet.compose.exclude.concept)
            if tmp := one_concept.code:
                # if concepts are explicitly stated within ValueSet.compose.include a ValueSet.expansion will be
                # created with all those concepts from ValueSet.compose.include
                #
                # if exclude is false, do_expansion will become true
                # if exclude is true, do_expansion will retain its current value
                do_expansion |= not exclude

                the_concept = ValueSet_ConceptSub()

                the_concept.set_code(codeSub(value=tmp))

                if tmp := one_concept.display:
                    the_concept.set_display(stringSub(value=tmp))

                if tmp := one_concept.designation:
                    the_concept.set_designation(f4csvs.exporto_concept_designation(globals(), ValueSet_DesignationSub, tmp))

                the_include.add_concept(the_concept)
            # if one_concept has got filters they will be transformed into ValueSet_Filter (i.e. ValueSet.compose.include.filter or ValueSet.compose.exclude.filter)
            elif tmp := one_concept.filter:
                filter_list = tmp
                for one_filter in filter_list:
                    the_filter = ValueSet_FilterSub()

                    if tmp := one_filter.property:
                        the_filter.set_property(codeSub(value=tmp))

                    if tmp := one_filter.op:
                        the_filter.set_op(FilterOperatorSub(value=tmp))

                    if tmp := one_filter.value:
                        the_filter.set_value(stringSub(value=tmp))

                    the_include.add_filter(the_filter)

            # NOT SUPPORTED ValueSet_Include.valueSet

        # set ValueSet.compose.include
        the_compose.set_include(list(system_include_dict.values()))
        # set ValueSet.compose.exclude
        the_compose.set_exclude(list(system_exclude_dict.values()))

        return do_expansion

    def exporto_expansion(self, concept_list):
        """Export information from the given concept_list to ValueSet.expansion.

        concept_list -- List of pcam.VSConcepts which will be processed.
        """
        the_concept_list = []

        for one_concept in concept_list:
            # only those concepts should be part of the expansion which have exclude=false
            if not one_concept.exclude:
                the_concept = ValueSet_ContainsSub()

                one_system = one_concept.system
                if one_system:
                    the_concept.set_system(uriSub(value=one_system))

                    # add the extension to the concept
                    if not f4csvs.fhir4_exporto_extension(globals(), the_concept, one_concept, systemoid.EXTENSION_CANONICAL):
                        pass
                        # TODO: introduce functionality to activate/deactivate extension
                        # systemoid.fhir4_vs_add_extension(self, globals(), one_system, the_concept)

                if tmp := one_concept.abstract:
                    the_concept.set_abstract(booleanSub(value=tmp))

                if tmp := one_concept.inactive:
                    the_concept.set_inactive(booleanSub(value=tmp))

                # write the system version if existent
                if tmp := one_concept.version:
                    the_concept.set_version(stringSub(value=tmp))
                else:
                    # retrieve version from metadata

                    # theoretically one_concept.system could be either canonical or OID in
                    # most cases, however, it would be the canonical
                    if tmp := self.gainVersionFromCanonical(one_system):
                        the_concept.set_version(stringSub(value=tmp))
                    elif tmp := self.gainVersionFromOid(one_system):
                        the_concept.set_version(stringSub(value=tmp))

                if tmp := one_concept.code:
                    the_concept.set_code(codeSub(value=tmp))

                if tmp := one_concept.display:
                    the_concept.set_display(stringSub(value=tmp))

                if tmp := one_concept.designation:
                    the_concept.set_designation(f4csvs.exporto_concept_designation(globals(), ValueSet_DesignationSub, tmp))

                # if one_concept contains any members a recursion will be started
                if tmp := one_concept.member:
                    the_concept.set_contains(ValueSetSub.exporto_expansion(self, tmp))

                the_concept_list.append(the_concept)

        return the_concept_list

supermod.ValueSet.subclass = ValueSetSub
# end class ValueSetSub

class ElementSub(supermod.Element):
    def __init__(self, id=None, extension=None, extensiontype_=None, **kwargs_):
        super(ElementSub, self).__init__(id, extension, extensiontype_,  **kwargs_)
supermod.Element.subclass = ElementSub
# end class ElementSub


class MetaSub(supermod.Meta):
    def __init__(self, id=None, extension=None, versionId=None, lastUpdated=None, source=None, profile=None, security=None, tag=None, **kwargs_):
        super(MetaSub, self).__init__(id, extension, versionId, lastUpdated, source, profile, security, tag,  **kwargs_)
supermod.Meta.subclass = MetaSub
# end class MetaSub


class AddressSub(supermod.Address):
    def __init__(self, id=None, extension=None, use=None, type_=None, text=None, line=None, city=None, district=None, state=None, postalCode=None, country=None, period=None, **kwargs_):
        super(AddressSub, self).__init__(id, extension, use, type_, text, line, city, district, state, postalCode, country, period,  **kwargs_)
supermod.Address.subclass = AddressSub
# end class AddressSub


class AddressUseSub(supermod.AddressUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AddressUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AddressUse.subclass = AddressUseSub
# end class AddressUseSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AddressTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class ContributorSub(supermod.Contributor):
    def __init__(self, id=None, extension=None, type_=None, name=None, contact=None, **kwargs_):
        super(ContributorSub, self).__init__(id, extension, type_, name, contact,  **kwargs_)
supermod.Contributor.subclass = ContributorSub
# end class ContributorSub


class ContributorTypeSub(supermod.ContributorType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContributorTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContributorType.subclass = ContributorTypeSub
# end class ContributorTypeSub


class AttachmentSub(supermod.Attachment):
    def __init__(self, id=None, extension=None, contentType=None, language=None, data=None, url=None, size=None, hash=None, title=None, creation=None, **kwargs_):
        super(AttachmentSub, self).__init__(id, extension, contentType, language, data, url, size, hash, title, creation,  **kwargs_)
supermod.Attachment.subclass = AttachmentSub
# end class AttachmentSub


class DataRequirementSub(supermod.DataRequirement):
    def __init__(self, id=None, extension=None, type_=None, profile=None, subjectCodeableConcept=None, subjectReference=None, mustSupport=None, codeFilter=None, dateFilter=None, limit=None, sort=None, **kwargs_):
        super(DataRequirementSub, self).__init__(id, extension, type_, profile, subjectCodeableConcept, subjectReference, mustSupport, codeFilter, dateFilter, limit, sort,  **kwargs_)
supermod.DataRequirement.subclass = DataRequirementSub
# end class DataRequirementSub


class DataRequirement_CodeFilterSub(supermod.DataRequirement_CodeFilter):
    def __init__(self, id=None, extension=None, path=None, searchParam=None, valueSet=None, code=None, **kwargs_):
        super(DataRequirement_CodeFilterSub, self).__init__(id, extension, path, searchParam, valueSet, code,  **kwargs_)
supermod.DataRequirement_CodeFilter.subclass = DataRequirement_CodeFilterSub
# end class DataRequirement_CodeFilterSub


class DataRequirement_DateFilterSub(supermod.DataRequirement_DateFilter):
    def __init__(self, id=None, extension=None, path=None, searchParam=None, valueDateTime=None, valuePeriod=None, valueDuration=None, **kwargs_):
        super(DataRequirement_DateFilterSub, self).__init__(id, extension, path, searchParam, valueDateTime, valuePeriod, valueDuration,  **kwargs_)
supermod.DataRequirement_DateFilter.subclass = DataRequirement_DateFilterSub
# end class DataRequirement_DateFilterSub


class DataRequirement_SortSub(supermod.DataRequirement_Sort):
    def __init__(self, id=None, extension=None, path=None, direction=None, **kwargs_):
        super(DataRequirement_SortSub, self).__init__(id, extension, path, direction,  **kwargs_)
supermod.DataRequirement_Sort.subclass = DataRequirement_SortSub
# end class DataRequirement_SortSub


class SortDirectionSub(supermod.SortDirection):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SortDirectionSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SortDirection.subclass = SortDirectionSub
# end class SortDirectionSub


class MoneySub(supermod.Money):
    def __init__(self, id=None, extension=None, value=None, currency=None, **kwargs_):
        super(MoneySub, self).__init__(id, extension, value, currency,  **kwargs_)
supermod.Money.subclass = MoneySub
# end class MoneySub


class HumanNameSub(supermod.HumanName):
    def __init__(self, id=None, extension=None, use=None, text=None, family=None, given=None, prefix=None, suffix=None, period=None, **kwargs_):
        super(HumanNameSub, self).__init__(id, extension, use, text, family, given, prefix, suffix, period,  **kwargs_)
supermod.HumanName.subclass = HumanNameSub
# end class HumanNameSub


class NameUseSub(supermod.NameUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(NameUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.NameUse.subclass = NameUseSub
# end class NameUseSub


class ContactPointSub(supermod.ContactPoint):
    def __init__(self, id=None, extension=None, system=None, value=None, use=None, rank=None, period=None, **kwargs_):
        super(ContactPointSub, self).__init__(id, extension, system, value, use, rank, period,  **kwargs_)
supermod.ContactPoint.subclass = ContactPointSub
# end class ContactPointSub


class ContactPointSystemSub(supermod.ContactPointSystem):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContactPointSystemSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContactPointSystem.subclass = ContactPointSystemSub
# end class ContactPointSystemSub


class ContactPointUseSub(supermod.ContactPointUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ContactPointUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ContactPointUse.subclass = ContactPointUseSub
# end class ContactPointUseSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, id=None, extension=None, use=None, type_=None, system=None, value=None, period=None, assigner=None, **kwargs_):
        super(IdentifierSub, self).__init__(id, extension, use, type_, system, value, period, assigner,  **kwargs_)
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class IdentifierUseSub(supermod.IdentifierUse):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(IdentifierUseSub, self).__init__(id, extension, value,  **kwargs_)
supermod.IdentifierUse.subclass = IdentifierUseSub
# end class IdentifierUseSub


class CodingSub(supermod.Coding):
    def __init__(self, id=None, extension=None, system=None, version=None, code=None, display=None, userSelected=None, **kwargs_):
        super(CodingSub, self).__init__(id, extension, system, version, code, display, userSelected,  **kwargs_)
supermod.Coding.subclass = CodingSub
# end class CodingSub


class SampledDataSub(supermod.SampledData):
    def __init__(self, id=None, extension=None, origin=None, period=None, factor=None, lowerLimit=None, upperLimit=None, dimensions=None, data=None, **kwargs_):
        super(SampledDataSub, self).__init__(id, extension, origin, period, factor, lowerLimit, upperLimit, dimensions, data,  **kwargs_)
supermod.SampledData.subclass = SampledDataSub
# end class SampledDataSub


class SampledDataDataTypeSub(supermod.SampledDataDataType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SampledDataDataTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SampledDataDataType.subclass = SampledDataDataTypeSub
# end class SampledDataDataTypeSub


class RatioSub(supermod.Ratio):
    def __init__(self, id=None, extension=None, numerator=None, denominator=None, **kwargs_):
        super(RatioSub, self).__init__(id, extension, numerator, denominator,  **kwargs_)
supermod.Ratio.subclass = RatioSub
# end class RatioSub


class ReferenceSub(supermod.Reference):
    def __init__(self, id=None, extension=None, reference=None, type_=None, identifier=None, display=None, **kwargs_):
        super(ReferenceSub, self).__init__(id, extension, reference, type_, identifier, display,  **kwargs_)
supermod.Reference.subclass = ReferenceSub
# end class ReferenceSub


class TriggerDefinitionSub(supermod.TriggerDefinition):
    def __init__(self, id=None, extension=None, type_=None, name=None, timingTiming=None, timingReference=None, timingDate=None, timingDateTime=None, data=None, condition=None, **kwargs_):
        super(TriggerDefinitionSub, self).__init__(id, extension, type_, name, timingTiming, timingReference, timingDate, timingDateTime, data, condition,  **kwargs_)
supermod.TriggerDefinition.subclass = TriggerDefinitionSub
# end class TriggerDefinitionSub


class TriggerTypeSub(supermod.TriggerType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(TriggerTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.TriggerType.subclass = TriggerTypeSub
# end class TriggerTypeSub


class QuantitySub(supermod.Quantity):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, extensiontype_=None, **kwargs_):
        super(QuantitySub, self).__init__(id, extension, value, comparator, unit, system, code, extensiontype_,  **kwargs_)
supermod.Quantity.subclass = QuantitySub
# end class QuantitySub


class QuantityComparatorSub(supermod.QuantityComparator):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(QuantityComparatorSub, self).__init__(id, extension, value,  **kwargs_)
supermod.QuantityComparator.subclass = QuantityComparatorSub
# end class QuantityComparatorSub


class PeriodSub(supermod.Period):
    def __init__(self, id=None, extension=None, start=None, end=None, **kwargs_):
        super(PeriodSub, self).__init__(id, extension, start, end,  **kwargs_)
supermod.Period.subclass = PeriodSub
# end class PeriodSub


class DurationSub(supermod.Duration):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(DurationSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Duration.subclass = DurationSub
# end class DurationSub


class RangeSub(supermod.Range):
    def __init__(self, id=None, extension=None, low=None, high=None, **kwargs_):
        super(RangeSub, self).__init__(id, extension, low, high,  **kwargs_)
supermod.Range.subclass = RangeSub
# end class RangeSub


class RelatedArtifactSub(supermod.RelatedArtifact):
    def __init__(self, id=None, extension=None, type_=None, label=None, display=None, citation=None, url=None, document=None, resource=None, **kwargs_):
        super(RelatedArtifactSub, self).__init__(id, extension, type_, label, display, citation, url, document, resource,  **kwargs_)
supermod.RelatedArtifact.subclass = RelatedArtifactSub
# end class RelatedArtifactSub


class RelatedArtifactTypeSub(supermod.RelatedArtifactType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(RelatedArtifactTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.RelatedArtifactType.subclass = RelatedArtifactTypeSub
# end class RelatedArtifactTypeSub


class AnnotationSub(supermod.Annotation):
    def __init__(self, id=None, extension=None, authorReference=None, authorString=None, time=None, text=None, **kwargs_):
        super(AnnotationSub, self).__init__(id, extension, authorReference, authorString, time, text,  **kwargs_)
supermod.Annotation.subclass = AnnotationSub
# end class AnnotationSub


class ContactDetailSub(supermod.ContactDetail):
    def __init__(self, id=None, extension=None, name=None, telecom=None, **kwargs_):
        super(ContactDetailSub, self).__init__(id, extension, name, telecom,  **kwargs_)
supermod.ContactDetail.subclass = ContactDetailSub
# end class ContactDetailSub


class UsageContextSub(supermod.UsageContext):
    def __init__(self, id=None, extension=None, code=None, valueCodeableConcept=None, valueQuantity=None, valueRange=None, valueReference=None, **kwargs_):
        super(UsageContextSub, self).__init__(id, extension, code, valueCodeableConcept, valueQuantity, valueRange, valueReference,  **kwargs_)
supermod.UsageContext.subclass = UsageContextSub
# end class UsageContextSub


class ExpressionSub(supermod.Expression):
    def __init__(self, id=None, extension=None, description=None, name=None, language=None, expression=None, reference=None, **kwargs_):
        super(ExpressionSub, self).__init__(id, extension, description, name, language, expression, reference,  **kwargs_)
supermod.Expression.subclass = ExpressionSub
# end class ExpressionSub


class ExpressionLanguageSub(supermod.ExpressionLanguage):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ExpressionLanguageSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ExpressionLanguage.subclass = ExpressionLanguageSub
# end class ExpressionLanguageSub


class SignatureSub(supermod.Signature):
    def __init__(self, id=None, extension=None, type_=None, when=None, who=None, onBehalfOf=None, targetFormat=None, sigFormat=None, data=None, **kwargs_):
        super(SignatureSub, self).__init__(id, extension, type_, when, who, onBehalfOf, targetFormat, sigFormat, data,  **kwargs_)
supermod.Signature.subclass = SignatureSub
# end class SignatureSub


class UnitsOfTimeSub(supermod.UnitsOfTime):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(UnitsOfTimeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.UnitsOfTime.subclass = UnitsOfTimeSub
# end class UnitsOfTimeSub


class EventTimingSub(supermod.EventTiming):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(EventTimingSub, self).__init__(id, extension, value,  **kwargs_)
supermod.EventTiming.subclass = EventTimingSub
# end class EventTimingSub


class CodeableConceptSub(supermod.CodeableConcept):
    def __init__(self, id=None, extension=None, coding=None, text=None, **kwargs_):
        super(CodeableConceptSub, self).__init__(id, extension, coding, text,  **kwargs_)
supermod.CodeableConcept.subclass = CodeableConceptSub
# end class CodeableConceptSub


class ParameterDefinitionSub(supermod.ParameterDefinition):
    def __init__(self, id=None, extension=None, name=None, use=None, min=None, max=None, documentation=None, type_=None, profile=None, **kwargs_):
        super(ParameterDefinitionSub, self).__init__(id, extension, name, use, min, max, documentation, type_, profile,  **kwargs_)
supermod.ParameterDefinition.subclass = ParameterDefinitionSub
# end class ParameterDefinitionSub


class PropertyRepresentationSub(supermod.PropertyRepresentation):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(PropertyRepresentationSub, self).__init__(id, extension, value,  **kwargs_)
supermod.PropertyRepresentation.subclass = PropertyRepresentationSub
# end class PropertyRepresentationSub


class ConstraintSeveritySub(supermod.ConstraintSeverity):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ConstraintSeveritySub, self).__init__(id, extension, value,  **kwargs_)
supermod.ConstraintSeverity.subclass = ConstraintSeveritySub
# end class ConstraintSeveritySub


class AggregationModeSub(supermod.AggregationMode):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AggregationModeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AggregationMode.subclass = AggregationModeSub
# end class AggregationModeSub


class ReferenceVersionRulesSub(supermod.ReferenceVersionRules):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ReferenceVersionRulesSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ReferenceVersionRules.subclass = ReferenceVersionRulesSub
# end class ReferenceVersionRulesSub


class SlicingRulesSub(supermod.SlicingRules):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SlicingRulesSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SlicingRules.subclass = SlicingRulesSub
# end class SlicingRulesSub


class BindingStrengthSub(supermod.BindingStrength):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(BindingStrengthSub, self).__init__(id, extension, value,  **kwargs_)
supermod.BindingStrength.subclass = BindingStrengthSub
# end class BindingStrengthSub


class DiscriminatorTypeSub(supermod.DiscriminatorType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(DiscriminatorTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.DiscriminatorType.subclass = DiscriminatorTypeSub
# end class DiscriminatorTypeSub


class ResourceSub(supermod.Resource):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extensiontype_=None, **kwargs_):
        super(ResourceSub, self).__init__(id, meta, implicitRules, language, extensiontype_,  **kwargs_)
supermod.Resource.subclass = ResourceSub
# end class ResourceSub


class PublicationStatusSub(supermod.PublicationStatus):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(PublicationStatusSub, self).__init__(id, extension, value,  **kwargs_)
supermod.PublicationStatus.subclass = PublicationStatusSub
# end class PublicationStatusSub


class SearchParamTypeSub(supermod.SearchParamType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(SearchParamTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.SearchParamType.subclass = SearchParamTypeSub
# end class SearchParamTypeSub


class AdministrativeGenderSub(supermod.AdministrativeGender):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(AdministrativeGenderSub, self).__init__(id, extension, value,  **kwargs_)
supermod.AdministrativeGender.subclass = AdministrativeGenderSub
# end class AdministrativeGenderSub


class FHIRVersionSub(supermod.FHIRVersion):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(FHIRVersionSub, self).__init__(id, extension, value,  **kwargs_)
supermod.FHIRVersion.subclass = FHIRVersionSub
# end class FHIRVersionSub


class NoteTypeSub(supermod.NoteType):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(NoteTypeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.NoteType.subclass = NoteTypeSub
# end class NoteTypeSub


class RemittanceOutcomeSub(supermod.RemittanceOutcome):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(RemittanceOutcomeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.RemittanceOutcome.subclass = RemittanceOutcomeSub
# end class RemittanceOutcomeSub


class ConceptMapEquivalenceSub(supermod.ConceptMapEquivalence):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(ConceptMapEquivalenceSub, self).__init__(id, extension, value,  **kwargs_)
supermod.ConceptMapEquivalence.subclass = ConceptMapEquivalenceSub
# end class ConceptMapEquivalenceSub


class DocumentReferenceStatusSub(supermod.DocumentReferenceStatus):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(DocumentReferenceStatusSub, self).__init__(id, extension, value,  **kwargs_)
supermod.DocumentReferenceStatus.subclass = DocumentReferenceStatusSub
# end class DocumentReferenceStatusSub


class DomainResourceSub(supermod.DomainResource):
    def __init__(self, id=None, meta=None, implicitRules=None, language=None, extension=None, modifierExtension=None, extensiontype_=None, **kwargs_):
        super(DomainResourceSub, self).__init__(id, meta, implicitRules, language, extension, modifierExtension, extensiontype_,  **kwargs_)
supermod.DomainResource.subclass = DomainResourceSub
# end class DomainResourceSub


class AgeSub(supermod.Age):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(AgeSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Age.subclass = AgeSub
# end class AgeSub


class DistanceSub(supermod.Distance):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(DistanceSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Distance.subclass = DistanceSub
# end class DistanceSub


class CountSub(supermod.Count):
    def __init__(self, id=None, extension=None, value=None, comparator=None, unit=None, system=None, code=None, **kwargs_):
        super(CountSub, self).__init__(id, extension, value, comparator, unit, system, code,  **kwargs_)
supermod.Count.subclass = CountSub
# end class CountSub


class BackboneElementSub(supermod.BackboneElement):
    def __init__(self, id=None, extension=None, modifierExtension=None, extensiontype_=None, **kwargs_):
        super(BackboneElementSub, self).__init__(id, extension, modifierExtension, extensiontype_,  **kwargs_)
supermod.BackboneElement.subclass = BackboneElementSub
# end class BackboneElementSub


class ExtensionSub(supermod.Extension):
    def __init__(self, id=None, extension=None, url=None, valueBase64Binary=None, valueBoolean=None, valueCanonical=None, valueCode=None, valueDate=None, valueDateTime=None, valueDecimal=None, valueId=None, valueInstant=None, valueInteger=None, valueMarkdown=None, valueOid=None, valuePositiveInt=None, valueString=None, valueTime=None, valueUnsignedInt=None, valueUri=None, valueUrl=None, valueUuid=None, valueAddress=None, valueAge=None, valueAnnotation=None, valueAttachment=None, valueCodeableConcept=None, valueCoding=None, valueContactPoint=None, valueCount=None, valueDistance=None, valueDuration=None, valueHumanName=None, valueIdentifier=None, valueMoney=None, valuePeriod=None, valueQuantity=None, valueRange=None, valueRatio=None, valueReference=None, valueSampledData=None, valueSignature=None, valueTiming=None, valueContactDetail=None, valueContributor=None, valueDataRequirement=None, valueExpression=None, valueParameterDefinition=None, valueRelatedArtifact=None, valueTriggerDefinition=None, valueUsageContext=None, valueDosage=None, valueMeta=None, **kwargs_):
        super(ExtensionSub, self).__init__(id, extension, url, valueBase64Binary, valueBoolean, valueCanonical, valueCode, valueDate, valueDateTime, valueDecimal, valueId, valueInstant, valueInteger, valueMarkdown, valueOid, valuePositiveInt, valueString, valueTime, valueUnsignedInt, valueUri, valueUrl, valueUuid, valueAddress, valueAge, valueAnnotation, valueAttachment, valueCodeableConcept, valueCoding, valueContactPoint, valueCount, valueDistance, valueDuration, valueHumanName, valueIdentifier, valueMoney, valuePeriod, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueTiming, valueContactDetail, valueContributor, valueDataRequirement, valueExpression, valueParameterDefinition, valueRelatedArtifact, valueTriggerDefinition, valueUsageContext, valueDosage, valueMeta,  **kwargs_)
supermod.Extension.subclass = ExtensionSub
# end class ExtensionSub


class decimalSub(supermod.decimal):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(decimalSub, self).__init__(id, extension, value,  **kwargs_)
supermod.decimal.subclass = decimalSub
# end class decimalSub


class positiveIntSub(supermod.positiveInt):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(positiveIntSub, self).__init__(id, extension, value,  **kwargs_)
supermod.positiveInt.subclass = positiveIntSub
# end class positiveIntSub


class idSub(supermod.id):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(idSub, self).__init__(id, extension, value,  **kwargs_)
supermod.id.subclass = idSub
# end class idSub


class timeSub(supermod.time):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(timeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.time.subclass = timeSub
# end class timeSub


class markdownSub(supermod.markdown):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(markdownSub, self).__init__(id, extension, value,  **kwargs_)
supermod.markdown.subclass = markdownSub
# end class markdownSub


class unsignedIntSub(supermod.unsignedInt):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(unsignedIntSub, self).__init__(id, extension, value,  **kwargs_)
supermod.unsignedInt.subclass = unsignedIntSub
# end class unsignedIntSub


class base64BinarySub(supermod.base64Binary):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(base64BinarySub, self).__init__(id, extension, value,  **kwargs_)
supermod.base64Binary.subclass = base64BinarySub
# end class base64BinarySub


class booleanSub(supermod.boolean):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(booleanSub, self).__init__(id, extension, value,  **kwargs_)
supermod.boolean.subclass = booleanSub
# end class booleanSub


class instantSub(supermod.instant):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(instantSub, self).__init__(id, extension, value,  **kwargs_)
supermod.instant.subclass = instantSub
# end class instantSub


class urlSub(supermod.url):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(urlSub, self).__init__(id, extension, value,  **kwargs_)
supermod.url.subclass = urlSub
# end class urlSub


class uuidSub(supermod.uuid):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(uuidSub, self).__init__(id, extension, value,  **kwargs_)
supermod.uuid.subclass = uuidSub
# end class uuidSub


class uriSub(supermod.uri):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(uriSub, self).__init__(id, extension, value,  **kwargs_)
supermod.uri.subclass = uriSub
# end class uriSub


class canonicalSub(supermod.canonical):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(canonicalSub, self).__init__(id, extension, value,  **kwargs_)
supermod.canonical.subclass = canonicalSub
# end class canonicalSub


class oidSub(supermod.oid):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(oidSub, self).__init__(id, extension, value,  **kwargs_)
supermod.oid.subclass = oidSub
# end class oidSub


class integerSub(supermod.integer):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(integerSub, self).__init__(id, extension, value,  **kwargs_)
supermod.integer.subclass = integerSub
# end class integerSub


class stringSub(supermod.string):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(stringSub, self).__init__(id, extension, value,  **kwargs_)
supermod.string.subclass = stringSub
# end class stringSub


class codeSub(supermod.code):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(codeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.code.subclass = codeSub
# end class codeSub


class dateTimeSub(supermod.dateTime):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(dateTimeSub, self).__init__(id, extension, value,  **kwargs_)
supermod.dateTime.subclass = dateTimeSub
# end class dateTimeSub


class dateSub(supermod.date):
    def __init__(self, id=None, extension=None, value=None, valueOf_=None, **kwargs_):
        super(dateSub, self).__init__(id, extension, value,  **kwargs_)
supermod.date.subclass = dateSub
# end class dateSub


class ValueSet_ContainsSub(supermod.ValueSet_Contains):
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, abstract=None, inactive=None, version=None, code=None, display=None, designation=None, contains=None, **kwargs_):
        super(ValueSet_ContainsSub, self).__init__(id, extension, modifierExtension, system, abstract, inactive, version, code, display, designation, contains,  **kwargs_)
supermod.ValueSet_Contains.subclass = ValueSet_ContainsSub
# end class ValueSet_ContainsSub


class ValueSet_ParameterSub(supermod.ValueSet_Parameter):
    def __init__(self, id=None, extension=None, modifierExtension=None, name=None, valueString=None, valueBoolean=None, valueInteger=None, valueDecimal=None, valueUri=None, valueCode=None, valueDateTime=None, **kwargs_):
        super(ValueSet_ParameterSub, self).__init__(id, extension, modifierExtension, name, valueString, valueBoolean, valueInteger, valueDecimal, valueUri, valueCode, valueDateTime,  **kwargs_)
supermod.ValueSet_Parameter.subclass = ValueSet_ParameterSub
# end class ValueSet_ParameterSub


class ValueSet_ExpansionSub(supermod.ValueSet_Expansion):
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, timestamp=None, total=None, offset=None, parameter=None, contains=None, **kwargs_):
        super(ValueSet_ExpansionSub, self).__init__(id, extension, modifierExtension, identifier, timestamp, total, offset, parameter, contains,  **kwargs_)
supermod.ValueSet_Expansion.subclass = ValueSet_ExpansionSub
# end class ValueSet_ExpansionSub


class ValueSet_FilterSub(supermod.ValueSet_Filter):
    def __init__(self, id=None, extension=None, modifierExtension=None, property=None, op=None, value=None, **kwargs_):
        super(ValueSet_FilterSub, self).__init__(id, extension, modifierExtension, property, op, value,  **kwargs_)
supermod.ValueSet_Filter.subclass = ValueSet_FilterSub
# end class ValueSet_FilterSub


class FilterOperatorSub(supermod.FilterOperator):
    def __init__(self, id=None, extension=None, value=None, **kwargs_):
        super(FilterOperatorSub, self).__init__(id, extension, value,  **kwargs_)
supermod.FilterOperator.subclass = FilterOperatorSub
# end class FilterOperatorSub


class ValueSet_DesignationSub(supermod.ValueSet_Designation):
    def __init__(self, id=None, extension=None, modifierExtension=None, language=None, use=None, value=None, **kwargs_):
        super(ValueSet_DesignationSub, self).__init__(id, extension, modifierExtension, language, use, value,  **kwargs_)
supermod.ValueSet_Designation.subclass = ValueSet_DesignationSub
# end class ValueSet_DesignationSub


class ValueSet_ConceptSub(supermod.ValueSet_Concept):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, display=None, designation=None, **kwargs_):
        super(ValueSet_ConceptSub, self).__init__(id, extension, modifierExtension, code, display, designation,  **kwargs_)
supermod.ValueSet_Concept.subclass = ValueSet_ConceptSub
# end class ValueSet_ConceptSub


class ValueSet_IncludeSub(supermod.ValueSet_Include):
    def __init__(self, id=None, extension=None, modifierExtension=None, system=None, version=None, concept=None, filter=None, valueSet=None, **kwargs_):
        super(ValueSet_IncludeSub, self).__init__(id, extension, modifierExtension, system, version, concept, filter, valueSet,  **kwargs_)
supermod.ValueSet_Include.subclass = ValueSet_IncludeSub
# end class ValueSet_IncludeSub


class ValueSet_ComposeSub(supermod.ValueSet_Compose):
    def __init__(self, id=None, extension=None, modifierExtension=None, lockedDate=None, inactive=None, include=None, exclude=None, **kwargs_):
        super(ValueSet_ComposeSub, self).__init__(id, extension, modifierExtension, lockedDate, inactive, include, exclude,  **kwargs_)
supermod.ValueSet_Compose.subclass = ValueSet_ComposeSub
# end class ValueSet_ComposeSub

class ElementDefinition_DiscriminatorSub(supermod.ElementDefinition_Discriminator):
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, path=None, **kwargs_):
        super(ElementDefinition_DiscriminatorSub, self).__init__(id, extension, modifierExtension, type_, path,  **kwargs_)
supermod.ElementDefinition_Discriminator.subclass = ElementDefinition_DiscriminatorSub
# end class ElementDefinition_DiscriminatorSub


class ElementDefinition_BindingSub(supermod.ElementDefinition_Binding):
    def __init__(self, id=None, extension=None, modifierExtension=None, strength=None, description=None, valueSet=None, **kwargs_):
        super(ElementDefinition_BindingSub, self).__init__(id, extension, modifierExtension, strength, description, valueSet,  **kwargs_)
supermod.ElementDefinition_Binding.subclass = ElementDefinition_BindingSub
# end class ElementDefinition_BindingSub


class ElementDefinition_SlicingSub(supermod.ElementDefinition_Slicing):
    def __init__(self, id=None, extension=None, modifierExtension=None, discriminator=None, description=None, ordered=None, rules=None, **kwargs_):
        super(ElementDefinition_SlicingSub, self).__init__(id, extension, modifierExtension, discriminator, description, ordered, rules,  **kwargs_)
supermod.ElementDefinition_Slicing.subclass = ElementDefinition_SlicingSub
# end class ElementDefinition_SlicingSub


class ElementDefinition_ExampleSub(supermod.ElementDefinition_Example):
    def __init__(self, id=None, extension=None, modifierExtension=None, label=None, valueBase64Binary=None, valueBoolean=None, valueCanonical=None, valueCode=None, valueDate=None, valueDateTime=None, valueDecimal=None, valueId=None, valueInstant=None, valueInteger=None, valueMarkdown=None, valueOid=None, valuePositiveInt=None, valueString=None, valueTime=None, valueUnsignedInt=None, valueUri=None, valueUrl=None, valueUuid=None, valueAddress=None, valueAge=None, valueAnnotation=None, valueAttachment=None, valueCodeableConcept=None, valueCoding=None, valueContactPoint=None, valueCount=None, valueDistance=None, valueDuration=None, valueHumanName=None, valueIdentifier=None, valueMoney=None, valuePeriod=None, valueQuantity=None, valueRange=None, valueRatio=None, valueReference=None, valueSampledData=None, valueSignature=None, valueTiming=None, valueContactDetail=None, valueContributor=None, valueDataRequirement=None, valueExpression=None, valueParameterDefinition=None, valueRelatedArtifact=None, valueTriggerDefinition=None, valueUsageContext=None, valueDosage=None, valueMeta=None, **kwargs_):
        super(ElementDefinition_ExampleSub, self).__init__(id, extension, modifierExtension, label, valueBase64Binary, valueBoolean, valueCanonical, valueCode, valueDate, valueDateTime, valueDecimal, valueId, valueInstant, valueInteger, valueMarkdown, valueOid, valuePositiveInt, valueString, valueTime, valueUnsignedInt, valueUri, valueUrl, valueUuid, valueAddress, valueAge, valueAnnotation, valueAttachment, valueCodeableConcept, valueCoding, valueContactPoint, valueCount, valueDistance, valueDuration, valueHumanName, valueIdentifier, valueMoney, valuePeriod, valueQuantity, valueRange, valueRatio, valueReference, valueSampledData, valueSignature, valueTiming, valueContactDetail, valueContributor, valueDataRequirement, valueExpression, valueParameterDefinition, valueRelatedArtifact, valueTriggerDefinition, valueUsageContext, valueDosage, valueMeta,  **kwargs_)
supermod.ElementDefinition_Example.subclass = ElementDefinition_ExampleSub
# end class ElementDefinition_ExampleSub


class ElementDefinition_TypeSub(supermod.ElementDefinition_Type):
    def __init__(self, id=None, extension=None, modifierExtension=None, code=None, profile=None, targetProfile=None, aggregation=None, versioning=None, **kwargs_):
        super(ElementDefinition_TypeSub, self).__init__(id, extension, modifierExtension, code, profile, targetProfile, aggregation, versioning,  **kwargs_)
supermod.ElementDefinition_Type.subclass = ElementDefinition_TypeSub
# end class ElementDefinition_TypeSub


class ElementDefinition_BaseSub(supermod.ElementDefinition_Base):
    def __init__(self, id=None, extension=None, modifierExtension=None, path=None, min=None, max=None, **kwargs_):
        super(ElementDefinition_BaseSub, self).__init__(id, extension, modifierExtension, path, min, max,  **kwargs_)
supermod.ElementDefinition_Base.subclass = ElementDefinition_BaseSub
# end class ElementDefinition_BaseSub


class ElementDefinition_MappingSub(supermod.ElementDefinition_Mapping):
    def __init__(self, id=None, extension=None, modifierExtension=None, identity=None, language=None, map=None, comment=None, **kwargs_):
        super(ElementDefinition_MappingSub, self).__init__(id, extension, modifierExtension, identity, language, map, comment,  **kwargs_)
supermod.ElementDefinition_Mapping.subclass = ElementDefinition_MappingSub
# end class ElementDefinition_MappingSub


class ElementDefinition_ConstraintSub(supermod.ElementDefinition_Constraint):
    def __init__(self, id=None, extension=None, modifierExtension=None, key=None, requirements=None, severity=None, human=None, expression=None, xpath=None, source=None, **kwargs_):
        super(ElementDefinition_ConstraintSub, self).__init__(id, extension, modifierExtension, key, requirements, severity, human, expression, xpath, source,  **kwargs_)
supermod.ElementDefinition_Constraint.subclass = ElementDefinition_ConstraintSub
# end class ElementDefinition_ConstraintSub


class ElementDefinitionSub(supermod.ElementDefinition):
    def __init__(self, id=None, extension=None, modifierExtension=None, path=None, representation=None, sliceName=None, sliceIsConstraining=None, label=None, code=None, slicing=None, short=None, definition=None, comment=None, requirements=None, alias=None, min=None, max=None, base=None, contentReference=None, type_=None, defaultValueBase64Binary=None, defaultValueBoolean=None, defaultValueCanonical=None, defaultValueCode=None, defaultValueDate=None, defaultValueDateTime=None, defaultValueDecimal=None, defaultValueId=None, defaultValueInstant=None, defaultValueInteger=None, defaultValueMarkdown=None, defaultValueOid=None, defaultValuePositiveInt=None, defaultValueString=None, defaultValueTime=None, defaultValueUnsignedInt=None, defaultValueUri=None, defaultValueUrl=None, defaultValueUuid=None, defaultValueAddress=None, defaultValueAge=None, defaultValueAnnotation=None, defaultValueAttachment=None, defaultValueCodeableConcept=None, defaultValueCoding=None, defaultValueContactPoint=None, defaultValueCount=None, defaultValueDistance=None, defaultValueDuration=None, defaultValueHumanName=None, defaultValueIdentifier=None, defaultValueMoney=None, defaultValuePeriod=None, defaultValueQuantity=None, defaultValueRange=None, defaultValueRatio=None, defaultValueReference=None, defaultValueSampledData=None, defaultValueSignature=None, defaultValueTiming=None, defaultValueContactDetail=None, defaultValueContributor=None, defaultValueDataRequirement=None, defaultValueExpression=None, defaultValueParameterDefinition=None, defaultValueRelatedArtifact=None, defaultValueTriggerDefinition=None, defaultValueUsageContext=None, defaultValueDosage=None, defaultValueMeta=None, meaningWhenMissing=None, orderMeaning=None, fixedBase64Binary=None, fixedBoolean=None, fixedCanonical=None, fixedCode=None, fixedDate=None, fixedDateTime=None, fixedDecimal=None, fixedId=None, fixedInstant=None, fixedInteger=None, fixedMarkdown=None, fixedOid=None, fixedPositiveInt=None, fixedString=None, fixedTime=None, fixedUnsignedInt=None, fixedUri=None, fixedUrl=None, fixedUuid=None, fixedAddress=None, fixedAge=None, fixedAnnotation=None, fixedAttachment=None, fixedCodeableConcept=None, fixedCoding=None, fixedContactPoint=None, fixedCount=None, fixedDistance=None, fixedDuration=None, fixedHumanName=None, fixedIdentifier=None, fixedMoney=None, fixedPeriod=None, fixedQuantity=None, fixedRange=None, fixedRatio=None, fixedReference=None, fixedSampledData=None, fixedSignature=None, fixedTiming=None, fixedContactDetail=None, fixedContributor=None, fixedDataRequirement=None, fixedExpression=None, fixedParameterDefinition=None, fixedRelatedArtifact=None, fixedTriggerDefinition=None, fixedUsageContext=None, fixedDosage=None, fixedMeta=None, patternBase64Binary=None, patternBoolean=None, patternCanonical=None, patternCode=None, patternDate=None, patternDateTime=None, patternDecimal=None, patternId=None, patternInstant=None, patternInteger=None, patternMarkdown=None, patternOid=None, patternPositiveInt=None, patternString=None, patternTime=None, patternUnsignedInt=None, patternUri=None, patternUrl=None, patternUuid=None, patternAddress=None, patternAge=None, patternAnnotation=None, patternAttachment=None, patternCodeableConcept=None, patternCoding=None, patternContactPoint=None, patternCount=None, patternDistance=None, patternDuration=None, patternHumanName=None, patternIdentifier=None, patternMoney=None, patternPeriod=None, patternQuantity=None, patternRange=None, patternRatio=None, patternReference=None, patternSampledData=None, patternSignature=None, patternTiming=None, patternContactDetail=None, patternContributor=None, patternDataRequirement=None, patternExpression=None, patternParameterDefinition=None, patternRelatedArtifact=None, patternTriggerDefinition=None, patternUsageContext=None, patternDosage=None, patternMeta=None, example=None, minValueDate=None, minValueDateTime=None, minValueInstant=None, minValueTime=None, minValueDecimal=None, minValueInteger=None, minValuePositiveInt=None, minValueUnsignedInt=None, minValueQuantity=None, maxValueDate=None, maxValueDateTime=None, maxValueInstant=None, maxValueTime=None, maxValueDecimal=None, maxValueInteger=None, maxValuePositiveInt=None, maxValueUnsignedInt=None, maxValueQuantity=None, maxLength=None, condition=None, constraint=None, mustSupport=None, isModifier=None, isModifierReason=None, isSummary=None, binding=None, mapping=None, **kwargs_):
        super(ElementDefinitionSub, self).__init__(id, extension, modifierExtension, path, representation, sliceName, sliceIsConstraining, label, code, slicing, short, definition, comment, requirements, alias, min, max, base, contentReference, type_, defaultValueBase64Binary, defaultValueBoolean, defaultValueCanonical, defaultValueCode, defaultValueDate, defaultValueDateTime, defaultValueDecimal, defaultValueId, defaultValueInstant, defaultValueInteger, defaultValueMarkdown, defaultValueOid, defaultValuePositiveInt, defaultValueString, defaultValueTime, defaultValueUnsignedInt, defaultValueUri, defaultValueUrl, defaultValueUuid, defaultValueAddress, defaultValueAge, defaultValueAnnotation, defaultValueAttachment, defaultValueCodeableConcept, defaultValueCoding, defaultValueContactPoint, defaultValueCount, defaultValueDistance, defaultValueDuration, defaultValueHumanName, defaultValueIdentifier, defaultValueMoney, defaultValuePeriod, defaultValueQuantity, defaultValueRange, defaultValueRatio, defaultValueReference, defaultValueSampledData, defaultValueSignature, defaultValueTiming, defaultValueContactDetail, defaultValueContributor, defaultValueDataRequirement, defaultValueExpression, defaultValueParameterDefinition, defaultValueRelatedArtifact, defaultValueTriggerDefinition, defaultValueUsageContext, defaultValueDosage, defaultValueMeta, meaningWhenMissing, orderMeaning, fixedBase64Binary, fixedBoolean, fixedCanonical, fixedCode, fixedDate, fixedDateTime, fixedDecimal, fixedId, fixedInstant, fixedInteger, fixedMarkdown, fixedOid, fixedPositiveInt, fixedString, fixedTime, fixedUnsignedInt, fixedUri, fixedUrl, fixedUuid, fixedAddress, fixedAge, fixedAnnotation, fixedAttachment, fixedCodeableConcept, fixedCoding, fixedContactPoint, fixedCount, fixedDistance, fixedDuration, fixedHumanName, fixedIdentifier, fixedMoney, fixedPeriod, fixedQuantity, fixedRange, fixedRatio, fixedReference, fixedSampledData, fixedSignature, fixedTiming, fixedContactDetail, fixedContributor, fixedDataRequirement, fixedExpression, fixedParameterDefinition, fixedRelatedArtifact, fixedTriggerDefinition, fixedUsageContext, fixedDosage, fixedMeta, patternBase64Binary, patternBoolean, patternCanonical, patternCode, patternDate, patternDateTime, patternDecimal, patternId, patternInstant, patternInteger, patternMarkdown, patternOid, patternPositiveInt, patternString, patternTime, patternUnsignedInt, patternUri, patternUrl, patternUuid, patternAddress, patternAge, patternAnnotation, patternAttachment, patternCodeableConcept, patternCoding, patternContactPoint, patternCount, patternDistance, patternDuration, patternHumanName, patternIdentifier, patternMoney, patternPeriod, patternQuantity, patternRange, patternRatio, patternReference, patternSampledData, patternSignature, patternTiming, patternContactDetail, patternContributor, patternDataRequirement, patternExpression, patternParameterDefinition, patternRelatedArtifact, patternTriggerDefinition, patternUsageContext, patternDosage, patternMeta, example, minValueDate, minValueDateTime, minValueInstant, minValueTime, minValueDecimal, minValueInteger, minValuePositiveInt, minValueUnsignedInt, minValueQuantity, maxValueDate, maxValueDateTime, maxValueInstant, maxValueTime, maxValueDecimal, maxValueInteger, maxValuePositiveInt, maxValueUnsignedInt, maxValueQuantity, maxLength, condition, constraint, mustSupport, isModifier, isModifierReason, isSummary, binding, mapping,  **kwargs_)
supermod.ElementDefinition.subclass = ElementDefinitionSub
# end class ElementDefinitionSub


class ProdCharacteristicSub(supermod.ProdCharacteristic):
    def __init__(self, id=None, extension=None, modifierExtension=None, height=None, width=None, depth=None, weight=None, nominalVolume=None, externalDiameter=None, shape=None, color=None, imprint=None, image=None, scoring=None, **kwargs_):
        super(ProdCharacteristicSub, self).__init__(id, extension, modifierExtension, height, width, depth, weight, nominalVolume, externalDiameter, shape, color, imprint, image, scoring,  **kwargs_)
supermod.ProdCharacteristic.subclass = ProdCharacteristicSub
# end class ProdCharacteristicSub


class Timing_RepeatSub(supermod.Timing_Repeat):
    def __init__(self, id=None, extension=None, modifierExtension=None, boundsDuration=None, boundsRange=None, boundsPeriod=None, count=None, countMax=None, duration=None, durationMax=None, durationUnit=None, frequency=None, frequencyMax=None, period=None, periodMax=None, periodUnit=None, dayOfWeek=None, timeOfDay=None, when=None, offset=None, **kwargs_):
        super(Timing_RepeatSub, self).__init__(id, extension, modifierExtension, boundsDuration, boundsRange, boundsPeriod, count, countMax, duration, durationMax, durationUnit, frequency, frequencyMax, period, periodMax, periodUnit, dayOfWeek, timeOfDay, when, offset,  **kwargs_)
supermod.Timing_Repeat.subclass = Timing_RepeatSub
# end class Timing_RepeatSub


class TimingSub(supermod.Timing):
    def __init__(self, id=None, extension=None, modifierExtension=None, event=None, repeat=None, code=None, **kwargs_):
        super(TimingSub, self).__init__(id, extension, modifierExtension, event, repeat, code,  **kwargs_)
supermod.Timing.subclass = TimingSub
# end class TimingSub


class ProductShelfLifeSub(supermod.ProductShelfLife):
    def __init__(self, id=None, extension=None, modifierExtension=None, identifier=None, type_=None, period=None, specialPrecautionsForStorage=None, **kwargs_):
        super(ProductShelfLifeSub, self).__init__(id, extension, modifierExtension, identifier, type_, period, specialPrecautionsForStorage,  **kwargs_)
supermod.ProductShelfLife.subclass = ProductShelfLifeSub
# end class ProductShelfLifeSub


class PopulationSub(supermod.Population):
    def __init__(self, id=None, extension=None, modifierExtension=None, ageRange=None, ageCodeableConcept=None, gender=None, race=None, physiologicalCondition=None, **kwargs_):
        super(PopulationSub, self).__init__(id, extension, modifierExtension, ageRange, ageCodeableConcept, gender, race, physiologicalCondition,  **kwargs_)
supermod.Population.subclass = PopulationSub
# end class PopulationSub


class SubstanceAmount_ReferenceRangeSub(supermod.SubstanceAmount_ReferenceRange):
    def __init__(self, id=None, extension=None, modifierExtension=None, lowLimit=None, highLimit=None, **kwargs_):
        super(SubstanceAmount_ReferenceRangeSub, self).__init__(id, extension, modifierExtension, lowLimit, highLimit,  **kwargs_)
supermod.SubstanceAmount_ReferenceRange.subclass = SubstanceAmount_ReferenceRangeSub
# end class SubstanceAmount_ReferenceRangeSub


class SubstanceAmountSub(supermod.SubstanceAmount):
    def __init__(self, id=None, extension=None, modifierExtension=None, amountQuantity=None, amountRange=None, amountString=None, amountType=None, amountText=None, referenceRange=None, **kwargs_):
        super(SubstanceAmountSub, self).__init__(id, extension, modifierExtension, amountQuantity, amountRange, amountString, amountType, amountText, referenceRange,  **kwargs_)
supermod.SubstanceAmount.subclass = SubstanceAmountSub
# end class SubstanceAmountSub


class MarketingStatusSub(supermod.MarketingStatus):
    def __init__(self, id=None, extension=None, modifierExtension=None, country=None, jurisdiction=None, status=None, dateRange=None, restoreDate=None, **kwargs_):
        super(MarketingStatusSub, self).__init__(id, extension, modifierExtension, country, jurisdiction, status, dateRange, restoreDate,  **kwargs_)
supermod.MarketingStatus.subclass = MarketingStatusSub
# end class MarketingStatusSub


class Dosage_DoseAndRateSub(supermod.Dosage_DoseAndRate):
    def __init__(self, id=None, extension=None, modifierExtension=None, type_=None, doseRange=None, doseQuantity=None, rateRatio=None, rateRange=None, rateQuantity=None, **kwargs_):
        super(Dosage_DoseAndRateSub, self).__init__(id, extension, modifierExtension, type_, doseRange, doseQuantity, rateRatio, rateRange, rateQuantity,  **kwargs_)
supermod.Dosage_DoseAndRate.subclass = Dosage_DoseAndRateSub
# end class Dosage_DoseAndRateSub


class DosageSub(supermod.Dosage):
    def __init__(self, id=None, extension=None, modifierExtension=None, sequence=None, text=None, additionalInstruction=None, patientInstruction=None, timing=None, asNeededBoolean=None, asNeededCodeableConcept=None, site=None, route=None, method=None, doseAndRate=None, maxDosePerPeriod=None, maxDosePerAdministration=None, maxDosePerLifetime=None, **kwargs_):
        super(DosageSub, self).__init__(id, extension, modifierExtension, sequence, text, additionalInstruction, patientInstruction, timing, asNeededBoolean, asNeededCodeableConcept, site, route, method, doseAndRate, maxDosePerPeriod, maxDosePerAdministration, maxDosePerLifetime,  **kwargs_)
supermod.Dosage.subclass = DosageSub
# end class DosageSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=True):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ValueSet'
        rootClass = supermod.ValueSet
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ValueSet'
        rootClass = supermod.ValueSet
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ValueSet'
        rootClass = supermod.ValueSet
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ValueSet'
        rootClass = supermod.ValueSet
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
