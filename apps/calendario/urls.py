from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^json/$', CalendarJsonListView.as_view(), name='calendar_json'),
  url(r'^calendario$', CalendarView.as_view(), name='calendar'),
    
]
