from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Measurements, name='measurements'),
	url(r'^buy/$', views.StripePay, name= 'pay'),
]