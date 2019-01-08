#encoding: utf-8
import os
PROJDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONFDIR = os.path.join(PROJDIR, 'etc')

# MongoDB配置
MONGODB_SETTINGS = {
    'db': 'bird_tools',
    'host': '127.0.0.1',
    'port': 27017,
    'username': 'root',
    'password': '',
    # 由于PyMongo不是进程安全的, 禁止MongoClient实例在进程之间的传递
    'connect': False,
    'authentication_source': 'admin'
}

# babel settings
BABEL_DEFAULT_LOCALE = 'zh'
BABEL_SUPPORTED_LOCALES = ['zh']

DEBUG = True

CSRF_ENABLED = True
SECRET_KEY = 'taihuoniao_tools'

PASSWORD_SECRET = 'thn'
