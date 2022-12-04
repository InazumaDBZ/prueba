from tkinter.tix import Form
from flask import Flask, render_template, request

app = Flask(__name__) #variable de entorno que contiene el "main"

@app.route("/") #definimos que hay una ruta de acceso con el arroba
def index():
    nombre = request.args.get('nombre', 'mundo')
    return render_template("home.html", nombre = nombre)

if __name__ == '__main__':
    app.run()