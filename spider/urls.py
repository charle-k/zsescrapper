from django.urls import path

from . import views

app_name = 'spider'
urlpatterns = [
    path('', views.index, name='index'),
    path('daily_pricesheet_listing/', views.daily_pricesheet_listing, name='daily_pricesheet_listing'),
    path('daily_pricesheet/<int:id>/', views.daily_pricesheet, name="daily_pricesheet"),
    path('tarisa/', views.check_zse, name='check_zse'),
]

