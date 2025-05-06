from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.tareas, name='tareas_ind'),

    path('tareas/<int:grupo_id>/', views.tareas_grupo, name='tareas'),
]