from flask import Flask
from dotenv import load_dotenv
from app.routes.employees import employees_bp
from app.routes.werehouse import werehouse_bp
from app.routes.home import home_db

def create_app():
    load_dotenv()
    app = Flask(__name__) 
    app.register_blueprint(home_db)
    app.register_blueprint(employees_bp)
    app.register_blueprint(werehouse_bp)
    return app


