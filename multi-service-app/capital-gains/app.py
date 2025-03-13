from flask import Flask
from capital_gains_routes import register_routes
import os

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app


if __name__ == '__main__':
    port = os.environ.get("CAPITAL_GAIN_SERVICE_PORT", 8080)
    app = create_app()
    app.run(host='0.0.0.0', port=port)
