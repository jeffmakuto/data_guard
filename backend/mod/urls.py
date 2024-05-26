from django.urls import path
from .views import NotificationListView, NotificationUpdateView


app_name = 'mod'

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationUpdateView.as_view(), name='notification-update'),
]
