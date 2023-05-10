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


# 开发接口 签名代码
import time, hashlib
# 用户签名+时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time', '')  # 客户端时间戳
        client_sign = request.POST.get('sign', '')  # 客户端签名
    else:
        return "error"

    if client_time == '' or client_sign == '':
        return "sign null"

        # 服务器时间
    now_time = time.time()  # 例：1466426831
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"

        # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    server_sign = md5.hexdigest()

    if server_sign != client_sign:
        return "sign fail"
    else:
        return "sign success"








