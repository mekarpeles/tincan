#!/usr/bin/env/python

import web
import urllib2
import json
from config import private_conf

class Api:
    def GET(self):
        """
        Root resource served when a GET request is made to /v1/api/
        """
        #render = web.ctx.shared['render']
        #slender = web.ctx.shared['slender']
        return "<p>This is be the root of our API</p>"


class Tropo:
    def GET(self):
        """ tropo webapi """
        url = private_conf['webapi']['tropo']['url'] 
        data = {'tropo': {'call': {'to' : ''}}}
        return "these are not the apis we're looking for... Carry on, carry on"
        #return webapi_hook(url, data)

def webapi_hook(url, data=None):
    """
    Call any REST Api over the web and return the JSON representation
    """
    data = urllib2.urlopen(url).read()
    json.dumps(data)
    return ""
