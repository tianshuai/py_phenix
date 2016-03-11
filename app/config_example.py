#encoding: utf-8
import os
PROJDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONFDIR = os.path.join(PROJDIR, 'etc')

# mongodb
MONGODB_DB = 'bird_tools'
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017

# babel settings
BABEL_DEFAULT_LOCALE = 'zh'
BABEL_SUPPORTED_LOCALES = ['zh']

DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = 'taihuoniao_tools'
