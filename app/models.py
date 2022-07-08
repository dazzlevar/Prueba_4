from pkgutil import extend_path
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombreCat = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCat


class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del Producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    descripcionProducto = models.TextField(verbose_name='Descripcion del producto')
    cantidadProducto = models.IntegerField(verbose_name='Cantidad', null = True)
    imagen = models.ImageField(upload_to='productos', null = True)
    nombreCat = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombreProducto

class DescuentoCategoria(models.Model):
    cantidad = models.IntegerField(verbose_name = 'Descuento de la categoria');
    nombreCat = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class DescuentoProducto(models.Model):
    cantidad = models.IntegerField(verbose_name = 'Descuento del producto');
    nombreProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)

opciones_consultas = [
    [0, 'Consulta'],
    [1, 'Reclamo por error'],
    [2, 'Sugerencia'],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_contacto = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

opciones_pago = [
    [0, 'Transferencia bancaria'],
    [1, 'Tarjeta de debito'],
    [2, 'Tarjeta de crédito'],
]

class Datos(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(verbose_name='Numero de contacto')
    correo = models.EmailField()
    metodo_pago = models.IntegerField(choices=opciones_pago)
    cupon = models.IntegerField(verbose_name='Cupon de descuento')

    def __str__(self):
        return self.nombre

class Tipo_sub(models.Model):
    tipo=models.CharField(max_length=50, verbose_name="Nombre del tipo de Suscripcion")

    def __str__(self):
        return self.tipo


class Suscripcion(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo_sub, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut

class Estado_despacho(models.Model):
    nombreEstado = models.CharField(max_length=50, verbose_name="Estado del Despacho")

    def __str__(self):
        return self.nombreEstado

class Despacho(models.Model):
    nombreCliente = models.CharField(max_length=50,verbose_name='Nombre del cliente')
    apellidoCliente = models.CharField(max_length=50, verbose_name='Apellido')
    correoCliente = models.EmailField(verbose_name='Correo electronico')
    telefonoCliente = models.IntegerField(verbose_name='Numero telefonico')
    direccionCliente = models.TextField(verbose_name='Direccion del cliente', null=True)
    metodo_pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.ForeignKey(Estado_despacho,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCliente

SLC = "SELECCIONAR BANCO"
BDC = "BANCO DE CHILE"
BCL = "BANCO INTERNACIONAL"
STB = "SCOTIABANK CHILE"
BCI = "BANCO DE CREDITO E INVERSIONES"
BBE = "BANCO BICE"
HSB = "HSBC BANK (CHILE)"
BSC = "BANCO SANTANDER-CHILE"
ICA = "ITAU CORPBANCA"
BSY = "BANCO SECURITY"
BFA = "BANCO FALABELLA"
BRY = "BANCO RIPLEY"
BCO = "BANCO CONSORCIO"
SBA = "SCOTIABANK AZUL"
BBP = "BANCO BTG PACTUAL CHILE"

bancos = (
    (SLC, "SELECCIONAR BANCO"),
    (BDC, "BANCO DE CHILE"),
    (BCL, "BANCO INTERNACIONAL"),
    (STB, "SCOTIABANK CHILE"),
    (BCI, "BANCO DE CREDITO E INVERSIONES"),
    (BBE, "BANCO BICE"),
    (HSB, "HSBC BANK (CHILE)"),
    (BSC, "BANCO SANTANDER-CHILE"),
    (ICA, "ITAU CORPBANCA"),
    (BSY, "BANCO SECURITY"),
    (BFA, "BANCO FALABELLA"),
    (BRY, "BANCO RIPLEY"),
    (BCO, "BANCO CONSORCIO"),
    (SBA, "SCOTIABANK AZUL"),
    (BBP, "BANCO BTG PACTUAL CHILE"),
)

tipo_cuenta = (
    (100, 'SELECCIONAR TIPO DE CUENTA'),
    (101, 'TARJETA DE DEBITO'),
    (102, 'TARJETA DE CREDITO'),
)

class MetodoPago(models.Model):
    bancoCliente = models.CharField(max_length=50, choices=bancos, default="SELECCIONAR BANCO")
    tipo_cuenta = models.IntegerField(choices=tipo_cuenta, default=0)
    numeroCuenta = models.IntegerField(verbose_name = "numero de cuenta", null=True)

    def __str__(self):
        return '%s %s %s'%(self.bancoCliente, self.tipo_cuenta, self.numeroCuenta)