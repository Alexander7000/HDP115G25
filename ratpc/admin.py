from django.contrib import admin
from .models import Vehiculo, Transportista, Informe, Mercaderia, Nacionalidad
# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa","modelo")
    list_filter = ("id_nacionalidad",)
    search_fields = ("id_vehiculo","placa")

admin.site.register(Vehiculo, VehiculoAdmin)

admin.site.register(Transportista)

admin.site.register(Informe)

admin.site.register(Mercaderia)

admin.site.register(Nacionalidad)