from django.contrib import admin
from .models import producto, empleado

# Register your models here.
class productoadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display =("tipo_prenda", "talla", "genero",)
    search_fields = ("tipo_prenda", "talla",)
    list_per_page = 10
admin.site.register(producto, productoadmin)

class empleadoadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display =("nombre", "apellido", "cargo",)
    search_fields = ("nombre", "apellido", "cargo",)
    list_per_page = 10
admin.site.register(empleado, empleadoadmin)