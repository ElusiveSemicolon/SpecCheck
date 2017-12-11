from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^ajax/update_info/$', views.update_info, name='update_info'),
]