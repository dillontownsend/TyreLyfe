from django.contrib import admin
from .models import CarGuy

# Register your models here.

class CarGuyAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'car')


admin.site.register(CarGuy, CarGuyAdmin)