# DJANGO

1. PASOS PARA INSTALARA DJANGO
- open cmd and go to the path of the directory
- pip install virtual env
- ejecute virtualenv venv
- ejecutar .\venv\Scripts\activate
- open project en vs code 
- ctrl ship p select interpreter
- para los que en windows 10 y 11 tengan problemas al ejecutar el entorno virtual deben activar la ejecucion de scripts en powershell con el comando: Get-ExecutionPolicy si les devuelve «Restricted» deben modificar con el siguiente comando: Set-ExecutionPolicy Unrestricted, todo esto debe ser ejecutado con permiso de administrador


- ejecute pip install django

2. asignar nombre al projecto

- django-admin startproject nameProject .

## COMANDO PARA LEVANTAR EL SERVIDOR
- python manage.py runserver

3. comand to change the SERVER PORT
- python manage.py runserver 3000


- python manage.py startapp blog
- python manage.py startapp store
- python manage.py startapp xname

4. creamos un nuevo modulo llamado urls.py dentro de myapp

- descargar dbbrowser for sqlite

5. Migraciones 
6. python manage.py makemigrations
7. python manage.py migrate

- en setting intalleds app agregra 'myapp'

python manage.py shell
from myapp.models import name,name
creamos una variable p
p = PROJECT(name='Aplicaicon')
p.save , para guardar en la base de datos
## comands 
Project.objects.all()
Project.objects.get(id=1)
project.objects.get(name= 'name')

### create superuser
- python manage.py createsuperuser

### para las imagenes instalar
python -m pip install Pillow

### PARA VER LOS MODELOS EN EL PANEL DE ADMIN

- debemos agregar en el archivo admin.py
#### PARA CREAR UN FORMULARIO DE TAREAS/TASKS 
- creamos dentro de task un archivo llamado forms.py
- importamos ModelForm
_ pedimos los campos que vamos a llenar
- importamos es formularion en las vistas de task

