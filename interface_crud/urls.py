from django.urls import path
from interface_crud import views_if, views_if_sec

urlpatterns = [
    # interface_crud system interface:
    # path('add_event/', include('sign.urls', namespace="sign")),
    # 接口发布会 /api/add_event
    path('add_event/', views_if.add_event, name='add_event'),
    # 接口嘉宾签到 /api/add_guest
    path('add_guest/', views_if.add_guest, name='add_guest'),
    # 获取发布会接口列表数据
    path('get_event_list/', views_if.get_event_list, name='get_event_list'),
    # 获取嘉宾签到接口列表数据
    path('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    # 获取用户签到信息
    path('user_sign/', views_if.user_sign, name='user_sign'),


    # 开发带Auth接口
    path('sec_get_event_list/', views_if.get_event_list, name='get_event_list'),
    #  开发接口签名 发布会接口
    path('sec_add_event/', views_if.add_event, name='add_event'),


]
# from django.urls import path
#
# from interface_crud import views_if
#
# urlpatterns = [
#     # sign system interface:
#     # ex : /api/add_event/
#     # url(r'^add_event/', views_if.add_event, name='add_event'),
#     # ex : /api/add_guest/
#     # url(r'^add_guest/', views_if.add_guest, name='add_guest'),
#     # ex : /api/get_event_list/
#     path('get_event_list/', views_if.get_event_list, name='get_event_list'),
#     # ex : /api/get_guest_list/
#     # url(r'^get_guest_list/', views_if.get_guest_list, name = 'get_guest_list'),
#     # ex : /api/user_sign/
#     # url(r'^user_sign/', views_if.user_sign, name='user_sign'),
# ]
