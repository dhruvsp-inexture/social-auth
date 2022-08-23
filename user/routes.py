from flask import Blueprint
from user.resources import Home, Logout

user_blueprint = Blueprint("user_blueprint", __name__)
user_blueprint.add_url_rule("/", view_func=Home.as_view("home"))
user_blueprint.add_url_rule("/logout", view_func=Logout.as_view("logout"))
