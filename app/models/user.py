from uuid import uuid4
from datetime import datetime
from ..lib.ext import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid4().hex)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def json():
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at.timestamp()
        }
