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


    return render_template('connexion.html')

@app.route('/sudoku')
def get_data():
    return model.get_data("SELECT * FROM SUDOKU")





