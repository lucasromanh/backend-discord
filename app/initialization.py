from app.models.server_models import Server
from app.models.channel_models import Channel

def initialize_servers_and_channels():
    servidores_predefinidos = [
        {"nombre": "Literatura"},
        {"nombre": "Cine"},
        {"nombre": "Viajes"},
        {"nombre": "Salud y Bienestar"},
        {"nombre": "Gaming"},
        {"nombre": "Deportes"},
        {"nombre": "Música"}
    ]

    for servidor_data in servidores_predefinidos:
        servidor = Server(nombre=servidor_data["nombre"])
        server_id = Server.create_server(servidor)

        canales_predefinidos = [
            {"nombre": "General", "server_id": server_id},
            {"nombre": "Discusión", "server_id": server_id},
            {"nombre": "Eventos", "server_id": server_id}
        ]

        for canal_data in canales_predefinidos:
            canal = Channel(nombre=canal_data["nombre"], server_id=canal_data["server_id"])
            Channel.create_channel(canal)
