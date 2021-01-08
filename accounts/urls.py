from django.urls import path
from . import views

#password reset views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.daemun, name = 'daemun'),
        path('signup/', views.signupform, name = 'signup'),
        path('signup/activate/<str:uid64>/<str:token>/', views.activate, name = 'activate'),
        path('login/', views.login, name = 'login'),
        path('logout/', views.logout, name = 'logout'),
        #find password
        path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
        path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
        path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
        path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
        ]


