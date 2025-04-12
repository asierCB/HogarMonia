from django.shortcuts import render

# Create your views here.

def tareas(request):
    return render(request, 'tareas/tareas.html')
