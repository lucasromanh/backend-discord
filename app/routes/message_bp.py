from flask import Blueprint
from ..controller.menssage_controllers import MessageController

message_bp = Blueprint('message_bp', __name__)

message_bp.route('/', methods=['POST'])(MessageController.create_message)
message_bp.route('/<int:message_id>', methods=['PUT'])(MessageController.update_message)
message_bp.route('/', methods=['GET'])(MessageController.get_all_messages)
message_bp.route('/<int:message_id>', methods=['GET'])(MessageController.get_message)
message_bp.route('/delete/<int:message_id>', methods=['DELETE'])(MessageController.delete_message)

