from .models import User, db, Post


def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def add_post(post:Post)->None:
    db.session.add(post)
    db.session.commit()

def get_all_users()->db.Query:
    return User.query.all()
