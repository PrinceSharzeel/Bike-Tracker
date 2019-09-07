from django.conf.urls import url
from . import views
app_name='rl'
urlpatterns = [

    url(r'^upload', views.upload),
    url(r'^home', views.home),

]
