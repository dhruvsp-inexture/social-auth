from flask import Blueprint
from google.resources import GoogleHome, GoogleLogin, GoogleAuth, GoogleLogout

google = Blueprint("google", __name__)
google.add_url_rule("/", view_func=GoogleHome.as_view("home"))
google.add_url_rule("/google/login", view_func=GoogleLogin.as_view("login"))
google.add_url_rule("/google/auth", view_func=GoogleAuth.as_view("auth"))
google.add_url_rule("/google/logout", view_func=GoogleLogout.as_view("logout"))
