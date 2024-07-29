from flask import Flask
from app.core.config import Config
from app.api.api import api_bp
from app.api.location.geocoding.geocode_api import geocode_bp
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(geocode_bp, url_prefix='/api/location/geocoding')
    return app

app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=os.getenv('DOCKER_PORT'))
    