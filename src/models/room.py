import uuid
from google.appengine.ext import ndb

class Room(ndb.Model):
    Topic = ndb.StringProperty()
    UUID = ndb.StringProperty()

    @classmethod
    def Put(cls,topic):
        room = Room(Topic = topic, UUID = str(uuid.uuid4()))
        room.put()
        return room

    @classmethod
    def Query(cls, id):
        return Room.query(Room.UUID == id).get()

    @classmethod
    def All(cls):
        return Room.query().fetch()
