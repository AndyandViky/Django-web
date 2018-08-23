# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime


from django.db import models

# Create your models here.


class CountryNews(models.Model):
    title = models.CharField(max_length=100,verbose_name=u"乡村新闻标题")
    href = models.CharField(max_length=300,verbose_name=u"链接")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"乡村新闻"
        verbose_name_plural = verbose_name


class baseCountry(models.Model):
     detail = models.CharField(max_length=300,verbose_name=u"详情")
     city = models.CharField(max_length=10,verbose_name=u"城市")
     href = models.CharField(max_length=300,verbose_name=u"链接")
     add_time = models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")
     detailDress = models.CharField(max_length=100,verbose_name=u"详细地址",default="")
     phone = models.CharField(max_length=12,verbose_name=u"电话",default="0598-7833822")
     
     class Meta:
         abstract = True


class CountryFoods(baseCountry):
     image = models.ImageField(max_length=100,verbose_name=u"美食图片",upload_to="static/images/%Y/%m", default=u"/static/images/default.jpg")
     name = models.CharField(max_length=20,verbose_name=u"美食名")
     price = models.CharField(max_length=20,verbose_name=u"价格",default="30")
     kinds_of = models.CharField(max_length=10,verbose_name=u"类型",default="美食")
     
     class Meta:
        verbose_name=u"乡村美食"
        verbose_name_plural = verbose_name


class CountryScince(baseCountry):
     image = models.ImageField(max_length=100,verbose_name=u"景色图片",upload_to="static/images/%Y/%m", default=u"/static/images/default.jpg")
     name = models.CharField(max_length=20,verbose_name=u"景色名")
     mark = models.CharField(max_length=1,verbose_name=u"乡村标记",default="F")
     kinds_of = models.CharField(max_length=10,verbose_name=u"类型",default="乡村风景")

     class Meta:
        verbose_name=u"乡村景色"
        verbose_name_plural = verbose_name


class CountryTourist(baseCountry):
     image = models.ImageField(max_length=100,verbose_name=u"旅游景色图片",upload_to="static/images/%Y/%m", default=u"/static/images/default.jpg")
     name = models.CharField(max_length=20,verbose_name=u"旅游景色名")
     season = models.CharField(max_length=6,verbose_name=u"季节")
     rank = models.CharField(max_length=2,verbose_name=u"等级")
     price = models.IntegerField(default=0,verbose_name=u"价格")
     person = models.IntegerField(default=0,verbose_name=u"人气")
     kinds_of = models.CharField(max_length=10,verbose_name=u"景点类型",default="山峰")
     open_time = models.CharField(max_length=100,verbose_name=u"开放时间",default="夏季：07:30~15:30 冬季：07:30~15:00")

     class Meta:
        verbose_name=u"乡村旅游"
        verbose_name_plural = verbose_name


class CountryCultural(baseCountry):
     image = models.ImageField(max_length=100,verbose_name=u"文化图片",upload_to="static/images/%Y/%m", default=u"/static/images/default.jpg")
     name = models.CharField(max_length=20,verbose_name=u"文化名")
     kinds_of = models.CharField(max_length=10,verbose_name=u"类型",default="乡村文化")

     class Meta:
        verbose_name=u"乡村文化"
        verbose_name_plural = verbose_name

