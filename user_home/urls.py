from django.urls import include, path
from django.conf.urls.static import static

from mysite import settings
from . import views
urlpatterns=[
    
    path('',views.user_home,name="user_home"),
    path('register_brand',views.register_brand,name="register_brand"),
    path('register_brand_action',views.register_brand_action,name="register_brand_action"),
    path('product_list',views.product_list,name="product_list"),
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)