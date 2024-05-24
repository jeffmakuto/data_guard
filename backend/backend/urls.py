from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from ilm.views import CourseViewSet, ModuleViewSet, ContentViewSet
from users.views import CustomTokenObtainPairView


# Define a simple view for the root URL
def index(request):
    return HttpResponse("Welcome to Data Guard application!")

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('', index),  # Handle requests to the root URL
    path('admin/', admin.site.urls),  # Admin route
    path('api/v1/', include(router.urls)),  # API v1 routes for ilm app
    path('api/v1/users/', include('users.urls', namespace='users')),  # User management routes with namespace
]
