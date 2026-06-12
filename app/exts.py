from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

jwt=JWTManager()
migrate=Migrate()
cors=CORS()