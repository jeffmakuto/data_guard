from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from ilm.views import CourseViewSet, ModuleViewSet, ContentViewSet


# Define a simple view for the root URL
def index(request):
    return HttpResponse("Welcome to Data Guard application!")

# Initialize the DefaultRouter
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls', namespace='users')),
    path('api/notifications/', include('mod.urls', namespace='mod'))
]
