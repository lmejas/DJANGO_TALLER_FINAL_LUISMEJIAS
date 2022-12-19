from django.contrib import admin
from test3y4.models import Institucion

# Register your models here.

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ["institucion"]

admin.site.register(Institucion, InstitucionAdmin)