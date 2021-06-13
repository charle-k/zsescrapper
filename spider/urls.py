from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tarisa/', views.check_zse, name='check_zse'),
]

