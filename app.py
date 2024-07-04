from flask import Flask, render_template
from config.config import Config
from models.models import db, User
from flask_login import LoginManager
from flask_migrate import Migrate
from extensions import mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app, db)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from routes.profile import profile as profile_blueprint
    from routes.auth import auth as auth_blueprint
    from routes.recommendations import recommendations as recommendations_blueprint

    app.register_blueprint(profile_blueprint, url_prefix='/profile')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(recommendations_blueprint, url_prefix='/recommendations')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)