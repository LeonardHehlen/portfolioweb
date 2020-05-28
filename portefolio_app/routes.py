from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from portefolio_app import app, db
from portefolio_app.models import Projects, Users, Messages, Msg

var_to_template = {}

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        var_to_template['language'] = request.form['lang']
        print("language requested: ", var_to_template['language'])

    var_to_template['projects'] = Projects.query.all()
    return render_template("index.html", var_to_template=var_to_template)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = Users(email=request.form['email'])
        db.session.add(user)
        var_to_template['errors'] = ''
        try:
            db.session.commit()
            return redirect(url_for('messenger', user_id = user.id))
        except:
            var_to_template['errors'] = ['Cet email est déjà enregistré.']
        
    return render_template("register.html", var_to_template=var_to_template)

@app.route("/messenger/<int:user_id>", methods = ['GET', 'POST'])
def messenger(user_id):
    var_to_template['user'] = Users.query.get_or_404(user_id)
    if request.method == 'POST':
        msg = Msg(obj = request.form['obj'], msg = request.form['msg'], user_id = user_id)
        db.session.add(msg)
        db.session.commit()

    var_to_template['messages'] = Msg.query.filter_by(user_id=user_id)
    return render_template("messenger.html", var_to_template=var_to_template)
