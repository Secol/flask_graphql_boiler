from flask import Blueprint, jsonify, request

from app import cfg

graphql_controller = Blueprint('graphql_controller', __name__, url_prefix='/rest')

@graphql_controller.route('/', methods=['GET'])
def rest_api_info():

    if request.method == 'GET':

        response = {
            'api_debug' : cfg.DEBUG
        }

        return jsonify(response), 200

    else:
        return jsonify(cfg.ERROR_HTTP_VERB), 412