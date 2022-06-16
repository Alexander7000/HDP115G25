from django import forms
from .models import Libro, Vehiculo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
