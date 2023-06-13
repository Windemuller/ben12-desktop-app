from django.urls import path

from . import views

urlpatterns = [
    path('api/clients', views.ClientAPIView.as_view()),
    path('api/clients/<int:client_id>', views.ClientDetailView.as_view()),
]
