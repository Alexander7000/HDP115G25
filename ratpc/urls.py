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
]
