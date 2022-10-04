from flask import Blueprint
from .import users

all_routes = Blueprint("routes", import_name=__name__)

all_routes.register_blueprint(users.router)
