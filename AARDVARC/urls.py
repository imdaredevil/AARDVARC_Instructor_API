"""AARDVARC URL Configuration

"""

from instructor_course_API import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'auth_token',views.AuthView, basename='auth_token')
router.register(r'course_code',views.InstructorCourseView, basename='instructor_course_code')


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name='swagger-ui.html', url_name="schema"
        ),
        name="swagger-ui",
    ), 
]