from django.contrib import admin
from .models import Libro
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ("id","titulo")
    list_filter = ("titulo",)
    search_fields = ("id","titulo")

admin.site.register(Libro, LibroAdmin)