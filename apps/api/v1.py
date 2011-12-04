#!/usr/bin/env/python

import web
import urllib, urllib2
import httplib
import json
from config import private_conf

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
        """ tropo """        
        params = {"tropo":[
                {"call":{
                        "to":[
                            "+6033056953"
                            ]}
                 },
                {"say":[
                        {"value":"Hello, you were the first to answer."}
                        ]}
                ]}
                                        
        url = "http://api.tropo.com/"
        path = "1.0/sessions"
        url = private_conf['webapi']['tropo']['url'] 

        params = urllib.urlencode(i)
        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        conn = httplib.HTTPConnection(url)
        response = conn.request("POST", path, params, headers)
        data = response.read()
        print(data)
        conn.close()
        return data

        return "these are not the apis we're looking for... Carry on, carry on"
        #return webapi_hook(url, data)

class REST:
    def GET(url):
        """
        Call any REST Api over the web and return the JSON representation
        """
        data = urllib2.urlopen(url).read()
        json.dumps(data)
        return ""

    def POST(url, path):
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

        

