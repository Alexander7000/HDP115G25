from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

# enlaces para mostrar las vistas (URLS)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agente', views.agenteInfos, name='agente'),

    path('personas', views.personas, name='personas'),
    path('personas/crear', views.crear_pe, name='crear_pe'),
    path('personas/<int:id>', views.eliminar_pe, name='eliminar_pe'),
    path('personas/editar/<int:id>', views.editar_pe, name='editar_pe'),

    path('vehiculos', views.vehiculos, name='vehiculos'),
    path('vehiculos/crear', views.crear_ve, name='crear_ve'),
    path('vehiculos/<int:id>', views.eliminar_ve, name='eliminar_ve'),
    path('vehiculos/editar/<int:id>', views.editar_ve, name='editar_ve'),

    path('transportistas', views.transportistas, name='transportistas'),
    path('transportistas/crear/<int:id>', views.crear_tr, name='crear_tr'),
    path('transportistas/<int:id>', views.eliminar_tr, name='eliminar_tr'),
    path('transportistas/editar/<int:id>', views.editar_tr, name='editar_tr'),

    path('informes', views.informes, name='informes'),
    path('informes/crear', views.crear_in, name='crear_in'),
    path('informes/<int:id>', views.eliminar_in, name='eliminar_in'),
    path('informes/editar/<int:id>', views.editar_in, name='editar_in'),

    path('mercaderias/<int:id>', views.mercaderias, name='mercaderias'),
    path('mercaderias2/<int:id>', views.mercaderias2, name='mercaderias2'),
    path('mercaderias/crear/<int:id>', views.crear_me, name='crear_me'),
    path('mercaderias/<int:id>', views.eliminar_me, name='eliminar_me'),
    path('mercaderias/editar/<int:id>', views.editar_me, name='editar_me'),

    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear_us, name='crear_us'),
    path('usuarios/<int:id>', views.eliminar_us, name='eliminar_us'),
    path('usuarios/editar/<int:id>', views.editar_us, name='editar_us'),


    path('accounts/',include('django.contrib.auth.urls')),
    path('salir/', views.salir , name = 'salir')
]
