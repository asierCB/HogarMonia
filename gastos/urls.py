from django.urls import path
from . import views

urlpatterns = [
    path('gastos/', views.gastos, name='gastos'),
]