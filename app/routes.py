from app import app
from flask import request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')