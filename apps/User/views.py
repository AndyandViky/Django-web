# _*_ coding: utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View #基类Ｖｉｅｗ用于我们重写view方法
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile,EmailVerifyRecode,banner,UploadImageForm
from Country.models import CountryNews,CountryFoods,CountryTourist,CountryCultural
from .forms import LoginForms,RegisterForms,ForgetForms,ChangePwForms
from utils.email_send import send_forgetPw_email

# Create your views here.

#重载authenticate方法自己判断user是否存在并且密码匹配
class CustoBomBackend(ModelBackend):
    def authenticate(self,username=None,password=None,**kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#登录
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = LoginForms(request.POST)
        if login_form.is_valid():  
            username = request.POST.get('username',"")
            password = request.POST.get('password',"")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                preview_news = CountryNews.objects.all()[:7]
                banners = banner.objects.all()
                preview_cat = CountryFoods.objects.all()[:8]
                preview_cultural = CountryCultural.objects.all()[:8]
                preview_tourist = CountryTourist.objects.all()[:8]
                return render(request,"FirstPage.html",{'preview_news':preview_news,'banners':banners,'preview_cat':preview_cat,'preview_cultural':preview_cultural,'preview_tourist':preview_tourist})
            else:
                error_info="用户不存在或者密码错误！"
                return render(request,"login.html",{"error_info":error_info})
        else:
            return render(request,"login.html",{"login_form":login_form})

#退出
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect("/")

#注册
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            username = request.POST.get('username',"")
            email = request.POST.get('email',"")
            if UserProfile.objects.filter(email=email):
                return render(request,'register.html',{"error_info":"用户已存在！"})
            password1 = request.POST.get('password1',"")
            password2 = request.POST.get('password2',"")
            UserProfile.objects.create(username=username,email=email,password=make_password(password1))
            return render(request,'login.html',{})
        else:
            return render(request,"register.html",{"register_form":register_form})

#忘记密码
class ForgetPwView(View):
    def get(self,request):
        return render(request,'forgetPw.html')

    def post(self,request):
        forget_forms = ForgetForms(request.POST)
        if forget_forms.is_valid():
            email = request.POST.get('email',"")
            if UserProfile.objects.filter(email=email):
                send_forgetPw_email(email,'forget')
                return render(request,'changePw.html',{})
            else:
                return render(request,'forgetPw.html',{"error_info":"用户不存在！"})
        else:
            return render(request,"forgetPw.html",{"forget_forms":forget_forms})

#修改密码
class ChangePwView(View):
    def post(self,request):
        changePw_forms = ChangePwForms(request.POST)
        if changePw_forms.is_valid():
            cphche = request.POST.get('cphche',"")
            if EmailVerifyRecode.objects.filter(code=cphche):
                email_code = EmailVerifyRecode.objects.get(code=cphche)
                user = UserProfile.objects.get(email=email_code.email)
                password = request.POST.get('password1',"")
                user.password=make_password(password)
                user.save()
                return render(request,'login.html',{})
            else:
                return render(request,"changePw.html",{"error_info":"验证码错误！"})
        else:
            return render(request,"changePw.html",{"changePw_forms":changePw_forms})

#个人信息
class PersonalView(View):
    def get(self,request):
        return render(request,'personalSet.html',{})

    
class UploadView(LoginRequiredMixin, View):
    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data["image"]
            if image != "static/images/default.jpg":
                request.user.image = image
            username = request.POST.get('username',"")
            nike_name = request.POST.get('nike_name',"")
            sex = request.POST.get('sex',"")
            email = request.POST.get('email',"")
            request.user.username = username
            request.user.nike_name = nike_name
            request.user.sex = sex
            request.user.email = email
            request.user.save()
            return render(request,'personalSet.html')
        
