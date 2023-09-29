from flask import request, jsonify
from app.models.member_models import Member

class MemberController:

    @classmethod
    def add_member_to_server(cls):
        data = request.json

        if not data.get('id_usuario'):
            return jsonify({'error': 'ID de usuario no proporcionado'}), 400

        if not data.get('id_servidor'):
            return jsonify({'error': 'ID de servidor no proporcionado'}), 400

        try:
            member = Member(
                id_usuario=data.get('id_usuario'),
                id_servidor=data.get('id_servidor')
            )
            Member.create_member(member)
            return jsonify({'message': 'Miembro agregado al servidor exitosamente'}), 201
        except Exception as e:
            return jsonify({'error': 'Error al agregar miembro al servidor'}), 500

    @classmethod
    def remove_member_from_server(cls, member_id):
        Member.delete_member(member_id)
        return jsonify({'message': 'Miembro eliminado del servidor exitosamente'}), 200

    @classmethod
    def get_server_members(cls, server_id):
        members = Member.get_server_members(server_id)
        if members:
            members_list = [member.__dict__ for member in members]
            return jsonify(members_list), 200
        else:
            return jsonify({'error': 'No se encontraron miembros en el servidor'}), 404
