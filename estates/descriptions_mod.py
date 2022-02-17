from database import db 
from estates import EstateModel

class Descriptions(db.Model):
    __tablename__ = "descriptions"
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(2), nullable=False)
    desc = db.Column(db.String, nullable=False)
    estate_id = db.Column(db.ForeignKey(EstateModel.id), nullable=False)
    estateR = db.relationship(EstateModel, foreign_keys='Descriptions.estate_id')