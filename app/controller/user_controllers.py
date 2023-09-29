from flask import request, jsonify, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import datetime
import mysql
from app.models.user_models import User


class UserController:

    @classmethod
    def register_user(cls):
        data = request.json
        print(f'Data received: {data}')

        if not data.get('nombre'):
            return jsonify({'error': 'Nombre no proporcionado'}), 400
        if not data.get('apellido'):
            return jsonify({'error': 'Apellido no proporcionado'}), 400

        if not data.get('correo'):
            return jsonify({'error': 'Correo no proporcionado'}), 400

        if not data.get('nombre_usuario'):
            return jsonify({'error': 'Nombre de usuario no proporcionado'}), 400

        if not data.get('contrasena'):
            return jsonify({'error': 'Contraseña no proporcionada'}), 400

        if not data.get('fecha_nacimiento'):
            return jsonify({'error': 'Fecha de nacimiento no proporcionada'}), 400

        try:
            user = User(
                nombre=data.get('nombre'),
                apellido=data.get('apellido'),
                correo=data.get('correo'),
                nombre_usuario=data.get('nombre_usuario'),
                contrasena=data.get('contrasena'),
                fecha_nacimiento=datetime.strptime(data.get('fecha_nacimiento'), '%Y-%m-%d')
            )
            User.create_user(user)

            access_token = create_access_token(identity=user.id)

            return jsonify({'message': 'Cuenta creada exitosamente', 'access_token': access_token}), 201
        except Exception:
            return jsonify({'error': 'Error en el registro'}), 500

    @classmethod
    def get_user(cls, user_id):
        user = User.get_user(user_id)
        if user:
            return user.__dict__, 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
    @classmethod
    def get_user_by_username(cls, username):
            user = User.get_user_by_username(username)    
            if user:
                return user.__dict__, 200
            else:
                return {'error': 'Usuario no encontrado'}, 404

    @classmethod
    def get_users(cls):
        users = User.get_all_users()
        if users:
            users_list = [user.__dict__ for user in users]
            return jsonify(users_list), 200
        else:
            return jsonify({'error': 'No se encontraron usuarios'}), 404

    @classmethod
    def update_user(cls, user_id):
        user = User.get_user(user_id)
        if user:
            data = request.json

            if 'nombre_usuario' in data:
                user.nombre_usuario = data['nombre_usuario']

            user.nombre = data.get('nombre', user.nombre)
            user.apellido = data.get('apellido', user.apellido)
            user.correo = data.get('correo', user.correo)
            user.fecha_nacimiento = data.get('fecha_nacimiento', user.fecha_nacimiento)
            User.update_user(user)
            return {}, 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        
    @classmethod
    def update_user_by_username(cls, username):
        try:
            data = request.json
            correo = data.get('correo')
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            contrasena = data.get('contrasena')
            nuevacontra = data.get('nuevacontra')

            user = User.get_user_by_username(username)
            if user:
                if correo:
                    user.correo = correo
                if nombre:
                    user.nombre = nombre
                if apellido:
                    user.apellido = apellido
                if contrasena:
                    if user.contrasena == contrasena:
                        user.contrasena = nuevacontra
                    else:
                        return jsonify({'error': 'Contraseña actual incorrecta'}), 400
                User.update_user(user)

                return jsonify({'message': 'Perfil actualizado correctamente'}), 200
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404

        except Exception as e:
            return jsonify({'error': f'Error al actualizar el perfil: {str(e)}'}), 500

    @classmethod
    def login_user(cls):
        data = request.json
        print(f'Data received: {data}')
        nombre_usuario = data.get('usuario')
        contrasena = data.get('contraseña')
        print(f'Nombre de usuario: {nombre_usuario}')
        print(f'Contraseña: {contrasena}')

        try:
            user_id = User.authenticate_user(nombre_usuario, contrasena)

            if user_id is not None:
                session['user_id'] = user_id

                access_token = create_access_token(identity=user_id)

                return jsonify({'mensaje': 'Inicio de sesión exitoso', 'access_token': access_token}), 200
            else:
                return jsonify({'error': 'Credenciales inválidas - ¿Ya tienes tu cuenta creada?'}), 401
        except mysql.connector.Error:
            return jsonify({'error': 'Error de base de datos'}), 500
        except Exception:
            return jsonify({'error': 'Error al autenticar usuario'}), 500

    @classmethod
    def logout(cls):
        session.clear()
        return jsonify({'mensaje': 'Sesión cerrada correctamente'}), 200

    @classmethod
    @jwt_required()
    def get_profile(cls):
        user_id = get_jwt_identity()
        user = User.get_user(user_id)

        if user:
            user_dict = user.__dict__
            user_dict['fecha_nacimiento'] = user_dict['fecha_nacimiento'].strftime('%d/%m/%Y')
            return jsonify(user_dict), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404

    @classmethod
    def update_profile(cls):
        user_id = session.get('user_id') 
        if user_id is not None:
            data = request.json
            user = User.get_user(user_id)

            if user:
                if 'nombre_usuario' in data:
                    user.nombre_usuario = data['nombre_usuario']

                user.nombre = data.get('nombre', user.nombre)
                user.apellido = data.get('apellido', user.apellido)
                user.correo = data.get('correo', user.correo)
                user.fecha_nacimiento = data.get('fecha_nacimiento', user.fecha_nacimiento)

                User.update_user(user)

                return jsonify({'mensaje': 'Perfil actualizado correctamente'}), 200
            else:
                return jsonify({'error': 'Usuario no encontrado'}), 404
        else:
            return jsonify({'error': 'No has iniciado sesión'}), 401
        
    @classmethod
    def delete_user(cls, user_id):
        User.delete_user(user_id)
        return {}, 200
