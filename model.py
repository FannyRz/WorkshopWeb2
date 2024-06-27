import mysql.connector
from flask import jsonify
import hashlib
import server
import random
import datetime

pseudo_actif = ""

mydb = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'sudokuDB'
}

def jsonify_a_cursor(cursor):
    # Récupération des résultats
    rows = cursor.fetchall()

    # Récupération des noms de colonnes
    column_names = [i[0] for i in cursor.description]

    # Transformation des résultats en liste de dictionnaires
    results = [dict(zip(column_names, row)) for row in rows]

    # Retour des résultats en JSON
    return jsonify(results)

def get_data(requete):
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute(requete,(pseudo_actif,))

    # result = jsonify_a_cursor(cursor)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def hash_psw(psw):
   return hashlib.sha256(str(psw).encode('utf-8')).hexdigest()

def form_info(nom, prenom, naissance, nationalite, pseudo, password):
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    newconn = mysql.connector.connect(**mydb)
    newcursor = newconn.cursor()
    newcursor.execute("SELECT id_joueur FROM JOUEUR ORDER BY id_joueur DESC LIMIT 1")
    joueur_actif = newcursor.fetchall()
    newcursor.close()
    newconn.close()

    #choix d'un score aléatoire
    score_tmp = random.randint(1, 5000)

    #date du jour de creation
    aujourd_hui = datetime.date.today()

    # Exécution de la requête
    cursor.execute("INSERT INTO JOUEUR(id_joueur, pseudo, nom, prenom, date_creation, nationalite, date_naissance, score, mot_de_passe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (joueur_actif[0][0]+1,pseudo, nom, prenom, aujourd_hui,  nationalite, naissance,score_tmp, password,))
    conn.commit()
    
    cursor.close()
    conn.close()

def supprimer(pseudo):
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("DELETE FROM JOUEUR WHERE pseudo = %s", (pseudo,))
    conn.commit()

    cursor.close()
    conn.close()

def mdp_oublie(pseudo, new_password):
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("UPDATE joueur SET mot_de_passe = %s WHERE pseudo= %s", (new_password,pseudo,))
    conn.commit()

    cursor.close()
    conn.close()

def debug() :
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM JOUEUR")

    # result = jsonify_a_cursor(cursor)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def give_json_player_data():
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM SESSION JOIN JOUEUR ON SESSION.id_joueur = JOUEUR.id_joueur WHERE JOUEUR.pseudo=%s", (pseudo_actif,))

    # result = jsonify_a_cursor(cursor)
    result = jsonify_a_cursor(cursor)

    cursor.close()
    conn.close()

    return result

def best_joueurs():
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM JOUEUR ORDER BY score DESC LIMIT 3")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows