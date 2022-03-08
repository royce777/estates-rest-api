from database import db
from estates import EstateModel


class EstateImages(db.Model):
    __tablename__ = 'estate_images'
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.ForeignKey('estates.id'),
                          nullable=False)
    estateR = db.relationship(
        EstateModel, foreign_keys='EstateImages.estate_id')
    url = db.Column(db.String, nullable=False)
