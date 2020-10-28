from .models import Donativo, Prestamo
from django import forms


class DonativoForm(forms.ModelForm):
    class Meta:
        model = Donativo
        fields = [
            'nombre', 
            'institucion', 
            'numero_contacto',
            'email',
            'mensaje',
            ]
        labels = {
            'nombre': 'Nombre', 
            'institucion': 'Institucion', 
            'numero_contacto': 'Telefono',
            'email': 'E-mail',
            'mensaje':'Mensaje',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control '}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control ','cols': 30, 'rows': 5}),
        }


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            'nombre_prestamista', 
            'telefono', 
            'tipo_identificacion', 
            'no_identificacion',
            'libro',
            'notas',
            ]
        labels = {
            'nombre_prestamista': 'Nombre Completo', 
            'telefono': 'No. Telefono',
            'tipo_identificacion': 'Identificacion', 
            'no_identificacion': 'No Identificacion',
            'libro': 'Libro',
            'notas': 'Comentarios',  
        }
        widgets = {
            'nombre_prestamista': forms.TextInput(attrs={'class': 'form-control '}),
            'telefono': forms.TextInput(attrs={'class': 'form-control col-md-4 '}),
            'tipo_identificacion' :forms.Select(attrs={'class': 'form-control'}),
            'no_identificacion': forms.TextInput(attrs={'class': 'form-control '}),
            'libro':forms.Select(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control ','cols': 30, 'rows': 5}),
        }