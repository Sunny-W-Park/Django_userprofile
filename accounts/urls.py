from django.urls import path
from . import views

urlpatterns = [
        path('', views.daemun, name = 'daemun'),
        path('signup/', views.signup, name = 'signup'),
        path('login/', views.login, name = 'login'),
        path('logout/', views.logout, name = 'logout'),
        ]

