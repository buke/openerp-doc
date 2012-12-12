#!/usr/bin/python
#-*- encoding: utf8 -*-

import sys
import os
import re
import optparse
from subprocess import Popen, PIPE

__version__ = '0.1'
USAGE = """%prog [options] <WARNING_LOG_FILE> <SEARCH_FILE> <FAKE_REF_FILE> <SOURCE_DIRECTORY>"""

FAKE_FILENAME = 'fake_ref.rst'

TEXT_TO_ADD = """(which can be found in a companion volume to this book and in the online book)"""

undef_label_regex = re.compile(r"""^WARNING:.*? undefined label: (?P<text>.*?)([ ]|$)""")


class FakeReferenceManager(object):
    def __init__(self, args, options):
        self._check_args(args, options)
        self.warn_lines = self._get_content(args[0])
        self.search_filename = args[1]
        self.fake_ref_filename = args[2]
        self.source_dir = args[3]

    def _check_args(self, args, options):
        if len(args) < 3:
            raise CommandLineException("Wrong number of arguments: expected 3, got %s" % (len(args), ))

    def _get_content(self, fn):
        fd = open(fn, 'r')
        content = fd.readlines()
        fd.close()
        return content

    def get_undefined_labels(self):
        texts = []
        for line in self.warn_lines:
            match_undef = undef_label_regex.search(line)

            if match_undef:
                texts.append(match_undef.group('text'))
            else:
                pass
        return set(texts)

    def build_fake_file(self):
        undefs = self.get_undefined_labels()
        if undefs:
            #find ../../source/book -iname '*.rst' | xargs /bin/grep -A 6 -E '\.\. _ch-projects|\.\. _part-ops|\.\. _ch-configacct|\.\. _part2-crm'
            cmd_find = ['find', self.source_dir, '-iname', '*.rst']
            p_find = Popen(cmd_find, stdout=PIPE)

            # -h: don't print filename
            # -A 6: print 6 lines after match
            # -E: use extended regexp
            cmd_grep = ['xargs', 'grep', '-h', '-A', '6', '-E']
            to_search = []
            for undef in undefs:
                to_search.append("\.\. _%s" % (undef, ))
            cmd_grep.append('|'.join(to_search))

            outfile = open(self.search_filename, 'w')
            p_grep = Popen(cmd_grep, stdin=p_find.stdout, stdout=outfile)
            out, err = p_grep.communicate()
            outfile.close()
            if err:
                sys.exit("Error:%s\n" % (err, ))

            infile = open(self.search_filename, 'r')
            lines = infile.readlines()
            infile.close()

            outlines = []
            for i, line in enumerate(lines):
                try:
                    next_line = lines[i+1]
                except (IndexError, ), e:
                    next_line = None

                if line.startswith('.. _'):
                    outlines.append('%s\n' % line)
                    continue
                elif next_line:
                    if len(line.strip()):
                        if len(line) <= len(next_line):
                            if len(set(next_line.strip())) == 1:
                                new_line = "%s %s" % (line.strip(), TEXT_TO_ADD)
                                outlines.append('%s\n%s\n\n' % (new_line, '#'*len(new_line)))
                                continue
        else:
            outlines = ['']

        fake_ref_file = open(self.fake_ref_filename, 'w')
        fake_ref_file.writelines(outlines)
        fake_ref_file.close()


class CommandLineException(Exception):
    pass


def _main():
    parser = optparse.OptionParser(usage=USAGE, version=__version__)
    (opt, args) = parser.parse_args()

    try:
        fake_ref = FakeReferenceManager(args, opt)
    except (CommandLineException, ), e:
        sys.stderr.write("%s\n" % (e, ))
        sys.exit(parser.print_usage())

    print fake_ref.build_fake_file()


if __name__ == '__main__':
    _main()

