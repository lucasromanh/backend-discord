from app.database import DatabaseConnection

class Member:
    def __init__(self, id=None, id_usuario=None, id_servidor=None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_servidor = id_servidor

    @classmethod
    def create_member(cls, member):
        query = "INSERT INTO MiembrosServidores (id_usuario, id_servidor) VALUES (%s, %s)"
        params = (member.id_usuario, member.id_servidor)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_member(cls, member_id):
        query = "DELETE FROM MiembrosServidores WHERE id = %s"
        params = (member_id,)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_server_members(cls, server_id):
        query = "SELECT * FROM MiembrosServidores WHERE id_servidor = %s"
        params = (server_id,)
        results = DatabaseConnection.fetch_all(query, params=params)
        members = []

        for result in results:
            member = Member(
                id=result['id'],
                id_usuario=result['id_usuario'],
                id_servidor=result['id_servidor']
            )
            members.append(member)

        return members
