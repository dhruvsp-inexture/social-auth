from flask import Blueprint
from instagram.resources import InstagramLogin, InstagramAuth

instagram = Blueprint("instagram", __name__)
instagram.add_url_rule("/instagram/login", view_func=InstagramLogin.as_view("login"))
instagram.add_url_rule("/instagram/auth", view_func=InstagramAuth.as_view("auth"))
