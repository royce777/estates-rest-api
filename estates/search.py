from email.mime import image
from flask import jsonify, request
from flask_restful import Resource, marshal_with, reqparse, abort, inputs
from sqlalchemy import and_, desc
from estates import EstateModel, Descriptions, ExtraFeatures, EstateImages, search_res_fields


class Search(Resource):

    @marshal_with(search_res_fields)
    def get(self):
        # delete keys without values in the multi-dict
        query_multi_dict = request.args.copy()
        keys_to_pop = []
        for key, val in query_multi_dict.items():
            if (val == ''):
                keys_to_pop.append(key)
        for key in keys_to_pop:
            query_multi_dict.pop(key)
        result_list = self.search(query_multi_dict)
        print(type(result_list))
        for result in result_list:
            # get extra_features, descriptions and pictures
            descriptions = Descriptions.query.filter_by(
                estate_id=result.id).all()
            extra_features = ExtraFeatures.query.filter_by(
                estate_id=result.id).all()
            images = EstateImages.query.filter_by(estate_id=result.id).all()
            result.add_props(extra_features, descriptions, images)
        return {"estates": result_list}

    def search(self, parameters):
        query_conditions = []
        print(parameters)
        for key, val in parameters.items():
            if key == 'location':
                query_conditions.append(EstateModel.location == val)
            if key == 'bedrooms':
                query_conditions.append(EstateModel.bedrooms >= val)
            if key == 'bathrooms':
                query_conditions.append(EstateModel.bathrooms >= val)
            if key == 'beds':
                query_conditions.append(EstateModel.beds >= val)
            if key == 'sea_dist':
                query_conditions.append(EstateModel.sea_dist <= val)
            if key == 'listing_type':
                query_conditions.append(
                    EstateModel.listing_type.in_(["both", val]))
            if key == 'area':
                query_conditions.append(EstateModel.area >= val)
            if key == 'category':
                query_conditions.append(EstateModel.category == val)
            if key == 'minPrice':
                query_conditions.append(EstateModel.price >= val)
            if key == 'maxPrice':
                query_conditions.append(EstateModel.price <= val)

        result = EstateModel.query.filter(and_(*query_conditions)).all()
        return result
