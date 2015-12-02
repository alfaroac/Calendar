from django.conf.urls import include, url
from .views import userRegister

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^usuarios$', 'apps.perfiles.views.listaUsuarios', name='users'),
    url(r'^registrar$', userRegister.as_view(), name='registrar_usuario'),   
    url(r'^usuarios/editar/(?P<id>\d+)$', 'apps.perfiles.views.editUsers', name='edit'),     
    url(r'^usuarios/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.deleteUsers', name='delete'),
]
