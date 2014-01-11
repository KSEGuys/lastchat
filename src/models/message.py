import uuid
from google.appengine.ext import ndb
from room import Room
from identity import Identity

class Message(ndb.Model):
    Timestamp = ndb.DateTimeProperty(auto_now_add=True)
    User = ndb.StructuredProperty(Identity)
    Content = ndb.StringProperty(indexed=False)
    Room = ndb.StructuredProperty(Room)
    UUID = ndb.StringProperty()

    @classmethod
    def Put(cls, user,content,roomId):
        room = Room.Query(roomId)
        user = Identity.Query(user)
        if room and user:
            message = Message(User = user, Content = content, Room = room, UUID = str(uuid.uuid4()))
            message.put()
            return message
        return None

    @classmethod
    def GetByRoom(cls,roomId):
        return Message.query(Message.Room.UUID == roomId).order(Message.Timestamp).fetch()

    def ToJSON(self):
        return '{"id":"%s","user":{"id":"%s","name":"%s"},"time":"%s","content":"%s"}'\
                %(self.UUID,self.User.UUID,self.User.DisplayName,str(self.Timestamp),self.Content)
