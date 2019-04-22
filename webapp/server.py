from flask import Flask, session, redirect, url_for, escape, request, jsonify, make_response
from model import datastore, transactionProcessor
from flask_cors import CORS

import json


app = Flask(__name__)
app.secret_key = 'any random string'

cors = CORS(app, resources={r"/*": {"origins": "*"}, r"/create_new_player": {"origins": "*"},
                            r"/get_location/*" : {"origins": "*"}})


@app.route('/')
def index():
   if 'username' in session:
       email = session['email']
       pswrd = session['pswrd']
       print("here")
       return datastore.new_user(email, pswrd)


@app.route('/new_user', methods = ['POST'])
def new_user():
    usr_info = json.loads(request.data.decode("utf-8"))
    if request.method == 'POST':
        print(usr_info['email'] + ', ' + usr_info['pswrd'])
        datastore.new_user(usr_info['email'], usr_info['pswrd'])
        return 'Done.'


@app.route('/login', methods = ['POST'])
def login():
    usr_info = json.loads(request.data.decode("utf-8"))
    if request.method == 'POST':
        datastore.get_user(usr_info['email'], usr_info['pswrd'])
        return jsonify(message='logged in')


@app.route('/create_new_player', methods = ['POST'])
def create_new_player():
    user_info = json.loads(request.data.decode("utf-8"))
    if request.method == 'POST':
        datastore.create_new_player(user_info['email'], user_info['pswrd'], user_info['data'])
        return jsonify(message='created new player')


@app.route('/get_location/<email>', methods = ['GET'])
def getLocation(email):
    if request.method == 'GET':
        return jsonify(datastore.getLocation(email))


@app.route('/get_credits/<email>', methods = ['GET'])
def getCredits(email):
    if request.method == 'GET':
        return jsonify(datastore.getCredits(email))


@app.route('/get_players/<email>', methods = ['GET'])
def getPlayers(email):
    if request.method == 'GET':
        return jsonify(datastore.getPlayers(email))


@app.route('/delete_player/<email>', methods = ['POST'])
def deletePlayer(email):
    if request.method == 'POST':
        key = request.data.decode("utf-8")
        datastore.deletePlayer(email, key)
        return 'SUCCESS'


@app.route('/load_player/<email>', methods = ['POST'])
def loadPlayer(email):
    if request.method == 'POST':
        key = request.data.decode("utf-8")
        return datastore.loadPlayer(email, key)


@app.route('/get_inventories/<email>', methods = ['GET'])
def getInventories(email):
    return jsonify(datastore.getInventories(email))


@app.route('/sell_item/<email>', methods = ['POST'])
def sellItem(email):
    if request.method == 'POST':
        item = request.data.decode("utf-8")
        res = jsonify(datastore.sellItem(email, item))
        return res


@app.route('/buy_item/<email>', methods = ['POST'])
def buyItem(email):
    if request.method == 'POST':
        item = request.data.decode("utf-8")
        res = jsonify(datastore.buyItem(email, item))
        return res

