import datetime
#from flask.ext.mongoengine.wtf import model_form
from .base import *

class User(db.Document):

    _id = db.IntField(primary_key=True, required=True, unique=True)
    account = db.StringField(max_value=20, required=True, unique=True)
    email = db.StringField(max_value=50)
    password = db.StringField(max_value=20)
    type = db.IntField(default=1)
    role_id = db.IntField(default=1)

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    #meta = {'collection': 'user'}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # ID 自增
        sequence = Sequence._get_collection()
        sequence = sequence.find_one_and_update({'name':'user_id'}, {'$inc':{'val':1}}, upsert=True)
        self._id = sequence['val']
        return super(User, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(User, self).update(*args, **kwargs)

    def __unicode__(self):
        return self.name

