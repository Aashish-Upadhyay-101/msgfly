from django.urls import path 
from . import views

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view(), name="register-user"),
    path("login/", views.LoginUserAPIView.as_view(), name="login-user"),
    path("logout/", views.logout_view, name="logout-user"),
]
