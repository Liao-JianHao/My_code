#!/usr/bin/python3
# python version:   Python 3.6
# System version:   Linux
# The date of:      19-6-11 下午2:46
# The author:       小喂喂  
# IDE:              PyCharm


from flask import Flask
from users import app_info
from werkzeug.routing import BaseConverter  # 转换器


class MobileConverter(BaseConverter):
    """自定义转换器(手机)"""
    regex = r'1[3-9]\d{9}'



def create_flask_app(config):
    """创建工厂"""

    # static_folder 静态文件夹名
    # template_folder  模板文件夹名
    # static_url_path  # 路径访问前缀
    app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path=None)

    # 指定配置对象
    app.config.from_object(config)

    # 制定环境变量名，如果没有保持沉默(silent)
    # 终端输入：export PROJECT_CONFIG=setting.py
    app.config.from_envvar('PROJECT_CONFIG', silent=True)

    # 指定配置文件
    # app.config.from_pyfile('setting.py')
    return app

class DefaultConfig:
    """默认配置"""
    SECRET_KEY = ""

class ProductionConfig(DefaultConfig):
    """生产环境配置"""
    DEBUG = False


class DevelopmentConfig(DefaultConfig):
    """开发环境配置"""
    DEBUG = True


app = create_flask_app(DevelopmentConfig)  # 使用工厂创建app对象
app.register_blueprint(app_info)  # 蓝图注册

# app.route('/get_info')(get_info)  # 不使用蓝图，采用后装饰

app.url_map.converters['mobile'] = MobileConverter  # 手机号码转换器


@app.route('/get_mobile/<mobile:num>')
def get_mobile(num):
    """获取手机号"""
    return "{}".format(num)


@app.route("/", methods=["GET"])
def index():
    # rule_list = app.url_map.iter_rules()  # 路由规则映射的迭代器
    print({rule.endpoint: rule.rule for rule in app.url_map.iter_rules()})

    print(app.config.get('SECRET_KEY'))
    print(app.config.get('DEBUG'))
    return "hello flask"


# if __name__ == '__main__':
#     app.run()
