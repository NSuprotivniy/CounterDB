from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get', views.get, name="get_likes"),
    url(r'like', views.like, name="like"),
    url(r'^$', views.index, name="index")
]