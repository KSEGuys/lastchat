#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
from lib import web
from google.appengine.api import channel
from google.appengine.api import memcache

from models import *
from config import urls,render,plainRender,_cookie_expire_time

class index:
    def GET(self):
        return render.index()

class room:
    def GET(self,id):
        room = Room.Get(id)
        messages = Message.GetByRoom(id)
        room.messages = messages
        channelId = uuid.uuid4().hex
        room.token = channel.create_channel(channelId)

        channels = memcache.get(room.Id) or []
        if channelId not in channels:
            channels.append(channelId)

        memcache.set(room.Id,channels,3600)

        return plainRender.room(room)

class rooms:
    def GET(self):
        rooms = Room.All()
        return render.rooms(rooms)

class message:
    def POST(self):
        data = web.input()
        message = Message.Put(data.Identity,data.Content,data.RoomId)
        if message:
            channels = memcache.get(data.RoomId) or []
            for channelId in channels:
                channel.send_message(channelId,message.ToJSON())

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
        browserId = ''
        user = None

        if identity:
            user = Identity.Update(identity,name,ip,browserId)
        if not user:
            user = Identity.Put(name,ip,browserId)

        web.setcookie(cookieName_identity,user.Id,_cookie_expire_time)
        web.setcookie(cookieName_name,user.DisplayName,_cookie_expire_time)

        return user.Id


def notfound():
    return web.notfound(render.index())

app = web.application(urls, globals())
app.notfound = notfound
app = app.gaerun()

#if __name__ == '__main__':
#    app.gaerun()
