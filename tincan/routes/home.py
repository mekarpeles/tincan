#-*- coding: utf-8 -*-

"""
    home
    ~~~~

    Homepage for the tincan web service
"""

from waltz import render

class Index:
    def GET(self):
        return render().index()
