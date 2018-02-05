from django.conf.urls import url
from django.urls import path

from gallery import views

app_name = 'gallery'

urlpatterns = [
    path(r'Gallery', views.GalleryView.as_view(), name='Gallery'),
    url(r'Gallery/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
]
