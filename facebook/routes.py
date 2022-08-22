from flask import Blueprint
from facebook.resources import FacebookLogin, FacebookAuth

facebook = Blueprint("facebook", __name__)

facebook.add_url_rule("/facebook/login", view_func=FacebookLogin.as_view("login"))
facebook.add_url_rule("/facebook/auth", view_func=FacebookAuth.as_view("auth"))
