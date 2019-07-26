#!/usr/bin/python3
# python version:   Python 3.6
# System version:   Linux
# The date of:      19-6-12 下午4:56
# The author:       小喂喂  
# IDE:              PyCharm


from flask import Flask,abort,g


app = Flask(__name__)

# @app.before_first_request
# def before_first_request():
#     """在第一次请求之前调用"""
#     pass

@app.before_request
def before_request():
    """在每一次请求之前调用"""
    # g.user_name = 123456
    g.user_name = None

# @app.after_request
# def after_request():
#     """执行完视图函数之后会调用"""
#     pass
#
# @app.teardown_request
# def teardown_request():
#     """每一次请求之后都会调用"""
#     pass


def login_username(func):
    def wrapper(*args, **kwargs):
        if g.user_name:
            return func()
        # if g.user_name is not None:
        #     return func(*args, **kwargs)
        else:
            abort(404)
    return wrapper


@app.route('/')
def login():
    return f"用户名：{g.user_name}"

@app.route('/userinfo')
@login_username
def login_info():
    return f"用户名：{g.user_name}"