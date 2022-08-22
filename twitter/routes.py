from flask import Blueprint
from twitter.resources import TwitterLogin, TwitterAuth

twitter = Blueprint("twitter", __name__)
twitter.add_url_rule("/twitter/login", view_func=TwitterLogin.as_view("login"))
twitter.add_url_rule("/twitter/auth", view_func=TwitterAuth.as_view("auth"))
