from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth


class GithubHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


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
        user = resp.json()
        if user:
            session['user'] = user
        return redirect('/')


class GithubLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
