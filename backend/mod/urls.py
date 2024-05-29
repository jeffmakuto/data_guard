from django.urls import path
from .views import NotificationListView, NotificationUpdateView


app_name = 'mod'

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationUpdateView.as_view(), name='notification-update'),
]
