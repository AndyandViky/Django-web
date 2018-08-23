# _*_ coding: utf-8 _*_ 
from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from django.core.files.base import ContentFile
from random import Random    


from .models import CountryScince,CountryNews,CountryFoods,CountryTourist,CountryCultural
from User.models import banner

# Create your views here.

#主页
class indexView(View):
    def get(self,request):
        preview_news = CountryNews.objects.all()[:7]
        banners = banner.objects.all()
        preview_cat = CountryFoods.objects.all()[:8]
        preview_cultural = CountryCultural.objects.all()[:8]
        preview_tourist = CountryTourist.objects.all()[:8]
        return render(request,'FirstPage.html',{'preview_news':preview_news,'banners':banners,'preview_cat':preview_cat,'preview_cultural':preview_cultural,'preview_tourist':preview_tourist})

    def post(self,request):
        pass

#乡村美景页
class BtScinceView(View):
    def get(self,request):
        scinces = CountryScince.objects.filter(mark="F")
        return render(request,'SencondPage.html',{'scinces':scinces})

#乡村美食页
class BtFoodsView(View):
    def get(self,request):
        foods = CountryFoods.objects.all()
        return render(request,'ThirdPage.html',{'foods':foods})

#乡村文化页
class BtCulturalView(View):
    def get(self,request):
        culturals = CountryCultural.objects.all()
        return render(request,'FivePage.html',{'culturals':culturals})

#乡村旅游页
class BtTouristView(View):
    def get(self,request):
        tourists = CountryTourist.objects.filter(season="春季")
        return render(request,'FourPage.html',{'tourists':tourists}) 

#将数据转换成列表
def put_country_list(countrys):
    country_list = []
    for country in countrys:
        country_dicts = {
            "id":country.id,
            "image":country.image.url,
            "name":country.name,
            "href":country.href,
            "detail":country.detail
        }
        country_list.append(country_dicts)
    return country_list

#ajax后台传出（美食，美景，文化）数据
def ajax(request,city,type):
    if city=="0":
        if type=="food": #获取美食
            countrys = CountryFoods.objects.all()
        elif type=="scince": #获取美景
            countrys = CountryScince.objects.filter(mark="F")
        elif type=="cultural": #获取文化
            countrys = CountryCultural.objects.all()
        return JsonResponse(put_country_list(countrys),safe=False)
    else:
        if type=="food": #获取美食
            countrys = CountryFoods.objects.filter(city=city)
        elif type=="scince": #获取美景
            countrys = CountryScince.objects.filter(city=city)
        elif type=="cultural": #获取文化
            countrys = CountryCultural.objects.filter(city=city)
        return JsonResponse(put_country_list(countrys),safe=False)

#ajax后台传出旅游景点数据
def ajax_tourist(request,season="春季"):
    if season!="春季" or season!="夏季" or season!="秋季" or season!="冬季":
        pass
    
    country_tourist = CountryTourist.objects.filter(season=season)
    tourist_list=[]
    for tourist in country_tourist:
        tourist_dicts = {
            "id":tourist.id,
            "image":tourist.image.url,
            "name":tourist.name,
            "href":tourist.href,
            "detail":tourist.detail,
            "person":tourist.person,
            "rank":tourist.rank,
            "price":tourist.price
        }
        tourist_list.append(tourist_dicts)
    return JsonResponse(tourist_list,safe=False)

#最美乡村页
class BtCountryView(View):
    def get(self,request):
        return render(request,'SixPage.html',{})

#最美乡村页ajx数据
def ajax_btCountry(request,ids):
    ids = int(ids)
    max_length = ids*6
    if ids==1:
        btCountrys = CountryScince.objects.filter(mark="T")[:max_length]
    elif ids>1:
        ids=max_length-5
        btCountrys = CountryScince.objects.filter(mark="T")[ids:max_length+1]
    elif ids==0:
        btCountrys = CountryScince.objects.all()
    btCountry_list=[]
    for btCountry in btCountrys:
        btCountry_dicts = {
            "id":btCountry.id,
            "name":btCountry.name,
            "image":btCountry.image.url,
            "detail":btCountry.detail
        }
        btCountry_list.append(btCountry_dicts)
    return JsonResponse(btCountry_list,safe=False)


def generate_random(len):
    random = Random()
    str=random.randint(0,len-1)
    return str

def get_length(arr):
    i=0
    for btCountry in arr:
        i=i+1
    return i

class DetailView(View):
    def get(self,request,Ctype,ids):
        ids = int(ids)
        if Ctype=="Scinces":
            country_dec = CountryScince.objects.get(id=ids)
            rec_country = CountryScince.objects.all()
            strs = generate_random(get_length(rec_country))
            if strs+4>=get_length(rec_country):
                rec_country = CountryScince.objects.all()[strs-4:strs]
            else:
                rec_country = CountryScince.objects.all()[strs:strs+4]
        elif Ctype=="Foods":
            country_dec = CountryFoods.objects.get(id=ids)
            rec_country = CountryFoods.objects.all()  
            strs = generate_random(get_length(rec_country))
            if strs+4>=get_length(rec_country):
                rec_country = CountryFoods.objects.all()[strs-4:strs]
            else:
                rec_country = CountryFoods.objects.all()[strs:strs+4]
        elif Ctype=="Tourists":
            country_dec = CountryTourist.objects.get(id=ids)
            rec_country = CountryTourist.objects.all()  
            strs = generate_random(get_length(rec_country))
            if strs+4>=get_length(rec_country):
                rec_country = CountryTourist.objects.all()[strs-4:strs]
            else:
                rec_country = CountryTourist.objects.all()[strs:strs+4]
        elif Ctype=="Culturals":
            country_dec = CountryCultural.objects.get(id=ids)
            rec_country = CountryCultural.objects.all()
            strs = generate_random(get_length(rec_country))
            if strs+4>=get_length(rec_country):
                rec_country = CountryCultural.objects.all()[strs-4:strs]
            else:
                rec_country = CountryCultural.objects.all()[strs:strs+4]
        elif Ctype=="btCountry":
            country_dec = CountryScince.objects.get(id=ids)
            rec_country = CountryScince.objects.all() 
            strs = generate_random(get_length(rec_country))
            if strs+4>=get_length(rec_country):
                rec_country = CountryScince.objects.all()[strs-4:strs]
            else:
                rec_country = CountryScince.objects.all()[strs:strs+4] 
        return render(request,'detail.html',{'country_dec':country_dec,'rec_country':rec_country,'Ctype':Ctype})


class MapView(View):
    def post(self,request,Ctype,ids):
        adress = request.POST.get('adress',"")
        return render(request,'map.html',{'adress':adress})


class error404View(View):
    def get(self,request):
        return render(request,'notFind404.html')


