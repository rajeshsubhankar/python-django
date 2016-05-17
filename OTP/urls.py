from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^get$',views.get,name='get'),
	url(r'^sendOtpEmail$',views.sendOtpEmail,name='sendOtpEmail')
]