from google.appengine.ext import ndb

class Model(ndb.Model):
    Id = ndb.StringProperty()

    @classmethod
    def Get(cls,_id):
        return cls.query(cls.Id == _id).get()

    @classmethod
    def Delete(cls,_id):
        instance = cls.Get(_id)
        instance.delete()

    @classmethod
    def All(cls):
        return cls.query().fetch()
