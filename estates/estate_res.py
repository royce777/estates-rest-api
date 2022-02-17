from flask import request
from flask_restful import Resource, marshal_with, reqparse, abort, inputs
from estates import EstateModel, Descriptions, ExtraFeatures
from estates import estate_fields
from database import db
import ast

class Estate(Resource):
    @marshal_with(estate_fields)
    def get(self, estate_id):
        lang = request.headers.get("Accept-Language", 'en')[:2]
        estate_result = EstateModel.query.filter_by(id=estate_id).first()
        description_result = Descriptions.query.filter_by(estate_id=estate_id,lang=lang).first()
        features = ExtraFeatures.query.filter_by(estate_id=estate_id)
        if not estate_result or not description_result or not features:
            abort(404, message="Estate id or required description or features does not exist! Check DB")
        return estate_result 

    @marshal_with(estate_fields)
    def post(self, estate_id):
        main_info = estates_args.parse_args()
        print(main_info)
        all_descriptions = main_info['description']
        parsed_descriptions = []
        for descr in all_descriptions:
            description = ast.literal_eval(descr)
            parsed_descriptions.append(description)

        features = features_args.parse_args(req=main_info)
        print(f"FEATURES ============ {features} ")
        result = EstateModel.query.filter_by(id=estate_id).first()
        if result :
            abort(409, message="Estate id already exists !")
        estate = EstateModel(id=estate_id, 
                            ref_id=main_info['ref_id'],
                            name=main_info['name'], 
                            area=main_info['area'],
                            rooms=main_info['rooms'],
                            bedrooms=main_info['bedrooms'], 
                            bathrooms=main_info['bathrooms'],
                            garden_area=main_info['garden_area'],
                            beds=main_info['beds'],
                            location=main_info['location'],
                            energy_class=main_info['energy_class'],
                            sea_dist=main_info['sea_dist'])
        
        estate.add_props(features, parsed_descriptions)

        db.session.add(estate)
        db.session.commit() 
        return estate, 201 

    def delete(self, estate_id):
        return '', 204

estates_args = reqparse.RequestParser()
estates_args.add_argument("name", type=str, help="Name of the estate", required=True)
estates_args.add_argument("area", type=int, help="Area of the estate", required=True)
estates_args.add_argument("rooms", type=int, help="Number of rooms of the estate", required=True)
estates_args.add_argument("bedrooms", type=int, help="Number of bedrooms of the estate", required=True)
estates_args.add_argument("bathrooms", type=int, help="Number of bathrooms of the estate", required=True)
estates_args.add_argument("garden_area", type=int, help="Area of the garden if present, 0 otherwise")
estates_args.add_argument("beds", type=int, help="Number of beds ( how many people can sleep )", required=True)
estates_args.add_argument("energy_class", type=str, help="Energy label of the estate")
estates_args.add_argument("description", action='append')
estates_args.add_argument("ref_id", type=str, help="Internal reference id", required=True)
estates_args.add_argument("location", type=str, help="Location town name", required=True)
estates_args.add_argument("sea_dist", type=int, help="Distance from the sea", )
estates_args.add_argument("features", type=dict)


descriptions_args = reqparse.RequestParser()
descriptions_args.add_argument("lang", type=str, help="Language of description", required=True, location='description')
descriptions_args.add_argument("desc", type=str, help="Estate description", required=True, location='description')
descriptions_args.add_argument("estate_id", type=int, help="Id of the estate", required=True, location='description')


features_args = reqparse.RequestParser()
features_args.add_argument("estate_id", type=int, location='features', required=True)
features_args.add_argument("pool", type=inputs.boolean, location='features', required=True)
features_args.add_argument("ac", type=inputs.boolean, location='features', required=True)
features_args.add_argument("park",type=bool, location='features', required=True)
features_args.add_argument("alarm", type=bool, location='features', required=True)
features_args.add_argument("auto_gate", type=bool, location='features', required=True)
features_args.add_argument("tv", type=bool, location='features', required=True)
features_args.add_argument("internet", type=bool, location='features', required=True)
features_args.add_argument("fireplace", type=bool, location='features', required=True)
features_args.add_argument("bbq", type=bool, location='features', required=True)
features_args.add_argument("gym", type=bool, location='features', required=True)
features_args.add_argument("pan_view", type=bool, location='features', required=True)
features_args.add_argument("sauna", type=bool, location='features', required=True)
features_args.add_argument("garage", type=bool, location='features', required=True)
