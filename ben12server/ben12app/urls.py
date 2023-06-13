from django.urls import path

from . import views

urlpatterns = [
    path('api/clients', views.ClientAPIView.as_view(), name="index"),
]