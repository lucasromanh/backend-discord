from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config import Config
from app.routes.user_bp import user_bp
from app.routes.server_bp import server_bp
from app.routes.channels_bp import channel_bp
from app.routes.message_bp import message_bp
from app.routes.member_bp import member_bp

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True,
         allow_headers=["Content-Type", "X-Auth-Token", "Origin", "Authorization"],
         allow_methods=["POST", "PUT", "GET", "DELETE", "OPTIONS"],
         max_age=3000)

    app.config['JWT_SECRET_KEY'] = 'discord'  
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)  
    jwt = JWTManager(app)

    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(server_bp, url_prefix='/servers')
    app.register_blueprint(channel_bp, url_prefix='/channels')
    app.register_blueprint(message_bp, url_prefix='/messages')
    app.register_blueprint(member_bp, url_prefix='/members')

    return app
