#!/usr/bin/env python

#
# Generated Thu Apr  8 15:08:49 2021 by generateDS.py version 2.38.5.
# Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)]
#
# Command line options:
#   ('-a', 'xml:')
#   ('-o', 'ClaML3Super.py')
#   ('-s', 'ClaML3.py')
#
# Command line arguments:
#   Y:\Termserver\MaLaC-CT\ClaML3.0.0.xsd
#
# Command line:
#   .\generateDS.py -a "xml:" -o "ClaML3Super.py" -s "ClaML3.py" Y:\Termserver\MaLaC-CT\ClaML3.0.0.xsd
#
# Current working directory (os.getcwd()):
#   generateDS-2.38.5
#

import os
import sys
from lxml import etree as etree_

import claml3super as supermod
from prop_csv_and_master import PropCsvAndMaster as pcam

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

class ClaML3Sub(supermod.ClaML3, pcam):
    def __init__(self, version=None, Classification=None, **kwargs_):
        super(ClaML3Sub, self).__init__(version, Classification,  **kwargs_)

    def get_title(self):
        return self.get_Classification()[0].get_Title()[0].get_name()

    def get_version(self):
        return self.get_Classification()[0].get_Title()[0].get_version()

    def exporto(self, outfile):
        #required ClaMl3 fields        
        claml3 = ClaML3Sub('3.0.0')
        if hasattr(self,'language'):
            lang = self.get_language()
        else:
            print("A language code is required in ClaMl3. Please type one in (i.e. 'en','de-DE' or 'de-AT') and press enter:")
            lang = 'en'#input()
        title = self.get_title()
        claKinds = ClassKindsSub()
        claKinds.add_ClassKind(ClassKindSub("code"))
        rubKinds = RubricKindsSub()
        rubKinds.add_RubricKind(RubricKindSub("preferred"))

        #optional ClaMl3 fields
        metas = []
        for oneProp in self.get_property():
            metas.append(MetaSub(oneProp.code, oneProp.type))#,oneProp.uri or None, oneProp.description or None)))

        claml3.add_Classification(ClassificationSub(lang,None,None,None,[TitleSub(title)],None,None,claKinds,None,rubKinds,None,None,None))
        claml3.export(outfile, 0)


supermod.ClaML3.subclass = ClaML3Sub
# end class ClaMLSub


class ClassificationSub(supermod.Classification):
    def __init__(self, lang=None, space='default', Meta=None, Identifier=None, Title=None, Authors=None, Variants=None, ClassKinds=None, UsageKinds=None, RubricKinds=None, Modifier=None, ModifierClass=None, Class=None, **kwargs_):
        super(ClassificationSub, self).__init__(lang, space, Meta, Identifier, Title, Authors, Variants, ClassKinds, UsageKinds, RubricKinds, Modifier, ModifierClass, Class,  **kwargs_)
supermod.Classification.subclass = ClassificationSub
# end class ClassificationSub


class VariantsSub(supermod.Variants):
    def __init__(self, Variant=None, **kwargs_):
        super(VariantsSub, self).__init__(Variant,  **kwargs_)
supermod.Variants.subclass = VariantsSub
# end class VariantsSub


class VariantSub(supermod.Variant):
    def __init__(self, name=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(VariantSub, self).__init__(name, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Variant.subclass = VariantSub
# end class VariantSub


class MetaSub(supermod.Meta):
    def __init__(self, name=None, value=None, variants=None, kind=None, **kwargs_):
        super(MetaSub, self).__init__(name, value, variants, kind,  **kwargs_)
supermod.Meta.subclass = MetaSub
# end class MetaSub


class IdentifierSub(supermod.Identifier):
    def __init__(self, authority=None, uid=None, variants=None, date=None, effectivedate=None, expirationdate=None, status=None, **kwargs_):
        super(IdentifierSub, self).__init__(authority, uid, variants, date, effectivedate, expirationdate, status,  **kwargs_)
supermod.Identifier.subclass = IdentifierSub
# end class IdentifierSub


class TitleSub(supermod.Title):
    def __init__(self, name=None, version=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(TitleSub, self).__init__(name, version, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Title.subclass = TitleSub
# end class TitleSub


class AuthorsSub(supermod.Authors):
    def __init__(self, variants=None, Author=None, **kwargs_):
        super(AuthorsSub, self).__init__(variants, Author,  **kwargs_)
supermod.Authors.subclass = AuthorsSub
# end class AuthorsSub


class AuthorSub(supermod.Author):
    def __init__(self, name=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(AuthorSub, self).__init__(name, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Author.subclass = AuthorSub
# end class AuthorSub


class ClassKindsSub(supermod.ClassKinds):
    def __init__(self, ClassKind=None, **kwargs_):
        super(ClassKindsSub, self).__init__(ClassKind,  **kwargs_)
supermod.ClassKinds.subclass = ClassKindsSub
# end class ClassKindsSub


class UsageKindsSub(supermod.UsageKinds):
    def __init__(self, variants=None, UsageKind=None, **kwargs_):
        super(UsageKindsSub, self).__init__(variants, UsageKind,  **kwargs_)
supermod.UsageKinds.subclass = UsageKindsSub
# end class UsageKindsSub


class RubricKindsSub(supermod.RubricKinds):
    def __init__(self, RubricKind=None, **kwargs_):
        super(RubricKindsSub, self).__init__(RubricKind,  **kwargs_)
supermod.RubricKinds.subclass = RubricKindsSub
# end class RubricKindsSub


class ClassKindSub(supermod.ClassKind):
    def __init__(self, name=None, variants=None, Display=None, **kwargs_):
        super(ClassKindSub, self).__init__(name, variants, Display,  **kwargs_)
supermod.ClassKind.subclass = ClassKindSub
# end class ClassKindSub


class UsageKindSub(supermod.UsageKind):
    def __init__(self, name=None, mark=None, variants=None, **kwargs_):
        super(UsageKindSub, self).__init__(name, mark, variants,  **kwargs_)
supermod.UsageKind.subclass = UsageKindSub
# end class UsageKindSub


class UsageSub(supermod.Usage):
    def __init__(self, kind=None, variants=None, **kwargs_):
        super(UsageSub, self).__init__(kind, variants,  **kwargs_)
supermod.Usage.subclass = UsageSub
# end class UsageSub


class RubricKindSub(supermod.RubricKind):
    def __init__(self, name=None, inherited=True, variants=None, Display=None, **kwargs_):
        super(RubricKindSub, self).__init__(name, inherited, variants, Display,  **kwargs_)
supermod.RubricKind.subclass = RubricKindSub
# end class RubricKindSub


class DisplaySub(supermod.Display):
    def __init__(self, lang=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(DisplaySub, self).__init__(lang, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Display.subclass = DisplaySub
# end class DisplaySub


class ModifierSub(supermod.Modifier):
    def __init__(self, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Meta=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierSub, self).__init__(code, kind, variants, version, effectivedate, expirationdate, status, Meta, SubClass, Rubric, History,  **kwargs_)
supermod.Modifier.subclass = ModifierSub
# end class ModifierSub


class ModifierClassSub(supermod.ModifierClass):
    def __init__(self, modifier=None, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Usage=None, Meta=None, SuperClass=None, SubClass=None, Rubric=None, History=None, **kwargs_):
        super(ModifierClassSub, self).__init__(modifier, code, kind, variants, version, effectivedate, expirationdate, status, Usage, Meta, SuperClass, SubClass, Rubric, History,  **kwargs_)
supermod.ModifierClass.subclass = ModifierClassSub
# end class ModifierClassSub


class ClassSub(supermod.Class):
    def __init__(self, code=None, kind=None, variants=None, version=None, effectivedate=None, expirationdate=None, status=None, Usage=None, Meta=None, SuperClass=None, SubClass=None, ModifiedBy=None, ValidModifierClass=None, ExcludeModifier=None, Rubric=None, History=None, **kwargs_):
        super(ClassSub, self).__init__(code, kind, variants, version, effectivedate, expirationdate, status, Usage, Meta, SuperClass, SubClass, ModifiedBy, ValidModifierClass, ExcludeModifier, Rubric, History,  **kwargs_)
supermod.Class.subclass = ClassSub
# end class ClassSub


class ModifiedBySub(supermod.ModifiedBy):
    def __init__(self, code=None, position=None, variants=None, optionalmodifier=False, Meta=None, **kwargs_):
        super(ModifiedBySub, self).__init__(code, position, variants, optionalmodifier, Meta,  **kwargs_)
supermod.ModifiedBy.subclass = ModifiedBySub
# end class ModifiedBySub


class ExcludeModifierSub(supermod.ExcludeModifier):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(ExcludeModifierSub, self).__init__(code, variants,  **kwargs_)
supermod.ExcludeModifier.subclass = ExcludeModifierSub
# end class ExcludeModifierSub


class ValidModifierClassSub(supermod.ValidModifierClass):
    def __init__(self, code=None, variants=None, position=None, Meta=None, ValidModifierClass_member=None, **kwargs_):
        super(ValidModifierClassSub, self).__init__(code, variants, position, Meta, ValidModifierClass_member,  **kwargs_)
supermod.ValidModifierClass.subclass = ValidModifierClassSub
# end class ValidModifierClassSub


class RubricSub(supermod.Rubric):
    def __init__(self, id=None, kind=None, variants=None, Usage=None, Label=None, History=None, **kwargs_):
        super(RubricSub, self).__init__(id, kind, variants, Usage, Label, History,  **kwargs_)
supermod.Rubric.subclass = RubricSub
# end class RubricSub


class LabelSub(supermod.Label):
    def __init__(self, lang=None, space='default', variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(LabelSub, self).__init__(lang, space, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Label.subclass = LabelSub
# end class LabelSub


class HistorySub(supermod.History):
    def __init__(self, author=None, date=None, variants=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(HistorySub, self).__init__(author, date, variants, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.History.subclass = HistorySub
# end class HistorySub


class SuperClassSub(supermod.SuperClass):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(SuperClassSub, self).__init__(code, variants,  **kwargs_)
supermod.SuperClass.subclass = SuperClassSub
# end class SuperClassSub


class SubClassSub(supermod.SubClass):
    def __init__(self, code=None, variants=None, **kwargs_):
        super(SubClassSub, self).__init__(code, variants,  **kwargs_)
supermod.SubClass.subclass = SubClassSub
# end class SubClassSub


class FragmentSub(supermod.Fragment):
    def __init__(self, class_=None, type_='item', Usage=None, valueOf_=None, mixedclass_=None, content_=None, **kwargs_):
        super(FragmentSub, self).__init__(class_, type_, Usage, valueOf_, mixedclass_, content_,  **kwargs_)
supermod.Fragment.subclass = FragmentSub
# end class FragmentSub


class IncludeSub(supermod.Include):
    def __init__(self, class_=None, rubric=None, **kwargs_):
        super(IncludeSub, self).__init__(class_, rubric,  **kwargs_)
supermod.Include.subclass = IncludeSub
# end class IncludeSub


class IncludeDescendantsSub(supermod.IncludeDescendants):
    def __init__(self, code=None, kind=None, **kwargs_):
        super(IncludeDescendantsSub, self).__init__(code, kind,  **kwargs_)
supermod.IncludeDescendants.subclass = IncludeDescendantsSub
# end class IncludeDescendantsSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
        rootTag = 'ClaML'
        rootClass = supermod.ClaML3
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
