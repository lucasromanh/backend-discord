import mysql
from app.database import DatabaseConnection



class User:

    def __init__(self, id=None, nombre=None, apellido=None, correo=None, nombre_usuario=None, contrasena=None, fecha_nacimiento=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.fecha_nacimiento = fecha_nacimiento

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM Usuarios"
        results = DatabaseConnection.fetch_all(query)
        users = []

        for result in results:
            user = User(
                id=result['id'],
                nombre=result['nombre'],
                apellido=result['apellido'],
                correo=result['correo_electronico'],
                nombre_usuario=result['nombre_usuario'],
                contrasena=result['contrasena'],
                fecha_nacimiento=result['fecha_nacimiento']
            )
            users.append(user)

        return users

    @classmethod
    def get_user(cls, user_id):
        query = "SELECT * FROM Usuarios WHERE id = %s"
        params = (user_id,)
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return User(
                id=result[0],  
                nombre=result[1],
                apellido=result[2],
                correo=result[3],
                nombre_usuario=result[4],
                contrasena=result[5],
                fecha_nacimiento=result[6]
            )
        else:
            return None
        
    @classmethod
    def get_user_by_username(cls, username):
        query = "SELECT * FROM Usuarios WHERE nombre_usuario = %s"
        params = (username,)
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return User(
                id=result[0],
                nombre=result[1],
                apellido=result[2],
                correo=result[3],
                nombre_usuario=result[4],
                contrasena=result[5],
                fecha_nacimiento=result[6]
            )
        else:
            return None
        
    @classmethod
    def create_user(cls, user):
        query = "INSERT INTO Usuarios (nombre, apellido, correo_electronico, nombre_usuario, contrasena, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            user.nombre,
            user.apellido,
            user.correo,
            user.nombre_usuario,
            user.contrasena,
            user.fecha_nacimiento
        )
        cursor = DatabaseConnection.execute_query(query, params=params)

        try:
            if cursor.rowcount == 1:
                user_id = cursor.lastrowid
                return user_id
        except mysql.connector.Error as db_error:
            print(f"Error de base de datos: {db_error}")
            raise db_error

    @classmethod
    def update_user(cls, user):
        query = "UPDATE Usuarios SET nombre = %s, apellido = %s, correo_electronico = %s, nombre_usuario = %s, contrasena = %s, fecha_nacimiento = %s WHERE id = %s"
        params = (
            user.nombre,
            user.apellido,
            user.correo,
            user.nombre_usuario,
            user.contrasena,
            user.fecha_nacimiento,
            user.id
        )
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def authenticate_user(cls, nombre_usuario, contrasena):
        query = "SELECT id FROM Usuarios WHERE nombre_usuario = %s AND contrasena = %s"
        params = (nombre_usuario, contrasena)

        try:
            connection = DatabaseConnection.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                print(f'Query: {cursor.statement}')  

                if result is not None:
                    user_id = result[0]
                    next_result = cursor.fetchone()
                    if next_result is not None:
                        print(f"Advertencia: Se encontraron múltiples resultados para {nombre_usuario}.")
                    return user_id
                else:
                    print('Usuario no encontrado')  
                    return None
        except mysql.connector.Error as db_error:
            print(f"Error de base de datos: {db_error}")
            return None
        except Exception as e:
            print(f"Error al autenticar usuario: {e}")
            return None
        finally:
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    @classmethod
    def delete_user(cls, user_id):
        query = "DELETE FROM Usuarios WHERE id = %s"
        params = (user_id,)
        DatabaseConnection.execute_query(query, params=params)

  
