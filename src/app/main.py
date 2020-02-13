from flask import Flask
from config import get_config
from db_pass import db, migrate
from api_pass import pass_bp, auth_bp, save_pass_bp, check_pass_bp


def create_app():
    """
    Create Flask-application
    :return: app
    """
    app = Flask(__name__)
    app.config.from_object(get_config(env='DEV'))
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(pass_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(save_pass_bp)
    app.register_blueprint(check_pass_bp)
    db.create_all(app=app)
    return app
