from flask import Flask
from flask_cors import CORS
from routes.detect import detect_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(detect_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
