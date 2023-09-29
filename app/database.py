import mysql.connector

class DatabaseConnection:
    _connection = None
    _config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'micram123',
        'port': '3306',
        'database': 'discord'
    }

    @classmethod
    def get_connection(cls):
        try:
            if cls._connection is None or not cls._connection.is_connected():
                cls._connection = mysql.connector.connect(**cls._config)
            return cls._connection
        except mysql.connector.Error as err:
            print(f"Error al conectar con la base de datos: {err}")
            raise

    @classmethod
    def execute_query(cls, query, params=None):
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close() 
            return cursor
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            raise

    @classmethod
    def fetch_all(cls, query, params=None):
        try:
            connection = cls.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            
            return results
        except mysql.connector.Error as err:
            print(f"Error al obtener resultados: {err}")
            raise


    @classmethod
    def fetch_one(cls, query, params=None):
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error al obtener resultado único: {err}")
            raise

    @classmethod
    def close_connection(cls):
        if cls._connection is not None and cls._connection.is_connected():
            cls._connection.close()
