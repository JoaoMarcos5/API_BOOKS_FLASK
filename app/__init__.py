from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .routes import book_model
from .models import book_model

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():

        from .models import book_model
        db.create_all()
        
        from .routes import book_model
        app.register_blueprint(book_bp)
       

    return app