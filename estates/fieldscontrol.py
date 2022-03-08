from flask_restful import fields

description_fields = {
    "lang": fields.String,
    "desc": fields.String,
    "estate_id": fields.Integer
}

image_fields = {
    "id": fields.Integer,
    "estate_id": fields.Integer,
    "url": fields.String
}

features_fields = {
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
    "spa": fields.Boolean,
    "jacuzzi": fields.Boolean,
    "taverna": fields.Boolean,
    "video_surv": fields.Boolean,
    "domotics": fields.Boolean,
    "terrace": fields.Boolean,
    "balcony": fields.Boolean,
    "veranda": fields.Boolean,
}
estate_fields = {
    "id": fields.Integer,
    "ref_id": fields.String,
    "name": fields.String,
    "area": fields.Integer,
    "rooms": fields.Integer,
    "bedrooms": fields.Integer,
    "bathrooms": fields.Integer,
    "garden_area": fields.Integer,
    "beds": fields.Integer,
    "location": fields.String,
    "energy_class": fields.String,
    "sea_dist": fields.Integer,
    "listing_type": fields.String,
    "build_year": fields.Integer,
    "floors": fields.Integer,
    "description": fields.List(fields.Nested(description_fields)),
    "features": fields.Nested(features_fields),
    "images": fields.List(fields.Nested(image_fields)),
    "price": fields.Integer,
    "m_rate": fields.Integer,
    "category": fields.String
}
