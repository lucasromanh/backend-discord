from flask import Blueprint, request, jsonify, session
from ..controller.user_controllers import UserController
from app.models.user_models import User


user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['POST'])(UserController.register_user)
user_bp.route('/login', methods=['POST'])(UserController.login_user)
user_bp.route('/registro', methods=['POST'])(UserController.register_user)
user_bp.route('/update/<int:user_id>', methods=['PUT'])(UserController.update_user)
user_bp.route('/update/<string:username>', methods=['PUT'])(UserController.update_user_by_username)
user_bp.route('/<int:user_id>', methods=['GET'])(UserController.get_user)
user_bp.route('/<string:username>', methods=['GET'])(UserController.get_user_by_username)
user_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete_user)
user_bp.route('/', methods=['GET'])(UserController.get_users)

