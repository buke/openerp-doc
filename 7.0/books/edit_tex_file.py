#!/usr/bin/python
#-*- encoding: utf8 -*-

import os, sys
from glob import glob
from shutil import copy2 as filecopy
import re
import optparse

__version__ = '0.1'
USAGE = """%prog [options] <latex build directory>"""

CRLF = '\n\r'
CONTENT_STARTS_AT_PAGE = 5 # we remove the first page and add 3 pages

rgxs = {
    'begin_chapter': r"""\\chapter""",
    'begin_conclusion': r"""(?P<directive>SPHINXBEGINCONCLUSIONDIRECTIVE)(?P<after>.*)""",
    'begin_document': r"""^\\begin\{document\}""",
    'begin_figure': r"""(?P<envname>\\begin\{figure\})(?P<opt>.*)""",
    'begin_notice': r"""\\begin\{notice\}""",
    'begin_quote': r"""\\begin\{quote\}""",
    'begin_tabular': r"""(?P<envname>\\begin\{tabular.*?\})(?P<opt>\{.*?\})(?P<coldef>\{.*?\})""",
    'begin_threeparttable': r"""(?P<envname>\\begin\{threeparttable.*?\})""",
    'documentclass': r"""^\\documentclass\[(?P<opt>[\w,]+)\]\{(?P<class>\w+)\}""",
    'end_document': r"""^\\end\{document\}""",
    'end_figure': r"""(?P<before>.*)(?P<envname>\\end\{figure\})(?P<after>)""",
    'end_foreword': r"""(?P<directive>SPHINXENDFOREWORDDIRECTIVE)(?P<after>.*)""",
    'end_notice': r"""\\end\{notice\}""",
    'end_quote': r"""\\end\{quote\}""",
    'end_tabular': r"""(?P<envname>\\end\{tabular.*?\})""",
    'end_threeparttable': r"""(?P<envname>\\end\{threeparttable.*?\})""",
    'fancychapter': r"""^\\usepackage\[Bjarne\]\{fncychap\}""",
    'maketitle': r"""^\\maketitle""",
    'printindex': r"""^\\printindex""",
    'tableofcontents': r"""^\\tableofcontents""",
    'front_or_back_matter_part': r"""\\part\*""",
    'part': r"""\\part{""",
}

begin_chapter_or_section_regex = re.compile(r"""\\chapter\*|\\section\*""")


class LatexRgx(object):
    def __init__(self, regexes):
        self.regexes = regexes
        self.compiled = {}
        self.compile_regexes()

    def compile_regexes(self):
        for k, v in self.regexes.items():
            self.compiled[k] = re.compile(v)

    def match(self, txt):
        for rgxname, rgxobj in self.compiled.items():
            matchobj = rgxobj.search(txt)
            if matchobj:
                return (rgxname, matchobj)
        return (None, None)


class LatexState(object):
    def __init__(self):
        self.in_threeparttable = False
        self.in_begin_document = False
        self.in_begin_notice = False
        self.in_chapter_intro_quote = False
        self.in_frontmatter = False
        self.in_mainmatter = False
        self.in_backmatter = False


class LatexBook(object):
    def __init__(self, args, options):
        self._check_args(args, options)
        self.build_dir = args[0]
        self.tex_files = self._get_tex_files()
        self.tex_rgx = LatexRgx(rgxs)
        self.state = LatexState()

    def _check_args(self, args, options):
        if len(args) != 1:
            raise CommandLineException("Wrong number of arguments: expected 1, got %s" % (len(args), ))

    def _get_tex_files(self):
        return glob('%s/*.tex' % (self.build_dir, ))

    def _make_backup(self, src):
        dst = "%s.orig" % (src, )
        if os.path.exists(dst):
            os.unlink(dst)
        filecopy(src, dst)

    def _get_content(self, tex_filename):
        tex_file = open(tex_filename, 'r')
        content = tex_file.readlines()
        tex_file.close()
        return content

    def _get_next_non_blank_line_index(self, where, lines):
        i = where
        while True:
            i += 1
            next_line = lines[i]
            if next_line.strip():
                return i
            elif i > len(lines):
                return None
        return None

    def _get_next_front_or_back_matter_part_end_line_index(self, where, lines):
        i = where
        while True:
            i += 1
            next_line = lines[i]
            if begin_chapter_or_section_regex.search(next_line):
                return i
            elif i > len(lines):
                return None
        return None

    def add_tex_command(self, cmd, s):
        def are_curly_brackets_matching(s):
            return s.count('{') == s.count('}')
        s = s.strip('\r\n')
        if are_curly_brackets_matching(s):
            return r"\%s{%s}" % (cmd, s)
        else:
            raise Exception("Non matching curly brackets in string: %s" % s)

    def transform(self):
        for tex_filename in self.tex_files:
            self._make_backup(tex_filename)

            orig_lines = self._get_content(tex_filename)
            try:
                tex_file = open(tex_filename, 'w')
                new_lines = []

                i_next_non_blank = None
                i_chapter = None
                i_front_or_back_matter_part_end = None
                for i, old_line in enumerate(orig_lines):
                    rgxname, matchobj = self.tex_rgx.match(old_line)

                    if rgxname:
                        if rgxname == 'documentclass':
                            # set 'book' document class:
                            new_line = """\\documentclass[%s]{book}\n""" % (matchobj.group('opt'), )
                        elif rgxname == 'begin_document':
                            self.state.in_begin_document = True
                            new_line = '\n'.join([old_line,
                                                  "",
                                                  r"\frontmatter",
                                                  r"\pagestyle{foreword}",
                                                  r"\pagenumbering{roman}",
                                                  "",
                                                 ])
                            self.state.in_frontmatter = True
                        elif rgxname == 'end_document':
                            self.state.in_begin_document = False
                            new_line = old_line
                        elif rgxname == 'fancychapter':
                            new_line = '\n'.join([
                                                  r"\usepackage[Tiny]{fncychap}",
                                                  "",
                                                 ])
                        elif rgxname == 'maketitle':
                            new_line = '\n'.join([old_line,
                                                  r"\thispagestyle{empty}",
                                                  r"\newpage",
                                                  "",
                                                 ])
                        elif rgxname == 'tableofcontents':
                            new_line = '\n'.join([r"\setcounter{page}{%s}" % (CONTENT_STARTS_AT_PAGE, ),
                                                  old_line,
                                                  r"\newpage",
                                                  "",
                                                 ])
                        elif rgxname == 'end_foreword':
                            new_line = '\n'.join(["",
                                                  r"\mainmatter",
                                                  r"\pagestyle{main}",
                                                  r"\pagenumbering{arabic}",
                                                  r"\setcounter{page}{1}",
                                                  "",
                                                 ])
                            self.state.in_frontmatter = False
                            self.state.in_mainmatter = True
                        elif rgxname == 'begin_conclusion':
                            part = matchobj.group('after')
                            new_line = '\n'.join(["",
                                                  r"\backmatter",
                                                  r"\pagestyle{conclusion}",
                                                  part
                                                 ])
                            self.state.in_frontmatter = False
                            self.state.in_mainmatter = False
                            self.state.in_backmatter = True
                        elif rgxname == 'printindex':
                            new_line = '\n'.join(["",
                                                  r"\chapter*{\indexname}",
                                                  "",
                                                  r"\begin{multicols}{2}",
                                                  r"\printindex",
                                                  r"\end{multicols}",
                                                  "",
                                                 ])
                        elif rgxname == 'begin_figure':
                            if self.state.in_begin_notice:
                                new_line = '\n'.join([r"\begin{staticfigure}",
                                                      ""
                                                     ])
                            else:
                                new_line = '\n'.join([old_line.strip(CRLF),
                                                      r"\begin{minipage}[htbp]{\linewidth}",
                                                      "",
                                                     ])
                        elif rgxname == 'end_figure':
                            if self.state.in_begin_notice:
                                # in a notice env, figure -> staticfigure
                                new_line = '\n'.join([matchobj.group('before'),
                                                      r"\end{staticfigure}",
                                                      matchobj.group('after'),
                                                      ""
                                                     ])
                            else:
                                new_line = '\n'.join([matchobj.group('before'),
                                                      r"\end{minipage}",
                                                      matchobj.group('envname'),
                                                      matchobj.group('after'),
                                                      ""
                                                     ])
                        elif rgxname == 'begin_tabular':
                            if self.state.in_begin_document:
                                coldef = matchobj.group('coldef').replace('|', '')
                                table_line = "%s%s%s\n" % (matchobj.group('envname'),
                                                           matchobj.group('opt'),
                                                           coldef,
                                                          )
                                if self.state.in_threeparttable:
                                    new_line = table_line
                                else:
                                    new_line = '\n'.join([r"\begin{center}",
                                                          table_line,
                                                          "",
                                                         ])
                        elif rgxname == 'end_tabular':
                            if self.state.in_begin_document and not self.state.in_threeparttable:
                                new_line = '\n'.join([old_line.strip(CRLF),
                                                      r"\end{center}",
                                                      "",
                                                     ])
                            else:
                                new_line = old_line
                        elif rgxname == 'begin_threeparttable':
                            self.state.in_threeparttable = True
                            new_line = '\n'.join([r"\begin{center}",
                                                  old_line,
                                                  "",
                                                 ])
                        elif rgxname == 'end_threeparttable':
                            self.state.in_threeparttable = False
                            old_line = old_line.strip(CRLF)
                            new_line = '\n'.join([old_line,
                                                  r"\end{center}",
                                                  "",
                                                 ])
                        elif rgxname == 'begin_notice':
                            self.state.in_begin_notice = True
                            i_next_non_blank = self._get_next_non_blank_line_index(i, orig_lines)
                            new_line = old_line
                        elif rgxname == 'end_notice':
                            self.state.in_begin_notice = False
                            new_line = old_line
                        elif rgxname == 'begin_chapter':
                            # The first quote after a chapter is the chapter intro.
                            # So it should begin and end with more space.
                            i_chapter = i
                            new_line = old_line
                        elif rgxname == 'begin_quote':
                            if i_chapter and (1 <= (i - i_chapter) < 3):
                               self.state.in_chapter_intro_quote = True
                               new_line = '\n'.join(["",
                                                     old_line.strip(CRLF),
                                                     r"\vspace{6mm}",
                                                     "",
                                                    ])
                            else:
                                new_line = old_line
                        elif rgxname == 'end_quote':
                            if self.state.in_chapter_intro_quote:
                                new_line = '\n'.join([old_line.strip(CRLF),
                                                      r"\vspace{5mm}",
                                                      "",
                                                     ])
                            else:
                                new_line = old_line
                            self.state.in_chapter_intro_quote = False # job done -> reset in_chapter_intro_quote
                        elif rgxname == 'front_or_back_matter_part':
                            if self.state.in_frontmatter or self.state.in_backmatter:
                                new_line = '\n'.join([old_line.strip(CRLF),
                                                      r"\vspace{8mm}",
                                                      "",
                                                     ])
                                i_front_or_back_matter_part_end = self._get_next_front_or_back_matter_part_end_line_index(i, orig_lines)
                            else:
                                new_line = old_line
                        elif rgxname == 'part':
                            new_line = '\n'.join([r'\afterpage', r'\clearpage', old_line.strip(CRLF)])
                        else:
                            raise UnhandledMatchException("Matching object '%s' was not handled (matching line: %s)." % (rgxname, i))

                    elif i == i_next_non_blank:
                        new_line = '\n'.join([self.add_tex_command('strong', old_line),
                                              "",
                                             ])
                        i_next_non_blank = None # job done -> reset i_next_non_blank
                    elif i == i_front_or_back_matter_part_end:
                        new_line = '\n'.join([r"\vspace{5mm}",
                                              old_line.strip(CRLF),
                                              "",
                                             ])
                        i_next_non_blank = None # job done -> reset i_next_non_blank
                        i_front_or_back_matter_part_end = None # job done -> reset i_front_or_back_matter_part_end
                    else:
                        new_line = old_line
                    new_lines.append(new_line)

                new_lines.append("\n".join(["%% ", "%% vi: fdm=manual", "%% "]))
                tex_file.writelines(new_lines)
            finally:
                tex_file.close()


class CommandLineException(Exception):
    pass


class UnhandledMatchException(Exception):
    pass


def _main():
    parser = optparse.OptionParser(usage=USAGE, version=__version__)
    (opt, args) = parser.parse_args()

    try:
        book = LatexBook(args, opt)
    except (CommandLineException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())

    book.transform()

if __name__ == '__main__':
    _main()

