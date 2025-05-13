from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.tareas, name='tareas_ind'),

    path('tareas/<int:grupo_id>/', views.tareas_grupo, name='tareas'),
    path('tareas/edit-tarea/<int:tarea_id>/', views.edit_tarea, name='tareas_edit_tarea'),
]