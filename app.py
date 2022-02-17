from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database import db 
from estates import Estate

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api.add_resource(Estate, "/estates/<int:estate_id>")



if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True)
