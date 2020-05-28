"""blockchainsurvey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

doc_schema = get_schema_view(
    openapi.Info(
        title="Blockchain Surveys APIs",
        default_version="v1",
        description="REST API documentation.",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("surveys/", include("surveys.urls")),
    path("swagger/", doc_schema.with_ui("swagger", cache_timeout=0), name="swagger_ui"),
    path("redoc/", doc_schema.with_ui("redoc", cache_timeout=0), name="redoc_ui")
]
