from . import views
from .views import donativos_view, index, prestamo_crear
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('libro/', views.LibroList.as_view(), name='libros'),
    path('<slug:slug>/', views.LibroDetail.as_view(), name='detalle'),  
    path('donativo/nuevo', donativos_view, name='donar'),
    path('libro/solicitud', prestamo_crear, name= 'crear')

]