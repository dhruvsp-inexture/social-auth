from flask_restful import Resource
from flask import session, redirect


class Home(Resource):
    def get(self):
        user_json = None
        if session.get('user') and session.get('message'):
            user_json = {"data": session["user"], "message": session["message"]}
        return user_json or {'message': 'please login to view profile'}


class Logout(Resource):
    def get(self):
        session.pop('user', None)
        return redirect('/')
