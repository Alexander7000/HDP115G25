from django.shortcuts import render, redirect
from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia, Usuario
from .forms import PersonaForm, VehiculoForm, TransportistaForm, InformeForm, MercaderiaForm, UsuarioForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#para el registrar usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django.views.generic import CreateView

# Create your views here.

# acceso a los archivos (paginas)

# paginas del sitio
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

def salir(request):
    return render(request, 'paginas/salir.html')


#personas
@login_required
def personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas': personas})

@login_required
def crear_pe(request):
    formulario = PersonaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/crear.html', {'formulario': formulario})

@login_required
def editar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    formulario = PersonaForm(request.POST or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/editar.html', {'formulario': formulario})

@login_required
def eliminar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    persona.delete()
    return redirect('personas')


#vehiculoss
@login_required
def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculos/index.html', {'vehiculos': vehiculos})

@login_required
def crear_ve(request):
    formulario = VehiculoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('vehiculos')
    return render(request, 'vehiculos/crear.html', {'formulario': formulario})

@login_required
def editar_ve(request, id):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id)
    formulario = VehiculoForm(request.POST or None, instance=vehiculo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('vehiculos')
    return render(request, 'vehiculos/editar.html', {'formulario': formulario})

@login_required
def eliminar_ve(request, id):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id)
    vehiculo.delete()
    return redirect('vehiculos')


#transportista
@login_required
def transportistas(request):
    transportistas = Transportista.objects.all()
    return render(request, 'transportistas/index.html', {'transportistas': transportistas})

@login_required
def crear_tr(request):
    formulario = TransportistaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('transportistas')
    return render(request, 'transportistas/crear.html', {'formulario': formulario})

@login_required
def editar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    formulario = TransportistaForm(request.POST or None, instance=transportista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('transportistas')
    return render(request, 'transportistas/editar.html', {'formulario': formulario})

@login_required
def eliminar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    transportista.delete()
    return redirect('transportistas')


#informe
@login_required
def informes(request):
    informes = Informe.objects.all()
    return render(request, 'informes/index.html', {'informes': informes})

@login_required
def crear_in(request):
    formulario = InformeForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'informes/crear.html', {'formulario': formulario})

@login_required
def editar_in(request, id):
    informe = Informe.objects.get(id_informe=id)
    formulario = InformeForm(request.POST or None, instance=informe)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('informes')
    return render(request, 'informes/editar.html', {'formulario': formulario})

@login_required
def eliminar_in(request, id):
    informe = Informe.objects.get(id_informe=id)
    informe.delete()
    return redirect('informes')


#mercaderia
@login_required
def mercaderias(request):
    mercaderias = Mercaderia.objects.all()
    return render(request, 'mercaderias/index.html', {'mercaderias': mercaderias})

@login_required
def crear_me(request):
    formulario = MercaderiaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mercaderias')
    return render(request, 'mercaderias/crear.html', {'formulario': formulario})

@login_required
def editar_me(request, id):
    mercaderia = Mercaderia.objects.get(id_mercaderia=id)
    formulario = MercaderiaForm(request.POST or None, instance=mercaderia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('mercaderias')
    return render(request, 'mercaderias/editar.html', {'formulario': formulario})

@login_required
def eliminar_me(request, id):
    mercaderia = Mercaderia.objects.get(id_mercaderia=id)
    mercaderia.delete()
    return redirect('mercaderias')


#usuario
@login_required
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

@login_required()
def crear_us(request):
    formulario = UsuarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})

@login_required
def editar_us(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    formulario = UsuarioForm(request.POST or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario': formulario})

@login_required
def eliminar_us(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('usuarios')

def salir(request):
    logout(request)
    return redirect('/')

