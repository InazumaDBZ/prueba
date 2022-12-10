from flask import Flask, render_template, request, redirect, flash, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

db = SQL('sqlite:///UnsirifaGames.db')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()
    # Validaciones de login
    if request.method == 'POST':
        userLog = request.form.get('user-login')
        passwordReg = request.form.get('password-login')

        # Consultamos a nuestra base de datos todos los datos relacionadas a la cuenta introducida
        rows = db.execute("SELECT * FROM users WHERE username = ?", userLog)

        # Comprobamos que estos existan en la base de datos
        if len(rows) != 1 or passwordReg != rows[0]['password']:
            flash('¡Usuario o contraseña inválida!')

        # Recordamos el id del usuario actual
        session["user_id"] = rows[0]["id"]

        username = rows[0]["username"]

        # Volvemos a la página principal
        return render_template('login.html', username = username)

@app.route('/logout')
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Validaciones de Register
    if request.method == 'POST':
        # Obtener la información escrita en los inputs
        email = request.form.get('email')
        userReg = request.form.get('user-register')
        passwordReg = request.form.get('password-register')

        # Verificamos que no se introduzca un nombre de usuario y correo ya existente
        check_user = db.execute('SELECT username, email FROM users WHERE username = ? AND email = ?', userReg, email)

        # Confirmamos que el usuario y correo estén disponibles
        if len(check_user) != 0:
            flash('¡Ya existe, elige otro!', "error")

        # Comprobamos que se provea un usuario
        elif not request.form.get('user-register'):
            flash('¡Se necesita un usuario!', "error")

        # Comprobamos que se provea una contraseña
        elif not request.form.get("password-register"):
            flash('¡Se necesita contraseña!', "error")

        # Insertamos los datos a la base de datos
        new_account = db.execute("INSERT INTO users (username, password, email) VALUES (?,?,?)", userReg, passwordReg, email)

        session["user_id"] = new_account

        return render_template('login.html')

    else:
        return render_template('index.html')


@app.route("/accion")
def accion():
    return render_template("accion.html")

@app.route("/dbz")
def dbz():
    return render_template("juegos.html")

if __name__ == "__main__":
    app.run()