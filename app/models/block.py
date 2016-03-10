import datetime
from flask.ext.mongoengine.wtf import model_form
from .base import *

class Block(db.Document):

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    mark = db.StringField(max_length=10, required=True, unique=True)
    name = db.StringField(max_length=20, required=True)


    #meta = {'collection': 'block'}


    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(Block, self).save(*args, **kwargs)


    def update(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(Block, self).update(*args, **kwargs)

    def __unicode__(self):
        return self.name

