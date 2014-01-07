#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import web
from google.appengine.api import channel
from google.appengine.ext import ndb
from datetime import datetime
from models import Room,Message,Identity

import uuid

urls = (
        "/",'index',
        "/rooms","rooms",
        '/identity','identity',
        '/room/(.+)','room',
        '/message','message'
        )

templateGlobals = {
        "strftime": datetime.strftime,
        "str": str
        }

templateDir = 'templates'

plainRender = web.template.render(templateDir, globals=templateGlobals)
templateGlobals["plainRender"] = plainRender
render = web.template.render(templateDir,base='layout',globals=templateGlobals)
templateGlobals["render"] = render

class index:
    def GET(self):
        return render.index()

class room:
    def GET(self,id):
        room = Room.query(Room.Id == int(id)).get()
        messages = Message.query(Message.Room.Id==int(id)).order(Message.Timestamp).fetch()
        room.messages = messages
        return plainRender.room(room)

class rooms:
    def GET(self):
        rooms = Room.query().fetch()
        return render.rooms(rooms)

class message:
    def POST(self):
        data = web.input()
        Message.Put(data.Identity,data.Content,int(data.RoomId))
        return 'success'

class identity:
    def POST(self):
        name = web.input().name
        ip = web.ctx.ip
        cookieName_identity = 'identity'
        cookieName_name = 'name'
        existedIdentity = web.cookies().get(cookieName_identity)
        newIdentity = existedIdentity

        if existedIdentity:
            entity = Identity.query(Identity.UUID==existedIdentity).get()
            if entity:
                if name:
                    entity.DisplayName=name
                else:
                    name = entity.DisplayName

                entity.IpAddress=ip
                entity.put()
                web.setcookie
        else:
            newEntity = Identity(UUID=str(uuid.uuid4()),DisplayName=name,IpAddress=ip)
            newEntity.put()
            newIdentity = newEntity.UUID

        web.setcookie(cookieName_identity,newIdentity)
        web.setcookie(cookieName_name,name)

        return newIdentity


def notfound():
    return web.notfound(render.index())

app = web.application(urls, globals())
app.notfound = notfound

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
