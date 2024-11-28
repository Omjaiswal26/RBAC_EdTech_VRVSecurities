from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="EdTech API",
        default_version='v1',
        description="API documentation for the EdTech platform",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@edtech.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('students/', include('student_panel.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),  # This will show Swagger UI
]
