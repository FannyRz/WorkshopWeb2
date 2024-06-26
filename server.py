# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,jsonify,abort
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

import json
import requests

debug_var = ""


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
    tab_joueurs = model.best_joueurs()
    joueur1 = tab_joueurs[0]
    joueur2 = tab_joueurs[1]
    joueur3 = tab_joueurs[2]
    return render_template("home.html",pseudo1 = joueur1[1], nationalite1 = joueur1[5], score1 = joueur1[7],
    pseudo2 = joueur2[1], nationalite2 = joueur2[5], score2 = joueur2[7],
    pseudo3 = joueur3[1], nationalite3 = joueur3[5], score3 = joueur3[7], )

@app.route("/deconnecter")
def deconnecter():
    model.pseudo_actif = ""
    tab_joueurs = model.best_joueurs()
    joueur1 = tab_joueurs[0]
    joueur2 = tab_joueurs[1]
    joueur3 = tab_joueurs[2]
    return render_template("home.html",pseudo1 = joueur1[1], nationalite1 = joueur1[5], score1 = joueur1[7],
    pseudo2 = joueur2[1], nationalite2 = joueur2[5], score2 = joueur2[7],
    pseudo3 = joueur3[1], nationalite3 = joueur3[5], score3 = joueur3[7],)

@app.route("/connexion", methods=['GET','POST'])
def connexion():

    if(model.pseudo_actif != "") :
        return render_template("profil.html", nom = model.pseudo_actif)

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

    if(model.pseudo_actif != "") :
        return render_template("profil.html", nom = model.pseudo_actif)

    model.pseudo_actif = request.form['pseudo']


    #enregistrer un mot de passe hasher 
    password_reshash = model.hash_psw(request.form['password'])
    
    joueur_bdd = model.get_data("SELECT mot_de_passe FROM JOUEUR WHERE pseudo=%s")
    model.pseudo_actif = ""
    if (joueur_bdd != []) :
        if(password_reshash == joueur_bdd[0][0]) :
            model.pseudo_actif = request.form['pseudo']
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
        password_reshash = model.hash_psw(request.form['password'])
        model.form_info(nom_res,prenom_res,naissance_res,nationalite_res,pseudo_res,password_reshash)
        # return password_reshash
        return render_template("connexion.html", create_account_message="Compte créé !")
    return render_template("connexion.html")

@app.route("/sudoku")
def get_data():
    return model.get_data("SELECT * FROM SUDOKU")

@app.route("/supprimer", methods=['GET', 'POST'])
def supprimer():
    model.supprimer(model.pseudo_actif)
    model.pseudo_actif = ""
    return render_template("connexion.html", create_account_message= model.debug(), pseudo_actif_debug=model.pseudo_actif)

@app.route("/mdp_oublie", methods=['GET', 'POST'])
def mdp_oublie():
    if (request.method == 'POST'):
        pseudo_res = request.form['pseudo']
        new_password_res = request.form['new_password']
        new_password_verif_res = request.form['new_password_verif']
        model.pseudo_actif = pseudo_res
        joueur_bdd = model.get_data("SELECT * FROM JOUEUR WHERE pseudo=%s")
        model.pseudo_actif = ""
        if( joueur_bdd != []):
            if(new_password_res != new_password_verif_res):
                return render_template("mot_de_passe_oublie.html", mdp_erreur="Erreur dans la saisie du mot de passe")
            new_password_hash = model.hash_psw(new_password_verif_res)
            model.mdp_oublie(pseudo_res,new_password_hash)
            return render_template("connexion.html", mdp_erreur = "Mot de passe modifié avec succès")
        else:
            return render_template("mot_de_passe_oublie.html", mdp_erreur = "Pseudo introuvé !")
    return render_template("mot_de_passe_oublie.html")


@app.route("/addsession")
def addsession():
    return render_template("addsession.html")


@app.route("/profiladdsession", methods=['GET', 'POST'])
def profil_addsession():
    if (request.method == 'POST'):
        date_res = request.form['date_session']
        temps_res = request.form['temps']
        erreur_res = request.form['erreur']
        sudoku_res = request.form['sudoku']
        model.input_session_info(date_res,temps_res,erreur_res,sudoku_res)
        return render_template("profil.html", nom=model.pseudo_actif)
    return render_template("addsession.html", add_session_message="Mauvaise saisie... Veuillez réessayer !")


@app.route("/listsession")
def listsession():
    return model.get_session()

@app.route("/profil/<int:id>", methods=['GET','DELETE'])
def del_session(id):
    model.del_session(id)
    return render_template("profil.html", nom=model.pseudo_actif)

@app.route("/a_propos")
def info():
    return render_template("a_propos.html")

@app.route("/sudokuplay")
def play_sudoku():
    return render_template("sudoku.html")