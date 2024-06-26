from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


# Setting the app name for namespacing
app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserDetailView.as_view(), name='user_profile'),
]
