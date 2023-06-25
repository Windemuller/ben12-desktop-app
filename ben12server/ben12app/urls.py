from django.urls import path

from . import views

urlpatterns = [
    path('api/clients', views.ClientGeneralView.as_view()),
    path('api/clients/<int:client_id>', views.ClientDetailView.as_view()),
    path('api/records/<int:client_id>', views.RecordDetailView.as_view()),
    path('api/records/<int:client_id>/alcohol', views.RecordAlcoholView.as_view()),
    path('api/records/<int:client_id>/heartbeat', views.RecordHeartbeatView.as_view()),
]
