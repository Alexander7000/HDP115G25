from django.shortcuts import render, redirect
from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia, Usuario
from .forms import PersonaForm, VehiculoForm, TransportistaForm, InformeForm, MercaderiaForm, UsuarioForm
# Create your views here.

# acceso a los archivos (paginas)

# paginas del sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')

def salir(request):
    return render(request, 'paginas/salir.html')


#personas
def personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas': personas})

def crear_pe(request):
    formulario = PersonaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/crear.html', {'formulario': formulario})

def editar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    formulario = PersonaForm(request.POST or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/editar.html', {'formulario': formulario})

def eliminar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    persona.delete()
    return redirect('personas')


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
    vehiculo = Vehiculo.objects.get(id_vehiculo=id)
    vehiculo.delete()
    return redirect('vehiculos')


#transportista
def transportistas(request):
    transportistas = Transportista.objects.all()
    return render(request, 'transportistas/index.html', {'transportistas': transportistas})

def crear_tr(request):
    formulario = TransportistaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('transportistas')
    return render(request, 'transportistas/crear.html', {'formulario': formulario})

def editar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    formulario = TransportistaForm(request.POST or None, instance=transportista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('transportistas')
    return render(request, 'transportistas/editar.html', {'formulario': formulario})

def eliminar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    transportista.delete()
    return redirect('transportistas')


#informe
def informes(request):
    informes = Informe.objects.all()
    return render(request, 'informes/index.html', {'informes': informes})

def crear_in(request):
    formulario = InformeForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'informes/crear.html', {'formulario': formulario})

def editar_in(request, id):
    informe = Informe.objects.get(id_informe=id)
    formulario = InformeForm(request.POST or None, instance=informe)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('informes')
    return render(request, 'informes/editar.html', {'formulario': formulario})

def eliminar_in(request, id):
    informe = Informe.objects.get(id_informe=id)
    informe.delete()
    return redirect('informes')


#mercaderia
def mercaderias(request):
    mercaderias = Mercaderia.objects.all()
    return render(request, 'mercaderias/index.html', {'mercaderias': mercaderias})

def crear_me(request):
    formulario = MercaderiaForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('mercaderias')
    return render(request, 'mercaderias/crear.html', {'formulario': formulario})

def editar_me(request, id):
    mercaderia = Mercaderia.objects.get(id_mercaderia=id)
    formulario = MercaderiaForm(request.POST or None, instance=mercaderia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('mercaderias')
    return render(request, 'mercaderias/editar.html', {'formulario': formulario})

def eliminar_me(request, id):
    mercaderia = Mercaderia.objects.get(id_mercaderia=id)
    mercaderia.delete()
    return redirect('mercaderias')


#usuario
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/index.html', {'usuarios': usuarios})

def crear_us(request):
    formulario = UsuarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})

def editar_us(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    formulario = UsuarioForm(request.POST or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario': formulario})

def eliminar_us(request, id):
    usuario = Usuario.objects.get(id_usuario=id)
    usuario.delete()
    return redirect('usuarios')