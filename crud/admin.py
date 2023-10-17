from django.contrib import admin
from .models import producto, empleado, compra, detalle_compra, categoria

# Register your models here.
class categoriaadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display =("nombre_categoria",)
    search_fields = ("nombre_categoria",)
    list_per_page = 10
admin.site.register(categoria, categoriaadmin)

class productoadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display =("tipo_prenda", "talla", "precio_compra","precio_venta", "existencias", )
    search_fields = ("tipo_prenda", "talla",)
    list_per_page = 10
admin.site.register(producto, productoadmin)

class empleadoadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display =("nombre", "apellido", "cargo",)
    search_fields = ("nombre", "apellido", "cargo",)
    list_per_page = 10
admin.site.register(empleado, empleadoadmin)

class detalle_compraadmin(admin.TabularInline):
    model = detalle_compra

class compraadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    list_display = ("numero_compra", "fecha_compra",)
    search_fields = ("numero_compra", "fecha_compra")   
    inlines = [
        detalle_compraadmin
    ]
admin.site.register(compra, compraadmin)