#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from Copyright import *

__version__      = '0.0.3'
__author__       = 'ytyaru'
__author_email__ = 'pypi1@outlook.jp'
__copyright__    = '© 2020 ytyaru'
__license__      = 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication'
__url__          = 'https://github.com/ytyaru/Copyright.py'
__all__ = ['Copyright']

vers = platform.python_version_tuple()
if   2 >= int(vers[0]): pass
elif 3 <= int(vers[0]): from Copyright.py3.Copyright import *
else: raise Exception('There is no source code corresponding to the specified Python version.')
