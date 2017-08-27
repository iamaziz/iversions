#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aziz Alto <iamaziz.alto@gmail.com>
# Aug. 26, 2017


"""
iversions is a simple cell magic command for IPython/Jupyter,
to display name and version of all imported modules (non built-in) in the current environment.


Usage:

  after loading it `%load_ext iversions` and importing some modules, just type:

  %iversions


Note:

  Currently, it does not work with non-module imports `from X import Y` :(
"""

from sys import version_info as ver_info
import types
from datetime import datetime


PYTHON_VER = '.'.join(map(str, [ver_info.major, ver_info.minor, ver_info.micro]))


def now():
    return datetime.strftime(datetime.now(), '%a %b %d, %Y %H:%M:%S %Z')


def imports(vars):
    """
    a generator over the imported modules in vars
    :param vars: globals() or locals()
        see https://stackoverflow.com/a/4858123/2839786
    """
    for val in list(vars.values()):
        if isinstance(val, types.ModuleType):
            yield val


def imports_versions(modules):
    """
    :param modules: a list of modules (types.ModuleType)
    :return: dict, {module_name: version_number}
    """
    vers = {}
    for module_ in modules:
        try:
            vers[module_.__name__] = module_.__version__
        except AttributeError:
            # built-ins will be excepted
            continue
    return vers.items()


def print_versions(symbol_table=locals()):
    imported = imports(symbol_table)

    for k, v in imports_versions(imported):
        print('{:<10}  {}'.format(k, v))

    print('\nPython {} [{}]'.format(PYTHON_VER, now().strip()))


# notebook cellmagic interface
from IPython.core.magic import Magics
from IPython.core.magic import magics_class
from IPython.core.magic import line_magic, register_line_magic, cell_magic


@magics_class
class IVersions(Magics):

    @line_magic
    def iversions(self, line):
        """
        Display name and version of the imported modules in current environment.

        Usage:
          import some modules, just type

          %iversions

        enjoy :-)
        """
        print_versions(self.shell.user_ns)
