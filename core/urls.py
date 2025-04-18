from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),

    #path('login/', views.login, name='login'),
    #path('register/', views.register, name='register'),

    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('perfil/', views.perfil, name='perfil'),
]