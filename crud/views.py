from django.shortcuts import render
from .models import producto

# Create your views here.
def home(request):
    #Transforma los resgistros a una lista
    productos = producto.objects.all()
    data = {
        'productos' : productos
    }
    return render (request, 'tienda/home.html', data)

def about(request):
    return render (request, 'tienda/about.html')