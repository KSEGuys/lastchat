#!/usr/bin/env python
from lib import web
from google.appengine.api import channel
from models import message
from datetime import datetime

urls = (
        "/","index",
        )

utils = {
        #"render" : web.template.render('templates/'),
        "strftime": datetime.strftime,
        "str": str
        }

utils["render"] = web.template.render('templates/',globals=utils)

render = web.template.render('templates/',base='layout',globals=utils)

class index:
    def GET(self):
        messages = message.sample()
        return render.room(messages)

app = web.application(urls, globals())

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
