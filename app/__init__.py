from flask import Flask
from .lib.ext import db, migrate, cors
from .config import AppConfig

# Importing models to be detected by alembic
from .models import *

def make_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)
    
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    
    from .routes import all_routes
    app.register_blueprint(all_routes)

    return app
