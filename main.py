from flask_app import *
from flask import render_template
from flask import request, session, redirect, url_for
from werkzeug.utils import secure_filename




@app.route("/home")
@app.route("/")
def home(context=None):
    data = {"Data":"Some data here to be sent as dict (JSON)"}
    return render_template("base.html", context=None)


@app.route("/user/<int:user_id>")
def user_page(user_id, context=None):
    query = db.session.query(User).join(Project).filter(Project.pr_author == user_id).first()
    if query:
        return render_template("user page.html", context=query)
    else:
        query = db.session.query(User).filter(User.user_id == user_id).first()
        return render_template("user page.html", context=query)

@app.route("/login", methods = ["GET", "POST"])
def login(context=None):
    if request.method == "POST":
        user = db.session.query(User).filter_by(login=request.form['username'], password=request.form['password']).first()
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
        fname = request.form['fname']
        sname = request.form['sname']
        pass1 = request.form['password']
        pass2 = request.form['password_conf']
        email = request.form['email']
        mobile = request.form['mobile']
        d_of_b = request.form['d_of_b']
        loc = request.form['loc']
        info = request.form['info']
        data = db.session.query(User).filter_by(login=request.form['username']).first()
        
        print(data)

        if data :
            return redirect(url_for("register", error="Already registered!"))
        elif pass1!=pass2:
            return redirect(url_for("register", error="Passowords do not match!"))
        else:
            crud.add_user(User(login=login, 
                                user_fname=fname,
                                user_sname=sname,
                                password=pass1, 
                                email=email,
                                mobile=mobile,
                                d_of_b=d_of_b,
                                loc=loc,
                                info=info
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
        app.run(port=2000)


