# coding: utf-8

import datetime
from ..app import db, app

class Sequence(db.Document):

    name = db.StringField(max_length=10, required=True, unique=True)
    val = db.IntField()



