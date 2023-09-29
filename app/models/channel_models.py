from mysqlx import DatabaseError
from app.database import DatabaseConnection

class Channel:

    def __init__(self, id=None, nombre=None, descripcion=None, id_servidor=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_servidor = id_servidor

    @classmethod
    def get_channel(cls, channel_id):
        query = "SELECT * FROM Canales WHERE id = %s"
        params = (channel_id,)
        try:
            result = DatabaseConnection.fetch_one(query, params=params)
            if result is not None:
                return Channel(
                    id=result[0],  
                    nombre=result[1], 
                    descripcion=result[2],  
                    id_servidor=result[3]  
                )
            else:
                return None
        except DatabaseError as e:
            print(f"Error de base de datos: {str(e)}")
            return None
        
    @classmethod
    def get_all_channels(cls):
        query = "SELECT * FROM Canales"
        try:
            results = DatabaseConnection.fetch_all(query)
            channels = []
            for result in results:
                channel = Channel(
                    id=result['id'],
                    nombre=result['nombre'],
                    descripcion=result['descripcion'],
                    id_servidor=result['id_servidor']
                )
                channels.append(channel)
            return channels
        except DatabaseError as e:
            print(f"Error de base de datos: {str(e)}")
            return []

    @classmethod
    def create_channel(cls, channel):
        query = "INSERT INTO Canales (nombre, descripcion, id_servidor) VALUES (%s, %s, %s)"
        params = (
            channel.nombre,
            channel.descripcion,
            channel.id_servidor
        )
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 1:
            channel_id = cursor.lastrowid
            return channel_id
        else:
            raise DatabaseError("No se pudo crear el nuevo canal")

    @classmethod
    def update_channel(cls, channel):
        query = "UPDATE Canales SET nombre = %s, descripcion = %s WHERE id = %s"
        params = (
            channel.nombre,
            channel.descripcion,
            channel.id
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_channel(cls, channel_id):
        query = "DELETE FROM Canales WHERE id = %s"
        params = (channel_id,)
        DatabaseConnection.execute_query(query, params=params)

