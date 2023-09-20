from flask import Flask, render_template, request
import utils.serialUtil as serialUtil

#currentChannel = input("Veuillez entrer le nom de la chaîne TV active afin de ne pas créer de soucis lors du changement de celle-ci :")
users = [{"id" : "baptiste.gosselin", "email" : "contact@baptiste-gosselin.fr", "password" : "zeyco"}]

app = Flask(__name__)

with app.app_context():
    print("init")
    # serialUtil.serialInitialization('COM1', 9600)

@app.route('/')
def connexion():
    return render_template("connexionPage.html")

@app.route('/media/direct/tv', methods=['POST'])
def tv():
    autorization = False
    result = request.form
    id = result['Identifiant']
    email = result['Email']
    password = result['Mot de passe']
    for user in users:
        if id == user["id"] and email == user["email"] and password == user["password"]:
            autorization = True
    if autorization:
        return render_template("tvPage.html")
    elif not autorization:
        return render_template("errorPage.html")

@app.route('/action/<action>', methods=['POST'])
def changeChannel(action):
    if not serialUtil.waitClick:
        if action == "1":
            futurChannel = 1
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "1"
        elif action == "2":
            futurChannel = 2
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "2"
        elif action == "3":
            futurChannel = 3
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "3"
        elif action == "4":
            futurChannel = 4
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "4"
        elif action == "5":
            futurChannel = 5
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "5"
        elif action == "6":
            futurChannel = 6
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "6"
        elif action == "7":
            futurChannel = 7
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "7"
        elif action == "8":
            futurChannel = 8
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "8"
        elif action == "9":
            futurChannel = 9
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "9"
        elif action == "10":
            futurChannel = 10
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "10"
        elif action == "11":
            futurChannel = 11
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "11"
        elif action == "12":
            futurChannel = 12
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "12"
        elif action == "13":
            futurChannel = 13
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "13"
        elif action == "14":
            futurChannel = 14
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "14"
        elif action == "15":
            futurChannel = 15
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "15"
        elif action == "16":
            futurChannel = 16
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "16"
        elif action == "17":
            futurChannel = 17
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "17"
        elif action == "18":
            futurChannel = 18
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "18"
        elif action == "19":
            futurChannel = 19
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "19"
        elif action == "20":
            futurChannel = 20
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "20"
        elif action == "21":
            futurChannel = 21
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "21"
        elif action == "22":
            futurChannel = 22
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "22"
        elif action == "23":
            futurChannel = 23
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "23"
        elif action == "24":
            futurChannel = 24
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "24"
        elif action == "25":
            futurChannel = 25
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "25"
        elif action == "26":
            futurChannel = 26
            # currentChannel = serialUtil.changeChannel(currentChannel, futurChannel)
            return "26"
        else:
            return "",403
    else:
        return "",403

app.run(host='0.0.0.0', port=8080)