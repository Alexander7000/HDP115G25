from django.shortcuts import render, redirect
from .models import Libro, Vehiculo
from .forms import LibroForm, VehiculoForm
# Create your views here.

# acceso a los archivos (paginas)

# paginas del sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')

def salir(request):
    return render(request, 'paginas/salir.html')

#libros
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')


#vehiculoss
def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/index.html', {'vehiculos': vehiculos})

def crear_ve(request):
    formulario = VehiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vehiculos')
    return render(request, 'vehiculos/crear.html', {'formulario': formulario})

def editar_ve(request, id):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id)
    formulario = VehiculoForm(request.POST or None, instance=vehiculo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vehiculos')
    return render(request, 'vehiculos/editar.html', {'formulario': formulario})

def eliminar_ve(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.delete()
    return redirect('vehiculos')