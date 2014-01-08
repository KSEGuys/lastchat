#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import web
from google.appengine.api import channel
from datetime import datetime

from models import Room,Message,Identity

urls = (
        "/",'index',
        "/rooms","rooms",
        '/identity','identity',
        '/room/(.+)','room',
        '/message','message',
        '/messagestyle','messageStyle'
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
        room = Room.Query(id)
        messages = Message.GetByRoom(id)
        room.messages = messages
        return plainRender.room(room)

class rooms:
    def GET(self):
        rooms = Room.All()
        return render.rooms(rooms)

class message:
    def POST(self):
        data = web.input()
        Message.Put(data.Identity,data.Content,data.RoomId)
        return 'success'

class messageStyle:
    def GET(self):
        return plainRender.message(Message())

class identity:
    def POST(self):
        name = web.input().name
        ip = web.ctx.ip
        cookieName_identity = 'identity'
        cookieName_name = 'name'
        identity  = web.cookies().get(cookieName_identity)

        user = None

        if identity:
            user = Identity.Update(identity,name,ip)
        if not user:
            user = Identity.Put(name,ip)

        web.setcookie(cookieName_identity,user.UUID)
        web.setcookie(cookieName_name,user.DisplayName)

        return user.UUID


def notfound():
    return web.notfound(render.index())

app = web.application(urls, globals())
app.notfound = notfound

app = app.gaerun()

#if __name__ == '__main__':
#    app.run()
