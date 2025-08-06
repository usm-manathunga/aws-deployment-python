from flask import Blueprint,request
from app.models.user import User
from app.utils.response import success_response, error_response
from app.services.user_service import get_all_users,create_user,get_user_by_username

user_bp = Blueprint('users',__name__)


# Load environment variables from .env file



@user_bp.route("/",methods=['GET'])
def get_users():
    users = get_all_users()
    return success_response([{"id":u.id, "username": u.username} for u in users])



@user_bp.route("/",methods=['POST'])
def create_user_api():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return error_response("Username and password are required", status=400)
    
    user = create_user(username, password)
    return success_response({"id": user.id, "username": user.username}, status=201)


@user_bp.route("/name/<string:username>", methods=['GET'])
def get_user_by_username_api(username):
    users = get_user_by_username(username)
    if not users:
        return error_response("User not found", status=404)
    
    return success_response([{"id": user.id, "username": user.username} for user in users])




    