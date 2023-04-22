import config
from flask import Flask
from flask_restful import Api

app = Flask(__name__,
            template_folder='views')

app.config.from_object(config.ProductionConfig)

api_router = Api(app, prefix='/v1')  # API Initialization

from controllers import index
from api import resources

# Register resources
api_router.add_resource(resources.Weather, '/weather')

# Register Blueprints
app.register_blueprint(index.bp)
