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

@app.route("/connexion", methods=['GET','POST'])
def connexion():
    if (request.method == 'POST'):
        nom_res = request.form['nom']
        prenom_res = request.form['prenom']
        naissance_res = request.form['naissance']
        nationalite_res = request.form['nationalite']
        pseudo_res = request.form['pseudo']
        password_res = request.form['password']
        



    return render_template('connexion.html')

# @app.route("/joueur")
# def getdrop():
#     return model.getdrop()


def form_info(nom, prenom, naissance, nationalite, pseudo, password):
    sql = "INSERT INTO JOUEUR(nom des champs) VALUES (%s,%s,%s,%s,%s,%s)"


