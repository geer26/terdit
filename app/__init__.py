from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import base64
from os import getenv
from cryptography.fernet import Fernet
from flask_login import LoginManager
from flask_socketio import SocketIO


app = Flask(__name__)
app.config.from_object(Config)
#print(app.config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

fernet = Fernet(base64.urlsafe_b64encode(getenv('FERNET_SECRET').encode('utf-8')))
#usage:
#fernet.encrypt(message.encode('utf-8'))
#fernet.decrypt(self.subject).decode('utf-8')

#az asszinkron kéréskezelő példányosítása és a szerverhez csatolása
socket = SocketIO(app)
#??????????? - ezzel működik!
socket.init_app(app, cors_allowed_origins="*")

from app import models, routes, socketio