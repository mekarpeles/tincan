# -*- coding: utf-8 -*-
"""
    config.py
    ~~~~~~~~~

    This module is the middle man for handling/consolidating
    configurations for the  project.

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import os
import types
import ConfigParser
from waltz import web

def getdef(self, section, option, default_value):
    try:
        return self.get(section, option)
    except:
        return default_value

path = os.path.dirname(__file__)
config = ConfigParser.ConfigParser()
config.read('%s/tincan.cfg' % path)
config.getdef = types.MethodType(getdef, config)

web.config.debug = config.getdef('twilio', 'debug', True)
TWILIO = {'sid': config.getdef('twilio', 'sid', ''),
          'token': config.getdef('twilio', 'token', ''),
          '#': config.getdef('twilio', 'number', ''),
          'url': config.getdef('twilio', 'url', 'https://api.twilio.com/')
          }
