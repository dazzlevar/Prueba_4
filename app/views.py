from pprint import pp
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Tipo_sub, Suscripcion
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm, DatosForm, SubForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import SuscripcionSerializer


class SuscripcionViewset(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer


def home(request):
    return render(request, 'app/home.html')


def catalogo(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'app/catalogo.html', data)


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado'
        else:
            data['form'] = formulario
    return render(request, 'app/contacto.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to = "home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            messages.success(request, 'producto registrado')
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)

@permission_required('app.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance = producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to = 'listar_productos')
        data['form'] = formulario
    return render(request, 'app/producto/modificar.html', data)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to = "listar_productos") 


def clima(request):
    return render(request, 'app/clima.html')

def pagar(request):
    return render(request, 'app/pago/pagar.html')

@login_required
def settings(request):
    return render(request, 'app/settings/settings_personales.html')

@login_required
def historial(request):
    return render(request, 'app/settings/settings_historial.html')

@login_required
def direcciones(request):
    return render(request, 'app/settings/settings_direcciones.html')

@login_required
def cupones(request):
    return render(request, 'app/settings/settings_cupones.html')

@login_required
def metodos_de_pago(request):
    return render(request, 'app/settings/settings_medPagos.html')

@login_required
def despacho(request):
    return render(request, 'app/settings/settings_despacho.html')

def pago(request):
    data = {
        'form': DatosForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST)
        if formulario.is_valid(): 
            formulario.save()
            messages.success(request, 'Compra realizada con exito.')
        else:
            data["form"] = formulario

    return render(request, 'app/pago/pago.html', data)

def agregar_sub(request):
    data = {
        'form': SubForm()
    }
    if request.method == 'POST':
        formulario = SubForm(data = request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has suscrito con exito!")
            return redirect(to = "home")
        else:
            data["form"] = formulario
    return render(request, 'app/suscripcion/agregar.html', data)

@permission_required('app.view_sub')
def listar_sub(request):
    suscripciones = Suscripcion.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(suscripciones, 7)
        suscripciones = paginator.page(page)
    except:
        raise Http404

    data = {
        'sub': suscripciones,
        'paginator' : paginator
    }
    return render(request, 'app/suscripcion/listar.html', data)

@permission_required('app.delete_sub')
def eliminar_sub(request, id):
    suscripcion = get_object_or_404(Suscripcion, id = id)
    suscripcion.delete()
    messages.success(request, "Se ha eliminado con exito!!")
    return redirect(to = "listar_sub")

