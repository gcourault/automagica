# -*- coding: utf-8 -*-


import os
import subprocess
import sys


def show_file(filepath):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))
    elif os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filepath))


def filepath(path, base_name, ext):
    return os.path.join(path, '{}.{}'.format(base_name, ext))


def latex_chapter_title(title, index_title=None):
    if not index_title:
        index_title = title
    return "\chapter*{{{title}}} \\addcontentsline{{toc}}{{chapter}}{{{index_title}}}".format(
        title=title, index_title=index_title)


def latex_chapter(path, split_paragraphs=False):
    with open(path, 'r') as f:
        lines = f.readlines()
        lines[0] = latex_chapter_title(lines[0])
        sep = "\n" if split_paragraphs else " "
        return sep.join(lines)


def latex_hyphenation(word):
    return "\hyphenation{{{word}}}".format(word=word)
