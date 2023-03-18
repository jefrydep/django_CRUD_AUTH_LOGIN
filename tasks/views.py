from django.shortcuts import render, redirect, get_object_or_404
# importamos para crear nuestro formulario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# importamos par registar usuarios
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# importamos error de integridad de usuarios duplicados
from django.db import IntegrityError
from .forms import TaskForm
# Create your views here

# importamos el modelo de las tareas para  mostrarlo
from .models import Task


def hello(request):
    # title= 'hello world '
    return render(request, 'home.html', {
        # 'form':UserCreationForm
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm

        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)

                return redirect('task')
                # return HttpResponse('User created sucessfully')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User name already exist'

                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'passwor does not match'
        })


def task(request):
    allTask = Task.objects.filter(
        user=request.user, datecompleted__isnull=True)
    print(allTask)
    return render(request, 'task.html', {'tareas': allTask})


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


def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            # print(request.POST)

            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except ValueError:
             return render(request, 'create_task.html', {
            'form': TaskForm,
            'error': 'Por favor ingresa datos validos'
        })


def task_detail(request, task_id):
     if request.method == 'GET':
    # task = Task.objects.get(pk=task_id)
        task = get_object_or_404(Task, pk=task_id)
    # llamamos al formulario para actualizar
        form = TaskForm(instance=task)
        return render(request, 'task_details.html', {'task': task, 'form': form})
     else:
            try:

                task = get_object_or_404(Task,pk=task_id)
                form = TaskForm(request.POST,instance=task)
                form.save()    
                return redirect('task')
            except ValueError:
                 return render(request, 'task_details.html', {'task': task, 'form': form,'error':'Error actuallizando tareas'})

        
         