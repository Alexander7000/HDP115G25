from django import forms

from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia, Usuario

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = ['fecha_nacimiento','direccion','tipo_licencia']


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = '__all__'

class MercaderiaForm(forms.ModelForm):
    class Meta:
        model = Mercaderia
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'