# _*_ coding: utf-8 _*_ 

import xadmin
from xadmin import views

from Country.models import CountryNews, CountryFoods, CountryScince, CountryTourist, CountryCultural





class CountryNewsAdmin(object):
    list_display=['title','add_time'] #以这两个标题在xadmin中显示
    search_fields=['title'] #以这title标题在xadmin中搜索
    list_filter=['title','add_time'] #以这这两个标题在xadmin中过滤


class CountryFoodsAdmin(object):
    list_display=['name','add_time'] #以这两个标题在xadmin中显示
    search_fields=['name','city'] #以这title标题在xadmin中搜索
    list_filter=['name','add_time'] #以这这两个标题在xadmin中过滤


class CountryScinceAdmin(object):
    list_display=['name','add_time'] #以这两个标题在xadmin中显示
    search_fields=['name','city'] #以这title标题在xadmin中搜索
    list_filter=['name','add_time'] #以这这两个标题在xadmin中过滤


class CountryTouristAdmin(object):
    list_display=['name','add_time'] #以这两个标题在xadmin中显示
    search_fields=['name','season','city'] #以这title标题在xadmin中搜索
    list_filter=['name','add_time','rank','price','person'] #以这这两个标题在xadmin中过滤


class CountryCulturalAdmin(object):
    list_display=['name','add_time'] #以这两个标题在xadmin中显示
    search_fields=['name','city'] #以这title标题在xadmin中搜索
    list_filter=['name','add_time'] #以这这两个标题在xadmin中过滤
    

xadmin.site.register(CountryNews,CountryNewsAdmin)
xadmin.site.register(CountryFoods,CountryFoodsAdmin)
xadmin.site.register(CountryScince,CountryScinceAdmin)
xadmin.site.register(CountryTourist,CountryTouristAdmin)
xadmin.site.register(CountryCultural,CountryCulturalAdmin)