# _*_ coding: utf-8 _*_ 
"""bcMath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin

from Country.views import indexView,BtFoodsView,ajax,BtScinceView,BtCulturalView,BtTouristView,ajax_tourist,BtCountryView,ajax_btCountry,DetailView,MapView,error404View
from User.views import LoginView,RegisterView,ForgetPwView,ChangePwView,LogoutView,PersonalView,UploadView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',indexView.as_view(),name="indexView"),
#用户操作
    url(r'^login/$',LoginView.as_view(),name="LoginView"),
    url(r'^logout/$',LogoutView.as_view(),name="LogoutView"),
    url(r'^register/$',RegisterView.as_view(),name="RegisterView"),
    url(r'^ForgetPw/$',ForgetPwView.as_view(),name="ForgetPwView"),
    url(r'^ChangePw/$',ChangePwView.as_view(),name="ChangePwView"),
    url(r'^PersonalSet/$',PersonalView.as_view(),name="PersonalView"),
#乡村美食
    url(r'^country/Foods/$',BtFoodsView.as_view(),name="BtFoodsView"),
#乡村美景
    url(r'^country/Scinces/$',BtScinceView.as_view(),name="BtScinceView"),
#乡村文化
    url(r'^country/Culturals/$',BtCulturalView.as_view(),name="BtCulturalView"),
#乡村旅游
    url(r'^country/Tourists/$',BtTouristView.as_view(),name="BtTouristView"),
#ajax接口
    url(r'^country/get_ajax/(?P<city>\w+)/(?P<type>\w+)/$',ajax,name="ajax"),
#ajax旅游数据接口
    url(r'^country/get_ajax_tourist/(?P<season>\w+)/$',ajax_tourist,name="ajax_tourist"),
#最美乡村页
    url(r'^country/btCountry/$',BtCountryView.as_view(),name="BtCountryView"),
#ajax获取最美乡村接口
    url(r'^country/get_btCountry/(?P<ids>\d+)/$',ajax_btCountry,name="ajax_btCountry"),
#详情页
    url(r'^country/(?P<Ctype>\w+)/(?P<ids>\d+)/$',DetailView.as_view(),name="DetailView"),
#地图页
    url(r'^country/(?P<Ctype>\w+)/get_maps/(?P<ids>\d+)/$',MapView.as_view(),name="MapView"),
#错误页
    url(r'^country/404/$',error404View.as_view(),name="error404View"),
#头像上传
    url(r'^info/upload/$', UploadView.as_view(), name="info_upload"),
]
