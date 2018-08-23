# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django import forms

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nike_name = models.CharField(max_length=10, verbose_name=u"昵称", default="", blank=True, null=True)
    sex = models.CharField(choices=(("male",u"男"), ("female",u"女")), default="男", max_length=6)
    image = models.ImageField(upload_to="static/images/%Y/%m", default="static/images/default.jpg", max_length=100)
    
    class Meta:
        verbose_name=u"用户信息"
        verbose_name_plural = verbose_name
    
    def __unicode__(self):
        return self.username

class EmailVerifyRecode(models.Model):
    code = models.IntegerField(verbose_name=u"邮箱验证码",default=12345)
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),("forget",u"忘记密码")),max_length=8)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural = verbose_name


class banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"标题")
    img = models.ImageField(max_length=100,verbose_name=u"轮播图",upload_to="static/images/banner/%Y/%m")
    url = models.CharField(max_length=100,verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural = verbose_name


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]