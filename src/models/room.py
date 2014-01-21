from uuid import uuid4
from google.appengine.ext import ndb
from model import Model

class Room(Model):
    Topic = ndb.StringProperty()

    @classmethod
    def Put(cls,topic):
        room = Room(Topic = topic, Id = uuid4().hex)
        room.put()
        return room
