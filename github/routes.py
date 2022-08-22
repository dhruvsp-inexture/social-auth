from flask import Blueprint
from github.resources import GithubLogin, GithubAuth

github = Blueprint("github", __name__)
github.add_url_rule("/github/login", view_func=GithubLogin.as_view("login"))
github.add_url_rule("/github/auth", view_func=GithubAuth.as_view("auth"))
