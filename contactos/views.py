from django.shortcuts import render,redirect
from .forms import FormularioContacto



# Create your views here.

def contactos(request):
    # productos=Producto.objects.all()
    formulario_contactos=FormularioContacto()
    return render(request, 'contactos.html',{'mi_formulario':formulario_contactos})