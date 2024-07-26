from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/', methods=['GET'])
def home():
    return jsonify("Endpoint test OK"), 200