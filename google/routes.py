from flask import Blueprint
from google.resources import GoogleLogin, GoogleAuth

google = Blueprint("google", __name__)
google.add_url_rule("/google/login", view_func=GoogleLogin.as_view("login"))
google.add_url_rule("/google/auth", view_func=GoogleAuth.as_view("auth"))
