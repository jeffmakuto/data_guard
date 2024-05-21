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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
