from app import app, db
from flask import request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


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