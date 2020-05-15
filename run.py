# /run.py

import os

from src.app import create_app
from dotenv import load_dotenv
import logging

if __name__ == '__main__':

    load_dotenv()
    print(os.getenv('FLASK_ENV'))
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)

    # run app
    port = os.getenv('PORT')
    app.run(port=port)
