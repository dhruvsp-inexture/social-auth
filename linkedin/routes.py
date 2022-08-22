from flask import Blueprint
from linkedin.resources import LinkedinLogin, LinkedinAuth

linkedin = Blueprint("linkedin", __name__)
linkedin.add_url_rule("/linkedin/login", view_func=LinkedinLogin.as_view("login"))
linkedin.add_url_rule("/linkedin/auth", view_func=LinkedinAuth.as_view("auth"))
