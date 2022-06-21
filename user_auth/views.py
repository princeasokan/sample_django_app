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

