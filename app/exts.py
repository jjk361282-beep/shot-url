from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

jwt=JWTManager()
migrate=Migrate()
cors=CORS()
login_manager=LoginManager()
bcrypt=Bcrypt()