from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar'),
    
]
