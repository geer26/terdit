from app import socket, db
from flask import request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


'''
EVENT LIST
 - test - 
    testing purposes
    
 - loginattempt -
    Attempts a login with username and password. If success: redirect to /, else send an error text.
'''


def send_message(sid, message, event='test'):
    socket.emit(event, message, room=sid)
    return True


def event_dispatcher(message):
    SID = request.sid
    print(f'DATA: {message}, SID: {SID}')
    print(f'USER IS LOGGED IN: {current_user.is_authenticated}')
    send_message(SID, 'DATA ACCEPTED')
    return True

def login_attempt(message):
    SID = request.sid
    if current_user.is_authenticated:
        return {'status': 1, 'message': 'Already logged in!'}
    username = message['username']
    password = message['password']
    user = User.query.filter_by(username=str(username)).first()
    if not user:
        send_message(SID, {'status': 2, 'message': 'Hibás felhasználónév vagy jelszó'}, event='loginattempt')
        return False
    if not user.check_password(str(password)):
        send_message(SID, {'status': 2, 'message': 'Hibás felhasználónév vagy jelszó'}, event='loginattempt')
        return False
    send_message(SID, {'status': 0}, event='loginattempt')
    return True



socket.on_event('test', event_dispatcher)
socket.on_event('loginattempt', login_attempt)
