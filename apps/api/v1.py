#!/usr/bin/env/python

import web
import urllib, urllib2
import httplib
import json
from config import private_conf as pc
import tropo
from twilio import twiml
from twilio.rest import TwilioRestClient


class Api:
    def GET(self):
        """
        Root resource served when a GET request is made to /v1/api/
        """
        #render = web.ctx.shared['render']
        #slender = web.ctx.shared['slender']
        i = web.input()
        #service = getattr(i, 'service', None)
        #url =  getattr(i, 'url', None)
        #if service and url:
        #    return REST(url).GET()
        return "<p>This is be the root of our API</p>"

class Sandbox:
    def GET(self):
        pass

class Directions:
    def GET(self, src=None, dest=None, loadsJson=False):
        """  """
        slender = web.ctx.shared['slender']
        if src and dest:
            #web.header('Content-Type', 'application/json')
            src = src.replace(" ", "+")
            dest = dest.replace(" ", "+")
            url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=walking&sensor=false" % (src, dest)
            data = urllib2.urlopen(url).read()            
            jdata = json.loads(data)
            return slender.directions(jdata['routes'][0]['legs'][0])                
        return "i gets get and post, fo real!"

class TincanSMS:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        resp = twiml.Response()
        resp.sms("Please enter your current location:")
        return str(resp)

class TincanVoice:
    def GET(self):
        account = pc.webapis['twilio']['account_sid']
        token = pc.webapis['twilio']['auth_token']
        client = TwilioRestClient(account, token)

        call = client.calls.create(to="16033056953",
                                   from_="14155992671",
                                   url="http://demo.twilio.com/welcome/voice")
        return call.sid

class Responder:
    def GET(self):
        resp = twiml.Response()
        resp.sms("Please enter your current location:")

class REST:
    def GET(self, url):
        """
        Call any REST Api over the web and return the JSON representation
        """
        data = urllib2.urlopen(url).read()
        json.dumps(data)
        return ""

    def POST(self, url, path):
        i = web.input()
        dest = getattr(i, 'dest', None)
        if dest:
            del i['dest']

        params = urllib.urlencode(i)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn = httplib.HTTPConnection(url)
        response = conn.request("POST", path, params, headers)
        data = response.read()
        print(data)
        conn.close()
        return data

        

