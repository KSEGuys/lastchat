#!/usr/bin/env python
from lib import web
from google.appengine.api import channel

urls = (
        "/","index",

        )

app = web.application(urls, globals())

render = web.template.render('templates/',base='layout')

class index:
    def GET(self):
        # token = channel.create_channel('lastr2d2')
        # return render.homepage(token)
        return render.room()

app = app.gaerun()
