from dotenv import load_dotenv  
from app import init_app
load_dotenv()

if __name__ == "__main__":
    app = init_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
