from .models import User, db, Post


def add_user(user:User)->None:
    db.session.add(user)
    db.session.commit()

def delete_user(user:User)->None:
    db.session.delete(user)
    db.session.commit()

def add_project(project:Post)->None:
    db.session.add(project)
    db.session.commit()

def get_all_users()->db.Query:
    return User.query.all()
