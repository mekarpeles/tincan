import web
from reloader import PeriodicReloader
import os, sys
import config
import apps

import subapps.v1 as v1

app_path = os.path.dirname(__file__)
sys.path.append(app_path)
if app_path: # Apache
    os.chdir(app_path)
else: # CherryPy
    app_path = os.getcwd()

urls = ("/api/v1", v1.subapp,
        "/key",   "apps.signup.key.ApiKey",
        "/?",     "apps.home.home.Home",
        ".*/?",   "Error")

app = web.application(urls, globals())

def session_hook():
    web.ctx.shared = {"slender": slender,
                      "render": render,
                       }
app.add_processor(web.loadhook(session_hook))

slender = web.template.render('templates', globals())
render = web.template.render('templates', globals(), base='layout')

class Error:
    def GET(self, err=None):
        """
        This class renders an error message
        """
        return "404, it's like 101 with sails."

if __name__ == "__main__":
    if web.config.debug:
        PeriodicReloader()
    app.run()

