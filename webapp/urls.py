from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [
    path('', views.get_header, name='get_header'),
]
