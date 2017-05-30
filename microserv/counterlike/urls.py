from django.conf.urls import url

from . import views

app_name='Likes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>[0-9]+)/save/$', views.save, name='save'),
]