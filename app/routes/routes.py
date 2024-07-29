
from flask import Blueprint
from app.core.security import require_api_key
from app.controllers.home_controller import home
from app.controllers.geocode_controller import reverse_geocode, geocode

api_bp = Blueprint('api', __name__)
location_geocoding_bp = Blueprint('api/geocode', __name__)

def register_routes(app):
    
    @api_bp.route('/', methods=['GET'])
    def _home():
        return home()

    @location_geocoding_bp.route('/reverse-geocode', methods=['GET'])
    @require_api_key
    def _reverse_geocode():
        return reverse_geocode()
    
    @location_geocoding_bp.route('/geocode', methods=['GET'])
    @require_api_key
    def _geocode():
        return geocode()
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(location_geocoding_bp, url_prefix='/api/geocode')

    