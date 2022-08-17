from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth


class GoogleHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


class GoogleLogin(Resource):
    def get(self):
        redirect_uri = url_for('google.auth', _external=True)
        oauth = get_oauth()
        return oauth.google.authorize_redirect(redirect_uri)


class GoogleAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.google.authorize_access_token()
        user = token.get('userinfo')
        if user:
            session['user'] = user
        return redirect('/')


class GoogleLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
