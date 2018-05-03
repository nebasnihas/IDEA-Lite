#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import os, time, signal

def reload():
    time.sleep(5)  # Wait to make sure that response is returned to client before server restart
    with open('master.pid', 'r') as f:
        try:
            os.kill(int(f.read()), signal.SIGHUP)
        except OSError:
            print('Signal-HUP Error')
