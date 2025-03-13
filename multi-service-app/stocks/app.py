"""
    This is the main entry point for the stocks service. 
"""
from flask import Flask
from stocks_routes import register_routes
import os
from utils.db import DB

def create_app():
    """
        Create and configure the Flask app.
    """
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == '__main__':
    # Initialize and connect to the MongoDB for stocks services
    db = DB()
    db.connect()
    port = 8000

    app = create_app()
    app.run(host='0.0.0.0', port=port)


