from src.models.user_model import user_model
user = user_model()

def login_control(data):
    loginStatus = user.login(data)
    if loginStatus:
        return True
    return False

def get_loggedIn_User(username):
    userId = user.get_loggedIn_User(username)
    return userId


def create_user(data):
    success = user.create_user(data)
    if success:
        return True
    return False
