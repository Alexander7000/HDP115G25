from django.urls import path
from . import views

# enlaces para mostrar las vistas (URLS)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('salir', views.salir, name='salir'),

    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),

    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('vehiculos/crear', views.crear_ve, name='crear_ve'),
    path('vehiculos/editar', views.editar_ve, name='editar_ve'),
    path('vehiculos/<int:id>', views.eliminar_ve, name='eliminar_ve'),
    path('vehiculos/editar/<int:id>', views.editar_ve, name='editar_ve'),
]
