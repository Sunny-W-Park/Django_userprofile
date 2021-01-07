from django.urls import path
from . import views

urlpatterns = [
        path('', views.daemun, name = 'daemun'),
        path('signup/', views.signupform, name = 'signup'),
        path('signup/activate/<str:uid64>/<str:token>/', views.activate, name = 'activate'),
        path('login/', views.login, name = 'login'),
        path('logout/', views.logout, name = 'logout'),
        ]


