from google.appengine.ext import ndb

class Room(ndb.Model):
    Id = ndb.IntegerProperty()
    Topic = ndb.StringProperty()

class Message(ndb.Model):
    Timestamp = ndb.DateTimeProperty(auto_now_add=True)
    User = ndb.StringProperty()
    Content = ndb.StringProperty(indexed=False)
    Room = ndb.StructuredProperty(Room)

    @classmethod
    def Put(cls, user,content,roomId):
        room = Room.query(Room.Id == roomId).get()
        if room:
            user = Identity.query(Identity.UUID == user).get()
            if user:
                message = Message(User =user.DisplayName, Content = content, Room = room)
                message.put()

class Identity(ndb.Model):
    UUID = ndb.StringProperty()
    DisplayName = ndb.StringProperty()
    IpAddress = ndb.StringProperty(indexed=False)

