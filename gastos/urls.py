from django.urls import path
from . import views

urlpatterns = [
    path('gastos/', views.gastos, name='gastos_ind'),

    path('gastos/info-deuda/<int:grupo_id>/', views.info_deuda, name='info_deuda'),
    path('gastos/edit-gasto/<int:gasto_id>/', views.edit_gasto, name='gastos_edit_gasto'),

    path('gastos/<int:grupo_id>/', views.miembros_del_grupo, name='gastos'),
]