from multiprocessing import context
from django import views
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from user_home.forms.register_brand import ProductDetailsForm
from user_home.models import ProductDetails
from django.core.files.storage import FileSystemStorage

# Create your views here.
def user_home(request):
    # print(request.session.get('user_session'),'-----<')
    # print('requested',request)
    return render(request,"user_home.html",{'user_logged':'sample'})
    
def register_brand(response):
    return render(response,"register_brand.html")

def register_brand_action(request):
    # form=ProductDetailsForm()
    # context={'form':form}
    
    if request.method == "POST":        
        user_form = ProductDetailsForm(data=request.POST)
        myfile = request.FILES['attachments']      
        
        if user_form.is_valid():            
            result =user_form.save(commit=False)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            result.attachments= uploaded_file_url
            result.user_id=request.user
            result.save()
            return redirect("/user/product_list")
            # user.save()
        else:
            print('invalid form',user_form)
            print(user_form.errors)
        return redirect("/user")
    #return render(request,"register_brand.html",contex
def product_list(request):  
    user_id= request.user.id
    product_list = ProductDetails.objects.filter(user_id=user_id)
    return render(request,'product_list.html',{'product_list':product_list})