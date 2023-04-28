from django.db import models

# Create your models here.

# interface_crud.models.py

from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=100)
    # active inactive
    status = models.CharField(max_length=10)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # delete alive
    status = models.CharField(max_length=10)


# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会标题
    limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地址
    start_time = models.DateTimeField('events time')  # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取 # 当前时间）

    def __str__(self):
        return self.name

    # 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 关联发布会id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)  # 手机号
    email = models.EmailField()  # 邮箱
    sign = models.BooleanField()  # 签到状态
    # contract = models.ForeignKey(Event, on_delete=models.CASCADE)


    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）


class Meta:
    unique_together = ("event", "phone")


def __str__(self):
    return self.realname


