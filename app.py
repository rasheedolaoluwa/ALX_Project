from flask import Flask, render_template
from config.config import Config
from models.models import db, User
from flask_login import LoginManager
from flask_migrate import Migrate
from routes.profile import profile
from routes.auth import auth

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except ValueError:
        return None

app.register_blueprint(profile)
app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)