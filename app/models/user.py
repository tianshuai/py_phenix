import datetime
from werkzeug import security
from .base import *
from ..helpers import gen_sha1

class User(db.Document):

    _id = db.IntField(primary_key=True, required=True)
    account = db.StringField(max_value=20, required=True, unique=True)
    email = db.StringField(max_value=50)
    password = db.StringField(max_value=20)
    type = db.IntField(default=1)
    role_id = db.IntField(default=1)
    token = db.StringField(max_value=20, required=True, unique=True)

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    #meta = {'collection': 'user'}

    def __init__(self, **kwargs):

        super(User, self).__init__(**kwargs)


    def save(self, *args, **kwargs):
        self.password = self.create_password(self.password, self.account)
        self.account = self.account.lower()
        self.token = self.create_token(16)
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

    @staticmethod
    def create_password(raw, account):
        passwd = '%s:%s:%s' % (raw, app.config['PASSWORD_SECRET'], account)
        return gen_sha1(passwd)

    @staticmethod
    def create_token(length=16):
        return security.gen_salt(length)

    def check_password(self, raw, account):
        passwd = '%s:%s:%s' % (raw, app.config['PASSWORD_SECRET'], account)
        return self.password == gen_sha1(passwd)

    def change_password(self, raw):
        self.password = self.create_password(raw)
        self.token = self.create_token()
        return self

