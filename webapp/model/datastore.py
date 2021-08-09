import pyrebase
from model import player, universe, good
import jsonpickle
from datetime import datetime
import re

config = {
    'apiKey': "",
    'authDomain': "",
    'databaseURL': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


def new_user(email, password):
    auth.create_user_with_email_and_password(email, password)
    return auth.sign_in_with_email_and_password(email, password)


def get_user(email, password):
    return auth.sign_in_with_email_and_password(email, password)


def get_current_player(email):
    email_tag = str(email).replace('.', '_')
    date = db.child('users').child(email_tag).child('current_player').get().val()
    player_pickled = db.child('users').child(email_tag).child('players').child(date).child('player_info').get().val()
    return jsonpickle.decode(player_pickled)

def get_current_universe(email):
    email_tag = str(email).replace('.', '_')
    date = db.child('users').child(email_tag).child('current_player').get().val()
    solar1_pickled = db.child('users').child(email_tag).child('players').child(date).child('universe').child('solar1').get().val()
    solar2_pickled = db.child('users').child(email_tag).child('players').child(date).child('universe').child('solar2').get().val()
    solar3_pickled=db.child('users').child(email_tag).child('players').child(date).child('universe').child('solar3').get().val()

    uni = universe.Universe()

    uni.solarSystems = [jsonpickle.decode(solar1_pickled), jsonpickle.decode(solar2_pickled), jsonpickle.decode(solar3_pickled)]
    return uni


def create_new_player(email, password, player_info):
    user = get_user(email, password)
    newUniverse = universe.Universe()

    solar1 = newUniverse.solarSystems[0]
    solar2 = newUniverse.solarSystems[1]
    solar3 = newUniverse.solarSystems[2]
    randLocation = universe.getRandLocation(newUniverse)

    newPlayer = player.Player(player_info['name'], player_info['prefDifficulty'], player_info['skillPoints'], randLocation)
    date = str(datetime.today())
    for punct in "<>?:;,./{}[]|+=_-)(*&^%$#@!~`":
        date = date.replace(punct, "_")

    email_tag = str(email).replace('.', '_')

    pickle_player = jsonpickle.encode(newPlayer)
    pickle_solar1, pickle_solar2, pickle_solar3 = jsonpickle.encode(solar1), jsonpickle.encode(solar2), jsonpickle.encode(solar3)

    db.child('users').child(email_tag).child("players").child(date).child("player_info").set(pickle_player)
    db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar1').set(pickle_solar1)
    db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar2').set(pickle_solar2)
    db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar3').set(pickle_solar3)
    db.child('users').child(email_tag).child("current_player").set(date)


def getLocation(email):
    player = get_current_player(email)
    return player.location.name


def getCredits(email):
    player = get_current_player(email)
    return player.credits


def getPlayers(email):
    email_tag = str(email).replace('.', '_')

    player_res = db.child('users').child(email_tag).child("players").get().val()
    player_dict = {}

    for key in player_res.keys():
        player = jsonpickle.decode(player_res.get(key).get('player_info'))
        player_date = re.split(' |_', str(key))

        player_date = player_date[1] + '/' + player_date[2] + '/' + player_date[0]

        newKey = key.replace(' ', '#')
        player_dict[newKey] = [player.name, player_date]

    return player_dict


def deletePlayer(email, player):
    email_tag = str(email).replace('.', '_')
    playerKey = player.replace('#', ' ')
    playerKey = playerKey.replace("\"", "")

    return db.child('users').child(email_tag).child("players").child(playerKey).remove()


def loadPlayer(email, player):
    email_tag = str(email).replace('.', '_')
    playerKey = player.replace('#', ' ')
    playerKey = playerKey.replace("\"", "")

    db.child('users').child(email_tag).child("current_player").set(playerKey)

    player = get_current_player(email)
    return player.name


def getInventories(email):
    player = get_current_player(email)
    uni = get_current_universe(email)

    planetInventory = universe.getPlanetMarket(player.location.name, uni).marketInventory
    playerInventory = player.inventory

    inventory = {}

    for item in good.values:
        price = "${:.2f}".format(planetInventory.inventory[item.name].price)
        inventory[item.name] = (price,
                                planetInventory.inventory[item.name].stock,
                                playerInventory.inventory[item.name].stock)

    return inventory


def buyItem(email, item):
    item = item.replace("\"", "")
    player = get_current_player(email)
    uni = get_current_universe(email)

    email_tag = str(email).replace('.', '_')
    date = db.child('users').child(email_tag).child('current_player').get().val()

    planetInventory = universe.getPlanetMarket(player.location.name, uni).marketInventory
    playerInventory = player.inventory

    if planetInventory.inventory[item].stock > 0:
        if player.credits >= planetInventory.inventory[item].price:
            playerInventory.inventory[item].stock += 1
            player.credits -= planetInventory.inventory[item].price
            planetInventory.inventory[item].stock -= 1

            pickle_player = jsonpickle.dumps(player)
            pickle_solar1 = jsonpickle.dumps(uni.solarSystems[0])
            pickle_solar2 = jsonpickle.dumps(uni.solarSystems[1])
            pickle_solar3 = jsonpickle.dumps(uni.solarSystems[2])

            db.child('users').child(email_tag).child("players").child(date).child("player_info").set(pickle_player)
            db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar1').set(pickle_solar1)
            db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar2').set(pickle_solar2)
            db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar3').set(pickle_solar3)

            return player.credits
        else:
            return "You do not have enough credits."
    else:
        return "Item is out of stock."


def sellItem(email, item):
    item = item.replace("\"", "")
    player = get_current_player(email)
    uni = get_current_universe(email)

    email_tag = str(email).replace('.', '_')
    date = db.child('users').child(email_tag).child('current_player').get().val()

    planetInventory = universe.getPlanetMarket(player.location.name, uni).marketInventory
    playerInventory = player.inventory

    if playerInventory.inventory[item].stock > 0:
        playerInventory.inventory[item].stock -= 1
        player.credits += planetInventory.inventory[item].price
        planetInventory.inventory[item].stock += 1

        pickle_player = jsonpickle.dumps(player)
        pickle_solar1 = jsonpickle.dumps(uni.solarSystems[0])
        pickle_solar2 = jsonpickle.dumps(uni.solarSystems[1])
        pickle_solar3 = jsonpickle.dumps(uni.solarSystems[2])

        db.child('users').child(email_tag).child("players").child(date).child("player_info").set(pickle_player)
        db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar1').set(
            pickle_solar1)
        db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar2').set(
            pickle_solar2)
        db.child('users').child(email_tag).child("players").child(date).child("universe").child('solar3').set(
            pickle_solar3)

        return player.credits
    else:
        return "You do not have any " + item + " in stock."








