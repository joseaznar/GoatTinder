from django.conf.urls import url
from . import views # . will look into docs with the name views in this file this 

urlpatterns =[
 	url(r'^$', views.home)		
 	]