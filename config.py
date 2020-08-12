import os
class Config:
    DEBUG =True
class Development(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
class Production(Config):
    DEBUG =False
    SECRET_KEY = os.environ.get("SECRET_KEY") 