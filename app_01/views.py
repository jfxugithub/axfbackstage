from flask import Blueprint, render_template, request, json, redirect, url_for
from flask.json import jsonify

from app_01.ext import cache
from .models import *
blue = Blueprint("axfbg",__name__)

def init_blue(app):
    app.register_blueprint(blue)


public_res = {
    'code':0,
    'msg':'',
    'data':''
}

##视图函数
@blue.route('/',methods=["GET","DELETE","POST"])
def item_view():

    if request.method == "GET":
        params = request.args

        page = params.get("page")
        page = int(page) if page else 1

        pre_page = params.get("pre_page")
        pre_page = int(pre_page) if pre_page else 20

        name = params.get("name")

        if name:
            pagination = Goods.query.filter(Goods.productlongname.contains(name)).paginate(page=page,per_page=pre_page)
        else:
            pagination = Goods.query.paginate(page=page,per_page=pre_page)

        return render_template('item/item.html', pagination=pagination)

    elif request.method == "DELETE":
        params = json.loads(request.get_data())

        goods_id = params.get("id")

        goods = Goods.query.get(goods_id)

        db.session.delete(goods)
        db.session.commit()

        public_res["code"]=0
        public_res["msg"] = '删除成功'
        public_res["data"] = '/'

        return jsonify(public_res)

    elif request.method == "POST":
        params = request.form
        goods = Goods.query.get(params.get('id'))

        goods.price = params.get('price')
        goods.productid = params.get('productid')
        goods.productlongname = params.get('name')
        goods.productimg = params.get('img')
        goods.storenums = params.get('goodsnum')

        db.session.add(goods)
        db.session.commit()

        return redirect(url_for("axfbg.item_view"))


@blue.route('/order_manage')
def order_manager():
    return render_template("order/order_index.html")

@blue.route('/nosale')
def nosale():
    return render_template('nosale/nosale.html')

@blue.route('/auto_bh')
def auto_bh():
    return render_template('auto/auto.html')

@blue.route('/index')
def index():
    return render_template('index/index.html')

@blue.route('/register')
def register_view():
    return render_template("register/register.html")

@blue.route('/active/<string:key>')
def active_verify(key):
    u_id = cache.get(key)

    user = User.query.get(u_id)

    if user :
        user.is_active = True
        db.session.add(user)
        db.session.commit()
        return "<h3>%s 激活成功 </h3>" % user.email
    else:
        return "<h3>激活失败</>"