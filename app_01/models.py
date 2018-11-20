from app_01.ext import db
from app_01.utils import enc_pwd


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(30),
        nullable=True,
    )

    email = db.Column(
        db.String(30),
        unique=True,
        index=True,
    )

    pwd = db.Column(
        db.String(255),
        nullable=False,
    )

    is_active = db.Column(
        db.Boolean,
        nullable=True,
    )

    is_delete = db.Column(
        db.Boolean,
        nullable=True,
    )

    @classmethod
    def creat_user(cls,email,pwd,name=None):
        #判断email是否已经存在
        users = User.query.filter(User.email == email)
        if users.count() > 0:
            # raise Exception('该email已被占用')
            return None
        #密码加密存储
        user_pwd = enc_pwd(pwd)

        #创建用户

        name = name if name else email

        user = cls(
            name = name,
            email = email,
            pwd = user_pwd,
        )

        db.session.add(user)
        db.session.commit()

        return user

    def set_pwd(self,pwd):
        '''
        用于修改密码
        :param pwd:
        :return:
        '''
        if pwd or len(pwd) > 0:
            raise Exception('密码不能为空')
        self.pwd = enc_pwd(pwd)

        db.session.add(self)
        db.session.commit()
        return True

    def check_pwd(self,pwd):
        u_pwd = enc_pwd(pwd)
        if u_pwd == self.pwd:
            return True
        else:
            return False





class Goods(db.Model):
    __tablename__ = "axf_goods"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    productid = db.Column(
        db.String(20)
    )
    productimg = db.Column(
        db.String(255)
    )
    productname = db.Column(
        db.String(130),
        nullable=True
    )
    productlongname = db.Column(
        db.String(190)
    )
    isxf = db.Column(
        db.Boolean,
        default=False
    )
    pmdesc = db.Column(
        db.Integer,
    )
    specifics = db.Column(
        db.String(40)
    )
    price = db.Column(
        db.Numeric(precision=10,scale=2)
    )
    marketprice = db.Column(
        db.Numeric(precision=10, scale=2)
    )
    categoryid = db.Column(
        db.Integer
    )
    childcid = db.Column(
        db.Integer
    )
    childcidname = db.Column(
        db.String(30)
    )
    dealerid = db.Column(
        db.String(30)
    )
    storenums = db.Column(
        db.Integer
    )
    productnum = db.Column(
        db.Integer
    )