from django.urls import path, re_path

from tienda import views

urlpatterns = [
    path('tienda',views.tienda,name='tienda')
    
]