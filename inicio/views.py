from django.shortcuts import render, redirect
from django.views import generic 
from django.http import HttpResponse
from .models import *
from .forms import DonativoForm, PrestamoForm

def index(request): 
    return render(request,'index.html')
     
class LibroList(generic.ListView):
    queryset = Libro.objects.all()
    template_name = 'libros.html'
    paginate_by = 9 

class LibroDetail(generic.DetailView):
    model = Libro
    template_name = 'libro_detalle.html' 

def donativos_view(request):
    if request.method=='POST':
        form = DonativoForm(request.POST)
        if form.is_valid(): 
            form.save()
        return redirect('donar')
    else: 
        form = DonativoForm()
    return render(request, 'donativos.html',{'form':form})

def prestamo_crear(request):
    prestamo = PrestamoForm(request)
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form = form.save()
            return render(request, 'prestamo.html', {'prestamo': prestamo})
    else:
        form = PrestamoForm()
    return render(request, 'prestamo.html', {'form': form})