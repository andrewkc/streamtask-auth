
import os
from dotenv import load_dotenv
import dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env' )
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

class ProductionConfig(Config):
    pass
