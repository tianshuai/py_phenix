import datetime
#from flask.ext.mongoengine.wtf import model_form
from .base import *

class Category(db.Document):

    _id = db.IntField(primary_key=True, required=True)
    mark = db.StringField(max_length=10)
    name = db.StringField(max_value=20, required=True, unique=True)
    user_id = db.IntField(required=True)
    domain = db.IntField(default=1)
    pid = db.IntField(default=0)
    cid = db.IntField(default=0)

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    #meta = {'collection': 'category'}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # ID 自增
        sequence = Sequence._get_collection()
        sequence = sequence.find_one_and_update({'name':'category_id'}, {'$inc':{'val':1}}, upsert=True)
        self._id = sequence['val']
        return super(Category, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(Category, self).update(*args, **kwargs)

    def __unicode__(self):
        return self.name

