from django.contrib import admin
from .models import Formulaire

class FormulaireAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Fillier', 'Code', 'Items', 'Date')

admin.site.register(Formulaire, FormulaireAdmin)