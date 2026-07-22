import os 
from dotenv import load_dotenv
from datetime import timedelta

basedir=os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,".env"))

env=os.getenv("APP_ENV","dev")

class Config:
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=3)
    API_TITLE="backend"
    API_VERSION="V1"
    SECRET_KEY=os.getenv("JWT_SECRET_KEY","secret_key")

class DeveloppementConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///test2.db"
    DEBUG=True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_URI")
    DEBUG=False

configs={
    "dev":DeveloppementConfig,
    "prod":ProductionConfig

}

def get_config()->Config:
    return configs.get(env,DeveloppementConfig)