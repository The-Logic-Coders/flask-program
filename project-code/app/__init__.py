from flask import Flask
from config import Config
from app.db import db 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        from app.routes.main import main
        from app.routes.quiz import quiz_bp
        from app.routes.utils import utils 

        app.register_blueprint(main)
        app.register_blueprint(quiz_bp)
        app.register_blueprint(utils)

    return app
