#python -m flask --app package run --port 8211 --debug
from flask import Flask

from package import pages
from package import app

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    return app