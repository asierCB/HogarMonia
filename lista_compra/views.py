from django.shortcuts import render

# Create your views here.

def lista_compra(request):
    return render(request, 'lista_compra/lista-compra.html')