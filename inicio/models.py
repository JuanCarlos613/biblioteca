from django.db import models
from django.urls import reverse
#Creaccion de mocelos para la biblioteca 
#Crearemos el modelo libro

class Categoria(models.Model):
    categoria= models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.categoria

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.nombre_autor   

class Identificacion(models.Model):
    tipo_identificacion = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.tipo_identificacion  

STATUS = (
    (0,"Disponible"),
    (1,"Reservado"),
    (2,"Ocupado")
)
class Libro(models.Model):
    nombre_libro = models.CharField(max_length=200, unique=True) 
    imagen=  models.ImageField(blank=True)
    autor_libro = models.ForeignKey(Autor, related_name='autor', on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name='categoria_libro', on_delete = models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    class Meta:
      verbose_name_plural = "libros"

    def __str__(self):
        return '{}'.format(self.nombre_libro)

class Prestamo(models.Model):
    nombre_prestamista = models.CharField(max_length=200, blank=False) 
    telefono= models.CharField(max_length=8, blank= False)
    tipo_identificacion = models.ForeignKey( 
                        Identificacion, 
                        related_name='identificacion', 
                        on_delete = models.CASCADE,
                        blank=False,
                        )
    no_identificacion = models.CharField(
                        max_length=20, 
                        blank= False
                        ) 
    libro = models.ForeignKey(
                        Libro, 
                        related_name='libro_prestado', 
                        on_delete = models.CASCADE,
                        blank=False
                        )
    fecha_prestamo= models.DateTimeField(blank= True, null=True)
    fecha_entrega= models.DateTimeField(blank = True, null=True)
    notas = models.CharField(max_length=200, blank= True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        return '{}'.format(self.id)

class Donativo(models.Model):
    nombre = models.CharField(max_length=200)
    institucion= models.CharField(max_length=80)
    numero_contacto = models.CharField(max_length=10)
    email= models.EmailField(max_length=254)
    mensaje = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    def __str__(self): 
        return self.nombre