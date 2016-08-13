from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.jobs_list, name = 'jobs_list'),
]
