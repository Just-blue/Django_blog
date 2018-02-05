from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'blog', views.BlogView.as_view(), name='blog'),

    url(r'search/$', views.search, name='search'),
    url(r'blog/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

    path(r'page', views.page, name='page'),
    path(r'contact', views.ContactView.as_view(), name='contact'),
    # path(r'page-elements', views.page - elements, name='page-elements'),
    # path(r'page-typography', views.page - typography, name='page-typography'),

    path(r'project', views.project, name='project'),
]
