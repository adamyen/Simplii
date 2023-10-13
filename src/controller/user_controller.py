from src.models.user_model import user_model
user = user_model()

def create_user(data):
    success = user.create_user(data)
    if success:
        return True
    return False