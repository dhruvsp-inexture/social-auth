from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth


class InstagramHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


class InstagramLogin(Resource):
    def get(self):
        redirect_uri = url_for('instagram.auth', _external=True)
        oauth = get_oauth()

        redirect_uri = "https://24b0-115-246-26-54.in.ngrok.io/instagram/auth"
        print(redirect_uri)
        return oauth.instagram.authorize_redirect(redirect_uri)


class InstagramAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.instagram.authorize_access_token()
        id_url = 'https://graph.instagram.com/v14.0/me'
        resp_id = oauth.instagram.get(id_url)
        user_id = resp_id.json()
        url = f"https://graph.instagram.com/{user_id['id']}?fields=id,account_type,username,media_count"
        resp = oauth.instagram.get(url)
        user = resp.json()
        media_url = f"https://graph.instagram.com/v14.0/{user_id['id']}/media?fields=id,caption,media_type,media_url,permalink, thumbnail_url, timestamp, username"
        media_resp = oauth.instagram.get(media_url)
        media = media_resp.json()
        user["media_details"] = media
        if user:
            session['user'] = user
        return redirect('/')


class InstagramLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
