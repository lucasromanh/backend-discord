from flask import Blueprint
from ..controller.channel_controllers import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/', methods=['GET'])(ChannelController.get_channels)
channel_bp.route('/', methods=['POST'])(ChannelController.create_channel)
channel_bp.route('/<int:channel_id>', methods=['PUT'])(ChannelController.update_channel)
channel_bp.route('/<int:channel_id>', methods=['DELETE'])(ChannelController.delete_channel)
channel_bp.route('/<int:channel_id>/messages', methods=['GET'])(ChannelController.get_channel_messages)

