import logging
from logging.handlers import RotatingFileHandler
from apiflask import APIFlask
from .exts import migrate,cors,jwt,login_manager,bcrypt
from .db import db
from config import get_config
from .view import UrlView,Authview,MainBp
import uuid
from .model  import User


def create_app():
    
    
    app=APIFlask(__name__,template_folder="templates")
    
    # config app
    app.config.from_object(get_config())

    # init extension

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)

    # log files

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s dans %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(), # Sortie Console
            RotatingFileHandler("app.log", maxBytes=1_000_000, backupCount=3) # Fichier
        ]
    )

    # add routes
    
    # protection
    login_manager.login_view="auth.sign"
    
    # load user
    @login_manager.user_loader
    def load(id):
        return User.query.get(uuid.UUID(id))

    app.register_blueprint(UrlView,url_prefix='/url')
    app.register_blueprint(Authview,url_prefix='/')
    app.register_blueprint(MainBp,url_prefix='/')

    return app