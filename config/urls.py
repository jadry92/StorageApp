"""
config URL Configuration
"""
# Django
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("users.urls")),
    path("",TemplateView.as_view(template_name="home.html"),name="home"),
    path("storage/", include("storage.urls"), name="storage"),
]
