from flask import Blueprint, jsonify
from app.lib.foods import get_all_food, get_food_by_id
from ..utils import serialize_document

foods_bp = Blueprint('foods', __name__)

@foods_bp.route('/foods', methods=['GET'])
def get_foods():
    foods = get_all_food()
    return jsonify([serialize_document(food) for food in foods]), 200
    #return jsonify(foods)

@foods_bp.route('/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    #try: 
    #    food_id = int(food_id)
    #except ValueError:
    #    return jsonify({'error': 'Invalid food ID'}), 400
    
    single_food = get_food_by_id(food_id)
    if "error" not in single_food:
        return jsonify(single_food), 404
    return jsonify(single_food)