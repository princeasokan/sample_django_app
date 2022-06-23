from django.shortcuts import redirect, render

from user_auth.forms import UserForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User

# from app.forms import UserForm

# Create your views here.
def login_v(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def login_validate(request):
    print(request)
    if request.method == "POST":
        #user_form = UserForm(data=request.POST)        
        username = request.POST['username']
        password = request.POST['password']

        # if user_form.is_valid():
        disableLogin()
        user = authenticate(username=username, password=password)
        if user is not None:
                print(user)
                request.session['user_session'] = user.id
                print(user.is_staff)
                #used to save the session
                login(request,user)
                if(user.is_staff):
                    
                    return redirect('admin/')
                    # render(request,'admin_home.html',{})
                return redirect("user/")
                # return render(request,'user_home.html',{})
        else:
                return redirect("/")
         
        # else:
            #print("form errors===>",user_form.errors)
    return redirect("/")
 
#    else:
#        user_form = UserForm()
#     return render(request, "app/registration.html", {"user_form": user_form})

def disableLogin():
    user_id=3
    user=User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    print(user)

def register(request):
    if(request.method=='GET'):
            return render(request,'register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        first_name= request.POST['first_name']
        print("first_name",first_name)
        try:
            user = User.objects.create_user(username=username,password=password)
            #Profile.objects.create(user=user,full_name=full_name)
            user.save()
            return render(request,'register_success.html',{'error':False,'message':""})
        except:            
             return render(request,'register_success.html',{'error':True,'message':"Unable to register the user,try different username"})
# def register_user(request):
#     print("in registier====>")
#     if request.method=='POST':
#         #PROCESS THE REQUES
#         #full_name = request.POST['full_name']
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.object.create_user(username=username,password=password)
#         #Profile.objects.create(user=user,full_name=full_name)
#         user.save()
#         response_data={}
#         response_data.message = 'Account created'
#         return HttpResponse(json.dumps(response_data), content_type="application/json")
#     return HttpResponse(json.dumps({"response":""}), content_type="application/json"
