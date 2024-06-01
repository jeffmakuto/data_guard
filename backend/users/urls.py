from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


# Setting the app name for namespacing
app_name = 'users'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserDetailView.as_view(), name='user_profile'),
]
