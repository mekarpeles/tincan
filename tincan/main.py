import waltz
import config
import apps

import subapps.v1 as api

urls = ("/api/v1", api.subapp,
        "/?",     "routes.home.Index",
        ".*",   "Error")

sessions = {}

app = waltz.setup.dancefloor(urls, globals(), sessions=sessions)

class Error:
    def GET(self, err=None):
        """This class renders an error message"""
        return "404, it's like 101 with sails."

if __name__ == "__main__":
    app.run()

