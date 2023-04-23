from werkzeug.security import generate_password_hash

users = {
        "admin": generate_password_hash("password"),
        "user": generate_password_hash("pass")
    }

WEATHER_API_KEY = "d33e1fd59e0d4d3ca86130130231904"

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weathers.sqlite3'



class ProductionConfig(Config):
    DEBUG = True

