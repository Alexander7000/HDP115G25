from builtins import print

from django.shortcuts import render, redirect
from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia
from .forms import PersonaForm, VehiculoForm, TransportistaForm, InformeForm, MercaderiaForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

# Create your views here.

# acceso a los archivos (paginas)

# paginas del sitio
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

def salir(request):
    return render(request, 'paginas/agente.html')


#personas
@login_required
def personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {'personas': personas})

@login_required
def crear_pe(request):
    formulario = PersonaForm(request.POST or None)
    if formulario.is_valid():
        x = formulario.save() #obtiene el objeto
        return redirect('crear_tr', x.id_persona)
    return render(request, 'personas/crear.html', {'formulario': formulario})

@login_required
def editar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    formulario = PersonaForm(request.POST or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('editar_tr',id)
    return render(request, 'personas/editar.html', {'formulario': formulario})

@login_required
def eliminar_pe(request, id):
    persona = Persona.objects.get(id_persona=id)
    persona.delete()
    return redirect('transportistas')


#vehiculoss
@login_required
def vehiculos(request):
    vehiculos = Vehiculo.objects.filter(id_usuario = request.user.id)
    return render(request, 'vehiculos/index.html', {'vehiculos': vehiculos})

@login_required
def crear_ve(request):
    formulario = VehiculoForm(request.POST or None)
    if formulario.is_valid():
        vehiculo = formulario.save(commit=False)
        user = User.objects.get(id=request.user.id)
        vehiculo.id_usuario = user
        vehiculo.save()
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
    transportistas = Transportista.objects.filter(id_usuario = request.user.id)
    return render(request, 'transportistas/index.html', {'transportistas': transportistas})

@login_required
def crear_tr(request, id):
    formulario = TransportistaForm(request.POST or None)
    if formulario.is_valid():
        persona = Persona.objects.get(id_persona=id)
        user = User.objects.get(id=request.user.id)
        transportista = formulario.save(commit=False)
        transportista.id_persona = persona
        transportista.id_usuario = user
        transportista.save()
        return redirect('transportistas')
    return render(request, 'transportistas/crear.html', {'formulario': formulario})

@login_required
def editar_tr(request, id):
    transportista = Transportista.objects.get(id_persona=id)
    formulario = TransportistaForm(request.POST or None, instance=transportista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('transportistas')
    return render(request, 'transportistas/editar.html', {'formulario': formulario})

@login_required
def eliminar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    id = transportista.id_persona
    transportista.delete()
    return redirect('eliminar_pe', id.id_persona)


#informe
@login_required
def informes(request):
    informes = Informe.objects.filter(id_usuario = request.user.id)
    return render(request, 'informes/index.html', {'informes': informes})

@login_required
def crear_in(request):
    formulario = InformeForm(request.POST or None)
    formulario.fields['id_transportista'].queryset = Transportista.objects.filter(id_usuario = request.user.id)
    formulario.fields['id_vehiculo'].queryset = Vehiculo.objects.filter(id_usuario = request.user.id)
    if formulario.is_valid():
        x = formulario.save(commit=False)
        user = User.objects.get(id=request.user.id)
        x.id_usuario = user
        x.save()
        return redirect('mercaderias', x.id_informe)
    return render(request, 'informes/crear.html',{'formulario': formulario})

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
def mercaderias(request, id):
    informe = Informe.objects.get(id_informe=id)

    mercaderias = informe.detalleMercaderia.all()

    return render(request, 'mercaderias/index.html', {'mercaderias': mercaderias, 'id': id})

@login_required
def mercaderias2(request, id):
    informe = Informe.objects.get(id_informe=id)

    mercaderias = informe.detalleMercaderia.all()

    return render(request, 'mercaderias/index2.html', {'mercaderias': mercaderias, 'id': id})

@login_required
def mercaderias3(request, id):
    informe = Informe.objects.get(id_informe=id)

    mercaderias = informe.detalleMercaderia.all()

    return render(request, 'mercaderias/index3.html', {'mercaderias': mercaderias, 'id': id})

@login_required
def crear_me(request, id):
    informe = Informe.objects.get(id_informe=id)
    formulario = MercaderiaForm(request.POST or None)
    if formulario.is_valid():
        informe.detalleMercaderia.add(formulario.save())
        return redirect('mercaderias', id)
    return render(request, 'mercaderias/crear.html', {'formulario': formulario, 'id': id})

@login_required
def editar_me(request, idInforme ,idMercaderia):
    mercaderia = Mercaderia.objects.get(id_mercaderia=idMercaderia)
    formulario = MercaderiaForm(request.POST or None, instance=mercaderia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('mercaderias', idInforme)
    return render(request, 'mercaderias/editar.html', {'formulario': formulario, 'id': idInforme})

@login_required
def eliminar_me(request, idInforme ,idMercaderia):
    mercaderia = Mercaderia.objects.get(id_mercaderia=idMercaderia)
    mercaderia.delete()
    return redirect('mercaderias', idInforme)


#agente
@login_required
def agenteInfos(request):
    informes = Informe.objects.all()
    return render(request, 'paginas/agente.html', {'informes': informes})

def salir(request):
    logout(request)
    return redirect('/')

def crear_log(request):
    formulario = LoginForm(request.POST or None)
    if formulario.is_valid():
            super = formulario.save(commit=False)
            super.es_agente = False
            super.password = make_password(super.password)
            super.save()
            return redirect('inicio')
    return render(request, 'registration/form.html', {'formulario': formulario})
