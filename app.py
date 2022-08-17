from flask import Flask, session
from authlib.integrations.flask_client import OAuth

from config import FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    from google.routes import google
    from facebook.routes import facebook
    from twitter.routes import twitter
    from github.routes import github
    from linkedin.routes import linkedin
    app.register_blueprint(google)
    app.register_blueprint(facebook)
    app.register_blueprint(twitter)
    app.register_blueprint(github)
    app.register_blueprint(linkedin)
    return app


def get_oauth():
    app = create_app()
    GOOGLE_CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    FACEBOOK_CONF_URL = 'https://www.facebook.com/.well-known/openid-configuration'
    oauth = OAuth(app)
    oauth.register(
        name='google',
        server_metadata_url=GOOGLE_CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    oauth.register(
        name='facebook',
        api_base_url='https://graph.facebook.com/v7.0/',
        access_token_url='https://graph.facebook.com/v7.0/oauth/access_token',
        authorize_url='https://www.facebook.com/v7.0/dialog/oauth',
        client_kwargs={'scope': 'email public_profile'}
    )

    oauth.register(
        name='twitter',
        # api_base_url='https://api.twitter.com/1.1/',
        # request_token_url='https://api.twitter.com/oauth/request_token',
        # access_token_url='https://api.twitter.com/oauth/access_token',
        # authorize_url='https://api.twitter.com/oauth/authenticate',
        # fetch_token=lambda: session.get('token'),  # DON'T DO IT IN PRODUCTION
        api_base_url='https://api.twitter.com/1.1/',
        request_token_url='https://api.twitter.com/oauth/request_token',
        access_token_url='https://api.twitter.com/oauth/access_token',
        authorize_url='https://api.twitter.com/oauth/authenticate',
    )

    oauth.register(
        name='github',
        api_base_url='https://api.github.com/',
        access_token_url='https://github.com/login/oauth/access_token',
        authorize_url='https://github.com/login/oauth/authorize',
        client_kwargs={'scope': 'user:email'},
        userinfo_endpoint='https://api.github.com/user',
    )

    oauth.register(
        name='linkedin',
        access_token_url='https://www.linkedin.com/oauth/v2/accessToken',
        authorize_url='https://www.linkedin.com/oauth/v2/authorization',
        client_kwargs={'scope': 'r_liteprofile r_emailaddress'},
    )

    return oauth


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
