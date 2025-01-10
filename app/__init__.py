from flask import Flask
import psycopg2
from .extentions import db, migrate, login_manager
from .config import Config
from .routes.user import user
from .routes.journal import journal
from .routes.auto_personnel import auto_personnel
from .routes.routes import routes
from .routes.auto import auto
from .routes.main import main
from .routes.excel import excel


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(journal)
    app.register_blueprint(auto_personnel)
    app.register_blueprint(routes)
    app.register_blueprint(auto)
    app.register_blueprint(main)
    app.register_blueprint(excel)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # LOGIN MANAGER
    login_manager.login_view = 'user.login'
    login_manager.login_message = "Please login to see more"

    with app.app_context():
        db.create_all()

    return app
