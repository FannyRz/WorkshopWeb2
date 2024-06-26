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

def form_info(nom, prenom, naissance, nationalite, pseudo, password):
    return get_data("INSERT INTO JOUEUR(nom des champs) VALUES (%s,%s,%s,%s,%s,%s)") 