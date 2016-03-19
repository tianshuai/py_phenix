# coding: utf-8

from flask import Blueprint
main = Blueprint('main', __name__, static_url_path='/static',
            static_folder='../../static', template_folder='../templates/main')

class BaseMain():
    def __init__(self):
        pass
        #self._obj = kwargs.get('obj', None)
        #super(BaseForm, self).__init__(*args, **kwargs)
