from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ilm.views import CourseViewSet, ModuleViewSet, ContentViewSet


# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('', index),  # Root URL
    path('super/', admin.site.urls),  # Admin interface
    path('api/', include(router.urls)),  # API routes
    path('api/users/', include('users.urls', namespace='users')),  # Users app routes
    path('api/notifications/', include('mod.urls', namespace='mod'))  # Notifications app routes
]
