import os


class AppConfig:
    SQLALCHEMY_DATABASE_URI = os.environ["DB_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
