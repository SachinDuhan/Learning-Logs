"""Defines URL patterns for users"""

from django.urls import re_path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Login page
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    re_path(r'^logout/$', views.logout_view, name='logout'),
    # Registration page
    re_path(r'^register/$', views.register, name='register'),
]