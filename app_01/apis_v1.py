from flask_restful import Resource, reqparse, fields, marshal_with

from app_01.models import User
from app_01.utils import create_uniqu_str
from app_01.ext import mail, cache
from flask import render_template, request
from flask_mail import  Message

public_fields = {
    'code':fields.Integer(default=1),
    'msg':fields.String(default='ok'),
    'data':fields.String()
}

register_parse = reqparse.RequestParser()
register_parse.add_argument('email',required=True,location='form',help='email必填')
register_parse.add_argument('pwd',location='form',help='密码必填')
register_parse.add_argument('confirm_pwd',required=True,location='form',help='确认密码必填')

class RegisterAPI(Resource):

    @marshal_with(public_fields)
    def post(self):
        params = register_parse.parse_args()
        email = params.get('email')
        pwd = params.get('pwd')
        confirm_pwd = params.get('confirm_pwd')

        if pwd != confirm_pwd:
            return {'code':2,'msg':"两次输入的密码不一致"}

        user = User.creat_user(email=email,pwd=pwd)

        print(type(request))

        url = "http://" + request.host + "/active/" + create_uniqu_str()

        if user:

            msg = Message('欢迎注册爱鲜蜂后台管理',
                          [email],
                          sender='2809276444@qq.com')

            msg.html = render_template('active.html', url=url)

            mail.send(msg)

            key = url.split('/')[-1]

            cache.set(key, user.id, timeout=60 * 60)


            return {"data":"/index"}
        else:
            return {'code':3,"msg":'注册失败'}




