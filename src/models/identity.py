import uuid
from google.appengine.ext import ndb

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
