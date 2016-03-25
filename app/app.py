#encoding: utf-8
from flask import Flask, g
from .config import PROJDIR
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__,
        static_url_path='/_static',
        static_folder=PROJDIR + '/static',
        template_folder='templates')

app.config.from_pyfile('config.py') #  这里config.py是文件

db = MongoEngine(app)
#app.session_interface = MongoEngineSessionInterface(db)

@app.before_request
def load_current_user():
    from .helpers import get_current_user
    g.user = get_current_user()
    if g.user:
        g.is_admin = True if g.user.role_id in [5, 8] else False
        g.is_system = True if g.user.role_id in [8] else False

def register_blueprints(app):
    # Prevents circular imports
    from .admin import admin
    from .main import main
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(admin, url_prefix='/admin')

register_blueprints(app)

