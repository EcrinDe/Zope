##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""Signature module

This provides support for simulating function signatures
"""

from functools import total_ordering


@total_ordering
class FuncCode(object):

    def __init__(self, varnames, argcount):
        self.co_varnames = varnames
        self.co_argcount = argcount

    def __eq__(self, other):
        if not isinstance(other, FuncCode):
            return False
        return ((self.co_argcount, self.co_varnames) ==
                (other.co_argcount, other.co_varnames))

    def __lt__(self, other):
        if not isinstance(other, FuncCode):
            return False
        return ((self.co_argcount, self.co_varnames) <
                (other.co_argcount, other.co_varnames))


def _setFuncSignature(self, defaults=None, varnames=(), argcount=-1):
    # This is meant to be imported directly into a class.
    # Simplify calls.
    if argcount < 0 and varnames:
        argcount = len(varnames)
    # Generate a change only if we have to.
    if self.func_defaults != defaults:
        self.func_defaults = self.__defaults__ = defaults
    code = FuncCode(varnames, argcount)
    if self.func_code != code:
        self.func_code = self.__code__ = code
