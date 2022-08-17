from flask import Blueprint
from linkedin.resources import LinkedinHome, LinkedinLogin, LinkedinAuth, LinkedinLogout

linkedin = Blueprint("linkedin", __name__)
linkedin.add_url_rule("/", view_func=LinkedinHome.as_view("home"))
linkedin.add_url_rule("/linkedin/login", view_func=LinkedinLogin.as_view("login"))
linkedin.add_url_rule("/linkedin/auth", view_func=LinkedinAuth.as_view("auth"))
linkedin.add_url_rule("/linkedin/logout", view_func=LinkedinLogout.as_view("logout"))
