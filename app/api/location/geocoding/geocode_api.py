from flask import Blueprint, request, jsonify
from app.services.location.geocoding.geocode_service import get_address_by_coordinates, get_coordinates_by_address
from app.core.security import require_api_key

geocode_bp = Blueprint('/location/geocoding', __name__)

@geocode_bp.route('/reverse-geocode', methods=['GET'])
@require_api_key
def reverse_geocode():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    
    if not lat or not lng:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    try:
        lat = float(lat)
        lng = float(lng)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude"}), 400

    address = get_address_by_coordinates(lat, lng)
    if address:
        return jsonify({"address": address}), 200
    else:
        return jsonify({"error": "Unable to retrieve address"}), 500
    
@geocode_bp.route('/geocode', methods=['GET'])
@require_api_key
def geocode():
    address = request.args.get('address')
    
    if not address:
        return jsonify({"error": "Address is required"}), 400

    coordinates = get_coordinates_by_address(address)
    if coordinates:
        return jsonify(coordinates), 200
    else:
        return jsonify({"error": "Unable to retrieve coordinates"}), 500