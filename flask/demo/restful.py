from flask import Flask
from flask_restful import Resource,Api,reqparse,inputs  # inputs 提供了请求约束中的type更多选择



app = Flask(__name__)
api = Api(app)

class UsersView(Resource):
    # method_decorators = []  # 装饰器列表
    method_decorators = {
        'get': [],
        'post': []
    }  # 有列表和字典两种方式可以进行装饰，列表为当前类视图全局使用，字典为指定到请求方式

    # @api.representation('application/json')  # 定制响应数据类型，参数：响应数据类型，需要修改源码 restful.representations.json
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument('name', type=str, help='error', required=True, location=['args'])
        # 请求参数的约束
        # 第一个参数:参数名，第二个参数：数据类型，第三参数：错误响应，第四个参数：是否必传，第五个参数(location)：请求参数的位置
        args = parse.parse_args()
        return f"get: hello Python {args}"

    def post(self):
        return "post: hello Python"


api.add_resource(UsersView, "/", endpoint='users')  # 路由配置 endpoint　路由别名




