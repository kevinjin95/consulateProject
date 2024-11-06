from consulate import db
# from flask_login import UserMixin, login_user
from wtforms.validators import ValidationError
class Person(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    firstName= db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer())
     # phoneNumber = db.Column(db.Integer(), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # ownerId = db.Column(db.Integer(), db.ForeignKey('person.id'))
    userName = db.Column(db.String(20), nullable=False, unique=True)
    emailAddress = db.Column(db.String(20), nullable=False, unique=True)
    passwordHash = db.Column(db.String(80), nullable=False)
   
    def checkUserName(self, userNameToCheck):
        user = User.query.all(userName=userNameToCheck)
        if user:
            raise ValidationError(f'The user {user} is already used !!')

    def __repr__(self):
        return f'User {self.userName}'

# def checkUserConnexion(form):
#     pass

# def getUserId(userName):
#     pass

# @loginManager.user_loader
# def load_user(user_id):
#     pass

class Home(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    live = db.Column(db.Integer(), db.ForeignKey('person.id'))
    doorNumber = db.Column(db.Integer())
    streetName = db.Column(db.String(30))
    city = db.Column(db.String(30))
    postalCode = db.Column(db.Integer())
