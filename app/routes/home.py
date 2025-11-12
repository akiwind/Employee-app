from flask import Blueprint, request, render_template

home_db = Blueprint("home", __name__)

@home_db.route("/")
def home():
    
    html = render_template("home/home.html")
    return html        
