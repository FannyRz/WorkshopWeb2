# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

pseudo_actif = ""

@app.route("/")
def accueil():
    return '<p> coucou accueil <p>'

@app.route("/connexion", methods=['GET','POST'])
def connexion():
    # if (request.method == 'POST'):
    #     nom_res = request.form['nom']
    #     prenom_res = request.form['prenom']
    #     naissance_res = request.form['naissance']
    #     nationalite_res = request.form['nationalite']
    #     pseudo_res = request.form['pseudo']

    #     #enregistrer un mot de passe hasher 
    #     password_reshash = model.hash_psw(request.form['password'])
    #     model.form_info(nom_res,prenom_res,naissances_res,nationalite_res,pseudo_res,password_reshash)
    #     return render_template("connexion.html")

    if (request.method == 'POST'):
        pseudo_actif = request.form['pseudo']

        #enregistrer un mot de passe hasher 
        password_reshash = model.hash_psw(request.form['password'])
        joueur_bdd = model.get_data("SELECT * FROM JOUEUR WHERE pseudo=%s", (pseudo_actif))
        if(password_reshash == joueur_bdd.mot_de_passe){
            return render_template("profil.html")
        }
        return render_template("connexion.html")
        

    return render_template("connexion.html")

@app.route("/profil", methods=['GET','POST'])
def profil():
    return render_template("profil.html", nom = pseudo_actif)

@app.route("/inscription", methods=['GET','POST'])
def inscription():

    return render_template("connexion.html")

@app.route("/sudoku")
def get_data():
    return model.get_data()





