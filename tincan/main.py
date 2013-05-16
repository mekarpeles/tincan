import waltz
import config
import apps

import subapps.v1 as v1

urls = ("/api/v1", v1.subapp,
        "/key",   "routes.signup.ApiKey",
        "/?",     "routes.home.Home",
        ".*",   "Error")

sessions = {}

app = waltz.setup.dancefloor(urls, globals(), sessions=sessions)

class Error:
    def GET(self, err=None):
        """This class renders an error message"""
        return "404, it's like 101 with sails."

if __name__ == "__main__":
    app.run()

