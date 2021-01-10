from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
]