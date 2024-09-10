import os

class Config:
    SECRET_KEY = os.urandom(24)



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://ahmedn:ahmed123@localhost:5432/lab4'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://ahmedn:ahmed123@localhost:5432/lab4'

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}