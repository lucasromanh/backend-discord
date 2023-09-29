from flask import Blueprint
from ..controller.server_controllers import ServerController

server_bp = Blueprint('server_bp', __name__)


server_bp.route('/create', methods=['POST'])(ServerController.create_server)
server_bp.route('/<int:server_id>', methods=['PUT'])(ServerController.update_server)
server_bp.route('/', methods=['GET'])(ServerController.get_servers)
server_bp.route('/<int:server_id>', methods=['GET'])(ServerController.get_servers)
server_bp.route('/<int:server_id>', methods=['DELETE'])(ServerController.delete_server)


