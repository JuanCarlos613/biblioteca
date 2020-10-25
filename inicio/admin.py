from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Sistema Bibliotecario de San Marcos'

class CategAdmin (admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ['categoria']
    list_filter = ("categoria",)
admin.site.register(Categoria, CategAdmin)


class AutorAdmin (admin.ModelAdmin):
    list_display = ('nombre_autor',)
    search_fields = ['nombre_autor']
    list_filter = ('nombre_autor',)
admin.site.register(Autor, AutorAdmin)

class TidentAdmin (admin.ModelAdmin):
    list_display = ('tipo_identificacion',) 
admin.site.register(Identificacion, TidentAdmin)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre_libro', 'imagen', 'autor_libro','categoria','status')
    list_filter = ('nombre_libro','status',)
    search_fields = ['nombre_libro','autor_libro']
    prepopulated_fields = {'slug': ('nombre_libro',)}

admin.site.register(Libro, LibroAdmin)

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('nombre_prestamista', 'no_identificacion',
                    'telefono','fecha_prestamo',
                    'fecha_entrega','notas')
    list_filter = ("nombre_prestamista",'no_identificacion')
    search_fields = ['nombre_prestamista','no_identificacion']
  
admin.site.register(Prestamo, PrestamoAdmin)

class DonativoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'institucion', 'numero_contacto', 
    'email', 'mensaje') 
admin.site.register(Donativo, DonativoAdmin)