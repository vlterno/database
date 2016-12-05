from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.devicedb_list, name='devicedb_list'),
]