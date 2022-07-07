from pprint import pp
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto, Tipo_sub, Suscripcion, Despacho, Estado_despacho
from .forms import CustomUserCreationForm, ContactoForm, ProductoForm, DatosForm, SubForm, CategoriaForm, DispatchForm, DispatchAdminForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import SuscripcionSerializer, Tipo_subSerializer


class SuscripcionViewset(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer

class Tipo_subViewset(viewsets.ModelViewSet):
    queryset = Tipo_sub.objects.all()
    serializer_class = Tipo_subSerializer

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

@login_required
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

@login_required
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

@login_required
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

@login_required
@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to = "listar_productos") 

@login_required
@permission_required('app.add_categoria')
def agregar_categoria(request):
    data = {
        'form': CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data = request.POST, files=request.FILES)
        if formulario.is_valid(): 
            formulario.save()
            messages.success(request, 'categoria registrada')
        else:
            data["form"] = formulario
    return render(request, 'app/categoria/agregar.html', data)

@login_required
@permission_required('app.view_categoria')
def listar_categorias(request):
    categorias = Categoria.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(categorias, 5)
        categorias = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': categorias,
        'paginator': paginator
    }
    return render(request, 'app/categoria/listar.html', data)

@login_required
@permission_required('app.change_categoria')
def modificar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    data = {
        'form': CategoriaForm(instance = categoria)
    }

    if request.method == 'POST':
        formulario = CategoriaForm(data = request.POST, instance = categoria, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to = 'listar_categoria')
        data['form'] = formulario
    return render(request, 'app/categoria/modificar.html', data)

@login_required
@permission_required('app.delete_categoria')
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id = id)
    categoria.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to = "listar_categoria")

@login_required
@permission_required('app.view_usuario')
def listar_usuarios(request):
    usuarios = User.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(usuarios, 5)
        usuarios = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': usuarios,
        'paginator': paginator
    }
    return render(request, 'app/usuarios/listar.html', data)

@login_required
@permission_required('app.delete_usuario')
def eliminar_usuario(request, id):
    usuario = get_object_or_404(User, id = id)
    usuario.delete()
    messages.success(request, "Se ha eliminado con exito!!")
    return redirect(to = "listar_usuarios")

@login_required
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

@login_required
@permission_required('app.delete_sub')
def eliminar_sub(request, id):
    suscripcion = get_object_or_404(Suscripcion, id = id)
    suscripcion.delete()
    messages.success(request, "Se ha eliminado con exito!!")
    return redirect(to = "listar_sub")

def error_404(request, exception):
    return render(request, 'app/404_error/notFound.html')    

def clima(request):
    return render(request, 'app/clima.html')

@login_required
def pagar(request):
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

    return render(request, 'app/pago/pagar.html', data)

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

# @login_required
# def despacho(request):
#     return render(request, 'app/settings/settings_despacho.html')

@login_required
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

@login_required
def agregar_despacho(request):
    data= {
        'form' : DispatchForm()
    }
    if request.method == 'POST':
        formulario = DispatchForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "La compra fue un exito!!")
            return redirect(to = "home")
        else:
            data["form"] = formulario

    return render(request, 'app/despacho/agregar.html',data)

@login_required
@permission_required('app.view_dispatch')
def listar_despacho(request):
    despacho = Despacho.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(despacho, 5)
        despacho = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': despacho,
        'paginator': paginator
    }
    return render(request, 'app/despacho/listar.html',data)

@login_required
@permission_required('app.change_dispatch')
def modificar_despacho(request ,  id):
    despacho = get_object_or_404(Despacho, id = id)
    data = {
        'form': DispatchAdminForm(instance=despacho)
    }

    if request.method == 'POST':
        formulario = DispatchAdminForm(data=request.POST, instance=despacho, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El despacho ha sido modificado!")
            return redirect(to="listar_despacho")
        data["form"]=formulario

    return render(request, 'app/despacho/modificar.html',data)

@login_required
@permission_required('app.delete_dispatch')
def eliminar_despacho(request, id):
    despacho = get_object_or_404(Despacho, id = id)
    despacho.delete()
    messages.success(request, "Se ha eliminado con exito!!")
    return redirect(to = "listar_despacho")

@login_required
def historial_usuario(request):
    despacho = Despacho.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(despacho, 5)
        despacho = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': despacho,
        'paginator': paginator
    }
    return render(request, 'app/historial.html',data)
