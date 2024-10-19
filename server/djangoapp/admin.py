from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class: allows CarModel to be displayed inline within CarMake in the admin interface
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of extra blank forms to show for CarModel

# CarModelAdmin class: Customize how CarModel is displayed in the admin site
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    search_fields = ['name', 'car_make__name']  # Allow search by car model or make
    list_filter = ['type', 'year']

# CarMakeAdmin class with CarModelInline: Display CarModel inline when viewing CarMake
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Include CarModel inline in CarMake admin view
    list_display = ['name', 'description']
    search_fields = ['name']

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
