from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from users import User
from werkzeug.security import generate_password_hash, check_password_hash

class Login(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, generate_password_hash(password)):
            return jsonify({'message': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200