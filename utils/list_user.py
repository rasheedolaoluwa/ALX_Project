# utils/list_users.py
import sys
import os

# Add the project directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models.models import db, User

with app.app_context():
    users = User.query.all()
    if users:
        for user in users:
            print(f"Username: {user.username}, Email: {user.email}, Email Verified: {user.email_verified}")
    else:
        print("No users found.")