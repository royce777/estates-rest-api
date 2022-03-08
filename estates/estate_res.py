from flask import request
from flask_restful import Resource, marshal_with, reqparse, abort, inputs
from estates import EstateModel, Descriptions, ExtraFeatures
from estates import estate_fields, create_model as cm
from database import db
import ast


class Estate(Resource):

    @marshal_with(estate_fields)
    def get(self, estate_id):
        lang = request.headers.get("Accept-Language", 'en')[:2]
        estate_result = EstateModel.query.filter_by(id=estate_id).first()
        description_result = Descriptions.query.filter_by(estate_id=estate_id,
                                                          lang=lang).first()
        features = ExtraFeatures.query.filter_by(estate_id=estate_id)
        if not estate_result or not description_result or not features:
            abort(
                404,
                message=
                "Estate id or required description or features does not exist! Check DB"
            )
        return estate_result

    @marshal_with(estate_fields)
    def post(self, estate_id):
        main_info = estates_args.parse_args()
        # print(main_info)
        # parse description list
        all_descriptions = main_info['description']
        parsed_descriptions = []
        for descr in all_descriptions:
            description = ast.literal_eval(descr)
            parsed_descriptions.append(description)

        # parse newly uploaded images list

        all_images = main_info['images']
        parsed_images = []
        for img in all_images:
            image = ast.literal_eval(img)
            parsed_images.append(image)

        # parse extra features
        parsed_features = features_args.parse_args(req=main_info)
        #print(f"FEATURES ============ {parsed_features} ")
        result = EstateModel.query.filter_by(id=estate_id).first()
        if result:
            abort(409, message="Estate id already exists !")
        estate = cm.create_model(estate_id, "estate", main_info)

        features = cm.create_model(estate_id, "features", parsed_features)
        description1, description2 = cm.create_model(estate_id, "description",
                                                     parsed_descriptions)
        images = cm.create_model(estate_id, "images", parsed_images)
        db.session.add(estate)
        db.session.add(description1)
        db.session.add(description2)
        db.session.add(features)
        for img in images:
            db.session.add(img)
        db.session.commit()
        estate.add_props(parsed_features, parsed_descriptions, parsed_images)
        return estate, 201

    def delete(self, estate_id):
        return '', 204


estates_args = reqparse.RequestParser()
estates_args.add_argument("name",
                          type=str,
                          help="Name of the estate",
                          required=True)
estates_args.add_argument("area",
                          type=int,
                          help="Area of the estate",
                          required=True)
estates_args.add_argument("rooms",
                          type=int,
                          help="Number of rooms of the estate",
                          required=True)
estates_args.add_argument("bedrooms",
                          type=int,
                          help="Number of bedrooms of the estate",
                          required=True)
estates_args.add_argument("bathrooms",
                          type=int,
                          help="Number of bathrooms of the estate",
                          required=True)
estates_args.add_argument("garden_area",
                          type=int,
                          help="Area of the garden if present, 0 otherwise")
estates_args.add_argument("beds",
                          type=int,
                          help="Number of beds ( how many people can sleep )",
                          required=True)
estates_args.add_argument("energy_class",
                          type=str,
                          help="Energy label of the estate")
estates_args.add_argument("description", action='append')
estates_args.add_argument("images", action='append')
estates_args.add_argument("ref_id",
                          type=str,
                          help="Internal reference id",
                          required=True)
estates_args.add_argument("location",
                          type=str,
                          help="Location town name",
                          required=True)
estates_args.add_argument(
    "sea_dist",
    type=int,
    help="Distance from the sea",
)
estates_args.add_argument("features", type=dict)
estates_args.add_argument("listing_type",
                          type=str,
                          help="Type of the listing : rent / sell/ both")
estates_args.add_argument("build_year",
                          type=int,
                          help="When the esatate was built")
estates_args.add_argument("floors", type=int, help="Number of floors")
estates_args.add_argument("price", type=int, help="Price of estate in euro")
estates_args.add_argument("m_rate", type=int, help="Monthly charge")
estates_args.add_argument(
    "category",
    type=str,
    help="Category of estate ( like villa or apartment )",
    required=True)

descriptions_args = reqparse.RequestParser()
descriptions_args.add_argument("lang",
                               type=str,
                               help="Language of description",
                               required=True,
                               location='description')
descriptions_args.add_argument("desc",
                               type=str,
                               help="Estate description",
                               required=True,
                               location='description')
descriptions_args.add_argument("estate_id",
                               type=int,
                               help="Id of the estate",
                               required=True,
                               location='description')

features_args = reqparse.RequestParser()
features_args.add_argument("estate_id",
                           type=int,
                           location='features',
                           required=True)
features_args.add_argument("pool",
                           type=inputs.boolean,
                           location='features',
                           required=True)
features_args.add_argument("ac",
                           type=inputs.boolean,
                           location='features',
                           required=True)
features_args.add_argument("park",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("alarm",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("auto_gate",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("tv", type=bool, location='features', required=True)
features_args.add_argument("internet",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("fireplace",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("bbq",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("gym",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("pan_view",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("sauna",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("garage",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("spa",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("jacuzzi",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("taverna",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("video_surv",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("domotics",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("terrace",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("balcony",
                           type=bool,
                           location='features',
                           required=True)
features_args.add_argument("veranda",
                           type=bool,
                           location='features',
                           required=True)
