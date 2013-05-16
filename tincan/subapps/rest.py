#!/usr/bin/env/python

import json
from waltz import web, slender
from api.v1 import phone

urls = ("/tincan/sms/?", "TincanSMS",
        "/tincan/voice/?", "TincanVoice",
        "/directions/(.*)/(.*)/?", "Directions",
        "/?", "Api",
        "/.*", "Error")

class TincanVoice:
    def GET(self):
        return phone.call()

class Directions:
    def GET(self, src=None, dest=None):
        web.header('Content-Type', 'application/json')
        if not(src and dest):
            return json.dumps({"status": "error",
                               "msg": "required args: src & dest",
                               "code": "400 Bad Request",
                               "exception": "ValueError"
                               })
        try:
            data = phone.directions(src, dest)
        except :
            return json.dumps({"status": "error",
                               "msg": "JSON encoding error",
                               "code": "424 Method Failure",
                               "exception": "TypeError"
                               })
        return json.dumps({"status": "success",
                           "data": data
                           })

class TincanSMS:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        return phone.sms("Please enter your current location.")

class Responder:
    def GET(self):
        return phone.sms("Please enter your current location.")

class Api:
    def GET(self):
        """Root resource served when a GET request is made to
        /v1/api/
        """
        return "Tincan API, v1.0"

class Error:
    def GET(self, **kwargs)
        raise web.notfound("404")

subapp = web.application(urls, globals())
