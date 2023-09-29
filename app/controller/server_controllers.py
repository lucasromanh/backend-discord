from flask import request, jsonify, session
from ..models.server_models import Server
from ..models.channel_models import Channel

class ServerController:

    @classmethod
    def get_servers(cls, server_id=None):
        user_id = session.get('user_id')
        if user_id is not None:
            if server_id is None:
                servers = Server.get_all_servers()
                server_list = [{'id': server.id, 'nombre': server.nombre} for server in servers]
                return jsonify(server_list), 200
            else:
                server = Server.get_server(server_id)
                if server is not None:
                    return jsonify({'id': server.id, 'nombre': server.nombre}), 200
                else:
                    return jsonify({'error': 'Servidor no encontrado'}), 404
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401

    @classmethod
    def create_server(cls):
        data = request.json
        user_id = session.get('user_id')

        if user_id is not None:
            if 'nombre' not in data:
                print("Datos incompletos. Se requiere nombre.")
                return jsonify({'error': 'Datos incompletos. Se requiere nombre.'}), 400

            nombre = data['nombre']
            descripcion = data.get('descripcion', '')  

            if not nombre.strip():
                print("El nombre del servidor no puede estar vacío o contener solo espacios en blanco.")
                return jsonify({'error': 'El nombre del servidor no puede estar vacío o contener solo espacios en blanco.'}), 400

            server = Server(nombre=nombre, descripcion=descripcion, user_id=user_id)

            try:
                server_id = Server.create_server(server)
                print(f'Servidor creado correctamente. ID del servidor: {server_id}')
                return jsonify({'mensaje': 'Servidor creado correctamente', 'server_id': server_id}), 201
            except Exception as e:
                print(f'Error al crear el servidor: {str(e)}')
                return jsonify({'error': 'Hubo un error al crear el servidor'}), 500
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401

    @classmethod
    def get_server_channels(cls):
        user_id = session.get('user_id')
        if user_id is not None:
            server_id = request.args.get('server_id')
            print(f'Received server_id: {server_id}')
            channels = Channel.get_channels_by_server(server_id)
            print(f'Channels for server_id {server_id}: {channels}')
            channel_list = [{'id': channel.id, 'nombre': channel.nombre} for channel in channels]
            return jsonify(channel_list), 200
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401
        
    @classmethod
    def update_server(cls, server_id):
        data = request.json
        user_id = session.get('user_id')

        if user_id is not None:
            server = Server.get_server(server_id)

            if server is None:
                return jsonify({'error': 'Servidor no encontrado'}), 404

            if server.user_id != user_id:
                return jsonify({'error': 'No tienes permisos para actualizar este servidor'}), 403

            if 'nombre' in data:
                nombre = data['nombre'].strip()
                if nombre:
                    server.nombre = nombre
                else:
                    return jsonify({'error': 'El nombre del servidor no puede estar vacío o contener solo espacios en blanco'}), 400

            Server.update_server(server)
            return jsonify({'mensaje': 'Servidor actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401


    @classmethod
    def create_channel(cls):
        data = request.json
        user_id = session.get('user_id')

        if user_id is not None:
            if 'nombre' not in data or 'server_id' not in data:
                return jsonify({'error': 'Datos incompletos. Se requiere nombre y server_id.'}), 400

            nombre = data['nombre']
            server_id = data['server_id']

            if not nombre.strip():
                return jsonify({'error': 'El nombre del canal no puede estar vacío o contener solo espacios en blanco.'}), 400

            channel = Channel(nombre=nombre, server_id=server_id)
            channel_id = Channel.create_channel(channel)
            return jsonify({'mensaje': 'Canal creado correctamente', 'channel_id': channel_id}), 201
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401
        
    @classmethod
    def delete_server(cls, server_id):
        user_id = session.get('user_id')

        if user_id is not None:
            server = Server.get_server(server_id)

            if server is None:
                return jsonify({'error': 'Servidor no encontrado'}), 404

            if server.user_id != user_id:
                return jsonify({'error': 'No tienes permisos para eliminar este servidor'}), 403

            Server.delete_server(server_id)
            return jsonify({'mensaje': 'Servidor eliminado correctamente'}), 200
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401


    @classmethod
    def options(cls):
        response = jsonify({'message': 'Preflight request is allowed.'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5500')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, X-Auth-Token, Origin, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST, PUT, GET, DELETE, OPTIONS')
        response.headers.add('Access-Control-Max-Age', '3000')
        return response