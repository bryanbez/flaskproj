from ..extensions import mongo

def init_db(app):
    mongo.init_app(app)

def get_db():
    return mongo.db