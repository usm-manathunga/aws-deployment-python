from flask import Flask
from .extension import db
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .api.users.routes import user_bp
    app.register_blueprint(user_bp,url_prefix='/api/users')
                           
                           
    return app