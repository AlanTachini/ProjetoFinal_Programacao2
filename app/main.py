from flask import Flask
from config import FLASK

def create_app():
    app = Flask(__name__)
    app.secret_key = FLASK["secret_key"]

    return app