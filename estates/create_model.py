from estates import EstateModel, ExtraFeatures, Descriptions, EstateImages


def create_model(estate_id, model: str, parsed_param):
    if model == "estate":
        return EstateModel(ref_id=parsed_param['ref_id'],
                           name=parsed_param['name'],
                           area=parsed_param['area'],
                           rooms=parsed_param['rooms'],
                           bedrooms=parsed_param['bedrooms'],
                           bathrooms=parsed_param['bathrooms'],
                           garden_area=parsed_param['garden_area'],
                           beds=parsed_param['beds'],
                           location=parsed_param['location'],
                           energy_class=parsed_param['energy_class'],
                           sea_dist=parsed_param['sea_dist'],
                           listing_type=parsed_param['listing_type'],
                           build_year=parsed_param['build_year'],
                           floors=parsed_param['floors'])
    elif model == "features":
        return ExtraFeatures(estate_id=estate_id,
                             pool=parsed_param['pool'],
                             ac=parsed_param['ac'],
                             park=parsed_param['park'],
                             alarm=parsed_param['alarm'],
                             auto_gate=parsed_param['auto_gate'],
                             tv=parsed_param['tv'],
                             internet=parsed_param['internet'],
                             fireplace=parsed_param['fireplace'],
                             bbq=parsed_param['bbq'],
                             gym=parsed_param['gym'],
                             pan_view=parsed_param['pan_view'],
                             sauna=parsed_param['sauna'],
                             garage=parsed_param['garage'],
                             spa=parsed_param['spa'],
                             jacuzzi=parsed_param['jacuzzi'],
                             taverna=parsed_param['taverna'],
                             video_surv=parsed_param['video_surv'],
                             domotics=parsed_param['domotics'],
                             terrace=parsed_param['terrace'],
                             balcony=parsed_param['balcony'],
                             veranda=parsed_param['veranda'])
    elif model == "description":
        # if(len(parsed_param)<2):
        parsed_d1 = parsed_param[0]
        parsed_d2 = parsed_param[1]
        description1 = Descriptions(lang=parsed_d1['lang'],
                                    desc=parsed_d1['desc'],
                                    estate_id=estate_id)
        description2 = Descriptions(lang=parsed_d2['lang'],
                                    desc=parsed_d1['desc'],
                                    estate_id=estate_id)
        return description1, description2

    elif model == 'images':
        image_models = []
        for param in parsed_param:
            parsed_img = EstateImages(estate_id=estate_id, url=param['url'])
            image_models.append(parsed_img)
        return image_models
