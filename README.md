# Proyecto de Cátedra de Programación 2 - UPATECO

## Tabal de contenido
- [Proyecto de Cátedra de Programación 2 - UPATECO](#proyecto-de-cátedra-de-programación-2---upateco)
  - [Tabal de contenido](#tabal-de-contenido)
  - [Descripcio del proyecto](#descripcio-del-proyecto)
  - [Integrantes](#integrantes)
  - [Instalación](#instalación)
    - [Requisitos previos](#requisitos-previos)
    - [Pasos de instalación](#pasos-de-instalación)
    - [Crear y activar un entorno virtual (opcional pero recomendado)](#crear-y-activar-un-entorno-virtual-opcional-pero-recomendado)
    - [Instalar las dependencias desde el archivo](#instalar-las-dependencias-desde-el-archivo)
    - [Ejecutar la aplicación](#ejecutar-la-aplicación)
  - [Rutas de la API](#rutas-de-la-api)
    - [Users](#users)
    - [Servers](#servers)
    - [Mensajes](#mensajes)
    - [Channels](#channels)
    - [Miembros del Servidor](#miembros-del-servidor)
  - [Ejecutar Pruebas](#ejecutar-pruebas)
  - [Contribuir](#contribuir)
  - [Licencia](#licencia)


***
## Descripcio del proyecto
Este proyecto es un clon de Discord desarrollado como parte de la cátedra de Programación 2 en la Universidad Provincial de Administración, Tecnología y Oficios (UPATECO). Utiliza Python con Flask como API REST para conectar un frontend a la API.

***
## Integrantes

- Roman Lucas Daniel
- Herrera Natalia Camila

***
## Instalación

Para ejecutar el programa, sigue los siguientes pasos:

***
### Requisitos previos

- Python 3.x instalado
- Entorno virtual (opcional pero recomendado)

***
### Pasos de instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   cd nombre_del_repositorio

***
### Crear y activar un entorno virtual (opcional pero recomendado)
1. Activar:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   venv\Scripts\activate  

***
### Instalar las dependencias desde el archivo 
1. Instalar
   `requirements.txt`
   ```bash
   pip install -r requirements.txt

***
### Ejecutar la aplicación

1. Ejecutar
   ```bash
   python app.py
   La aplicación debería estar ahora en funcionamiento en http://localhost:5000/

***
## Rutas de la API

A continuación, se presentan las rutas de la API junto con una breve descripción de su funcionalidad:

***
### Users

- `POST /users`: Registrar un nuevo usuario.
- `POST /users/login`: Iniciar sesión de usuario.
- `POST /users/registro`: Registrar un nuevo usuario.
- `PUT /users/update/<int:user_id>`: Actualizar información de usuario.
- `PUT /users/update//<string:username>`: Actualizar información de usuario por username.
- `GET /users/<int:user_id>`: Obtener información de usuario.
- `DELETE /users/<int:user_id>`: Eliminar un usuario.
- `GET /users`: Obtener la lista de usuarios.
- `GET /users//<string:username>`: Obtener usuarios por username.

***
### Servers

- `POST /servers/create`: Crear un nuevo servidor.
- `PUT /servers/<int:server_id>`: Actualizar información de servidor.
- `GET /servers`: Obtener la lista de servidores.
- `DELETE /servers/<int:server_id>`: Eliminar un servidor.

***
### Mensajes

- `POST /messages`: Crear un nuevo mensaje.
- `PUT /messages/<int:message_id>`: Actualizar un mensaje.
- `GET /messages`: Obtener la lista de mensajes.
- `GET /messages/<int:message_id>`: Obtener un mensaje específico.
- `DELETE /messages/<int:message_id>`: Eliminar un mensaje.

***
### Channels

- `POST /channels`: Crear un nuevo canal.
- `PUT /channels/<int:channel_id>`: Actualizar información de canal.
- `DELETE /channels/<int:channel_id>`: Eliminar un canal.
- `GET /channels/<int:channel_id>/messages`: Obtener los mensajes de un canal.

***
### Miembros del Servidor

- `POST /members/add`: Agregar un miembro a un servidor.
- `DELETE /members/<int:member_id>`: Eliminar un miembro de un servidor.
- `GET /members/server/<int:server_id>`: Obtener la lista de miembros de un servidor.

***
## Ejecutar Pruebas

Para ejecutar pruebas, puedes utilizar la suite de pruebas de Python. Asegúrate de haber instalado las dependencias de desarrollo antes de ejecutar las pruebas.

1. Usar
   ```bash
   pytest

***
## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Crea un fork del repositorio en GitHub.
2. Clona tu fork en tu máquina local.
3. Crea una nueva rama para tus cambios.
4. Haz tus modificaciones y realiza commits.
5. Envía tus cambios a tu fork en GitHub.
6. Abre un pull request para que tus cambios sean revisados.

Gracias por contribuir!
***
## Licencia

**Saltacoders.com
Copyrigth (c) 2023**