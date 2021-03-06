import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # 初始化app配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 扩展初始化配置
    db.init_app(app)

    # TODO:: just import frontend and backend, and the router defined in modules's __init__.py
    from .frontend import article
    app.register_blueprint(article.bp)

    return app
