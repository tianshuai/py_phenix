from flask import render_template, jsonify, url_for, request, redirect, flash
from ..forms import SigninForm, SignupForm
from .base import main 

@main.route('/login', methods=['POST', 'GET'])
def login():

    form = SigninForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            return jsonify(success=False, message='OK')
        else:
            return jsonify(success=False, message=str(form.errors))

        next_url = request.args.get('next', '/')
        #account = request.form['account']
        #password = request.form['password']

        return jsonify(success=False, message='创建失败!')

    return render_template('auth/login.html', form=form)


@main.route('/register', methods=['POST', 'GET'])
def register():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return jsonify(success=False, message='OK')
        else:
            return jsonify(success=False, message=str(form.errors))
    else:
        pass

    return render_template('auth/register.html', form=form)

