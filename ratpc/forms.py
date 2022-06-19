from apt.progress.text import _
from django import forms
from django.contrib.auth.models import User

from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email','username','password')
        labels = {
            'first_name': _('Nombres'),
            'last_name': _('Apellidos'),
            'email': _('Correo electronico'),
            'password': _('Contraseña'),
        }


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        labels = {
            'id_nacionalidad': _('Nacionalidad'),
            'tipo_identificacion': _('Tipo de identificacion'),
            'nombre_persona': _('Nombres'),
            'apellido': _('Apellidos'),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('placa', 'id_nacionalidad', 'modelo', 'ano','cant_asientos', 'color')
        labels = {
            'id_nacionalidad': _('Nacionalidad'),
            'ano': _('Año'),
            'modelo': _('Marca - Modelo'),
            'cant_asientos': _('Cantidad de asientos'),
            'color': _('Colores del vehiculo'),
        }

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = ('fecha_nacimiento','direccion','tipo_licencia')
        labels = {
            'fecha_nacimiento': _('Fecha de nacimiento'),
            'tipo_licencia': _('Tipo de licencia'),
        }


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ('id_transportista','id_vehiculo','tipo_traslacion')

        labels = {
            'id_transportista': _('Transportista ID'),
            'id_vehiculo': _('Vehiculo ID'),
            'tipo_traslacion': _('Tipo de traslacion'),
        }

class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = '__all__'