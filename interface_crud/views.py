from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
# 增加文章
from interface_crud.models import Article, User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json

# from django.http import HttpResponse,JsonResponse
# from interface_crud.models import User,Article
# import json
#
# #新增文章
# def add_article(request):
#     if request.method == "POST":
#         req = json.loads(request.body)
#         print (req)
#         key_flag = req.get("title") and req.get("content") and len(req)==2
#         #判断请求体是否正确
#         if key_flag:
#             title = req["title"]
#             content = req["content"]
#             #title返回的是一个list
#             title_exist = Article.objects.filter(title=title)
#             #判断是否存在同名title
#             if len(title_exist) != 0:
#                 return JsonResponse({"status":"BS.400","msg":"title aleady exist,fail to publish."})
#
#             '''插入数据'''
#             add_art = Article(title=title,content=content,status="alive")
#             add_art.save()
#             return JsonResponse({"status":"BS.200","msg":"publish article sucess."})
#         else:
#             return  JsonResponse({"status":"BS.400","message":"please check param."})



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, 'index.html')

# 登录动作
def login_action1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            # return HttpResponse('login success!')
            # return HttpResponseRedirect('/event_manage/')
            # cookie
            response = HttpResponseRedirect('/event_manage/')
            # cookie 更类似使用的存折， session类似于银行卡，客户拿到的只是一个银行卡号（即浏览器只保留一个Sessionid），用户的存钱、取钱记录是根据银行卡号保存在银行的系统里（即Web服务器端），只得到一个Sessionid并没有什么意义。
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie,user表示写入浏览器的Cookie名，username代表登陆页输入的用户名，3600代表cookie信息在浏览器I帧hong的保持时间，默认为秒
            # session
            request.session['user'] = username # 将session信息记录到浏览器中
            return response
            # session

        else:
            return render(request, 'index.html', {'error': 'username or passworderror!'})


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

# 发布会管理
@login_required
def event_manage(request):
    # return render(request, 'event_manage.html')
    # cookie
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    # session
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "event_manage.html", {"user": username})  # 通过render将cookie和html页面一起返回。









import hashlib
# 获取token
def get_token(request):
    req = json.loads(request.body)
    uname = req["username"]
    upwd = req["password"]
    if request.method == "POST":
        try:
            print("--------")
            ss = User.objects.get(user_name=uname)
            print(ss)
            tmppwd = User.objects.get(user_name=uname).user_password
            print('=========')
            if upwd == tmppwd:
                md5 = hashlib.md5()
                # 把密码变成一个长度固定的字符串
                md5.update(upwd.encode("utf-8"))
                return JsonResponse({"status": "BS.201", "X-Token": md5.hexdigest()})
            else:
                return JsonResponse({"status": "BS.401", "msg": "username or password may wrong."})

        except User.DoesNotExist:
            return JsonResponse({"status": "BS.500", "msg": "username is not exist."})


# 用户认证
# 四个简单的接口已经可以运行了，但是在发请求之前没有进行鉴权，毫无安全性可言。下面来实现简单的认证机制。需要用到内建模块hashlib，hashlib提供了常见的摘要算法，如MD5，SHA1等。
def user_auth(request):
    token = request.META.get("HTTP_X_TOKEN", b'')
    print("token: ", token)
    if token:
        # 暂时写上 auth 接口返回的数据
        if token == '96e79218965eb72c92a549dd5a330112':
            return "auth_success"
        else:
            return "auth_fail"
    else:
        return "auth_fail"


# 查询文章
def query_article(request):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'GET':
            articles = {}
            query_articles = Article.objects.all()
            print('query_articles: ', query_articles)
            for title in query_articles:
                articles[title.title] = title.status
            return JsonResponse({"status": "BS.200", "all_titles": articles, "msg": "query articles success."})
            print("request.body", request.body)
        else:
            return HttpResponse("方法错误")


def add_article(request):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == "POST":
            # b''
            print('request.body: ', request.body)
            print('request.body: ', type(request.body))
            req_dict = json.loads(request.body)
            print('req_json: ', req_dict)  # {'title': 'dddde', 'content': 'ddd天气真舒服！'}
            print('req_json: ', type(req_dict))
            key_flag = req_dict.get('title') and req_dict.get('content') and len(req_dict) == 2
            print('key_flag: ', key_flag)
            # 判断请求体是否正确
            if key_flag:
                title = req_dict['title']
                content = req_dict['content']
                # title返回的是一个list
                title_exist = Article.objects.filter(title=title)
                # 判断是否存在同名的title
                if len(title_exist) != 0:
                    return JsonResponse({"status": "BS.400", "msg": "title already exist, fail to publish."})

                add_art = Article(title=title, content=content, status='alive')
                add_art.save()
                return HttpResponse(add_art)
                return JsonResponse({"status": "BS.200", "msg": "add article success."})
            else:
                return JsonResponse({"status": "BS.400", "message": "please check param."})
        else:
            return HttpResponse("方法错误，你应该使用POST请求方式")


# 更新文章
def modify_article(request, article_id):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'POST':
            modify_req = json.loads(request.body)
            try:
                article = Article.objects.get(id=article_id)
                print("article", article)
                key_flag = modify_req.get('title') and modify_req.get('content') and len(modify_req) == 2
                if key_flag:
                    title = modify_req['title']
                    content = modify_req['content']
                    title_exist = Article.objects.filter(title=title)
                    if len(title_exist) > 1:
                        return JsonResponse({"status": "BS.400", "msg": "title already exist."})

                    # 更新文章
                    old_article = Article.objects.get(id=article_id)
                    old_article.title = title
                    old_article.content = content
                    old_article.save()
                    return JsonResponse({"status": "BS.200", "msg": "modify article sucess."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to modify."})
        else:
            return HttpResponse("方法错误，你应该使用POST请求方式")


# 删除文章
def delete_article(request, article_id):
    auth_res = user_auth(request)
    if auth_res == "auth_fail":
        return JsonResponse({"status": "BS.401", "msg": "user auth failed."})
    else:
        if request.method == 'DELETE':
            try:
                article = Article.objects.get(id=article_id)
                article_id = article.id
                article.delete()
                return JsonResponse({"status": "BS.200", "msg": "delete article success."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "BS.300", "msg": "article is not exists,fail to delete."})
        else:
            return HttpResponse("方法错误，你应该使用DELETE请求方式")

