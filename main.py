from flask import Flask
from app.core.config import Config
from app.routes.routes import register_routes
from app.routes.routes import api_bp
from app.routes.routes import location_geocoding_bp

import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_routes(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('DOCKER_PORT'))
    