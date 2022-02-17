from flask_restful import fields

description_fields = {
    "lang": fields.String,
    "desc": fields.String,
    "estate_id":fields.Integer
}
features_fields= {
    "id": fields.Integer,
    "estate_id": fields.Integer,
    "pool": fields.Boolean,
    "ac": fields.Boolean,
    "park": fields.Boolean,
    "alarm": fields.Boolean,
    "auto_gate": fields.Boolean,
    "tv": fields.Boolean,
    "internet": fields.Boolean,
    "fireplace": fields.Boolean,
    "bbq": fields.Boolean,
    "gym": fields.Boolean,
    "pan_view": fields.Boolean,
    "sauna": fields.Boolean,
    "garage": fields.Boolean,
}
estate_fields= {
    "id" : fields.Integer,
    "ref_id": fields.String,
    "name" : fields.String,
    "area" : fields.Integer,
    "rooms": fields.Integer,
    "bedrooms": fields.Integer,
    "bathrooms": fields.Integer,
    "garden_area": fields.Integer,
    "beds": fields.Integer,
    "location": fields.String,
    "energy_class": fields.String,
    "sea_dist": fields.Integer,
    "description": fields.List(fields.Nested(description_fields)),
    "features": fields.Nested(features_fields)
}
