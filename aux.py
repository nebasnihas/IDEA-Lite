#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import sys
from functools import partial
from hashlib import sha1

print2 = partial(print, file=sys.stderr)

def str2bool(s):
    return s.lower() in ["1", "true", "yes"]

def bool2str(s):
    return "true" if s else "false"

def sha1str(s):
    return sha1(s.encode("utf-8")).hexdigest()
