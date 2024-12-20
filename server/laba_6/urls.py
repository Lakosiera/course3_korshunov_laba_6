from django.urls import path, include
from rest_framework import routers
from laba_6 import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'deposit', views.DepositViewSet)
router.register(r'loan', views.LoanViewSet)


# пути для модуля 'laba_6'
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
