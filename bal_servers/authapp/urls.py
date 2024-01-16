from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('edit/', views.CustomUpdateView.as_view(), name='edit'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    ]