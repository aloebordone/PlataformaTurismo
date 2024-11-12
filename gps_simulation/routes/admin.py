from django.contrib import admin
from .models import City, Route

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'population']

admin.site.register(Route)

