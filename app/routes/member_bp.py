from flask import Blueprint
from ..controller.member_controllers import MemberController

member_bp = Blueprint('member_bp', __name__)

member_bp.route('/add', methods=['POST'])(MemberController.add_member_to_server)
member_bp.route('/<int:member_id>', methods=['DELETE'])(MemberController.remove_member_from_server)
member_bp.route('/server/<int:server_id>', methods=['GET'])(MemberController.get_server_members)
