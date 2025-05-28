from django.urls import path
from . import views

urlpatterns = [
    path('lista_compra/', views.lista_compra, name='lista_compra'),

    path('lista_compra/<int:grupo_id>/', views.lista_grupo, name='lista_grupo'),
]