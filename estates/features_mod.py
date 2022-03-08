from database import db
from estates import EstateModel


class ExtraFeatures(db.Model):
    __tablename__ = 'extra_features'
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.ForeignKey('estates.id'), nullable=False)
    estateR = db.relationship(
        EstateModel, foreign_keys='ExtraFeatures.estate_id')
    pool = db.Column(db.Boolean, nullable=False)
    ac = db.Column(db.Boolean, nullable=False)
    park = db.Column(db.Boolean, nullable=False)
    alarm = db.Column(db.Boolean, nullable=False)
    auto_gate = db.Column(db.Boolean, nullable=False)
    tv = db.Column(db.Boolean, nullable=False)
    internet = db.Column(db.Boolean, nullable=False)
    fireplace = db.Column(db.Boolean, nullable=False)
    bbq = db.Column(db.Boolean, nullable=False)
    gym = db.Column(db.Boolean, nullable=False)
    pan_view = db.Column(db.Boolean, nullable=False)
    sauna = db.Column(db.Boolean, nullable=False)
    garage = db.Column(db.Boolean, nullable=False)
    spa = db.Column(db.Boolean, nullable=False)
    jacuzzi = db.Column(db.Boolean, nullable=False)
    taverna = db.Column(db.Boolean, nullable=False)
    video_surv = db.Column(db.Boolean, nullable=False)
    domotics = db.Column(db.Boolean, nullable=False)
    terrace = db.Column(db.Boolean, nullable=False)
    balcony = db.Column(db.Boolean, nullable=False)
    veranda = db.Column(db.Boolean, nullable=False)

    # TODO : smart home, terrazza, balcony, veranda
