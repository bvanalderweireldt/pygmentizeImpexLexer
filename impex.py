# -*- coding: utf-8 -*-
"""
    pygments.lexers.impex
    ~~~~~~~~~~~~~~~~~~~

    Lexers for Impex dialect (SAP Hybris).
    
    More informations about impex : https://blogs.sap.com/2016/12/14/what-is-impex-syntax-of-impex-different-modes-of-impex-and-import-via-impex-web/

    :copyright: Copyright 2017 by Hybhub.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, do_insertions, bygroups, words
from pygments.token import Punctuation, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.lexers import get_lexer_by_name, ClassNotFound
from pygments.util import iteritems


__all__ = ['ImpexLexer']

class ImpexLexer(RegexLexer):
    """
    Lexer for Impex.
    """

    name = 'Impex'
    aliases = ['impex']
    filenames = ['*.impex']
    mimetypes = ['text/x-impex']

    flags = re.IGNORECASE
    tokens = {
        'root': [
            (r'#.*\n', Comment.Singleline),
            (r'(\$[^=]+)(=)([^\n]+\n)', bygroups(Name.Constant, Operator, String.Single)),
            (r'(insert_update|insert|update|remove)( .*\n)', bygroups(Keyword, Name.Function)),
            (r"'(''|[^'])*'", String.Single),
            (r'"(""|[^"])*"', String.Single),
            (r';', Operator),
            (r'[^;\n"\']+?', String.Single)
            ]
        }
