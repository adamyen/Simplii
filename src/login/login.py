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

@login.route('/signup', methods=['POST'])
def signUpMethod():
    data = request.form
    print("In signup new\n", data.items(), "\n\n")

    for key, value in data.items():
        print(key, " ============== ", value)

    """This function logs in users and redirects to home page."""
    return "Testing"

@login.route('/logout', methods=['GET'])
def logoutMethod():
    """This function logsout of the application and redirects to login page again."""
    return redirect("/login")


def print(data):
    print("printing")
    for key, value in data.items():
        print(key, " ============== ", value)