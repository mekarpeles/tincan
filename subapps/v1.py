#!/usr/bin/env/python

import web

from apps.api import v1

urls = ("/?", "apps.api.v1.Api",
        "/.*", "Error",)

#===============================================================#
# Error
#===============================================================#
class Error:
    def GET(self, err1=None, err2=None, err3=None):
        """
        """
        raise web.seeother(web.ctx.homedomain + "/404")

subapp = web.application(urls, globals())
