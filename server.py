# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)



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

        #enregistrer un mot de passe hasher 
        password_reshash = model.hash_psw(request.form['password'])
        model.form_info(nom_res,prenom_res,naissances_res,nationalite_res,pseudo_res,password_reshash)
        return render_template("connexion.html")

    if (request.method == 'GET'):
        return render_template("connexion.html")
    # if (request.method == 'POST'):
    #     pseudo_res = request.form['pseudo']

    #     #enregistrer un mot de passe hasher 
    #     password_reshash = model.hash_psw(request.form['password'])
    #     model.form_info(nom_res,prenom_res,naissances_res,nationalite_res,pseudo_res,password_reshash)

@app.route("/profil", methods=['GET','POST'])
def profil():
    return render_template("profil.html")

@app.route("/inscription", methods=['GET','POST'])
def inscription():
    return render_template("connexion.html")

@app.route("/sudoku")
def get_data():
    return model.get_data()





