
from django.contrib import admin
from .models import Laboratorio, DirectorGeneral,Producto

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('id','nombre',)
    

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    search_fields = ('id','nombre','laboratorio')

    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    search_fields = ('id','nombre','laboratorio')
    
admin.site.register(Laboratorio)
admin.site.register(DirectorGeneral)
admin.site.register(Producto)