from django.urls import path, include
from django.conf.urls import url
from apps.clientes.views import home, index
from django.contrib import admin

urlpatterns = [
    path('administrador/', home, name='home'),
    path('mensajes/', include('apps.mensajes.urls', namespace='mensajes')),
    path('', index, name="index"),
    url(r'^administrador/', include('apps.administrador.urls', namespace='administrador')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('myadmin/', admin.site.urls),
]