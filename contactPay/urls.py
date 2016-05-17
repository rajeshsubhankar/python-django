from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^getUserContactListByMobile$',views.getUserContactListByMobile,name='getUserContactListByMobile'),
	url(r'^getUserDetailsByUniqueId$',views.getUserDetailsByUniqueId,name='getUserDetailsByUniqueId'),
	url(r'^getUserDetailsByEmailAndPassword$',views.getUserDetailsByEmailAndPassword,name='getUserDetailsByEmailAndPassword'),
	url(r'^setUserCredentials$',views.setUserCredentials,name='setUserCredentials')
]