from google.appengine.ext import ndb

class Room(ndb.Model):
    Id = ndb.IntegerProperty()
    Topic = ndb.StringProperty()

class Message(ndb.Model):
    Timestamp = ndb.DateTimeProperty(auto_now_add=True)
    User = ndb.StringProperty()
    Content = ndb.StringProperty(indexed=False)
    Room = ndb.StructuredProperty(Room)



