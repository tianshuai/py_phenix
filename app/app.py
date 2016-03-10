
from flask import Flask, render_template
from .config import PROJDIR
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

app = Flask(__name__,
        static_url_path='/_static',
        static_folder=PROJDIR + '/static',
        template_folder='templates')

app.config.from_pyfile('config.py') #  这里config.py是文件

app.config["MONGODB_SETTINGS"] = {"DB":"tian", 'alias':'default'}
db = MongoEngine(app)
#app.session_interface = MongoEngineSessionInterface(db)

def register_blueprints(app):
    # Prevents circular imports
    from .admin import admin
    from .main import main
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(admin, url_prefix='/admin')

register_blueprints(app)

