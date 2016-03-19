from flask import render_template
from .base import main 

@main.route('/user/<int:id>')
def user(id):
    return render_template('user/index.html')

