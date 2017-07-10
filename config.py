#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import json

with open("config.json") as f:
    j = json.load(f)

    appName = j["name"]

    bindPort = j["port"]

    tasksDir = j["tasks"]

    dataDir = j["data"]

redisCachePrefix = appName + ":"
redisCacheTimeout = 3600
