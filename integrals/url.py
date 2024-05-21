from django.urls import path
from .views import IntegralApiView
urlpatterns = [
    path('api/integral/',IntegralApiView.as_view(),name='integral'),
]