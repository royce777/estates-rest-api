from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database import db
from estates import Estate
from estates import Search
from auth import Login
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'  # Ensure the path is set correctly
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # For simplicity, disable CSRF protection
app.config['JWT_COOKIE_SECURE'] = False  # Only allow JWT cookies over https

api = Api(app)
jwt = JWTManager(app)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])


db.init_app(app)

api.add_resource(Estate, "/estates/<int:estate_id>")
api.add_resource(Search, "/search")
api.add_resource(Login, "/login")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
