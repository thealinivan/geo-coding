from flask import Flask
from app.core.config import Config
from app.api.routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api, url_prefix='/api')
    return app

app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=5000)
    