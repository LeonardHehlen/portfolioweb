from flask import Flask, render_template, redirect, url_for, request, session
from portefolio_app import app

var_to_template = {}

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        var_to_template['language'] = request.form['lang']
        print("language requested: ", var_to_template['language'])

    return render_template("index.html", var_to_template=var_to_template)