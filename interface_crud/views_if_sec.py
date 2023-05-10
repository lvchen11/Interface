from django.contrib import auth as django_auth
import base64


# 用户认证
from django.http import JsonResponse


def user_auth(request):
    """

    request.META是一个Python字典，包含了本次HTTP请求的Header信息，
    例如用户认证、IP地址和用户Agent（通常是浏览器的名称和版本号）等。HTTP_AUTHORIZATION用于获取HTTP认证数据。
    如果为空，将到一个空的bytes对象。当客户端传输的认证数据为：admin/admin123456，这里得到的数据为：Basic YWRtaW46YWRtaW4xMjM0NTY=
    """
    get_http_auth = request.META.get('HTTP_AUTHORIZATION', b'')
    """
    通过split()方法将其拆分成list。拆分后的数据为：['Basic','YWRtaW46YWRtaW4xMjM0NTY=']
    """
    auth = get_http_auth.split()
    """
    取出list中的加密串，通过base64对加密字符串进行解码。通过decode()
    方法以UTF - 8
    编码对字符串进行解码。partition()
    方法以冒号“:”为分隔符对字符串进行分隔，得到的数据为：('admin', ':', '111111')。
    """
    try:
        auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')

    except IndexError:
        return "null"
    username, password = auth_parts[0], auth_parts[2]
    user = django_auth.authenticate(username=username, password=password)
    if user is not None:
        django_auth.login(request, user)
        return "success"
    else:
        return "fail"



# # 查询发布会接口---增加用户认证
# def get_event_list(request):
#     auth_result = user_auth(request)  # 调用认证函数
#     if auth_result == "null":
#         return JsonResponse({'status': 10011, 'message': 'user auth null'})
#
#     if auth_result == "fail":
#         return JsonResponse({'status': 10012, 'message': 'user auth fail'})
#
#     eid = request.GET.get("eid", "")  # 发布会id
#     name = request.GET.get("name", "")  # 发布会名称





