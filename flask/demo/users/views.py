#!/usr/bin/python3
# python version:   Python 3.6
# System version:   Linux
# The date of:      19-6-11 下午5:26
# The author:       小喂喂  
# IDE:              PyCharm


from . import app_info
from flask import render_template, request, jsonify,redirect,make_response






@app_info.route('/get_info')
def get_info():
    name = 'Mr.C'
    # return render_template("info.html", str_name=name)  # 模板渲染

    # return redirect('http://www.c-blogs.cn')  # 重定向

    info = make_response('make_response测试数据')
    info.headers['name'] = 'Mr.C'
    info.status = '404 not found'
    return info  # 构造响应

@app_info.route('/json')
def print_json():
    json_dict = {
        'name': 'hello'
    }
    return jsonify(json_dict)


@app_info.route('/upload', methods=['POST'])
def upload_photo():
    """上传图片"""
    photo = request.files['img']
    photo.save('./demo.jpg')
    return "upload success"
