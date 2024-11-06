from .database import get_db
from bson.objectid import ObjectId

def get_all_food():
    db = get_db()
    return list(db.foods.find())

def get_food_by_id(food_id):
    db = get_db()
    try: 
        single_food = db.foods.find_one({'id': food_id})

        if single_food:
            single_food['_id'] = str(single_food['_id'])
        else:
            return {"error": "Food not Found"}, 404
        return single_food 
    except Exception as e:
        return {"error": str(e)}, 500
   


