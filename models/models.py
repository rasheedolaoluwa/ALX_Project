from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    email_verified = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id})

    @staticmethod
    def verify_confirmation_token(token, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expiration)
        except:
            return None
        return User.query.get(data['confirm'])

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    life_stage_score = db.Column(db.Integer)
    financial_resources_score = db.Column(db.Integer)
    investment_experience_score = db.Column(db.Integer)
    emotional_risk_tolerance_score = db.Column(db.Integer)
    total_score = db.Column(db.Integer)
    risk_category = db.Column(db.String(64))
    life_stage_message = db.Column(db.String(256))
    financial_resources_message = db.Column(db.String(256))
    investment_experience_message = db.Column(db.String(256))
    emotional_risk_tolerance_message = db.Column(db.String(256))