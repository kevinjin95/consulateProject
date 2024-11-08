from consulate import db, bcrypt, loginManager
from flask_login import UserMixin, login_user

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName= db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer())
     # phoneNumber = db.Column(db.Integer(), nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # ownerId = db.Column(db.Integer(), db.ForeignKey('person.id'))
    userName = db.Column(db.String(20), nullable=False, unique=True)
    emailAddress = db.Column(db.String(20), nullable=False, unique=True)
    passwordHash = db.Column(db.String(80), nullable=False)
   
    def __repr__(self):
        return f'User {self.userName}'

    @property
    def password(self):
        return self.password
    
    @password.getter
    def password(self):
        return self.passwordHash

    @password.setter
    def password(self, password1):
        self.passwordHash = bcrypt.generate_password_hash(password1).decode('utf-8')
    
    @password.deleter
    def password(self):
        del self._name
   
class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    live = db.Column(db.Integer(), db.ForeignKey('person.id'))
    doorNumber = db.Column(db.Integer())
    streetName = db.Column(db.String(30))
    city = db.Column(db.String(30))
    postalCode = db.Column(db.Integer())
