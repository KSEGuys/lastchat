#!/usr/bin/env python
from lib import web
from google.appengine.api import channel
from models import message

urls = (
        "/","index",

        )

app = web.application(urls, globals())

render = web.template.render('templates/',base='layout')

class index:
    def GET(self):
        messages = message.sample()
        return render.room(web.template.render('templates/'),messages)

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
