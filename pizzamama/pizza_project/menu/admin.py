from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('noms','ingredients', 'vegetarienne', 'prix')
    search_fields = ['noms','ingredients']
# Register your models here.

admin.site.register(Pizza, PizzaAdmin)
