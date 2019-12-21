# -*- coding: utf-8 -*-
# @Author: Rootrl
# @Date: 2019-12-21 13:42:41

import os

from time import strftime
import logging

log_name = os.path.join(
    os.getenv('HOME'), 'log/flask/log_{}.log'.format(strftime('%Y%m%d')))

FLASK_LOG_FILE = os.getenv('FLASK_LOG_FILE') or log_name

if not os.path.exists(os.path.dirname(FLASK_LOG_FILE)):
    os.makedirs(os.path.dirname(FLASK_LOG_FILE))


def get_handler():

    # 获取处理器
    f_handler = logging.FileHandler(FLASK_LOG_FILE, encoding='utf-8')
    formatter = logging.Formatter(
        '[%(asctime)s %(filename)s:%(lineno)s] - %(message)s')
    f_handler.setFormatter(formatter)
    f_handler.setLevel(logging.DEBUG)

    return f_handler


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = '.md'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can you guess it'
    DEBUG = True
    # sqlalchemy format: mysql+pymysql://username:password@host/database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost/flask_project?charset=utf8'
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        # app.logger.setLevel(logging.DEBUG)
        # app.logger.addHandler(get_handler)
        pass


class DevelopmentConfig(Config):
    """开发环境
    """
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost/flask_project?charset=utf8'


class TestConfig(Config):
    """测试环境
    """

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost/flask_project?charset=utf8'


class ProductionConfig(Config):
    """生产环境
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@localhost/flask_project?charset=utf8'


# 设置配置映射
config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
