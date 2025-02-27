from django.urls import path
from . import views

app_name = 'auth'  # namespace para autenticação

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('menu/',  views.menu_view, name='menu'),
    path('logout/', views.logout_view, name='logout'), 
]