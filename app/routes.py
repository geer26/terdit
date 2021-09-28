from app import app, db
from flask import request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated and current_user.userlevel == 0:
        print('SUPERUSER!')
        return render_template('adminindex.html')
    return render_template('index.html')


@app.route('/addsu/<suname>/<password>')
def addsu(suname, password):
    hassu = False
    sus = User.query.filter_by(userlevel=0).all()
    if len(sus) > 0:
        hassu = True
    if not hassu:
        user = User()
        user.username = suname
        user.userlevel = 0
        user.is_enabled = True
        user.set_password(str(password))
        db.session.add(user)
        db.session.commit()
    return redirect('/')


@app.route('/logout', methods=['GET'])
def logout():
    if not current_user.is_authenticated:
        return {'message': 'Logout refused'}, 401
    user = current_user
    user.last_modified_at = datetime.now()
    db.session.commit()
    logout_user()
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():

    if request.method != 'POST' or current_user.is_authenticated:
        return {'message': 'Login refused'}, 401

    username = request.form['login-username']
    password = request.form['login-password']

    try:
        remember = request.form['remember_me']
    except:
        remember = None

    user = User.query.filter_by(username=str(username)).first()

    if user.check_password(str(password)):
        if not remember:
            login_user(user)
        else:
            login_user(user, remember=remember)

        user.last_modified_at = datetime.now()
        db.session.commit()
        return redirect('/')
    
    else:
        return {'message': 'Login refused'}, 401
