# from flask_restful import fields
#
# one_fields = {
#     "id": fields.Integer,
#     # "title": fields.String
#     "name": fields.String(attribute="title"),
#     "hehe": fields.String(default="lalala")
# }
#
# # {
# #     "name":"hehe",
# #     "hobby":[
# #         "抽烟",
# #         "喝酒",
# #         "推车"
# #     ]
# # }
# two_fields = {
#     "name": fields.String(default="tom"),
#     # 列表 里是字符串
#     "hobby": fields.List(fields.String)
# }
#
# # {
# #     "data":{
# #         "id":1,
# #         "hehe":"lalala",
# #         "name":"震惊1下课是不可能"
# #     },
# #     "msg":"OK",
# #     "code":1
# # }
# three_fields = {
#     "code": fields.Integer(default=1),
#     "msg": fields.String(default="OK"),
#     "data": fields.Nested(one_fields)
# }
#
# # {
# #     "data":[
# #         {
# #             "name":"震惊6下课是不可能",
# #             "hehe":"lalala",
# #             "id":6
# #         },
# #         {
# #             "name":"震惊7下课是不可能",
# #             "hehe":"lalala",
# #             "id":7
# #         }
# #     ],
# #     "code":2,
# #     "msg":"OK"
# # }
# # four_fields = {
# #     "code": fields.Integer(default=1),
# #     "msg": fields.String(default="OK"),
# #     "data": fields.List(fields.Nested(one_fields))
# # }
# four_fields = three_fields
# four_fields["data"] = fields.List(fields.Nested(one_fields))
# four_fields.pop("msg")
