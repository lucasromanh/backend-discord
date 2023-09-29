from flask import request, jsonify, session
from ..models.message_models import Message

class MessageController:

    @classmethod
    def get_all_messages(cls):
        messages = Message.get_all_messages()
        message_list = [{'id': message.id, 'contenido': message.contenido, 'canal_id': message.id_canal} for message in messages]
        return jsonify(message_list), 200
    
    @classmethod
    def get_message(cls, message_id):
        user_id = session.get('user_id')

        if user_id is not None:
            message = Message.get_message(message_id)

            if message is not None and message.usuario_id == user_id:
                return jsonify({'id': message.id, 'contenido': message.contenido}), 200
            else:
                return jsonify({'error': 'No tienes permiso para acceder a este mensaje'}), 403
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401

    @classmethod
    def create_message(cls):
        data = request.get_json()  
        user_id = session.get('user_id')

        if user_id is not None:
            message = Message(
                contenido=data.get('contenido'),
                fecha_envio=data.get('fecha_envio'), 
                id_usuario=user_id,
                id_canal=data.get('canal_id')  
            )
            message_id = Message.create_message(message)
            return jsonify({'message_id': message_id}), 201
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401

    @classmethod
    def update_message(cls, message_id):
        data = request.json
        user_id = session.get('user_id')

        if user_id is not None:
            message = Message.get_message(message_id)
            if message:
                message.contenido = data.get('contenido')
                message.id_canal = data.get('canal_id') 
                Message.update_message(message)
                return jsonify({'message_id': message_id}), 200
            else:
                return jsonify({'error': 'Mensaje no encontrado'}), 404
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401

    def delete_message(message_id):
        try:
            message_id = int(message_id)
            message = Message.get_message(message_id)
            if message is not None:
                Message.delete_message(message_id)
                print(f"Mensaje {message_id} eliminado correctamente en el backend")
                return jsonify({'message': 'Mensaje eliminado correctamente'}), 200
            else:
                print(f"Mensaje {message_id} no se encontró en el backend")
                return jsonify({'message': 'El mensaje no se encontró'}), 404
        except ValueError:
            return jsonify({'error': 'ID de mensaje no válido'}), 400

    @classmethod
    def get_user_messages(cls, user_id):
        user_messages = Message.get_user_messages(user_id)
        message_list = [{'id': message.id, 'contenido': message.contenido, 'canal_id': message.canal_id} for message in user_messages]
        return jsonify(message_list), 200

    @classmethod
    def get_server_messages(cls, server_id):
        server_messages = Message.get_server_messages(server_id)
        message_list = [{'id': message.id, 'contenido': message.contenido, 'canal_id': message.canal_id} for message in server_messages]
        return jsonify(message_list), 200
