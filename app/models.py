import json
from datetime import datetime
from random import SystemRandom

import bcrypt
from app import db, login, fernet
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


def generate_API(N):
    import string
    key = ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))
    return key


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String, nullable=False, default= fernet.encrypt( 'nomail@all'.encode('utf-8') ) )
    name = db.Column(db.String, nullable=False, default= fernet.encrypt( 'noname'.encode('utf-8') ) )
    address = db.Column(db.String, nullable=False, default= fernet.encrypt( 'noaddress'.encode('utf-8') ) )
    phone = db.Column(db.String, nullable=False, default= fernet.encrypt( 'nophone'.encode('utf-8') ) )
    APIkey = db.Column(db.String(32), nullable=False, default=generate_API(32))
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    last_modified_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    userlevel = db.Column(db.Integer, nullable=False, default=2) #0-SU; 1-ADM; 2-CL
    is_enabled = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Username: {self.username}>; <userlevel: {self.userlevel}>; <API: {self.APIkey}>'


    def set_password(self, password):
        salt = bcrypt.gensalt(14)
        p_bytes = password.encode()
        pw_hash = bcrypt.hashpw(p_bytes, salt)
        self.password_hash = pw_hash.decode()
        self.salt = salt.decode()
        return True


    def check_password(self, password):
        c_password = bcrypt.hashpw(password.encode(), self.salt.encode()).decode()
        if c_password == self.password_hash:
            return True
        else:
            return False


    def set_enc_data(self, **kwargs):
        """
        usage:
            u = User()
            u.set_enc_data( email= 'testmail@test.te', name= 'John Doe', address= '1234, Qwert, Zuio st. 45.' ... )
        """
        if not len(kwargs): return False

        for key in kwargs:
            pass

        for key in kwargs:
            if not key in self.__dict__:
                continue
            else:
                self.key = fernet.encrypt( kwargs[key].encode('utf-8') )

        return True


    def get_enc_data(self, *args):
        """
            usage:
                u = User()
                u.get_enc_data([ 'email', 'address', ... ])
                -> { 'email': 'testmail@test.te', 'address': '1234, Qwert, Zuio st. 45.', ... }
        """
        if not len(args): return False

        params = {}
        for arg in args:
            try:
                for arg in args:
                    params[arg] = fernet.decrypt(self.arg).decode('utf-8')
            except:
                return False

        return params


    def get_self_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'settings': self.settings,
            'created_at': self.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
            'last_modified_at': self.last_modified_at.strftime("%m/%d/%Y, %H:%M:%S"),
            'is_superuser': self.is_superuser,
            'is_enabled': self.is_enabled,
            'email': self.get_enc_data(['email']),
            'name': self.get_enc_data(['name']),
            'address': self.get_enc_data(['address']),
            'phone': self.get_enc_data(['phone']),
            'APIkey': self.APIkey,
            'userlevel': self.userlevel
        }


    def re_enc_data(self, new_fernet):

        old_data = self.get_enc_data( ['email', 'name', 'address', 'phone'] )

        self.email = new_fernet.encrypt(old_data['email'].encode('utf-8'))
        self.name = new_fernet.encrypt(old_data['name'].encode('utf-8'))
        self.address = new_fernet.encrypt(old_data['address'].encode('utf-8'))
        self.phone = new_fernet.encrypt(old_data['phone'].encode('utf-8'))

        return True


class Event(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)

    def __repr__(self):
        return f'<Username: {self.username}>; <userlevel: {self.userlevel}>; <API: {self.APIkey}>'


class Wallet(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    last_modified_at = db.Column(db.Date(), default=datetime.now(), nullable=False)
    balance = db.Column(db.Integer, nullable=False, default=0)
    owner = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE") )
    modified_by = db.Column( db.Integer, db.ForeignKey('user.id') )

    def __repr__(self):
        return f'<Username: {self.owner}>; <balance: {self.balance}>'