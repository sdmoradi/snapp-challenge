class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = True