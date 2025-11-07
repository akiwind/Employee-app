from flask import Flask
from dotenv import load_dotenv
from app.routes.employees import employees_bp

def create_app():
    load_dotenv()
    app = Flask(__name__)   
    app.register_blueprint(employees_bp)
    return app