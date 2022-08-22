from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth
from models import User


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
        user_data = resp.json()
        if user_data:
            if User.query.filter_by(username=user_data['screen_name'], platform="Twitter").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=user_data['screen_name'], name=user_data["name"],
                                   platform="Twitter")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data

        return redirect('/')


