from django.shortcuts import render

# Create your views here.

def gastos(request):
    context = {'mensaje': '¡Hola desde la vista de la página 1!'}
    return render(request, 'gastos/gastos.html', context)