from flask import Flask
from dotenv import load_dotenv
import os

from .apis import api_bp
from .routes import route_bp
from .extensions import mongo

def create_app():

    load_dotenv()

    app = Flask(__name__)
    app.debug = True

    #mongodb configuration
    app.config['MONGO_URI'] = f"mongodb+srv://{os.environ.get('MONGO_USER')}:{os.environ.get('MONGO_PASS')}@cluster0.aoytkvo.mongodb.net/fastfood?retryWrites=true&w=majority"

    mongo.init_app(app)

    app.register_blueprint(route_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
   