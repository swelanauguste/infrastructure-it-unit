from django.contrib import admin

from .models import Computer, ComputerModel, ComputerType, Maker, Status

admin.site.register(ComputerType)
admin.site.register(Maker)
admin.site.register(Status)
admin.site.register(ComputerModel)
admin.site.register(Computer)
