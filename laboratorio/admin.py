
from django.contrib import admin
from .models import Laboratorio, DirectorGeneral,Producto

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre')
    search_fields = ('nombre',)
    
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre','laboratorio')
    search_fields = ('nombre','laboratorio')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','laboratorio')
    search_fields = ('nombre','laboratorio')
    
admin.site.register(Laboratorio)
admin.site.register(DirectorGeneral)
admin.site.register(Producto)