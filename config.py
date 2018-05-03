#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import json
from hashlib import sha256

def sha256str(s):
    return sha256(s.encode("utf-8")).hexdigest()

with open("config.json") as f:
    j = json.load(f)

    appName = j["name"]

    bindPort = j["port"]

    tasksDir = j["tasks"]
    dataDir = j["data"]
    importsDir = j["imports"]

    authCodes = set(sha256str(code) for code in j["auth"])

redisCachePrefix = appName + ":"
redisCacheTimeout = 3600
