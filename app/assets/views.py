from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    CommentCreateForm,
    ComputerForm,
    MicrosoftOfficeUpdateForm,
    MonitorForm,
    PrinterForm,
)
from .models import (
    Computer,
    ComputerComment,
    ComputerModel,
    ComputerType,
    Maker,
    MicrosoftOffice,
    Monitor,
    MonitorModel,
    Printer,
    PrinterModel,
    Status,
)


class MicrosoftOfficeListView(ListView):
    model = MicrosoftOffice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["microsoft_office_count"] = MicrosoftOffice.objects.all().count()
        context["microsoft_office_update_form"] = MicrosoftOfficeUpdateForm()
        return context


class MicrosoftOfficeDetailView(DetailView):
    model = MicrosoftOffice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["microsoft_office_update_form"] = MicrosoftOfficeUpdateForm()
        return context


class MicrosoftOfficeUpdateView(UpdateView):
    model = MicrosoftOffice
    form_class = MicrosoftOfficeUpdateForm
    
    def form_valid(self, form):
        form.instance.is_installed = True
        return super().form_valid(form)


def add_computer_comment_view(request, pk):
    computer = get_object_or_404(Computer, pk=pk)

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.computer = computer
            comment.save()
            return redirect("computer-detail", pk=pk)

    # If the form is not valid or the request method is not POST
    return render(
        request, "assets/computer_detail.html", {"ticket": ticket, "comment_form": form}
    )


class ComputerListView(ListView):
    model = Computer
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["computer_count"] = Computer.objects.all().count()
        return context

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
                | Q(location__name__icontains=query)
            ).distinct()
        return Computer.objects.all()


class ComputerModelListView(ListView):
    model = ComputerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["computer_model_count"] = ComputerModel.objects.all().count()
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["printer_count"] = Printer.objects.all().count()
        return context

    def get_queryset(self):
        query = self.request.GET.get("printers")

        if query:
            return Printer.objects.filter(
                Q(serial_number__icontains=query)
                | Q(printer_name__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__maker__name__icontains=query)
                | Q(status__name__icontains=query)
                # | Q(location__name__icontains=query)
                | Q(ip_addr__icontains=query)
                | Q(department__name__icontains=query)
            ).distinct()
        return Printer.objects.all()


class PrinterModelListView(ListView):
    model = PrinterModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["printer_model_count"] = PrinterModel.objects.all().count()
        return context

    def get_queryset(self):
        query = self.request.GET.get("printer-models")

        if query:
            return PrinterModel.objects.filter(
                Q(name__icontains=query) | Q(maker__name__icontains=query)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentCreateForm()
        return context


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


class MonitorListView(ListView):
    model = Monitor

    def get_queryset(self):
        query = self.request.GET.get("monitors")

        if query:
            return Monitor.objects.filter(
                Q(serial_number__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__maker__name__icontains=query)
                | Q(status__name__icontains=query)
            ).distinct()
        return Monitor.objects.all()


class MonitorModelListView(ListView):
    model = MonitorModel

    def get_queryset(self):
        query = self.request.GET.get("monitor-models")

        if query:
            return MonitorModel.objects.filter(
                Q(name__icontains=query) | Q(maker__name__icontains=query)
            ).distinct()
        return MonitorModel.objects.all()


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
