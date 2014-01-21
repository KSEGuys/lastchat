from uuid import uuid4
from google.appengine.ext import ndb
from model import Model

class Identity(Model):
    DisplayName = ndb.StringProperty()
    IpAddress = ndb.StringProperty(indexed=False)
    BrowserId = ndb.StringProperty()

    @classmethod
    def Put(cls, name, ip, browserId):
        user = Identity(Id = uuid4().hex, DisplayName = name, IpAddress = ip, BrowserId = browserId)
        user.put()
        return user

    @classmethod
    def Update(cls, id, name, ip, browserId):
        user = Identity.Get(id)
        if not user:
            return None
        if name and len(name) > 0:
            user.DisplayName = name
        if ip and len(ip)>0:
            user.IpAddress = ip
        if browserId and len(browserId) >0:
            user.BrowserId = browserId
        user.put()
        return user
