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

#### Seguridad de la aplicacion
- vamos  a settings e importamos el paquete 

import os


### despliegue de la aplicaion en un hosting gratuito

1. crearse una cuenta en render.com  ya sea con github o google
- vamos a renderdeply.com y copiamos al configuracin de secrete key

* la configuracion podemos encontralo en https://render.com/docs/deploy-django
2. vamos a settings.py de la aplicacion principal y modificamos el secret Key
```js
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
```
3. configuramos el debu
```js
DEBUG = 'RENDER' not in os.environ
```
4. configuramos la variable de entorno que nos da render con este codigo
```js

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```
5. vamos a configura la base de datos con Postgres

- ejecutamos estos comandos
```
pip install dj-database-url
pip install psycopg2-binary
```
6- vamos a settings para configurar la base de datos impotamos dj-database

```js
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}
```
