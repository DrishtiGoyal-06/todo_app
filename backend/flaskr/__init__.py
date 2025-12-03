import flaskr.models

from flask import Flask
from config import DevelopmentConfig
from flaskr.extensions import migrate, api, cors, jwt
from flaskr.db import db

from flaskr.routes.auth_route import bp as auth_route
from flaskr.routes.user_route import bp as user_route
from flaskr.routes.tag_route import bp as tag_route
from flaskr.routes.task_route import bp as task_route


def create_app(test_config=None):
    app = Flask(__name__)

    # Load config
    if test_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(test_config)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    
    # CORS FIX — allow frontend domain + credentials
    cors.init_app(
        app,
        resources={r"/api/*": {"origins": "*"}},   # or restrict to your Vercel domain later
        supports_credentials=True
    )

    jwt.init_app(app)

    # Register routes
    api.register_blueprint(auth_route, url_prefix="/api/v1")
    api.register_blueprint(user_route, url_prefix="/api/v1")
    api.register_blueprint(tag_route, url_prefix="/api/v1")
    api.register_blueprint(task_route, url_prefix="/api/v1")

    return app
