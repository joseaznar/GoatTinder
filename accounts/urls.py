from django.conf.urls import url
from .views import * # . will look into docs with the name views in this file this 

urlpatterns =[
 	url(r'^$', home, name="index"),
    url(r'^login/$', LogIn, name="login"),
    url(r'^signup/$', SignUp, name="signup"),
    url(r'^logout/$', Logout, name="logout"),
]