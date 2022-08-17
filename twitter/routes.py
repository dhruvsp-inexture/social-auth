from flask import Blueprint
from twitter.resources import TwitterHome, TwitterLogin, TwitterAuth, TwitterLogout

twitter = Blueprint("twitter", __name__)
twitter.add_url_rule("/twitter", view_func=TwitterHome.as_view("home"))
twitter.add_url_rule("/twitter/login", view_func=TwitterLogin.as_view("login"))
twitter.add_url_rule("/twitter/auth", view_func=TwitterAuth.as_view("auth"))
twitter.add_url_rule("/twitter/logout", view_func=TwitterLogout.as_view("logout"))
