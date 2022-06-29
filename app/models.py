from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombreCat = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCat


class Producto(models.Model):
    nombreProducto = models.CharField(
        max_length=50, verbose_name='Nombre del Producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    descripcionProducto = models.TextField(
        verbose_name='Descripcion del producto')
    cantidadProducto = models.IntegerField(verbose_name='Cantidad', null=True)
    imagen = models.ImageField(upload_to='productos', null=True)
    nombreCat = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombreProducto


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
