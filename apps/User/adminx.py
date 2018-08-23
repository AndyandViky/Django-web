# _*_ coding: utf-8 _*_ 

import xadmin
from xadmin import views

from User.models import banner,EmailVerifyRecode


class BaseSetting(object): #基础主题设置
    enable_themes=True #自带参数，默认为False
    use_bootswatch=True #自带参数，默认为False


class GlobalSettings(object): #全局设置
    site_title=u'最美乡村' #左上角logo设置
    site_footer=u'最美乡村' #底部logo设置
    menu_style = 'accordion'


class BannerAdmin(object):
    list_display=['title','add_time'] #以这两个标题在xadmin中显示
    search_fields=['title'] #以这title标题在xadmin中搜索
    list_filter=['title','add_time'] #以这这两个标题在xadmin中过滤


class EmailVerifyRecodeAdmin(object):
    list_display=['email'] #以这两个标题在xadmin中显示s
    search_fields=['email'] #以这title标题在xadmin中搜索
    list_filter=['email'] #以这这两个标题在xadmin中过滤


xadmin.site.register(EmailVerifyRecode,EmailVerifyRecodeAdmin)
xadmin.site.register(banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting) #注册主题设置，管理页面上会出现主题选择样式
xadmin.site.register(views.CommAdminView,GlobalSettings) #注册全局内容，左上角和底部logo改变，菜单样式改变（收起）