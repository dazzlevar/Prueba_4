from django.db import router
from django.urls import path, include
from .views import SuscripcionViewset, home, registro, contacto, agregar_producto, listar_productos, \
    modificar_producto, eliminar_producto, catalogo, clima, pagar, settings, agregar_sub, \
    listar_sub, eliminar_sub, error_404, agregar_categoria, listar_categorias, modificar_categoria, eliminar_categoria, \
    listar_usuarios, eliminar_usuario,  agregar_despacho, listar_despacho, historial_usuario, modificar_despacho, eliminar_despacho
from .viewsLogin import login
from rest_framework import routers

router = routers.DefaultRouter()
router.register('suscripcion', SuscripcionViewset)

urlpatterns = [
    path('', home, name = "home"),
    path('registro/', registro, name = 'registro'),
    path('contacto/', contacto, name = 'contacto'),
    path('catalogo/', catalogo, name = 'catalogo'),

    # PRODUCTOS
    path('agregar-producto/', agregar_producto, name = "agregar_producto"),
    path('listar-productos/', listar_productos, name = 'listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name = "modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name = "eliminar_producto"),

    # CATEGORIAS
    path('agregar-categoria/', agregar_categoria, name = "agregar_categoria"),
    path('listar-categorias/', listar_categorias, name = 'listar_categorias'),
    path('modificar-categoria/<id>/', modificar_categoria, name = "modificar_categoria"),
    path('eliminar-categoria/<id>/', eliminar_categoria, name = "eliminar_categoria"),

    # USUARIO
    path('listar-usuarios', listar_usuarios, name = 'listar_usuarios'),
    path('eliminar-usuario/<id>/', eliminar_usuario, name = "eliminar_usuario"),

    # API
    path('clima/', clima, name = "clima"),

    # SETTINGS
    path('settings/', settings, name = 'settings'),
    path('pagar', pagar, name = 'pagar'),

    # SUSCRIPCION
    path('agregar-sub/', agregar_sub, name = "agregar_sub"),
    path('listar-sub/', listar_sub, name = 'listar_sub'),
    path('eliminar-sub/<id>/', eliminar_sub, name = "eliminar_sub"),
    path('api/', include(router.urls)),
    path('login', login, name="login"),
    path('error_404', error_404, name = 'error_404'),

    # DESPACHO e HISTORIAL
    path('agregar-despacho/', agregar_despacho, name = "agregar_despacho"),
    path('listar-despacho/', listar_despacho, name = "listar_despacho"),
    path('historial-usuario/', historial_usuario, name = "historial_usuario"),
    path('modificar-despacho/<id>/', modificar_despacho, name = "modificar_despacho"),
    path('eliminar-despacho/<id>/', eliminar_despacho, name = "eliminar_despacho"),
]
