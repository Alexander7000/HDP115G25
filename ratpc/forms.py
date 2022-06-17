from apt.progress.text import _
from django import forms

from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia, Usuario

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
        fields = '__all__'
        labels = {
            'id_nacionalidad': _('Nacionalidad'),
            'ano': _('Año'),
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
        fields = ('id_usuario','id_transportista','id_vehiculo','tipo_traslacion','detalleMercaderia')

        labels = {
            'id_transportista': _('Transportista ID'),
            'id_vehiculo': _('Vehiculo ID'),
            'tipo_traslacion': _('Tipo de traslacion'),
            'detalleMercaderia': _('Mercancia'),
        }

class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'