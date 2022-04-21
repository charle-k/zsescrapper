from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'pricesheets', views.ZSEDataViewSet)


app_name = 'spider'
urlpatterns = [
    path('', views.index, name='index'),
    path('daily_pricesheet_listing/', views.daily_pricesheet_listing, name='daily_pricesheet_listing'),
    path('daily_pricesheet/<int:id>/', views.daily_pricesheet, name="daily_pricesheet"),
    path('tarisa/', views.check_zse, name='check_zse'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

