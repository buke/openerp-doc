#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
import re
import optparse
import pickle
from shutil import copy as filecopy, copytree as dircopy
import operator


__version__ = '0.3.1'
USAGE = """%prog [options] <lang code>
eg. %prog fr"""

conf = {
    'ext': 'rst',
    'build_default_dir': 'i18n',
}

I18N_PREFIX = '.. i18n:'
I18N_REGEX = r'^\.\. i18n: '
# TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970
I18N_REGEXFIX = r'(\n\.\. i18n: .*\n)..\n\n'
# TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970
PICKLE_FILENAME = 'i18n.pickle'
REQUIRED_ARG_NBR = 1
IGNORED_FILES_SUFFIX = ['pyc', conf['ext']]
IGNORED_FILES_SUFFIX.extend(['~%d~' % nbr for nbr in range(1, 10)])
FILES_TO_COPY = ['Makefile', 'copy_images.sh', 'index.php' ]
DIRS_TO_COPY = ['texfiles']


has_directive_regex = re.compile(r"""\.\.\s+(?P<directive>[\w-]+)::(?P<content>.*)""")
# TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
#is_literal_block_regex = re.compile(r""".*::$""")
is_literal_block_regex = re.compile(r""".*::(?P<literal>.*)""")
# TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
is_list_item_regex = re.compile(r"""^\s*(?P<list_item_char>#\.|\*|-|\d+\.){1,1}\s+(?P<content>.*)""")
is_indented_regex = re.compile(r"""^\s+""")
is_label_regex = re.compile(r"""^\s*\.\.\s+_[\w-]+:""")


def propertx(fct):
    """Decorator to simplify the use of property.
       Like @property for attrs who need more than a getter.
       For getter only property use @property."""
    arg = [None, None, None, None]
    for i, f in enumerate(fct()):
        arg[i] = f
    if not arg[3]:
        arg[3] = fct.__doc__

    return property(*arg)


class I18nSection(object):

    _slice_int = 80 # how many chars to display in repr.
    def __init__(self, lines, i18n=False):
        self.lines = lines
        self._raw_content = ''
        self._content = ''
        self._i18n = i18n

    def __len__(self):
        return len(self.lines)

    @propertx
    def content():
        def get(self):
            if self._i18n:
                lines = ["%s %s" % (I18N_PREFIX, line,) for line in self.lines]
            else:
                lines = self.lines
            return '\n'.join(lines)
        return (get, None)

    @propertx
    def raw_content():
        def get(self):
            return '\n'.join([re.sub(I18N_REGEX, '', line) for line in self.lines])
        return (get, None)

    @propertx
    def i18n():
        """is this an i18n section or an original section ?"""
        def get(self):
            return self._i18n or self.content.startswith(I18N_PREFIX)
        return (get, None)

    def has_directive(self):
        match_obj = has_directive_regex.search(self.content)
        if match_obj:
            return match_obj.group('directive')
        else:
            return False

    def is_literal_block(self):
        match_obj = is_literal_block_regex.search(self.content)
        if match_obj:
            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
            # TruongSinh Tran: I dont know why, but I have to return True rather than the numbers of literal
            return True
            #return match_obj.group('literal')
            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
        else:
            return False

    def is_indented(self):
        match_obj = is_indented_regex.search(self.content)
        if match_obj:
            return True
        else:
            return False

    def is_label_and_not_merged(self):
        def _is_merged(content, match_object):
            """A label is merged if it's followed by 2 new lines (or the like)"""
            return content[match_object.start():match_object.end()+2][-2:] in ('\n\n', '\r\n\r\n', '\r\r')

        match_obj = is_label_regex.search(self.content)
        if match_obj and not _is_merged(self.content, match_obj):
            return True
        else:
            return False

    def is_list_item(self):
        match_obj = is_list_item_regex.search(self.content)
        if match_obj:
            return match_obj.group('list_item_char')
        else:
            return False

    def merge(self, next_section):
        self.lines.append('')
        self.lines.extend(next_section.lines)
        next_section.lines = []

    def __repr__(self):
        return """<%s object, lines: %s, directive:%s literal_block: %s list:%s "%s">""" % (
            self.__class__.__name__,
            len(self.lines),
            self.has_directive() or 'None',
            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
            #bool(self.is_literal_block()) or 'None',
            self.is_literal_block() or 'None',
            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/401597
            self.is_list_item() or 'None',
            self.content[:self._slice_int],
        )


class FileContent(object):
    def __init__(self, lines, lang):
        self.lines = lines
        self.lang = lang
        self._content = ''

    def _get_content(self):
        raise NotImplementedError("Please implement this method in a subclass")

    @propertx
    def content():
        def get(self):
            return self._get_content()
        return (get, None)

    def build_sections(self, lines):
        # separate file sections:
        section = []
        sections = []
        for i, line in enumerate(lines):
            line = line.replace('\n', '')
            orig_section = I18nSection(filter(None, section))
            # line is empty -> this is a paragraph separator
            if not line:
                sections.append(orig_section)
                section = []
                continue
            # (or this is the last line):
            elif i+1 == len(lines):
                section.append(line)
                orig_section = I18nSection(filter(None, section))
                sections.append(orig_section)
                section = []
                continue
            section.append(line)
        return sections

    def merge_sections(self, sections):
        """Merge contiguous sections when necessary (eg.: multiline directives for example)"""
        def _merge_section(sections, last):
            for i, section in enumerate(sections):
                if i+1 == len(sections):
                    last = True
                next_section = self._get_next_non_empty_section(sections, i)

                if section and next_section:
                    if (section.has_directive() or section.is_literal_block()) and \
                        next_section.is_indented() or \
                        section.is_label_and_not_merged():
                        section.merge(next_section)
                        return sections, last
                    elif section.is_list_item() and next_section.is_list_item():
                        section.merge(next_section)
                        return sections, last
            return sections, last

        if sections:
            last = False
            while not last:
                sections, last = _merge_section(sections, last)

        return sections

    def _get_next_non_empty_section(self, sections, index):
        for section in sections[index+1:]:
            if section:
                return section
        return None


class TemplateContent(FileContent):
    def __init__(self, lines, lang):
        super(TemplateContent, self).__init__(lines, lang)

    def add_i18n_sections(self, sections):
        new_sections = []
        for section in sections:
            i18nsection = I18nSection(section.lines, True)
            new_sections.append(i18nsection)
            new_sections.append(section)
        return new_sections

    def _get_content(self):
        sections = self.build_sections(self.lines)
        sections = self.merge_sections(sections)
        sections = self.add_i18n_sections(sections)

        # build file content:
        content = ''
        for i, section in enumerate(sections):
            if section:
                if not section.i18n:
                    translated_content = TranslationMemory.remember(section.raw_content, self.lang)
                    content += '\n' + translated_content + '\n'
                else:
                    # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970
                    #content += '\n' + section.content + '\n'
                    content += '\n' + section.content + '\n..\n'
                    # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970
        return content


class SectionManager(object):
    def __init__(self, lang, options=None):
        self.lang = lang
        self.src_dir, self.dst_dir = self._get_src_and_dst_dir()
        self.options = options

        self._check_src_dir()
        self.source_content, self.files_to_copy = self.get_structure()
        self._build_dst_structure()
        self.translation_memory = {}

    def _get_src_and_dst_dir(self):
        src_dir = os.path.join('.', 'source')
        dst_dir = os.path.join(conf['build_default_dir'], self.lang, 'source') + os.sep
        return (src_dir, dst_dir)

    def run(self):
        # checking that files are new to avoid overwriting a big work:
        allexisting, allnew = 0, 0
        for k, v in self.source_content.items():
            existing, new = self._check_files(k, v)
            allexisting += existing
            allnew += new

        TranslationMemory.create_memory()
        for k, v in self.source_content.items():
            self.create_templates(k, v)

    def _check_src_dir(self):
        """Check that source directory is a valid directory."""
        if not os.path.isdir(self.src_dir):
            if self.cmd == 'copy-translated':
                msg = "Source directory '%s' does not exists."
                msg += " You should probably create the translation templates before trying to copy them."
            else:
                msg = "Source directory '%s' does not exists."
            msg = msg % (self.src_dir, )
            raise OSError(msg)

    def _build_dst_structure(self):
        """Create the necessary directory tree. eg.:
             i18n
             `-- fr
                 |-- build
                 `-- source
                     `-- ...
        """
        for d in self.source_content.keys():
        #for d in self.source_content.keys():
            dst_filepath = re.sub("^%s" % self.src_dir, self.dst_dir, d)
            if not os.path.exists(dst_filepath):
                os.makedirs(dst_filepath)
        build_dir = os.path.join(conf['build_default_dir'], self.lang, 'build')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        for fn in FILES_TO_COPY:
            filecopy(fn, os.path.join(conf['build_default_dir'], self.lang, fn))

        for dn in DIRS_TO_COPY:
            if not os.path.exists(os.path.join(conf['build_default_dir'], self.lang, dn)):
                dircopy(dn, os.path.join(conf['build_default_dir'], self.lang, dn), symlinks=True)

        for d, lst in self.files_to_copy.items():
            for fn in lst:
                if not os.path.exists(os.path.join(conf['build_default_dir'], self.lang, d, fn)):
                    src = os.path.join(d, fn)
                    dst = os.path.join(conf['build_default_dir'], self.lang, d, fn)
                    filecopy(src, dst)

    def get_structure(self):
        """Get the source directory structure"""
        def _visit_func(arg, dirname, names):
            content[dirname] = [name for name in names if name.endswith('.'+conf['ext'])]
            files_to_copy[dirname] = [name for name in names if not filter(name.endswith, map(operator.add, '.'*len(IGNORED_FILES_SUFFIX), IGNORED_FILES_SUFFIX))]

        content = {}
        files_to_copy = {}
        os.path.walk(self.src_dir, _visit_func, None)
        for directory in os.listdir(self.src_dir):
            directory = os.path.join(self.src_dir, directory)
            os.path.walk(directory, _visit_func, None)
        return content, files_to_copy

    def create_template(self, src_filepath, dst_filepath):
        def _get_file_content(filepath):
            _f = open(filepath, 'r')

            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970
            #_lines = _f.readlines()
            lines = _f.read()
            lines = re.sub(I18N_REGEXFIX, r'\1\n', lines)
            _lines = lines.splitlines(True)
            # It is quite dirty, isn't it? Somebody can refractor?
            # TruongSinh Tran: Fix https://bugs.launchpad.net/openobject-doc/+bug/400970

            _f.close()
            return _lines

        src_lines = _get_file_content(src_filepath)
        # if dst file exists: read it:
        if os.path.exists(dst_filepath):
            old_lines = _get_file_content(dst_filepath)
            old_tmpl = TemplateContent(old_lines, self.lang)
#             old_content = old_tmpl.content
            # store old content (bacause it can be translated) in translation memory:
            sections = old_tmpl.build_sections(old_lines)
            sections = old_tmpl.merge_sections(sections)
            for i, section in enumerate(sections):
                if section and not section.i18n:
                    previous_section = sections[i-1]
                    TranslationMemory.memorize(previous_section.raw_content, section.content, self.lang)

        # write destination file:
        dst_file = open(dst_filepath, 'w')
        tmpl_content = TemplateContent(src_lines, self.lang).content
        dst_file.write(tmpl_content)
        dst_file.close()

    def _check_files(self, directory, files):
        def _set_dst_filepath(filepath):
            dst_filepath = re.sub(self.src_dir, self.dst_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dst_filepath

        existing, new = 0, 0
        for filename in files:
            filepath = os.path.join(directory, filename)
            dst_filepath = _set_dst_filepath(filepath)
            new += 1
            if os.path.exists(dst_filepath):
                existing += 1
        return existing, new

    def create_templates(self, directory, files):
        def _set_dst_filepath(filepath):
            dst_filepath = re.sub(self.src_dir, self.dst_dir, filepath).replace('.'+conf['ext'], '') + '.' + conf['ext']
            return dst_filepath

        for filename in files:
            filepath = os.path.join(directory, filename)
            dst_filepath = _set_dst_filepath(filepath)
            self.create_template(filepath, dst_filepath)


class TranslationMemory(object):
    pickle_filename = PICKLE_FILENAME
    memory = {}

    @classmethod
    def memorize(cls, key, content, lang):
        if not cls.memory.get(lang, None):
            cls.memory[lang] = {key: content}
        else:
            cls.memory[lang][key] = content

    @classmethod
    def remember(cls, key, lang):
        if not cls.memory.get(lang, None):
            content = key
        else:
            try:
                content = cls.memory[lang][key]
            except KeyError:
                content = key
        return content

    @classmethod
    def save_memory(cls):
        try:
            pickled_file = open(cls.pickle_filename, 'w')
            pickle.dump(cls.memory, pickled_file)
        finally:
            pickled_file.close()

    @classmethod
    def create_memory(cls):
        if os.path.exists(cls.pickle_filename):
            try:
                pickled_file = open(cls.pickle_filename, 'r')
                cls.memory = pickle.load(pickled_file)
            finally:
                pickled_file.close()
        else:
            cls.memory = {}


class I18nBuilderArgumentException(Exception):
    pass


class ArgDispatcher(object):
    def __init__(self, args, opts):
        self.args = args
        self.options = opts
        self._check_args()

    def _check_args(self):
        args_len = len(self.args)
        if args_len != REQUIRED_ARG_NBR:
            raise I18nBuilderArgumentException("Incorrect number of arguments. Expected %d, got %d" % (REQUIRED_ARG_NBR, args_len, ))

    def dispatch(self):
        src_mngr = SectionManager(self.args[0], self.options)
        src_mngr.run()


def _main():
    parser = optparse.OptionParser(usage=USAGE, version=__version__)
    #parser.add_option('', '--save-memory', dest='save_memory', default=False, action="store_true", help="Save the translation memory in a Python pickle file")
    (opt, args) = parser.parse_args()

    try:
        argdispatcher = ArgDispatcher(args, opt)
    except (I18nBuilderArgumentException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())
    try:
        argdispatcher.dispatch()
    except (OSError, ), e:
        sys.exit("Error: %s" % (e, ))


if __name__ == '__main__':
    _main()

