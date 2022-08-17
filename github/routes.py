from flask import Blueprint
from github.resources import GithubHome, GithubLogin, GithubAuth, GithubLogout

github = Blueprint("github", __name__)
github.add_url_rule("/github", view_func=GithubHome.as_view("home"))
github.add_url_rule("/github/login", view_func=GithubLogin.as_view("login"))
github.add_url_rule("/github/auth", view_func=GithubAuth.as_view("auth"))
github.add_url_rule("/github/logout", view_func=GithubLogout.as_view("logout"))