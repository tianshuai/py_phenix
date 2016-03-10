from flask import render_template
from .base import admin

@admin.route('/doc')
def doc():
    return render_template('doc/list.html')

