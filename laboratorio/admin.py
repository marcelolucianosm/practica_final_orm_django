
from django.contrib import admin
from .models import Laboratorio, DirectorGeneral,Producto

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','laboratorio')
    ordering = ('id',)
    search_fields = ('id','laboratorio',)
    #list_filter = ('id','laboratorio')
    

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    ordering = ('id',)
    search_fields = ('id','nombre','laboratorio')
    #list_filter = ('nombre','laboratorio')

    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    ordering = ('id',)
    search_fields = ('id','nombre','laboratorio')
    list_filter = ('nombre','laboratorio')
    
admin.site.register(Laboratorio,LaboratorioAdmin)
admin.site.register(DirectorGeneral,DirectorGeneralAdmin)
admin.site.register(Producto,ProductoAdmin)