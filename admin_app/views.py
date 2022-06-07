from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaulttags import register

from user_home.models import ProductDetails

# Create your views here.
def admin_home(response):
    return render(response,'admin_home.html')

@register.filter(name='split')
def all_products(request):
    product_list = ProductDetails.objects.select_related('user_id')
    for item in product_list:
        if item.user_id:
            print(item.user_id.id)
            print(item.user_id.username)
    return render(request,'all_products.html',{"product_list":product_list})

def users_list(request):
    user_list = User.objects.all()
   
    return render(request,'users_list.html',{"user_list":user_list})
