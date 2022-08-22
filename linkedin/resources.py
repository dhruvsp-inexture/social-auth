from flask_restful import Resource
from flask import session, url_for, redirect
from app import get_oauth
from models import User


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
        user_data = resp.json()
        user_data["email_details"] = email_user

        if user_data:
            if User.query.filter_by(username=user_data['email_details']['elements'][0]['handle~']['emailAddress'],
                                    platform="Linkedin").first():
                session['message'] = "Data already exists"
            else:

                user_object = User(username=user_data['email_details']['elements'][0]['handle~']['emailAddress'],
                                   name=f'{user_data["localizedFirstName"]} {user_data["localizedLastName"]}',
                                   platform="Linkedin")
                session['message'] = 'Data registered successfully'
                user_object.save_to_db()
            session['user'] = user_data

        return redirect('/')

