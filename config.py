from werkzeug.security import generate_password_hash

users = {
        "admin": generate_password_hash("password"),
        "user": generate_password_hash("pass")
    }

class Config(object):
    DEBUG = False
    TESTING = False



class ProductionConfig(Config):
    DEBUG = True

