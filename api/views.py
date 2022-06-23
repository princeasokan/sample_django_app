import json
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# from api.models import Profile

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def register_user(request):
    print("in registier====>")
    if request.method=='POST':
        #PROCESS THE REQUES
        #full_name = request.POST['full_name']
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        first_name= request.data['first_name']
        print("first_name",first_name)
        try:
            user = User.objects.create_user(username=username,password=password)
            #Profile.objects.create(user=user,full_name=full_name)
            user.first_name = first_name
            user.save()
            response_data={
                'status':True,
                'message':"user created"
            }
            #return render(request,'register_success.html',{'error':False,'message':""})
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        except:            
             #return render(request,'register_success.html',{'error':True,'message':"Unable to register the user,try different username"})
        
            return HttpResponse(json.dumps({  'status':False,
                'message':"user created not created"}), content_type="application/json")
def test(request):
        response={}
        response['message'] = 'Account created'
        return HttpResponse(json.dumps(response), content_type="application/json")


