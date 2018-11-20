from flask import Flask
from app_01 import settings
from app_01.ext import init_ext
from app_01.urls_apis_v1 import init_api
from app_01.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(settings.config.get(env))

    # 初始化第三方插件
    init_ext(app)

    # 注册蓝图
    init_blue(app)

    # 注册restful的路由
    init_api(app)

    return app
