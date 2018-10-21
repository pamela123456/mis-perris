from django.contrib import admin
from .models import Vivienda, Region, Ciudad, Postulante
# Register your models here.

class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'run', 'fechaNacimiento', 'region', 'ciudad', 'vivienda', 'telefono', 'correo')
    search_fields =['run']
admin.site.register(Vivienda)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Postulante, PostulanteAdmin)
