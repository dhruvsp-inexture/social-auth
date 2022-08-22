from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth
from models import User


class GithubLogin(Resource):
    def get(self):
        redirect_uri = url_for('github.auth', _external=True)
        oauth = get_oauth()
        return oauth.github.authorize_redirect(redirect_uri)


class GithubAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.github.authorize_access_token()
        resp = oauth.github.get('https://api.github.com/user')
        user_data = resp.json()
        if user_data:
            if not user_data["email"]:
                username = user_data["login"]
            else:
                username = user_data["email"]
            if User.query.filter_by(username=username, platform="Github").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=username, name=user_data["name"],
                                   platform="Github")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data
        return redirect('/')

