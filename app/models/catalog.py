import datetime
#from flask.ext.mongoengine.wtf import model_form
from .base import *

class Catalog(db.Document):

    _id = db.IntField(primary_key=True, required=True)
    name = db.StringField(max_value=50, required=True)
    user_id = db.IntField(required=True)
    item_id = db.IntField(required=True)
    sort = db.IntField(default=99)

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    #meta = {'collection': 'catalog'}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        # ID 自增
        sequence = Sequence._get_collection()
        sequence = sequence.find_one_and_update({'name':'catalog_id'}, {'$inc':{'val':1}}, upsert=True)
        self._id = sequence['val']

        return super(Catalog, self).save(*args, **kwargs)


    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(Catalog, self).update(*args, **kwargs)

    def __unicode__(self):
        return self.name

