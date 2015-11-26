from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
<<<<<<< HEAD
    url(r'^json/$', CalendarJsonListView.as_view(), name='calendar_json'),
  url(r'^calendario$', CalendarView.as_view(), name='calendar'),
=======
    url(r'^actividad$', 'apps.calendario.views.actividad', name='actividad'),
>>>>>>> 608bef6e2ee93663e9478217778a90c22cacd00a
    
]
