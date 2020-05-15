# /src/config.py

import os
from datetime import timedelta


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    CORS_ORIGIN_WHITELIST = []
    JWT_HEADER_TYPE = 'Token'
    CORS_HEADERS = os.getenv('CORS_HEADERS')
    CACHE_TYPE = 'simple'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10 ** 6)


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    CORS_ORIGIN_WHITELIST = []
    JWT_HEADER_TYPE = 'Token'
    CACHE_TYPE = 'simple'


app_config = {
    'development': Development,
    'production': Production,
}
