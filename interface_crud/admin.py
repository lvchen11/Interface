from django.contrib import admin

# Register your models here.

# 导入模型user,article
from interface_crud.models import User, Article, Event, Guest

admin.site.register(User)
admin.site.register(Article)
#  通过Admin后台管理用户/用户组非常方便。创建的发布会和嘉宾表同样可以通过Admin后台管理。

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

# admin.site.register(Event)
# admin.site.register(Guest)

