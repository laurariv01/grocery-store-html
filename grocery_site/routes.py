'''
ROUTES.py
'''
from flask import render_template, redirect
from grocery_site import app
from grocery_site.models import db


@app.route("/")
def hello_world():
    return render_template("home.html")
    