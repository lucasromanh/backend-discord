from flask import request, jsonify, session
from ..models.channel_models import Channel
from ..models.message_models import Message
from datetime import datetime

class ChannelController:

    @classmethod
    def create_channel(cls):
        if request.method == 'POST':
            data = request.json
            user_id = session.get('user_id')

            if user_id is not None:
                if 'nombre' not in data:
                    return jsonify({'error': 'Datos incompletos. Se requiere nombre.'}), 400

                nombre = data['nombre']

                if not nombre.strip():
                    return jsonify({'error': 'El nombre del canal no puede estar vacío o contener solo espacios en blanco.'}), 400

                channel = Channel(nombre=nombre)
                channel_id = Channel.create_channel(channel)
                return jsonify({'mensaje': 'Canal creado correctamente', 'channel_id': channel_id}), 201
            else:
                return jsonify({'error': 'No has iniciado sesión'}), 401
        else:
            return jsonify({'error': 'Method Not Allowed'}), 405
        
    @classmethod
    def get_channels(cls):
        if request.method == 'GET':
            user_id = session.get('user_id')

            if user_id is not None:
                channels = Channel.get_all_channels()
                channel_list = [{'id': channel.id, 'nombre': channel.nombre, 'descripcion': channel.descripcion} for channel in channels]
                return jsonify(channel_list), 200
            else:
                return jsonify({'error': 'No has iniciado sesión'}), 401
        else:
            return jsonify({'error': 'Method Not Allowed'}), 405

    @classmethod
    def update_channel(cls, channel_id):
        if request.method == 'PUT':
            data = request.json

            if 'nombre' not in data:
                return jsonify({'error': 'Datos incompletos. Se requiere nombre.'}), 400

            nombre = data['nombre']

            if not nombre.strip():
                return jsonify({'error': 'El nombre del canal no puede estar vacío o contener solo espacios en blanco.'}), 400

            channel = Channel(id=channel_id, nombre=nombre)
            Channel.update_channel(channel)
            return jsonify({'mensaje': 'Canal actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'Method Not Allowed'}), 405

    @classmethod
    def delete_channel(cls, channel_id):
        if request.method == 'DELETE':
            Channel.delete_channel(channel_id)
            return jsonify({'mensaje': 'Canal eliminado correctamente'}), 200
        else:
            return jsonify({'error': 'Method Not Allowed'}), 405

    @classmethod
    def get_channel_messages(cls, channel_id):
        if request.method == 'GET':
            user_id = session.get('user_id')

            if user_id is not None:
                channel = Channel.get_channel(channel_id)

                if channel is not None:
                    if user_id == channel.id_servidor:  
                        messages = Message.get_channel_messages(channel_id)
                        message_list = [{'id': message.id, 'contenido': message.contenido} for message in messages]
                        return jsonify(message_list), 200
                    else:
                        return jsonify({'error': 'No tienes permiso para acceder a este canal'}), 403
                else:
                    return jsonify({'error': 'El canal no existe'}), 404
            else:
                return jsonify({'error': 'No has iniciado sesión'}), 401
        else:
            return jsonify({'error': 'Method Not Allowed'}), 405
