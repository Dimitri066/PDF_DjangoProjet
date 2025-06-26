from django.contrib import admin

# Register your models here.
from PDF_Django.models import Template

class TemplateAdmin(admin.ModelAdmin):
    """Classe crée pour l'administartion des templates, elle est améliorable
    en fonction des besoins administrateur"""
    list_display = ("nom", "createur")
    search_fields = ("nom",)
    ordering = ("nom",)

admin.site.register(Template, TemplateAdmin)