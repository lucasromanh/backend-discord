from mysqlx import DatabaseError
from app.database import DatabaseConnection


class Message:

    def __init__(self, id=None, contenido=None, fecha_envio=None, id_usuario=None, id_canal=None):
        self.id = id
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.id_usuario = id_usuario
        self.id_canal = id_canal

    @classmethod
    def get_message(cls, message_id):
        query = "SELECT * FROM Mensajes WHERE id = %s"
        params = (message_id,)  
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            if 'id' in result:
                return Message(
                    id=result['id'],
                    contenido=result['contenido'],
                    fecha_envio=result['fecha_envio'],
                    id_usuario=result['id_usuario'],
                    id_canal=result['id_canal']
                )
            else:
                return None
        else:
            return None

        
    @classmethod
    def get_all_messages(cls):
        query = "SELECT * FROM Mensajes"
        results = DatabaseConnection.fetch_all(query)
        messages = []

        for result in results:
            message = Message(
                id=result['id'],
                contenido=result['contenido'],
                fecha_envio=result['fecha_envio'],
                id_usuario=result['id_usuario'],
                id_canal=result.get('id_canal')  
            )
            messages.append(message)

        return messages


    @classmethod
    def create_message(cls, message):
        query = "INSERT INTO Mensajes (contenido, fecha_envio, id_usuario, id_canal) VALUES (%s, %s, %s, %s)"
        params = (
            message.contenido,
            message.fecha_envio,
            message.id_usuario,
            message.id_canal
        )
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 1:
            message_id = cursor.lastrowid
            return message_id
        else:
            raise DatabaseError("No se pudo crear el nuevo mensaje")

    @classmethod
    def update_message(cls, message):
        query = "UPDATE Mensajes SET contenido = %s WHERE id = %s"
        params = (
            message.contenido,
            message.id
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_message(cls, message_id):
        query = "DELETE FROM Mensajes WHERE id = %s"
        params = (message_id,)
        DatabaseConnection.execute_query(query, params=params)

