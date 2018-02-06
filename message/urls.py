from django.conf.urls import url

from message import views

app_name = 'message'
urlpatterns = [
    url(r'message', views.message, name='message'),
]

