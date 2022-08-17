from flask_restful import Resource
from flask import session, url_for, redirect, request
from app import get_oauth


class TwitterHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


class TwitterLogin(Resource):
    def get(self):
        redirect_uri = url_for('twitter.auth', _external=True)
        oauth = get_oauth()
        return oauth.twitter.authorize_redirect(redirect_uri)


class TwitterAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.twitter.authorize_access_token()
        url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

        resp = oauth.twitter.get(
            url, params={'skip_status': True, 'include_email': True})
        user = resp.json()
        print("userrrrrrrrrrrrrrrrr", user)
        if user:
            session['user'] = user
        return redirect('/')


class TwitterLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')


