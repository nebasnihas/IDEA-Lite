#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from functools import wraps

from flask import jsonify, request
from flask_api import status

from config import authCodes

def auth(func):
    @wraps(func)
    def call(*args, **kwargs):
        token = request.args.get('token', "", type=str).lower()
        if len(authCodes) > 0 and token not in authCodes:
            return jsonify(auth=False, message="Invalid token."), status.HTTP_401_UNAUTHORIZED

        return func(*args, **kwargs)
    return call
