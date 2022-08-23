from authlib.integrations.flask_client import OAuth
from flask_restful import Resource
from flask import session, url_for, redirect, current_app
from models import User

github_oauth = OAuth(current_app)
github_oauth.register(
    name='github',
    api_base_url='https://api.github.com/',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    client_kwargs={'scope': 'user:email'},
    userinfo_endpoint='https://api.github.com/user',
)


class GithubLogin(Resource):
    def get(self):
        redirect_uri = url_for('github.auth', _external=True)
        oauth = github_oauth
        return oauth.github.authorize_redirect(redirect_uri)


class GithubAuth(Resource):
    def get(self):
        oauth = github_oauth
        token = oauth.github.authorize_access_token()
        resp = oauth.github.get('https://api.github.com/user')
        user_data = resp.json()
        if user_data:
            username = user_data["email"] or user_data["login"]
            if User.query.filter_by(username=username, platform="Github").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=username, name=user_data["name"],
                                   platform="Github")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data
        return redirect('/')
