from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.

def contactos(request):
    
    # productos=Producto.objects.all()
    formulario_contactos = FormularioContacto()
    if request.method == 'POST':
        formulario_contactos=FormularioContacto(data=request.POST)
        if formulario_contactos.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            email=EmailMessage('Mensaje ,Mensaje de : {}email addres:{}message:\n\n{}'.format(nombre,email,contenido)," ",['jefrydep@gmail.com'],reply_to=[email])
            try:
                email.send()
                return redirect('contactos/?valido')
            except:
                return redirect('contactos/?novalido')


    return render(request, 'contactos.html', {'mi_formulario': formulario_contactos})
