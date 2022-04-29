from django.contrib.auth import login

from . import views
from django.urls import path

from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register")
]
