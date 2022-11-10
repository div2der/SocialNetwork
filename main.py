from flask_app import *
from flask import render_template
from flask import request, session, redirect, url_for
from werkzeug.utils import secure_filename
from flask_socketio import SocketIO, send
from database.models import User, db, Post
from database import crud
import hashlib
import os

socketio = SocketIO(app, cors_allowed_origins = "*")

def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

@app.route("/home")
def index(context = None):
    posts = Post.query.all()
    return render_template("home.html", posts = posts[::-1])
@app.route("/")
def home(context=None):
    posts = Post.query.all()
    return render_template("home.html", posts = posts[::-1])


@app.route("/user/<int:user_id>")
def user_page(user_id, context=None):
    query = db.session.query(User).join(Post).filter(Post.post_author == user_id).first()
    if query:
        return render_template("profile.html", context=query)
    else:
        query = db.session.query(User).filter(User.user_id == user_id).first()
        return render_template("profile.html", context=query)


@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    print(request)
    if message != 'user connected':
        send(message, broadcast = True)


@app.route("/messenger")
def messenger(context=None):
    return render_template("messenger.html", context=context)


@app.route("/login", methods = ["GET", "POST"])
def login(context=None):
    if request.method == "POST":
        user = db.session.query(User).filter_by(login=request.form['username'], password = hash_password (request.form['password'])).first()
        print(user)
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['username'] = user.login
            return redirect(url_for("user_page", user_id=user.user_id))
        else:
            return render_template("login.html", context="The login or username were wrong")

    return render_template("login.html", context=context)

@app.route("/logout")
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/register', methods = ["GET", "POST"])
def register(context=None):
    if request.method == "POST":
        login = request.form['username']
        first_name = request.form['fname']
        second_name = request.form['sname']
        pass1 = request.form['password']
        pass2 = request.form['password_conf']
        email = request.form['email']
        data = db.session.query(User).filter_by(login=request.form['username']).first()
        
        print(data)

        if data :
            return redirect(url_for("register", error="Already registered!"))
        elif pass1!=pass2:
            return redirect(url_for("register", error="Passowords do not match!"))
        else:
            crud.add_user(User(login=login, 
                                first_name=first_name,
                                second_name=second_name,
                                password= hash_password(request.form['password']), 
                                email=email
                                ))

            print(pass2, login)

            return redirect(url_for("login", context="Succesfully registered!"))
    return render_template("registration.html", context=context)

@app.route("/upload", methods=["GET", "POST"])
def upload_file(context=None):
    if request.method=="POST":
        f = request.files["file_to_save"]
        f.save(f"static/img/{secure_filename(f.filename)}")
        return redirect(url_for('upload_file', context={"Status":"Successfully uploaded"}))
    return render_template("file upload.html", context=context)

@app.route("/add_post", methods=["GET", "POST"])
def add(context=None):
    if request.method == "POST":
        image = request.files['image_to_upload']

        title = request.form['title']
        text_post = request.form['info_post']
        mood = request.form['mood']
        
        try:
            image.save(f"static/files/{session['username']}/{secure_filename(image.filename)}")
        except FileNotFoundError:
            os.mkdir(f"static/files/{session['username']}")
            image.save(f"static/files/{session['username']}/{secure_filename(image.filename)}")
        post = Post(title = title, post_media_name = secure_filename(image.filename), post_username = session['username'], text_about = text_post, mood = mood, post_author = session['uid'])
        crud.add_post(post)

        user = db.session.query(User).filter_by(login=session['username']).first()
        return redirect(url_for("user_page", user_id=user.user_id))
    return render_template("add_post.html", context=context)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(host='192.168.131.66', port=2000)


