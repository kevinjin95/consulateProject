from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config['SECRET_KEY'] = '44d9de2b82a1deb9057de798'
bcrypt = Bcrypt(app)

from consulate import routes