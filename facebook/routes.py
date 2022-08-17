from flask import Blueprint
from facebook.resources import FacebookHome, FacebookLogin, FacebookAuth, FacebookLogout

facebook = Blueprint("facebook", __name__)

facebook.add_url_rule("/facebook", view_func=FacebookHome.as_view("home"))
facebook.add_url_rule("/facebook/login", view_func=FacebookLogin.as_view("login"))
facebook.add_url_rule("/facebook/auth", view_func=FacebookAuth.as_view("auth"))
facebook.add_url_rule("/facebook/logout", view_func=FacebookLogout.as_view("logout"))