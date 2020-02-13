from flask_migrate import Migrate
from flask_restful import fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


class StoredPass(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)


password_fields = {'password': fields.String,
                   'user_id': fields.Integer}