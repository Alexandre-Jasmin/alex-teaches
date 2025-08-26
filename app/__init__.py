from flask import Flask
from app.extensions import db
from config import get_config

class FlaskApp:

    def __init__(self, config_name="development"):
        self.app = Flask(__name__)
        self.app.config.from_object(get_config(config_name))
        self.register_extensions() # Initialize extensions like db
        self.register_blueprints() # Register blueprints

    def register_extensions(self):
        db.init_app(self.app)

    def register_blueprints(self):
        from app.routes.main import main_bp
        self.app.register_blueprint(main_bp)

    def run(self, **kwargs):
        self.app.run(**kwargs)

def create_app(config_name="development"):
    flask_app = FlaskApp(config_name)
    return flask_app.app