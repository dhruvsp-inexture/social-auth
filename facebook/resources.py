from authlib.integrations.flask_client import OAuth
from flask_restful import Resource
from flask import session, url_for, redirect, current_app
from models import User

facebook_oauth = OAuth(current_app)
facebook_oauth.register(
        name='facebook',
        api_base_url='https://graph.facebook.com/v7.0/',
        access_token_url='https://graph.facebook.com/v7.0/oauth/access_token',
        authorize_url='https://www.facebook.com/v7.0/dialog/oauth',
        client_kwargs={'scope': 'email public_profile'}
    )


class FacebookLogin(Resource):
    def get(self):
        redirect_uri = url_for('facebook.auth', _external=True)
        oauth = facebook_oauth

        return oauth.facebook.authorize_redirect(redirect_uri)


class FacebookAuth(Resource):
    def get(self):
        oauth = facebook_oauth
        token = oauth.facebook.authorize_access_token()
        resp = oauth.facebook.get(
            'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
        user_data = resp.json()
        if user_data:
            if User.query.filter_by(username=user_data["email"], platform="Facebook").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=user_data["email"], name=user_data["name"],
                                   platform="Facebook")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data
        return redirect('/')

