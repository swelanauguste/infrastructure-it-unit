from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ComputerForm, MonitorForm, PrinterForm
from .models import (
    Computer,
    ComputerModel,
    ComputerType,
    Maker,
    Monitor,
    MonitorModel,
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
        "monitors": Monitor.objects.all(),
        "monitor_models": MonitorModel.objects.all(),
    }
    return render(request, "assets/inventory.html", context)


class ComputerCreateView(CreateView):
    model = Computer
    form_class = ComputerForm


class ComputerUpdateView(UpdateView):
    model = Computer
    form_class = ComputerForm



class ComputerModelCreateView(CreateView):
    model = ComputerModel
    fields = "__all__"


class ComputerModelUpdateView(UpdateView):
    model = ComputerModel
    fields = "__all__"


class ComputerDetailView(DetailView):
    model = Computer


class ComputerModelDetailView(DetailView):
    model = ComputerModel


class PrinterCreateView(CreateView):
    model = Printer
    form_class = PrinterForm


class PrinterUpdateView(UpdateView):
    model = Printer
    form_class = PrinterForm



class PrinterModelCreateView(CreateView):
    model = PrinterModel
    fields = "__all__"


class PrinterModelUpdateView(UpdateView):
    model = PrinterModel
    fields = "__all__"


class PrinterDetailView(DetailView):
    model = Printer


class PrinterModelDetailView(DetailView):
    model = PrinterModel


class MonitorCreateView(CreateView):
    model = Monitor
    form = MonitorForm


class MonitorUpdateView(UpdateView):
    model = Monitor
    form_class = MonitorForm


class MonitorModelCreateView(CreateView):
    model = MonitorModel
    fields = "__all__"


class MonitorModelUpdateView(UpdateView):
    model = MonitorModel
    fields = "__all__"


class MonitorDetailView(DetailView):
    model = Monitor


class MonitorModelDetailView(DetailView):
    model = MonitorModel
