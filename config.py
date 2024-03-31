
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER= "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS= False
    MAIL_USE_SSL=True
    MAIL_USERNAME="jceanciens@gmail.com"
    MAIL_PASSWORD='conl ccqy jmop yzex'
    APP_MAIL_SUBJECT_PREFIX= '[ajce]'
    APP_MAIL_SENDER= 'Ajce admin <jceanciens@gmail.com>'
    APP_ADMIN=os.environ.get('APP_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, "data-dev.sqlite3")

class TestingConfig:
    TESTING=True
    SQLALCHEMY_DATABASE_URI='sqlite://'

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite3')

config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production' : ProductionConfig,
    'default': DevelopmentConfig
}
