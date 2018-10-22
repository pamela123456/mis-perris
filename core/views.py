from django.shortcuts import render
from .models import Vivienda, Region, Ciudad, Postulante

from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def formulario(request):

    viviendas = Vivienda.objects.all()
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()

    variables = {
        'viviendas':viviendas,
        'regiones': regiones,
        'ciudades': ciudades
    }

    if request.POST:
        postulante = Postulante()
        postulante.nombre = request.POST.get('txtNombre')
        postulante.run = request.POST.get('txtRun')
        postulante.fechaNacimiento = request.POST.get('txtFechaNacimiento')
        postulante.telefono = int(request.POST.get('txtTelefono'))
        postulante.correo = request.POST.get('txtCorreo')
        region = Region()
        region.id = int(request.POST.get('cboVivienda'))
        postulante.region = region
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        postulante.ciudad = ciudad
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))
        postulante.vivienda = vivienda

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'
    
    return render(request, 'core/formulario.html', variables)