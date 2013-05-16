#-*- coding: utf-8 -*-

"""
    util
    ~~~~

    Various general utilities to support the tincan project
"""

import random
import hashlib
import base64

def gentoken():
    base = str(random.getrandbits(256))
    digest = hashlib.sha256(base).digest()
    rchoice = random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])
    return base64.b64encode(digest, rchoice).rstrip('==')
