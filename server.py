# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# mydb=mysql.connector.connect("")

# mycursor=mydb.cursor()

# def getdrop():
#     response = mycursor.execute("select * from joueur ")
#     return response.fetchall()

@app.route("/")
def accueil():
    return '<p> coucou accueil <p>'

@app.route("/connexion")
def connexion():
    return render_template('connexion.html')

# @app.route("/joueur")
# def getdrop():
#     return model.getdrop()



