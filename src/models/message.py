from uuid import uuid4
from google.appengine.ext import ndb
from model import Model
from room import Room
from identity import Identity

class Message(Model):
    Timestamp = ndb.DateTimeProperty(auto_now_add=True)
    User = ndb.StructuredProperty(Identity)
    Content = ndb.StringProperty(indexed=False)
    Room = ndb.StructuredProperty(Room)

    @classmethod
    def Put(cls, userId,content,roomId):
        room = Room.Get(roomId)
        user = Identity.Get(userId)
        if room and user:
            message = Message(User = user, Content = content, Room = room, Id = uuid4().hex)
            message.put()
            return message
        return None

    @classmethod
    def GetByRoom(cls,roomId):
        return Message.query(Message.Room.Id == roomId).order(Message.Timestamp).fetch()

    def ToJSON(self):
        return '{"id":"%s","user":{"id":"%s","name":"%s"},"time":"%s","content":"%s"}'\
                %(self.Id,self.User.Id,self.User.DisplayName,str(self.Timestamp),self.Content)
