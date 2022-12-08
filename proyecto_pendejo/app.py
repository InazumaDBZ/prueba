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

#Inicio De Juegos De Accion

@app.route("/accion/spiderdoll")
def spiderdoll():
    return render_template("accion/spiderdoll.html")


@app.route("/accion/sandbox-city")
def sandbox_city():
    return render_template("accion/sandbox-city---cars-zombies-ragdolls.html")

@app.route("/accion/amazing-vice-spider")
def amazing_vice_spider():
    return render_template("accion/amazing-strange-rope-police.html")

@app.route("/accion/armed-with-wings-2")
def armed_wings2():
    return render_template("accion/armed-with-wings2.html")

@app.route("/accion/infeccion-z")
def infectionZ():
    return render_template("accion/infectionZ.html")

@app.route("/accion/time-shooter2")
def time_shooter2():
    return render_template("accion/time-shooter2.html")

@app.route("/accion/fields-of-fury")
def fields_fury():
    return render_template("accion/fields-of-fury.html")

@app.route("/accion/air-wars3")
def air_wars():
    return render_template("accion/air-wars3.html")

@app.route("/accion/hobo")
def hobo():
    return render_template("accion/hobo.html")

@app.route("/accion/ghost-walker")
def ghost_walker():
    return render_template("accion/ghost-walker.html")

@app.route("/accion/hero-battle---fantasy-arena")
def hero_battle():
    return render_template("accion/hero-battle-FA.html")

@app.route("/accion/smash-karts")
def smash_kart():
    return render_template("accion/smash-karts.html")

@app.route("/accion/dead-shot")
def dead_shot():
    return render_template("accion/dead-shot.html")

@app.route("/accion/shotgun-highway")
def shotgun_highway():
    return render_template("accion/shotgun-highway.html")

@app.route("/accion/bullet-force")
def bullet_force():
    return render_template("accion/bullet-force.html")

#fin de juegos de accion

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

#terror-----------------------------------

@app.route("/terror")
def terror():
    return render_template("terror.html")

@app.route("/terror/kuzbass-horror")
def kuzbass_horror():
    return render_template("/terror/kuzbass-horror.html")

@app.route("/terror/backwoods")
def backwoods():
    return render_template("/terror/backwoods.html")

@app.route("/terror/creepy-granny-scream-scary-freddy")
def creepy_granny_scream_scary_freddy():
    return render_template("/terror/creepy-granny-scream-scary-freddy.html")

@app.route("/terror/haunted-school---horror-game")
def haunted_school_horror_game():
    return render_template("/terror/haunted-school---horror-game.html")

@app.route("/terror/isles-of-mists-horror-story")
def isles_of_mists_horror_story():
    return render_template("/terror/isles-of-mists-horror-story.html")

@app.route("/terror/brother-wake-up")
def brother_wake_up():
    return render_template("/terror/brother-wake-up.html")

@app.route("/terror/house-of-celestina")
def house_of_celestina():
    return render_template("/terror/house-of-celestina.html")

@app.route("/terror/bear-haven-2")
def bear_haven_2():
    return render_template("/terror/bear-haven-2.html")

@app.route("/terror/celestina-chapter-two")
def celestina_chapter_two():
    return render_template("/terror/celestina-chapter-two.html")

@app.route("/terror/case-smile-horror-game-adventure")
def case_smile_horror_game_adventure():
    return render_template("/terror/case-smile-horror-game-adventure.html")

@app.route("/terror/case-smile-2")
def case_smile_2():
    return render_template("/terror/case-smile-2.html")

@app.route("/terror/in-to-the-forest")
def in_to_the_forest():
    return render_template("/terror/in-to-the-forest.html")

@app.route("/terror/saw-4-trapped")
def saw_4_trapped():
    return render_template("/terror/saw-4-trapped.html")

@app.route("/terror/slenderman-must-die-silent-streets")
def slenderman_must_die_silent_streets():
    return render_template("/terror/slenderman-must-die-silent-streets.html")

@app.route("/terror/slenderman-must-die-sanatorium-2021")
def slenderman_must_die_sanatorium_2021():
    return render_template("/terror/slenderman-must-die-sanatorium-2021.html")
