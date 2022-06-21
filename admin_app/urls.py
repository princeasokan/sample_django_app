from django.urls import include, path
from . import views
urlpatterns=[
    
    path('',views.admin_home,name="admin_home"),
    path('all_products',views.all_products,name="all_products"),
    path('users_list',views.users_list,name="users_list"),
    path('api/disable_login/<int:id>',views.disable_login,name='disable_login'),
     path('api/enable_login/<int:id>',views.enable_login,name='enable_login')
    
    
]