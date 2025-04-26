from django.urls import path
from . import views

urlpatterns = [
    path('gastos/', views.gastos, name='gastos_ind'),
    #path('gastos/<int:grupo_id>/', views.miembros_del_grupo, name='miembros'),

    path('gastos/<int:grupo_id>/', views.miembros_del_grupo, name='gastos'),
]