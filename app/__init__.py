from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# database instance
# global (db) but will be initialized with app in create_app

db = SQLAlchemy()


def create_app():
    """Factory pattern for creating Flask app"""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # import and register blueprints
    from .auth import auth_bp
    from .main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app
