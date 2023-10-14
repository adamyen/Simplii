from flask import Blueprint, request, session, flash
from flask import render_template, redirect
from src.controller.user_controller import create_user, login_control, get_loggedIn_User

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def loginMethod():
    """This function renders the login page."""
    return render_template("login.html")

@login.route('/login', methods=['POST'])
def loginPostMethod():
    """This function logs in users and redirects to home page."""
    loginStatus  = login_control(request.form)
    if loginStatus:
        session["username"] = get_loggedIn_User(request.form["username"])
        return redirect("/")
    flash("Incorrect username or password!", 'error')
    return redirect("/login")

@login.route('/signup', methods=['POST'])
def signUpMethod():
    """This function logs in users and redirects to home page."""
    data = request.form
    success = create_user(data)
    if success:
        flash("Sign up successful!", 'success')
        return redirect("/login")
    else:
        flash("Sign up failed, Please try again!", 'error')
        return redirect("/login")

@login.route('/logout', methods=['GET'])
def logoutMethod():
    """This function logsout of the application and redirects to login page again."""
    session["username"] = ""
    return redirect("/login")