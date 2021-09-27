from app import socket
from flask import request, redirect, render_template
from flask_login import current_user, login_user, logout_user, login_required


def send_message(sid, message):
    print('SOMETHING SENT BACK!')
    socket.send('event', message, namespace='/downstream', room=sid)
    return True


def event_dispatcher(message):

    SID = request.sid
    print(f'DATA: {message}, SID: {SID}')

    print(current_user.is_authenticated)

    #send_message(SID, 'Connection accepted')
    socket.send('event', message, namespace='/downstream', room=SID)

    return True


socket.on_event('event', event_dispatcher, namespace='/upstream')
