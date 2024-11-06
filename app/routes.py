from flask import Blueprint, render_template

route_bp = Blueprint('route_bp', __name__)

@route_bp.route('/')
def home():
    return render_template('pages/index.html')

@route_bp.route('/about')
def about():
    return render_template('pages/about.html')