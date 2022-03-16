from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from database import db
from estates import Estate
from estates import Search

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

api.add_resource(Estate, "/estates/<int:estate_id>")
api.add_resource(Search, "/search")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
