from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Customer, Department


class CustomerListView(ListView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = "__all__"


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"


class CustomerDetailView(DetailView):
    model = Customer


class DepartmentListView(ListView):
    model = Department
