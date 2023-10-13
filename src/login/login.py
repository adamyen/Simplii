from flask import Blueprint, request, session
from flask import render_template, redirect
from src.models.user_model import user_model

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def loginMethod():
    """This function renders the login page."""
    return render_template("login.html")

@login.route('/login', methods=['POST'])
def loginPostMethod():
    """This function logs in users and redirects to home page."""
    return redirect("/")

@login.route('/signup', methods=['POST'])
def signUpMethod():
    print(request.form)
    data = request.form
    #print("In signup new\n", data.items(), "\n\n")
    user = user_model()
    x = user.create_user(data)
    if x:
        return "User Created Successfully"
    else:
        return "Error! Check logs"
    """This function logs in users and redirects to home page."""

@login.route('/logout', methods=['GET'])
def logoutMethod():
    """This function logsout of the application and redirects to login page again."""
    return redirect("/login")