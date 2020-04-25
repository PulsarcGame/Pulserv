from . import app, loginMan
from .. import database
from flask import request, render_template, redirect, flash, Markup
from flask_login import current_user, logout_user, login_user, login_required
from ..sharedFunctions import emailValid, usernameValid, passwordValid

# Public Facing Authentication Routes


# User loader function for flask-login
@loginMan.user_loader
def userLoader(userID):
    return database.models.Player.objects(id=userID).first()


@app.route("/register", methods=["GET", "POST"])
def registerPlayer():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        if usernameValid(username) is True:
            if emailValid(email) is True:
                if passwordValid(password):
                    if password == confirmPassword:
                        newPlayer = database.models.Player(username=username, email=email)
                        newPlayer.setPassword(password)
                        newPlayer.save()
                        return redirect("/")
                    else:
                        flash("Passwords don't match!")
                        return render_template("register.html")
                else:
                    flash(passwordValid(password))
                    return render_template("register.html")
            else:
                flash(emailValid(email))
                return render_template("register.html")
        else:
            flash(usernameValid(username))
            return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        playerObject = database.models.Player.objects(email=email).first()
        if playerObject is None:
            flash(Markup('User does not exist!, try registering at <a href="/register">Register</a>'))
            return render_template("login.html")
        else:
            if playerObject.checkPassword(password):
                login_user(playerObject)
                return redirect("/")
            else:
                flash("Invalid password!")
                return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logged Out!")
        return redirect("/")
    else:
        return redirect("/")


@app.route("/loginTest")
@login_required
def loginTest():
    return "Epic"
