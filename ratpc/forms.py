from apt.progress.text import _
from django import forms
from django.contrib.auth.models import User

from .models import Vehiculo, Transportista, Informe, Mercaderia

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
    def __init__(self, user, *args, **kwargs):
        self.id_usuario = user
        print(self.id_usuario)
        super(TransportistaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TransportistaForm, self).clean()
        identificacion = cleaned_data.get('identificacion')
        id_nacionalidad = cleaned_data.get('id_nacionalidad')
        id_usuario = self.id_usuario
        print(identificacion)
        print(id_nacionalidad)
        print(id_usuario)
        if (Transportista.objects.filter(identificacion=identificacion).exists() and
            Transportista.objects.filter(id_nacionalidad=id_nacionalidad).exists() and
            Transportista.objects.filter(id_usuario=id_usuario).exists()):
            raise forms.ValidationError('Ya hay un registro con esta Identificacion y Nacionalidad')

    class Meta:
        model = Transportista
        fields = ('id_nacionalidad', 'identificacion', 'tipo_identificacion', 'tipo_licencia',
                  'nombre_persona', 'apellido', 'telefono', 'fecha_nacimiento', 'direccion')

        labels = {
            'id_nacionalidad': _('Nacionalidad'),
            'tipo_identificacion': _('Tipo de identificacion'),
            'nombre_persona': _('Nombres'),
            'apellido': _('Apellidos'),
            'fecha_nacimiento': _('Fecha de nacimiento'),
            'tipo_licencia': _('Tipo de licencia'),
        }

class TransportistaForm2(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = ('id_nacionalidad', 'identificacion', 'tipo_identificacion', 'tipo_licencia',
                  'nombre_persona', 'apellido', 'telefono', 'fecha_nacimiento', 'direccion')

        labels = {
            'id_nacionalidad': _('Nacionalidad'),
            'tipo_identificacion': _('Tipo de identificacion'),
            'nombre_persona': _('Nombres'),
            'apellido': _('Apellidos'),
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