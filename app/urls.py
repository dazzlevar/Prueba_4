from django.urls import path
from .views import home, registro, contacto, agregar_producto, listar_productos, \
    modificar_producto, eliminar_producto, catalogo, clima, pagar, settings, \
    historial, direcciones, cupones, metodos_de_pago, despacho, pago

urlpatterns = [
    path('', home, name = "home"),
    path('registro/', registro, name = 'registro'),
    path('contacto/', contacto, name = 'contacto'),
    path('catalogo/', catalogo, name = 'catalogo'),
    path('agregar-producto/', agregar_producto, name = "agregar_producto"),
    path('listar-productos/', listar_productos, name = 'listar_productos'),
    path('modificar-producto/<id>/', modificar_producto, name = "modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name = "eliminar_producto"),
    path('clima/', clima, name = "clima"),
    path('settings/', settings, name = 'settings'),
    path('settings/historial/', historial, name = 'historial'),
    path('settings/direcciones/', direcciones, name = 'direcciones'),
    path('settings/cupones/', cupones, name = 'cupones'),
    path('settings/metodos_de_pago/', metodos_de_pago, name = 'metodos_de_pago'),
    path('settings/despacho/', despacho, name = 'despacho'),
    path('pagar', pagar, name = 'pagar'),
    path('pago', pago, name = 'pago'),
]
