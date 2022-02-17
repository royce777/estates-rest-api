from database import db


class EstateModel(db.Model):
    __tablename__ = 'estates'
    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    garden_area = db.Column(db.Integer, nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    energy_class = db.Column(db.String(1))
    sea_dist = db.Column(db.Integer)

    def __repr__(self):
        return f"Estate (name = {self.name} , ref_id = {self.ref_id} area = {self.area} , bedr. = {self.bedrooms} , bathr. = {self.bathrooms})"

    def add_props(self,features, descriptions):
        self.description = descriptions
        self.features = features