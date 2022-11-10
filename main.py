from flask_app import *
from flask import render_template
from flask import request, session, redirect, url_for
from werkzeug.utils import secure_filename
import hashlib
import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.VARCHAR(255), unique = True, nullable = False)
    email = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(255), nullable = False)
    user_posts = db.relationship("Posts", back_populates = "owner", cascade = "all, delete-orphan")

class Posts(db.Model):
    __tablename__ = "Posts"
    post_id = db.Column(db.Integer, primary_key = True)
    post_username = db.Column(db.VARCHAR(255), db.ForeignKey("User.username"), nullable = False)
    post_text = db.Column(db.VARCHAR(255))
    post_media_name = db.Column(db.VARCHAR(255))
    owner = db.relationship("User", back_populates = "user_posts")

def addUser(user:User) -> None:
    db.session.add(user)
    db.session.commit()

def addPost(post:Posts) -> None:
    db.session.add(post)
    db.session.commit()

def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

@app.route("/home")
def home(context = None):
    posts = Posts.query.all()
    return render_template("base.html", posts = posts[::-1])

@app.route("/")
def index(context=None):
    return render_template("base.html", context=None)

@app.route("/user/<int:user_id>")
def user_page(user_id, context=None):
    query = db.session.query(User).join(Project).filter(Project.pr_author == user_id).first()
    if query:
        return render_template("user page.html", context=query)
    else:
        query = db.session.query(User).filter(User.user_id == user_id).first()
        return render_template("user page.html", context=query)

@app.route('/register', methods = ["GET", "POST"])
def register(context=None):
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user = db.session.query(User).filter_by(username = username).first()
        if user:
            return redirect(url_for("register", context = "Already registered!"))
        elif password != confirm_password:
            return redirect(url_for("register", context = "Passwords don't match!"))
        addUser(User(username = username, email = email, password = hash_password(password)))
        return redirect(url_for("login", context = "Succesfully registered"))
    return render_template("register.html", context = None)

@app.route("/login", methods = ["GET", "POST"])
def login(context=None):
    if request.method == "POST":
        user = db.session.query(User).filter_by(username = request.form['username'], password = hash_password(request.form['password'])).first()
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['username'] = user.username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", context="Username or password is wrong. Try again.")
    return render_template("login.html", context=context)

@app.route("/logout")
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/post_upload", methods = ["GET", "POST"])
def post_upload(context = None):
    if request.method == "POST":
        caption = request.form["caption"]
        image = request.files["image_to_upload"]
        try:
            image.save(f"static/files/{session['username']}/{secure_filename(image.filename)}")
        except FileNotFoundError:
            os.mkdir(f"static/files/{session['username']}")
            image.save(f"static/files/{session['username']}/{secure_filename(image.filename)}")
        post = Posts(post_username = session['username'], post_text = caption, post_media_name = secure_filename(image.filename))
        db.session.add(post)
        db.session.commit()
        return render_template("post_upload.html", context = "Post succesfully uploaded!")
    return render_template("post_upload.html", context = None) 

@app.route("/upload", methods=["GET", "POST"])
def upload_file(context=None):
    if request.method=="POST":
        f = request.files["file_to_save"]
        f.save(f"static/img/{secure_filename(f.filename)}")
        return redirect(url_for('upload_file', context={"Status":"Successfully uploaded"}))
    return render_template("file upload.html", context=context)


@app.route("/add_project", methods=["GET", "POST"])
def add(context=None):
    if request.method == "POST":
        title = request.form['title']
        info_pr = request.form['info_pr']
        data = db.session.query(Project).filter_by(title=request.form['title']).first()
        
        print(data)

        if data :
            return redirect(url_for("add", error="Project Add"))
        else:
            
            crud.add_user(Project(title=title, 
                                text_about=info_pr,
                                pr_author=session['uid']
                                ))
            return redirect(url_for("profile", context="Succesfully registered!"))
    return render_template("add_pr.html", context=context)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run()


