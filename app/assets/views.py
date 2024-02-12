from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Computer, ComputerModel, ComputerType, Maker, Status


def inventory_view(request):
    context = {
        "computer_list": Computer.objects.all(),
        "computer_model_list": ComputerModel.objects.all(),
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
