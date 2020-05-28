from portefolio_app import db

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    link = db.Column(db.String(200), unique=False, nullable=False)
    img = db.Column(db.String(200), unique=False, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obj = db.Column(db.String(120), unique=False, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, unique=False, nullable=False)

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obj = db.Column(db.String(120), unique=False, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, unique=False, nullable=False)