from authlib.integrations.flask_client import OAuth
from flask_restful import Resource
from flask import session, url_for, redirect, current_app
from models import User

GOOGLE_CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
FACEBOOK_CONF_URL = 'https://www.facebook.com/.well-known/openid-configuration'
google_oauth = OAuth(current_app)
google_oauth.register(
    name='google',
    server_metadata_url=GOOGLE_CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


class GoogleLogin(Resource):
    def get(self):
        redirect_uri = url_for('google.auth', _external=True)
        oauth = google_oauth
        return oauth.google.authorize_redirect(redirect_uri)


class GoogleAuth(Resource):
    def get(self):
        oauth = google_oauth
        token = oauth.google.authorize_access_token()
        user_data = token.get('userinfo')

        if user_data:
            if User.query.filter_by(username=user_data["email"], platform="Google").first():
                session['message'] = "Data already exists"
            else:
                user_object = User(username=user_data["email"], name=user_data["name"], platform="Google")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data

        return redirect('/')
