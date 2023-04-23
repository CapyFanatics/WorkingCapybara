from App.models import User
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        db.session.commit()
        return user
    return None

def update_password(id, password):
    user = get_user(id)
    if user:
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    return None
    
# def jwt_authenticate(username, password):
#     user = get_user_by_username(username)
#     if user and check_password_hash(user.password, password):
#         return user
#     else:
#         return None

def jwt_authenticate(username, password):
    user = get_user_by_username(username)
    if user and user.check_password(password):
        return user
    else:
        return None