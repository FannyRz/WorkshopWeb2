import mysql.connector
from flask import jsonify



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
    cursor.execute(requete)

    result = jsonify_a_cursor(cursor)

    cursor.close()
    conn.close()

    return result

def hash_psw(psw):
   return hashlib.sha256(str(psw).encode('utf-8')).hexdigest()

def form_info(nom, prenom, naissance, nationalite, pseudo, password):
    # Connexion à la base de données
    conn = mysql.connector.connect(**mydb)
    cursor = conn.cursor()

    joueur_actif = cursor.get_data("SELECT id_joueur FROM JOUEUR order by id_joueur desc limit 1")

    # Exécution de la requête
    cursor.execute("INSERT INTO JOUEUR(id_joueur, pseudo,nom,prenom,date_creation,nationalite,date_naissance,score,mot_de_passe) VALUES (0,%s,%s,%s,24/20/20,%s,%s,0,%s)")

    cursor.close()
    conn.close()