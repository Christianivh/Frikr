from django.conf.urls import url
from . import views

app_name = 'photos'

urlpatterns = [
    # /photos/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /photos/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /photos/album/add/
    url(r'album/add/$', views.AlbumCreateView.as_view(), name='album-add'),

    # /photos/album/pk/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /photos/album/pk/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]

