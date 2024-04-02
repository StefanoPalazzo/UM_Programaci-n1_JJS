from flask_restful import Resource
from flask import request


class Login(Resource):
    def post(self):
        logdata = request.get_json()

        # Get the email and password from the data
        email = logdata.get('email')
        password = logdata.get('password')
        if email == 'admin' and password == 'admin':
            return {'message': 'Successfully logged as an Admin'}, 200
        return {'message': 'Invalid credentials'}, 401