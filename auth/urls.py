"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.task, name='task'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('taks/<int:task_id>/complete',views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.signOut, name='logout'),
    path('signin/', views.signIn, name='signin'),
    path('task/create/', views.create_task, name='create_task'),
    path('tienda/',include('tienda.urls')),
    path('contactos/',include('contactos.urls')),
    path('blog/',include('blog.urls')),

    # path('tienda/', views.tienda, name='tienda'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
