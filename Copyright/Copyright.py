#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
vers = platform.python_version_tuple()
if   2 >= int(vers[0]): from py2.Copyright import *
elif 3 <= int(vers[0]): from py3.Copyright import *
else: raise Exception('There is no source code corresponding to the specified Python version.')
