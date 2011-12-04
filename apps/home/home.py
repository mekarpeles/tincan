import web

class Home:
    def GET(self):
        render = web.ctx.shared['render']
        slender = web.ctx.shared['slender']
        return slender.index()
        #return "<h1>Random Hacks of Kindness SF 2011</h1>"
