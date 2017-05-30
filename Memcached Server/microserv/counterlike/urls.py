from django.conf.urls import url

from . import views


app_name='Likes'

urlpatterns = [
    url(r'^$', views.LikesView.index, name='index'),
		url(r'^(?P<post_id>[0-9]+)/save/$', views.LikesView.save, name='save'),
		url(r'^(?P<post_id>[0-9]+)/get/$', views.LikesView.get, name='get'),
]