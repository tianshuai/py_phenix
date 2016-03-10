# coding: utf-8

from flask import Blueprint
admin = Blueprint('admin', __name__, static_url_path='/static',
            static_folder='../../static', template_folder='../templates/admin')

class BaseAdmin():
    def __init__(self):
        a=1
        #self._obj = kwargs.get('obj', None)
        #super(BaseForm, self).__init__(*args, **kwargs)
