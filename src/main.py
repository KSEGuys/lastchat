#!/usr/bin/env python
from lib import web
from google.appengine.api import channel
from google.appengine.ext import ndb
from datetime import datetime
from models import Room,Message

urls = (
        "/","index",
        #"/init",'init'
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
        messages = Message.query(Message.Room.Id==1).order(Message.Timestamp).fetch()
        return render.room(messages)

class init:
    def GET(self):
        for i in range(10):
            room = Room(Id=i, Topic='Room '+str(i))
            room.put()

            for j in range(10):
                message = Message(Room=room,User="Wayne Wang",Content=str(j)+" Test Message")
                message.put()

        return 'success'

app = web.application(urls, globals())

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
