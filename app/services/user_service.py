from app.models.user import User
from app.extension import db

def get_all_users():
    return User.query.all()

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_username(username):
    return User.query.filter_by(username=username).all()