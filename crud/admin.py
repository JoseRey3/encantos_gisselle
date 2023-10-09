from django.contrib import admin
from .models import producto, empleado

# Register your models here.
class productoadmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
admin.site.register(producto, productoadmin)

admin.site.register(empleado)
