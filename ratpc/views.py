from django.shortcuts import render, redirect
from .models import Vehiculo, Transportista, Informe, Mercaderia
from .forms import VehiculoForm, VehiculoForm2,TransportistaForm, TransportistaForm2,InformeForm, MercaderiaForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.

# acceso a los archivos (paginas)

# paginas del sitio
@login_required
def inicio(request):
    if request.user.is_staff:
        return redirect('agente')

    nom = request.user
    return render(request, 'paginas/inicio.html', {'nom': nom})

def salir(request):
    return render(request, 'paginas/agente.html')

#vehiculoss
@login_required
def vehiculos(request):
    vehiculos = Vehiculo.objects.filter(id_usuario = request.user.id)
    return render(request, 'vehiculos/index.html', {'vehiculos': vehiculos})

@login_required
def crear_ve(request):
    formulario = VehiculoForm(request.user.id, request.POST or None)

    if formulario.is_valid():
        vehiculo = formulario.save(commit=False)
        user = User.objects.get(id=request.user.id)
        vehiculo.id_usuario = user
        vehiculo.save()
        messages.success (request, "Se agrego el vehiculo exitosamente!")

        return redirect('vehiculos')
    return render(request, 'vehiculos/crear.html', {'formulario': formulario})

@login_required
def editar_ve(request, id):
    vehiculo = Vehiculo.objects.get(id_vehiculo=id)
    formulario = VehiculoForm2(request.POST or None, instance=vehiculo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
        return redirect('vehiculos')
    return render(request, 'vehiculos/editar.html', {'formulario': formulario})

@login_required
def eliminar_ve(request, id):
    if Informe.objects.filter(id_vehiculo=id):
        messages.error(request, "Este vehiculo esta ligado a un informe por lo que no se puede eliminar")
    else:
        vehiculo = Vehiculo.objects.get(id_vehiculo=id)
        temp = vehiculo.placa
        vehiculo.delete()
        messages.success (request, "Se ha eliminado el vehiculo con placa: " + temp)

    return redirect('vehiculos')


#transportista
@login_required
def transportistas(request):
    transportistas = Transportista.objects.filter(id_usuario = request.user.id)
    return render(request, 'transportistas/index.html', {'transportistas': transportistas})

@login_required
def crear_tr(request):
    formulario = TransportistaForm(request.user.id, request.POST or None)

    if formulario.is_valid():
        transportista = formulario.save(commit=False)
        user = User.objects.get(id=request.user.id)
        transportista.id_usuario = user
        transportista.save()
        messages.success(request, "Se agrego el transportista exitosamente!")
        return redirect('transportistas')

    return render(request, 'transportistas/crear.html', {'formulario': formulario})

@login_required
def editar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    formulario = TransportistaForm2(request.POST or None, instance=transportista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
        return redirect('transportistas')
    return render(request, 'transportistas/editar.html', {'formulario': formulario})

@login_required
def eliminar_tr(request, id):
    if Informe.objects.filter(id_transportista=id):
        messages.error(request, "Este transportista esta ligado a un informe por lo que no se puede eliminar")
    else:
        transportista = Transportista.objects.get(id_transportista=id)
        temp =transportista.identificacion
        transportista.delete()
        messages.success (request, "Se ha eliminado el transportista con identificacion: " + temp)

    return redirect('transportistas')


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
        messages.success(request, "Se agrego la mercaderia exitosamente!")
        return redirect('mercaderias', id)
    return render(request, 'mercaderias/crear.html', {'formulario': formulario, 'id': id})

@login_required
def editar_me(request, idInforme ,idMercaderia):
    mercaderia = Mercaderia.objects.get(id_mercaderia=idMercaderia)
    formulario = MercaderiaForm(request.POST or None, instance=mercaderia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
        return redirect('mercaderias', idInforme)
    return render(request, 'mercaderias/editar.html', {'formulario': formulario, 'id': idInforme})

@login_required
def eliminar_me(request, idInforme ,idMercaderia):
    mercaderia = Mercaderia.objects.get(id_mercaderia=idMercaderia)
    mercaderia.delete()
    messages.success(request, "Se ha eliminado la mercaderia")
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
            messages.success(request, "Su usuario se a registrado correctamente")
            return redirect('inicio')
    return render(request, 'registration/form.html', {'formulario': formulario})
