from django.contrib import admin
from .models import CarMake, CarModel

admin.site.register(CarMake)
admin.site.register(CarModel)
# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):  # You can also use StackedInline
    model = CarModel
    extra = 1  # Number of empty forms to display for adding new related objects

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
