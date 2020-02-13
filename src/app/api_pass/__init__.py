from flask import Blueprint
from flask_restful import Api

from api_pass.resource import Login, Logout, Registration, PasswordResourse, PasswordSave, CheckPass

pass_bp = Blueprint('password', __name__)
save_pass_bp = Blueprint('password_save', __name__)
auth_bp = Blueprint("auth", __name__)
check_pass_bp = Blueprint("check_pass", __name__)

pass_api = Api(pass_bp)
api_auth = Api(auth_bp)
save_pass_api = Api(save_pass_bp)
check_pass_api = Api(check_pass_bp)

api_auth.add_resource(Login, "/login")
api_auth.add_resource(Logout, "/logout")
api_auth.add_resource(Registration, "/register")
pass_api.add_resource(PasswordResourse, "/")
save_pass_api.add_resource(PasswordSave, "/save", "/save/<int:password_id>")
check_pass_api.add_resource(CheckPass, "/check/<int:password_id>")


