from django.conf.urls import url
from . import views
app_name='rl'
urlpatterns = [

    url(r'^map', views.Vehicle_Map),
    url(r'^home', views.home),

]
