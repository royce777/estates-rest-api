from flask_restful import Resource
from flask import make_response, request, jsonify
from flask_jwt_extended import create_access_token
from users import User
from werkzeug.security import check_password_hash

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        print("[Login] : login request received for user: ", username)

        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            print("[Login] : An error occurred querying the database: ", e)
            response = make_response(jsonify({'message': 'An error occurred querying the database'}))
            response.status_code = 401
            return response

        if not user or not check_password_hash(user.password, password):
            response = make_response(jsonify({'message': 'Wrong credentials'}))
            response.status_code = 401
            return response

        access_token = create_access_token(identity=username)
        response = make_response()
        response.set_cookie('access_token_cookie', access_token, httponly=True)
        response.status_code = 200
        return response 