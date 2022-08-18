from flask import Blueprint
from instagram.resources import InstagramHome, InstagramLogin, InstagramAuth, InstagramLogout

instagram = Blueprint("instagram", __name__)
instagram.add_url_rule("/", view_func=InstagramHome.as_view("home"))
instagram.add_url_rule("/instagram/login", view_func=InstagramLogin.as_view("login"))
instagram.add_url_rule("/instagram/auth", view_func=InstagramAuth.as_view("auth"))
instagram.add_url_rule("/instagram/logout", view_func=InstagramLogout.as_view("logout"))
