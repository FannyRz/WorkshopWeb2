# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

import json
import requests



def json_to_json_string(json_string):
    """
    Transforme une chaîne JSON en une autre chaîne JSON après l'avoir convertie en dictionnaire.

    :param json_string: La chaîne JSON de base.
    :return: Une nouvelle chaîne JSON.
    """
    try:
        # Convertir la chaîne JSON en dictionnaire
        dictionary = json.loads(json_string)
        
        # Convertir le dictionnaire en une nouvelle chaîne JSON
        new_json_string = json.dumps(dictionary, indent=4)  # Indentation pour la lisibilité
        return new_json_string
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la transformation du JSON: {e}")
        return None

@app.route("/")
def accueil():
    return '<p> coucou accueil <p>'

@app.route("/connexion", methods=['GET','POST'])
def connexion():

    # if (request.method == 'POST'):
    #     pseudo_actif = request.form['pseudo']

    #     #enregistrer un mot de passe hasher 
    #     password_reshash = model.hash_psw(request.form['password'])
    #     # joueur_bdd = model.get_data("SELECT * FROM JOUEUR WHERE pseudo=%s", (pseudo_actif))
    #     # if(password_reshash == joueur_bdd.mot_de_passe) :
    #     return render_template("profil.html", nom = pseudo_actif)
        
    #     # return render_template("connexion.html")
        

    return render_template("connexion.html")

@app.route("/profil", methods=['GET','POST'])
def profil():

    model.pseudo_actif = request.form['pseudo']

    #enregistrer un mot de passe hasher 
    # password_reshash = model.hash_psw(request.form['password'])
    password_res = request.form['password']
    joueur_bdd = model.get_data("SELECT mot_de_passe FROM JOUEUR WHERE pseudo=%s", model.pseudo_actif)
    if (joueur_bdd != []) :
        if(password_res == joueur_bdd[0][0]) :
            return render_template("profil.html", nom = model.pseudo_actif)
        return render_template("connexion.html", mdp_erreur = "Mot de passe incorrecte !")
    return render_template("connexion.html", mdp_erreur = "Identifiant incorrecte !")

@app.route("/inscription", methods=['GET','POST'])
def inscription():
    if (request.method == 'POST'):
        nom_res = request.form['nom']
        prenom_res = request.form['prenom']
        naissance_res = request.form['naissance']
        nationalite_res = request.form['nationalite']
        pseudo_res = request.form['pseudo']
        password_res = request.form['password']
    #     #enregistrer un mot de passe hasher 
    #     password_reshash = model.hash_psw(request.form['password'])
        model.form_info(nom_res,prenom_res,naissance_res,nationalite_res,pseudo_res,password_res)
    #     return render_template("connexion.html")
        return render_template("connexion.html", create_account_message= model.debug())
    return render_template("connexion.html")

@app.route("/sudoku")
def get_data():
    return model.get_data("SELECT * FROM SUDOKU")

@app.route("/supprimer", methods=['GET', 'POST'])
def supprimer():
    model.supprimer(model.pseudo_actif)
    model.pseudo_actif = ""
    return render_template("connexion.html", create_account_message= model.debug(), pseudo_actif_debug=model.pseudo_actif)







