from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .foods import foods_bp

api_bp.register_blueprint(foods_bp)

