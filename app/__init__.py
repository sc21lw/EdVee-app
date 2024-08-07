import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail, Message
# from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c688aa277b92d0769ee053a9609d1482'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# load_dotenv()

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
app.config['MAIL_USERNAME'] = "info.edvee@gmail.com"
app.config['MAIL_PASSWORD'] = "wbzf tidd tdvb ngmq"
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

from app import routes