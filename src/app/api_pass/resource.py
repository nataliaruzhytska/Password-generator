import json
import hashlib
from flask import request, jsonify, session
from flask_restful import Resource, marshal_with
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from api_pass.utils import random_chars
from db_pass import db, User, StoredPass, password_fields
from config import CHECK_PASS_API


class PasswordResourse(Resource):

    def post(self):
        """
        Homepage with link to generate password
        """
        n = request.form.get('n') or '12'
        uppercase = request.form.get('uppercase')
        symbol = request.form.get('symbol')
        digit = request.form.get('digit')
        if int(n) < 6 or int(n) > 16:
            return 'Your password length is wrong', 404
        return random_chars(n, uppercase, symbol, digit)


class PasswordSave(Resource):

    @marshal_with(password_fields)
    def get(self):
        if session["logged_in"]:
            try:
                user_id = int(session["user_id"])
                password = StoredPass.query.filter_by(user_id=user_id).all()
                user = User.query.get(user_id)
                return password, 200
            except:
                return f"There is no passwords in our system for user {user.username}", 401
        else:
            return "You are not logged in", 401

    def post(self):
        data = json.loads(request.data)
        if session["logged_in"]:
            password = data.get("password")
            user_id = int(session["user_id"])
            try:
                new_pass = StoredPass(password=password, user_id=user_id)
                db.session.add(new_pass)
                db.session.commit()
                return 'Password saved successfully', 201
            except:
                return 'An error occurred saving the password to the database', 500
        else:
            return "You are not logged in", 401

    def delete(self, password_id):
        if session["logged_in"]:
            try:
                password = StoredPass.query.get(password_id)
                db.session.delete(password)
                db.session.commit()
                return f"Successfully deleted the password {password.password}", 200
            except:
                return 'An error occurred deleting the password from the database', 500
        else:
            return "You are not logged in", 401


class Login(Resource):
    def post(self):
        """
        Add to session new value logged_in = True and return success msg
        if user registered and put correct login and password
        :return: str
        """
        data = json.loads(request.data)
        name = data.get("username")
        password = data.get('password')
        user = User.query.filter_by(username=name).first()
        if not user:
            return "There is no users in our system, please register", 401

        if name == user.username and check_password_hash(user.password, password):
            session["logged_in"] = True
            session["user_id"] = user.id
            return "You are successfully logged in", 200
        else:
            return "Wrong login or password", 403


class Logout(Resource):
    def get(self):
        """
        Change logged_in session value to False, which means that our decorator
        won't give access to see the page content from views where is it set.
        :return: str
        """
        session["logged_in"] = False
        session["user_id"] = None
        return "You are successfully logged out"


class Registration(Resource):
    def post(self):
        """
        Add new user
        :return:
        """
        data = json.loads(request.data)
        try:
            new_user = User(username=data.get('username'),
                            password=generate_password_hash(data.get('password')))
            db.session.add(new_user)
            db.session.commit()
            return 'User registered successfully', 201
        except:
            return 'An error occurred saving the user to the database', 500


class CheckPass(Resource):
    def get(self, password_id):
        password = StoredPass.query.get(password_id)
        check_pass = (hashlib.sha1(b'{password.password}')).hexdigest()[:5].upper()
        hash_pass = (hashlib.sha1(b'{password.password}')).hexdigest()[5:].upper()
        resp = requests.get(f'{CHECK_PASS_API}{check_pass}', )
        if resp.status_code != 200:
            return "An error occurred", resp.status_code
        else:
            data = resp.text.split()
            for i in data:
                if i[:35] == hash_pass:
                    return f" {i[36:]} matches found for your password's hash in the database", 200
            else:
                return "Your password was not found in our system", 200
