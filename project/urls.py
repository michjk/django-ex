from django.conf.urls import include, url
from django.contrib import admin

from goodie import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
#   url(r'^request/', views.event_request, name='eventrequest'),
    url(r'^check/(?P<event_code>\w+)/', views.check_event),
    url(r'^manual/(?P<event>\w+)/',views.manual_register, name='manualregister'),
    url(r'^register/(?P<event>\w+)/(?P<matric_number>\w+)', views.register, name='register'),
    url(r'^list/(?P<event>\w+)/', views.list_matric),
]