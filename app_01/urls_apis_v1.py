from flask_restful import Api
from app_01.apis_v1 import *

# 初始化
api = Api()

# 绑定app
def init_api(app):
    api.init_app(app)

# 下边注册各种路由
api.add_resource(RegisterAPI, "/apis_v1/register")
