
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload),
    path('about', views.about),
    path('contact', views.contact),
 ] 