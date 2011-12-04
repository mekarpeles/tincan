import web

class Home:
    def GET(self):
        render = web.ctx.shared['render']
        slender = web.ctx.shared['slender']
        return render.index()
