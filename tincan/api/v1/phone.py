#!/usr/bin/env/python
#-*- coding: utf-8 -*-

"""
    phone
    ~~~~~

    Phone API to support the tincan project
"""

import httplib
import json
from urllib import urlencode
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient

GMAPS_URL = "https://maps.googleapis.com/maps/api/directions/json?"
TWILIO_URL = "http://api.twilio.com/2010-04-01"

def directions(src, dest, mode="walking", sensor=False):
    src = src.replace(" ", "+")
    dest = dest.replace(" ", "+")            
    params = {"origin": src,
              "destination": dest,
              "mode": mode,
              "sensor": sensor
              }
    url = GMAPS_URL + urlencode(params)
    r = requests.get(url)
    return json.loads(r.json())['routes'][0]['legs'][0]

def sms(msg):
    resp = twiml.Response()
    resp.sms(msg)
    return str(resp)

def call(sid, token, from_, to, url=TWILIO_URL):
    client = TwilioRestClient(sid, token)    
    call = client.calls.create(to=to, from_=from_,
                               url="%s/Accounts/%s/Calls.json" % (url, sid))
    return call.sid

