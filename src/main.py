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
        "/init",'init',
        '/identity','identity',
        '/room/(.+)','room'
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
        room = Room.query(Room.Id == int(id)).fetch(1)[0]
        messages = Message.query(Message.Room.Id==int(id)).order(Message.Timestamp).fetch()
        room.messages = messages
        return plainRender.room(room)

class rooms:
    def GET(self):
        rooms = Room.query().fetch()
        return render.rooms(rooms)

class identity:
    def POST(self):
        name = web.input().name
        ip = web.ctx.ip
        cookieName = 'identity'
        existedIdentity = web.cookies().get(cookieName)
        newIdentity = existedIdentity

        if existedIdentity:
            entity = Identity.query(Identity.UUID==existedIdentity).fetch(1)
            if entity:
                if name:
                    entity[0].DisplayName=name
                entity[0].IpAddress=ip
                entity[0].put()
        else:
            newEntity = Identity(UUID=str(uuid.uuid4()),DisplayName=name,IpAddress=ip)
            newEntity.put()
            newIdentity = newEntity.UUID

        web.setcookie(cookieName,newIdentity)
        return newIdentity

class init:
    '''
        for test purpose
    '''
    def GET(self):
        for room in Room.query().fetch():
            room.key.delete()

        for message in Message.query().fetch():
            message.key.delete()

        room = Room(Id=1,Topic='Default Room')
        room.put()

        contents = ['quick brown fox jumps over the lazy dog',
                u'中文似乎也可以啊',
                '<script>alert("hi")</script>',
                'This is the fourth message',
                'This is the last message',
                u'骗你的,这才是第一条消息']
        for content in contents:
            message = Message(Room=room,User="Wayne Wang",Content=content)
            message.put()

        return 'success'

app = web.application(urls, globals())

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
