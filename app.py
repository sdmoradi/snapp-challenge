import config
from flask import Flask

app = Flask(__name__,
            template_folder='views')

app.config.from_object(config.ProductionConfig)

from controllers import index

# Register Blueprints
app.register_blueprint(index.bp)
