import os
PROJDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONFDIR = os.path.join(PROJDIR, 'etc')

# mongodb
#MONGODB_DB = 'tian'
#MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017

CSRF_ENABLED = True
SECRET_KEY = 'taihuoniao_tools'
