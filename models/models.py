from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='portfolios')
    total_value = db.Column(db.Float, nullable=False, default=0.0)

    def __repr__(self):
        return f'<Portfolio {self.id} - User {self.user_id}>'

class PortfolioInvestment(db.Model):
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), primary_key=True)
    investment_id = db.Column(db.String, primary_key=True)
    quantity = db.Column(db.Float, nullable=False)
    current_value = db.Column(db.Float, nullable=False)

    portfolio = db.relationship('Portfolio', back_populates='investments')

    def __repr__(self):
        return f'<PortfolioInvestment {self.portfolio_id} - Investment {self.investment_id}>'

User.portfolios = db.relationship('Portfolio', order_by=Portfolio.id, back_populates='user')
Portfolio.investments = db.relationship('PortfolioInvestment', order_by=PortfolioInvestment.investment_id, back_populates='portfolio')