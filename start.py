#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

import os

from flask import Flask, jsonify, request
from flask_api import status
from flask_cors import CORS
from flask_compress import Compress
from flask_cache import Cache

from aux import sha1str
from auth import auth
from config import appName, bindPort, tasksDir, redisCachePrefix, redisCacheTimeout, authCodes

app = Flask(appName)
# cache = Cache(app, config={
    # 'CACHE_TYPE': 'redis',
    # 'CACHE_KEY_PREFIX': redisCachePrefix + "view:",
    # 'CACHE_DEFAULT_TIMEOUT': redisCacheTimeout
# })
cache = Cache(app, config={
    'CACHE_TYPE': 'null'
})
CORS(app)
Compress(app)

def makeCacheKey():
    return sha1str(request.url)

sys.path.insert(0, tasksDir)

def getTask(d):
    sys.path.insert(0, os.path.join(tasksDir, d))
    return __import__(d)

tasks = {
    d: getTask(d) for d in os.listdir(tasksDir)
    if os.path.isdir(os.path.join(tasksDir, d))
}

@app.route('/auth/verify')
def auth_verify():
    token = request.args.get('token', "", type=str)
    return jsonify(auth=(token in authCodes))

@app.route('/<task>/<command>')
@auth
@cache.cached(key_prefix=makeCacheKey)
def runTask(task, command):
    if task not in tasks:
        return jsonify(message="Task does not exist."), status.HTTP_404_NOT_FOUND

    try:
        func = getattr(tasks[task], command)
    except:
        return jsonify(message="Command does not exist."), status.HTTP_404_NOT_FOUND

    return jsonify(data=func(**{
        k: (v[0] if len(v) == 1 else v)
        for k, v in request.args.iterlists()
        if k != "token"
    }))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=bindPort, threaded=False, debug=True)
