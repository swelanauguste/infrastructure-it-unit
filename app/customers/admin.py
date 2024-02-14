from django.contrib import admin

from .models import Customer, Department

admin.site.register(Department)
admin.site.register(Customer)
