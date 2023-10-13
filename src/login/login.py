from flask import Blueprint, request, session
from flask import render_template, redirect

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def loginMethod():
    """This function renders the login page."""
    return render_template("login.html")

@login.route('/login', methods=['POST'])
def loginPostMethod():
    """This function logs in users and redirects to home page."""
    return redirect("/")

@login.route('/logout', methods=['GET'])
def logoutMethod():
    """This function logsout of the application and redirects to login page again."""
    return redirect("/login")