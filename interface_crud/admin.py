from django.contrib import admin

# Register your models here.

# 导入模型user,article
from interface_crud.models import User, Article

admin.site.register(User)
admin.site.register(Article)
