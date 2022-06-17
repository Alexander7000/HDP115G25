from django.contrib import admin
from .models import Persona, Vehiculo, Transportista, Informe, Mercaderia, Usuario, Nacionalidad
# Register your models here.

#class PersonaAdmin(admin.ModelAdmin):
#   list_display = ("identificacion","nombre_persona")
#   list_filter = ("id_nacionalidad",)
#   search_fields = ("identificacion","nombre_persona")

admin.site.register(Persona)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa","modelo")
    list_filter = ("id_nacionalidad",)
    search_fields = ("id_vehiculo","placa")

admin.site.register(Vehiculo, VehiculoAdmin)

admin.site.register(Transportista)

admin.site.register(Informe)

admin.site.register(Mercaderia)

admin.site.register(Usuario)

admin.site.register(Nacionalidad)