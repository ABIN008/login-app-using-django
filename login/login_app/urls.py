from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name='home'),
    path('login/', views.loginview, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]