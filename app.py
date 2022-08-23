from flask import Flask
from authlib.integrations.flask_client import OAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    import models
    Migrate(app, db)

    from google.routes import google
    from facebook.routes import facebook
    from twitter.routes import twitter
    from github.routes import github
    from linkedin.routes import linkedin
    from instagram.routes import instagram
    from user.routes import user_blueprint
    app.register_blueprint(google)
    app.register_blueprint(facebook)
    app.register_blueprint(twitter)
    app.register_blueprint(github)
    app.register_blueprint(linkedin)
    app.register_blueprint(instagram)
    app.register_blueprint(user_blueprint)
    return app


# def get_oauth():
    # app = create_app()
    # GOOGLE_CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    # FACEBOOK_CONF_URL = 'https://www.facebook.com/.well-known/openid-configuration'
    # oauth = OAuth(app)
    # oauth.register(
    #     name='google',
    #     server_metadata_url=GOOGLE_CONF_URL,
    #     client_kwargs={
    #         'scope': 'openid email profile'
    #     }
    # )
    # oauth.register(
    #     name='facebook',
    #     api_base_url='https://graph.facebook.com/v7.0/',
    #     access_token_url='https://graph.facebook.com/v7.0/oauth/access_token',
    #     authorize_url='https://www.facebook.com/v7.0/dialog/oauth',
    #     client_kwargs={'scope': 'email public_profile'}
    # )

    # oauth.register(
    #     name='twitter',
    #     api_base_url='https://api.twitter.com/1.1/',
    #     request_token_url='https://api.twitter.com/oauth/request_token',
    #     access_token_url='https://api.twitter.com/oauth/access_token',
    #     authorize_url='https://api.twitter.com/oauth/authenticate',
    # )

    # oauth.register(
    #     name='github',
    #     api_base_url='https://api.github.com/',
    #     access_token_url='https://github.com/login/oauth/access_token',
    #     authorize_url='https://github.com/login/oauth/authorize',
    #     client_kwargs={'scope': 'user:email'},
    #     userinfo_endpoint='https://api.github.com/user',
    # )

    # oauth.register(
    #     name='linkedin',
    #     access_token_url='https://www.linkedin.com/oauth/v2/accessToken',
    #     authorize_url='https://www.linkedin.com/oauth/v2/authorization',
    #     client_kwargs={'scope': 'r_liteprofile r_emailaddress'},
    # )

    # oauth.register(
    #     name='instagram',
    #     api_base_url='https://api.instagram.com',
    #     access_token_url='https://api.instagram.com/oauth/access_token',
    #     authorize_url='https://api.instagram.com/oauth/authorize',
    #     client_kwargs={
    #         'response_type': 'code',
    #         'token_endpoint_auth_method': 'client_secret_post',
    #         'scope': 'user_profile user_media'
    #     },
    # )

    # return oauth


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
