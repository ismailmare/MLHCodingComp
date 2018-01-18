from django.conf.urls import include, url
from . import views

urlpatterns = ( 
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^campus/$', views.campus, name='campus'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^emailsent/$', views.emailsent, name='emailsent'),
)