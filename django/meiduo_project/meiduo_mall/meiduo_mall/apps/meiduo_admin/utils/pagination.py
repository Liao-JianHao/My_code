# from collections import OrderedDict
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
#
# class StandardResultPagination(PageNumberPagination):
#     page_size = 1
#     page_size_query_param = 'pagesize'
#     max_page_size = 5
#
#     def get_paginated_response(self, data):
#         """{
#             "counts": "用户总量",
#             "lists": [
#                 {
#                     "id": "用户id",
#                     "username": "用户名",
#                     "mobile": "手机号",
#                     "email": "邮箱"
#                 },
#                 ...
#             ],
#             "page": "页码",
#             "pages": "总页数",
#             "pagesize": "页容量"
#         }
#         """
#         return Response(OrderedDict([
#             ('count', self.page.paginator.count),
#             ('lists', data),
#             ('page', self.page.number),
#             ('pages', self.page.paginator.num_pages),
#             ('pagesize', self.get_page_size(self.request))
#         ]))
#
#
#
#


from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response


class StandardResultPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'pagesize'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('lists', data),
            ('page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('pagezise', self.get_page_size(self.request))
        ]))