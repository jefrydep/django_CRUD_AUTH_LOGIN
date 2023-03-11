from django.shortcuts import render,redirect
# importamos para crear nuestro formulario
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# importamos par registar usuarios
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# importamos error de integridad de usuarios duplicados
from django.db import IntegrityError
# Create your views here.
def hello(request):
    # title= 'hello world '
    return render (request,'home.html',{
        # 'form':UserCreationForm
    })

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
        'form':UserCreationForm

    })
    else:
        if request.POST['password1'] == request.POST['password2']:
          try:
            user = User.objects.create_user(username=request.POST['username'],
            password=request.POST['password1'])
            user.save()
            login(request,user)

            return redirect('task')
            # return HttpResponse('User created sucessfully')

          except IntegrityError:
            return render(request,'signup.html',{
               'form':UserCreationForm,
               'error':'User name already exist'
               
            })
        return render(request,'signup.html',{
            'form':UserCreationForm,
            'error':'passwor does not match'
        })
    

def task(request):
   return render(request,'task.html')

def signOut(request):
   logout(request)
   return redirect('home')

def signIn(request):
  
    if request.method == 'GET':
        return render(request, 'sign_in.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign_in.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('task')