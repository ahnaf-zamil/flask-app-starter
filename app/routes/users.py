from flask import Blueprint
from ..models import User

router = Blueprint("users", import_name=__name__, url_prefix="/users")

@router.get("/")
def get_user():
    """Not really adding any proper functionality here"""
    user = User.query.first()
    if user:
        return user.json()
    return {"error": "No user found in DB"}
