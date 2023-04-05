from django.urls import path 

from contactos import views

urlpatterns = [
    path('',views.contactos,name='contactos')
    
]