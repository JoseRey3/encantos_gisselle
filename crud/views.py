from django.shortcuts import render
from .models import producto, categoria

# Create your views here.
def home(request):
    #Transforma los resgistros a una lista
    productos = producto.objects.all()
    categorias = categoria.objects.all()
    data = {
        'productos' : productos,
        'categorias' : categorias
    }
    return render (request, 'tienda/home.html', data)

def product_detail(request, product_id):
    product = producto.objects.get(pk= product_id)
    categorias = categoria.objects.all()
    data = {
        'categorias' : categorias,
        'product':product
    }   
    return render(request, 'tienda/product_detail.html', data)

def categoria_page(request, categoria_id):
    nom_cat = categoria.objects.get(pk= categoria_id)
    productos = producto.objects.filter(nombre_categoria=nom_cat)
    categorias = categoria.objects.all()
    data = {
        'productos' : productos,
        'categorias' : categorias
    }
    return render(request, 'tienda/categoria_page.html', data)

def about(request):
    categorias = categoria.objects.all()
    data = {
        'categorias' : categorias
    }
    return render (request, 'tienda/about.html', data)