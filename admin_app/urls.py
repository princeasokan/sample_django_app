from django.urls import include, path
from . import views
urlpatterns=[
    
    path('',views.admin_home,name="admin_home"),
    path('all_products',views.all_products,name="all_products"),
    path('users_list',views.users_list,name="users_list")
    
    
]