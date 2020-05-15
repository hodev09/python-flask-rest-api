# src/app.py

import os
from flask import Flask
from flask_cors import CORS
from .config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint  # import user api


def create_app(env_name):
    """
    Create app
    """
    try:

        # app initialization
        app = Flask(__name__)
        CORS(app, supports_credentials=True)
        app.config.from_object(app_config[env_name])
        app.config['CORS-HEADERS'] = app_config[env_name].CORS_HEADERS

        # initailize bcrypt
        bcrypt.init_app(app)

        # initailize db
        db.init_app(app)

        app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

        return app

    except Exception as e:
        print('Some error', e.__doc__)
