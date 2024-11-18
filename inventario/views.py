from django.shortcuts import render
from .models import Producto


# Create your views here.

           
def listado_productos_view(request):
    contexto = {}
    productos = Producto.objects.all()
    contexto["productos"] = productos    
    return render(request, "inventario/listado_productos.html", contexto)
