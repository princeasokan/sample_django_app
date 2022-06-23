from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.template.defaulttags import register
import json


from user_home.models import ProductDetails

# Create your views here.
def admin_home(request):
    print("inside login")
    if not request.user.is_authenticated:
        return render(request,"login.html")
    print("inside login",request.user.is_authenticated)
    return render(request,'admin_home.html')

@register.filter(name='split')
def all_products(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")
    product_list = ProductDetails.objects.select_related('user_id')
    #disableLogin()
    for item in product_list:
        if item.user_id:
            print(item.user_id.id)
            print(item.user_id.username)
    return render(request,'all_products.html',{"product_list":product_list})

def users_list(request):
    user_list = User.objects.all()   
    return render(request,'users_list.html',{"user_list":user_list})

def disable_login(request,id):
   # user_id=1
    user=User.objects.get(id=id)
    user.is_active = False
    user.save()
    print(user)
    response_data = {'user_id':id,'status':True}
    response_data['result'] = 'error'
    response_data['message'] = 'User login disabled'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def enable_login (request,id):
   # user_id=1
    user=User.objects.get(id=id)
    user.is_active = True
    user.save()
    print(user)
    response_data = {'user_id':id,'status':True}
    response_data['result'] = 'User login enabled'
    response_data['message'] = 'User login enabled'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
