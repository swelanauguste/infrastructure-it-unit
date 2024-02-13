from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import (
    Computer,
    ComputerModel,
    ComputerType,
    Maker,
    Printer,
    PrinterModel,
    Status,
)


def inventory_view(request):
    context = {
        "computers": Computer.objects.all(),
        "computer_models": ComputerModel.objects.all(),
        "printers": Printer.objects.all(),
        "printer_models": PrinterModel.objects.all(),
    }
    return render(request, "assets/inventory.html", context)


class ComputerCreateView(CreateView):
    model = Computer
    fields = "__all__"


class ComputerModelCreateView(CreateView):
    model = ComputerModel
    fields = "__all__"


class ComputerDetailView(DetailView):
    model = Computer


class ComputerModelDetailView(DetailView):
    model = ComputerModel


class PrinterCreateView(CreateView):
    model = Printer
    fields = "__all__"


class PrinterModelCreateView(CreateView):
    model = PrinterModel
    fields = "__all__"


class PrinterDetailView(DetailView):
    model = Printer


class PrinterModelDetailView(DetailView):
    model = PrinterModel
