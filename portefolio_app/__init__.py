from flask import Flask
from flask_sqlalchemy import SQLAlchemy, sqlalchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SECRET_KEY'] = 'dbabe71f14251434a2029af6db081dd5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'

db = SQLAlchemy(app)

from portefolio_app import routes