# from flask_restful import reqparse
#
# my_params = reqparse.RequestParser()
# my_params.add_argument("name", dest="my_name") #给 ‘name’参数改名
# my_params.add_argument("id", type=int, required=True, help="id 是必填字段 int类型")
# my_params.add_argument("hobby", required=True, action="append") #解析一个参数多个值
#
#
# two_args = reqparse.RequestParser()
# # 指定解析的位置是form
# two_args.add_argument("name", location=["form", "args"])
#
# three_args = my_params.copy()
# three_args.replace_argument("id", help="我是新的")
# three_args.remove_argument("hobby") #移出
# three_args.remove_argument("name")
# three_args.add_argument("age", required=True, type=int, choices=[18,19, 20])
# # 现在参数还剩id age