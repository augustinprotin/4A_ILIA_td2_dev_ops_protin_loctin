from flask import Flask

app = Flask(__name__)

compteur = 0


@app.route("/")
def hello_world():
    return "<p>Hello, ceci est un compteur !</p>"


@app.route("/cpt")
def get_compteur():
    global compteur
    return str(compteur)


@app.route("/incr")
def incr_compteur():
    global compteur
    compteur += 1
    return str(compteur)


@app.route("/decr")
def decr_compteur():
    global compteur
    compteur -= 1
    return str(compteur)
