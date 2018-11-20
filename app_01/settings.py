from os import environ
import os

CACHES = {
    "default": {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": "redis://127.0.0.1:6379/7"
    },
    "debug:": {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": "redis://127.0.0.1:6379/8"
    }
}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(conf):
    uri = "{backend}+{engine}://{user}:{pwd}@{ip}:{port}/{db}".format(
        backend=conf.get("backend"),
        engine=conf.get("engine"),
        user=conf.get("user"),
        pwd=conf.get("pwd"),
        ip=conf.get("host"),
        port=conf.get("port"),
        db=conf.get("db")
    )
    return uri

class Config:
    DEBUG = False
    ONLINE = False

    SECRET_KEY = "sadjklasfhui3728ry?<?>LKPOJ"

    SESSION_TYPE = 'redis'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '2809276444@qq.com'
    MAIL_PASSWORD = 'udfumdkgeqledeja'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME





class DebugConfig(Config):
    DEBUG = True
    DATA_BASE = {
        'engine':'pymysql',
        'backend': 'mysql',
        'host': '127.0.0.1',
        'port': 3306,
        'user': environ.get("DB_USERNAME"),
        'pwd': environ.get("DB_PASSWORD"),
        'db': 'db_axf_dev'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATA_BASE)


config = {
    'debug': DebugConfig
}