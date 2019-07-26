#!/usr/bin/python3
# python version:   Python 3.6
# System version:   Linux
# The date of:      19-6-11 下午5:25
# The author:       小喂喂  
# IDE:              PyCharm


from flask import Blueprint


app_info = Blueprint('app_info', __name__, template_folder="templates", url_prefix='/user')


from .views import get_info,print_json,upload_photo