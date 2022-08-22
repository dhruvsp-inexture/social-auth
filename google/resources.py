from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth
from models import User


class GoogleLogin(Resource):
    def get(self):
        redirect_uri = url_for('google.auth', _external=True)
        oauth = get_oauth()
        return oauth.google.authorize_redirect(redirect_uri)


class GoogleAuth(Resource):
    def get(self):
        oauth = get_oauth()
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
