from django.urls import path

from .views import (
    ComputerCreateView,
    ComputerDetailView,
    ComputerModelCreateView,
    ComputerModelDetailView,
    PrinterCreateView,
    PrinterDetailView,
    PrinterModelCreateView,
    PrinterModelDetailView,
    inventory_view,
)

urlpatterns = [
    path("", inventory_view, name="inventory"),
    path(
        "computer/detail/<int:pk>/",
        ComputerDetailView.as_view(),
        name="computer-detail",
    ),
    path("add/computer/", ComputerCreateView.as_view(), name="computer-create"),
    path(
        "computer-model/detail/<int:pk>/",
        ComputerModelDetailView.as_view(),
        name="computer-model-detail",
    ),
    path(
        "add/computer-model/",
        ComputerModelCreateView.as_view(),
        name="computer-model-create",
    ),
    path(
        "printer/detail/<int:pk>/",
        PrinterDetailView.as_view(),
        name="printer-detail",
    ),
    path("add/printer/", PrinterCreateView.as_view(), name="printer-create"),
    path(
        "printer-model/detail/<int:pk>/",
        PrinterModelDetailView.as_view(),
        name="printer-model-detail",
    ),
    path(
        "add/printer-model/",
        PrinterModelCreateView.as_view(),
        name="printer-model-create",
    ),
]
