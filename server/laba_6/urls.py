from django.urls import path, include
from rest_framework import routers
from laba_6 import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'deposit', views.DepositViewSet)
router.register(r'loan', views.LoanViewSet)


# пути для модуля 'laba_6'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/customer/', views.CustomerList.as_view()),
    path('api/customer/<int:customer_id>/', views.CustomerDetail.as_view()),
    path('api/customer/<int:customer_id>/deposit/', views.DepositList.as_view()),
    path('api/customer/<int:customer_id>/deposit/<int:id>/', views.DepositDetail.as_view()),
]
