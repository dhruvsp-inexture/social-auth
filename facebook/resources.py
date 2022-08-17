from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth


class FacebookHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


class FacebookLogin(Resource):
    def get(self):
        redirect_uri = url_for('facebook.auth', _external=True)
        oauth = get_oauth()
        return oauth.facebook.authorize_redirect(redirect_uri)


class FacebookAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.facebook.authorize_access_token()
        resp = oauth.facebook.get(
            'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
        user = resp.json()
        if user:
            session['user'] = user
        return redirect('/')


class FacebookLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
