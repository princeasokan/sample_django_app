from django.urls import include, path
from . import views
urlpatterns=[
    
    
    path('login',views.login_v,name="login_v"),
    path('login_validate',views.login_validate,name="login_validate"),
    path('logout',views.logout_user,name="logout_user"),
    path('register',views.register,name="logout_user"),
    path('',views.login_v,name="login_v"),
    
]