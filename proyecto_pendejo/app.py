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
