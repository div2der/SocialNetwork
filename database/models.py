from flask_app import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True) # integer primary key will be autoincremented by default
    login = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    posts = db.relationship("Post", back_populates = "author", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.first_name!r}, surname={self.second_name!r})"


class Post(db.Model):
    __tablename__ = "post"
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text_about = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(20))
    post_author = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    author = db.relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return super().__repr__()

