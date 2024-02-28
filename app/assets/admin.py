from django.contrib import admin

from .models import (
    Computer,
    ComputerModel,
    ComputerType,
    Maker,
    Monitor,
    MonitorModel,
    OperatingSystem,
    Printer,
    PrinterModel,
    Status,
    Location,
    Project,
    MicrosoftOfficeVersion,
    MicrosoftOffice
)

admin.site.register(ComputerType)
admin.site.register(Maker)
admin.site.register(Status)
admin.site.register(ComputerModel)
admin.site.register(Computer)
admin.site.register(PrinterModel)
admin.site.register(Printer)
admin.site.register(OperatingSystem)
admin.site.register(MonitorModel)
admin.site.register(Monitor)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(MicrosoftOfficeVersion)
admin.site.register(MicrosoftOffice)

