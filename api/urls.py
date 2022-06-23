from django.urls import include, path
from . import views

urlpatterns=[
    path('register_user',views.register_user,name='register_user'),
    path('test',views.test,name='test'),
]