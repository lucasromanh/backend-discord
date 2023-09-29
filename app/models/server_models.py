from mysqlx import DatabaseError
from app.database import DatabaseConnection
import mysql.connector


class Server:

    def __init__(self, id=None, nombre=None, descripcion=None, fecha_creacion=None, user_id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.user_id = user_id 

    @classmethod
    def get_all_servers(cls):
        query = "SELECT * FROM Servidores"
        results = DatabaseConnection.fetch_all(query)
        servers = []

        for result in results:
            server = Server(
                id=result['id'],
                nombre=result['nombre'],
                descripcion=result['descripcion'],
                fecha_creacion=result['fecha_creacion']
            )
            servers.append(server)

        return servers

    @classmethod
    def get_server(cls, server_id):
        query = "SELECT * FROM Servidores WHERE id = %s"
        params = (server_id,)

        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="micram123",
                database="discord"
            )

            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchone()

            if result is not None:
                return Server(
                    id=result['id'],
                    nombre=result['nombre'],
                    descripcion=result['descripcion'],
                    fecha_creacion=result['fecha_creacion']
                )
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def create_server(cls, server):
        query = "INSERT INTO Servidores (nombre, descripcion, fecha_creacion) VALUES (%s, %s, %s)"
        params = (
            server.nombre,
            server.descripcion,
            server.fecha_creacion
        )
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 1:
            server_id = cursor.lastrowid
            return server_id
        else:
            raise DatabaseError("No se pudo crear el nuevo servidor")

    @classmethod
    def update_server(cls, server):
        query = "UPDATE Servidores SET nombre = %s, descripcion = %s WHERE id = %s"
        params = (
            server.nombre,
            server.descripcion,
            server.id
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete_server(cls, server_id):
        query = "DELETE FROM Servidores WHERE id = %s"
        params = (server_id,)
        DatabaseConnection.execute_query(query, params=params)
