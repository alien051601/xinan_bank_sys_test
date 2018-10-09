from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def creat_app():
    app = Flask(__name__)
    print('创建app----start')
    return app

# if __name__ == '__main__':
#     creat_app()