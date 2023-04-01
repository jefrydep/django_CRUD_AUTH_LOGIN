from django.urls import path 

from contactos import views

urlpatterns = [
    path('contactos',views.contactos,name='contactos')
    
]