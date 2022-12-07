from flask import Flask, render_template, request

app = Flask(__name__) #variable de entorno que contiene el "main"

@app.route("/") #definimos que hay una ruta de acceso con el arroba
def index():
    return render_template("index.html")

@app.route("/accion")
def accion():
    return render_template("accion.html")

@app.route("/dbz")
def dbz():
    return render_template("juegos.html")

@app.route("/casuales")
def casuales():
    return render_template("casuales.html")

@app.route("/casuales/getting-over-it")
def gettingOver():
    return render_template("/casuales/getting-over.html")

@app.route("/casuales/geometry-neon-dash-subzero")
def geoDash():
    return render_template("/casuales/geodash.html")

@app.route("/casuales/chess-online-multiplayer-game")
def chessOnlineMultiplayerGame():
    return render_template("/casuales/chess-online-multiplayer-game.html")

@app.route("/casuales/bloxdhop-io")
def bloxdhopIo():
    return render_template("/casuales/bloxdhop-io.html")

@app.route("/casuales/crazy-roll-3d")
def crazyRoll3d():
    return render_template("/casuales/crazy-roll-3d.html")

@app.route("/casuales/cut-the-rope")
def cutTheRope():
    return render_template("/casuales/cut-the-rope.html")

@app.route("/casuales/international-super-animal-soccer")
def internationalSuperAnimalSoccer():
    return render_template("/casuales/international-super-animal-soccer.html")

@app.route("/casuales/internet-gaming-cafe-simulator")
def internetGamingCafeSimulator():
    return render_template("/casuales/internet-gaming-cafe-simulator.html")

@app.route("/casuales/market-boss")
def marketBoss():
    return render_template("/casuales/market-boss.html")

@app.route("/casuales/royaledudes-io")
def royaledudesIo():
    return render_template("/casuales/royaledudes-io.html")

@app.route("/casuales/total-crush")
def totalCrush():
    return render_template("/casuales/total-crush.html")

@app.route("/casuales/turbo-dismounting")
def turboDismounting():
    return render_template("/casuales/turbo-dismounting.html")

@app.route("/casuales/wood-farmer")
def woodFarmer():
    return render_template("/casuales/wood-farmer.html")

@app.route("/casuales/lampada-street")
def lampadaStreet():
    return render_template("/casuales/lampada-street.html")

# @app.route("/casuales/")
# def geoDash():
#     return render_template("/casuales/")

# @app.route("/casuales/")
# def geoDash():
#     return render_template("/casuales/")

