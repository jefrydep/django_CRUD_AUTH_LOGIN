from django.shortcuts import render
from .models import Post,Categoria

# Create your views here.
def blog(request):
    posts=Post.objects.all() 
    return render(request,'blog.html',{'posts':posts})

# def categoria()