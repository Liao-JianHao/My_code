from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime



class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.47.157/toutiao'  # MYSQL的连接方式
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 数据追踪修改
    SQLALCHEMY_ECHO = False  # 是否显示SQL语句

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Hero(db.Model):
