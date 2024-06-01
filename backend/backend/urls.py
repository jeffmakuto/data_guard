from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ilm.views import CourseViewSet, ModuleViewSet, ContentViewSet
from users.views import RegisterView, CustomTokenObtainPairView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('super/', admin.site.urls),  # Admin interface
    path('api/', include(router.urls)),  # API routes
    path('api/users/register/', RegisterView.as_view(), name='register'),
    path('api/users/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/profile/', UserDetailView.as_view(), name='user_profile'),
    path('api/notifications/', include('mod.urls', namespace='mod'))  # Notifications app routes
]
