from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth


class LinkedinHome(Resource):
    def get(self):
        user = session.get('user')
        return user or {'message': 'please login to view profile'}


class LinkedinLogin(Resource):
    def get(self):
        redirect_uri = url_for('linkedin.auth', _external=True)
        oauth = get_oauth()
        return oauth.linkedin.authorize_redirect(redirect_uri)


class LinkedinAuth(Resource):
    def get(self):
        oauth = get_oauth()
        token = oauth.linkedin.authorize_access_token()
        email_url = 'https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))'
        email_resp = oauth.linkedin.get(email_url)
        email_user = email_resp.json()
        url = 'https://api.linkedin.com/v2/me'
        resp = oauth.linkedin.get(url)
        user = resp.json()
        user["email_details"] = email_user
        print("tokennnnnnnnnnnn", user)
        if user:
            session['user'] = user
        return redirect('/')


class LinkedinLogout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
