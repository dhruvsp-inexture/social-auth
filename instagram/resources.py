from authlib.integrations.flask_client import OAuth
from flask_restful import Resource
from flask import session, url_for, redirect, current_app
from models import User

instagram_oauth = OAuth(current_app)
instagram_oauth.register(
        name='instagram',
        api_base_url='https://api.instagram.com',
        access_token_url='https://api.instagram.com/oauth/access_token',
        authorize_url='https://api.instagram.com/oauth/authorize',
        client_kwargs={
            'response_type': 'code',
            'token_endpoint_auth_method': 'client_secret_post',
            'scope': 'user_profile user_media'
        },
    )


class InstagramLogin(Resource):
    def get(self):
        redirect_uri = url_for('instagram.auth', _external=True)
        oauth = instagram_oauth

        redirect_uri = "https://0a71-115-246-26-54.in.ngrok.io/instagram/auth"
        return oauth.instagram.authorize_redirect(redirect_uri)


class InstagramAuth(Resource):
    def get(self):
        oauth = instagram_oauth
        token = oauth.instagram.authorize_access_token()
        id_url = 'https://graph.instagram.com/v14.0/me'
        resp_id = oauth.instagram.get(id_url)
        user_id = resp_id.json()
        url = f"https://graph.instagram.com/{user_id['id']}?fields=id,account_type,username,media_count"
        resp = oauth.instagram.get(url)
        user_data = resp.json()
        media_url = f"https://graph.instagram.com/v14.0/{user_id['id']}/media?fields=id,caption,media_type,media_url,permalink, thumbnail_url, timestamp, username"
        media_resp = oauth.instagram.get(media_url)
        media = media_resp.json()
        user_data["media_details"] = media
        print(user_data)
        if user_data:
            if User.query.filter_by(username=user_data['username'],
                                    platform="Instagram").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=user_data['username'],
                                   name=None,
                                   platform="Instagram")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data
        return redirect('/')

