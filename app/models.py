from app import db
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

# an ORM model class, also correspond to a table named user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(16), default="user")  # user, admin, etc.

    notes = db.relationship('Note', backref='user', lazy=True)  # all notes of the user

    def set_password(self, raw_password):  # PBKDF2 salted algorithm: default SHA256
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):  # just return True or False
        return check_password_hash(self.password_hash, raw_password)

    def __repr__(self):  # Magic Method, defines what you see when print the object, like: <User Deck>
        return f"<User {self.username}>"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)  # generated from GPT api
    tags = db.Column(db.String(256))  # comma-separated tags
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # lambda is a anonymous function, executed every time it's called

    def __repr__(self):
        return f"<Note {self.title}>"
