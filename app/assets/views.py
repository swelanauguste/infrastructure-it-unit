from django.db.models import Q
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
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


class ComputerListView(ListView):
    model = Computer

    def get_queryset(self):
        query = self.request.GET.get("computers")

        if query:
            return Computer.objects.filter(
                Q(serial_number__icontains=query)
                | Q(computer_name__icontains=query)
                | Q(os__name__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__computer_type__name__icontains=query)
                | Q(model__maker__name__icontains=query)
                | Q(model__processor__icontains=query)
                | Q(model__ram__icontains=query)
                | Q(model__hdd__icontains=query)
                | Q(user__icontains=query)
                | Q(status__name__icontains=query)
                | Q(warranty_info__icontains=query)
                | Q(location__icontains=query)
                | Q(dept__icontains=query)
            ).distinct()
        return Computer.objects.all()


class ComputerModelListView(ListView):
    model = ComputerModel

    def get_queryset(self):
        query = self.request.GET.get("computer-models")

        if query:
            return ComputerModel.objects.filter(
                Q(name__icontains=query)
                | Q(computer_type__name__icontains=query)
                | Q(maker__name__icontains=query)
                | Q(processor__icontains=query)
                | Q(ram__icontains=query)
                | Q(hdd__icontains=query)
            ).distinct()
        return ComputerModel.objects.all()


class PrinterListView(ListView):
    model = Printer

    def get_queryset(self):
        query = self.request.GET.get("printers")

        if query:
            return Printer.objects.filter(
                Q(serial_number__icontains=query)
                | Q(printer_name__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__maker__name__icontains=query)
                | Q(status__name__icontains=query)
                | Q(location__icontains=query)
                | Q(ip_addr__icontains=query)
                | Q(dept__icontains=query)
            ).distinct()
        return Printer.objects.all()


class PrinterModelListView(ListView):
    model = PrinterModel

    def get_queryset(self):
        query = self.request.GET.get("printer-models")

        if query:
            return PrinterModel.objects.filter(
                Q(name__icontains=query)
                | Q(maker__name__icontains=query)
            ).distinct()
        return PrinterModel.objects.all()


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
    form_class = MonitorForm


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
