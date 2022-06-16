from django.contrib import admin
from .models import Libro, Vehiculo
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ("id","titulo")
    list_filter = ("titulo",)
    search_fields = ("id","titulo")

admin.site.register(Libro, LibroAdmin)

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa","modelo")
    list_filter = ("id_nacionalidad",)
    search_fields = ("id_vehiculo","placa")

admin.site.register(Vehiculo, VehiculoAdmin)