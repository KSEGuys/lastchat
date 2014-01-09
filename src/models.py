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

class Identity(ndb.Model):
    UUID = ndb.StringProperty()
    DisplayName = ndb.StringProperty()
    IpAddress = ndb.StringProperty(indexed=False)

    @classmethod
    def Put(cls, displayName, ipAddress):
        user = Identity(UUID = str(uuid.uuid4()), DisplayName = displayName, IpAddress = ipAddress)
        user.put()
        return user

    @classmethod
    def Query(cls, id):
        return Identity.query(Identity.UUID == id).get()

    @classmethod
    def Update(cls, id, name, ip):
        user = Identity.Query(id)
        if not user:
            return None
        if name and len(name) > 0:
            user.DisplayName = name
        if ip and len(ip)>0:
            user.IpAddress = ip
        user.put()
        return user


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
        return Message.query(Message.Room.UUID == roomId).fetch()

    def ToJSON(self):
        return '{"id":"%s","user":{"id":"%s","name":"%s"},"time":"%s","content":"%s"}'\
                %(self.UUID,self.User.UUID,self.User.DisplayName,str(self.Timestamp),self.Content)
