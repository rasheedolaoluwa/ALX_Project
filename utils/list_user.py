import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models.models import User

def list_users():
    users = User.query.all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Email Verified: {user.email_verified}")

if __name__ == '__main__':
    with app.app_context():
        list_users()