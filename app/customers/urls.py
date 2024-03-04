from django.urls import path

from .views import (
    CustomerCreateView,
    CustomerDetailView,
    CustomerListView,
    CustomerUpdateView,
    DepartmentListView,
)

urlpatterns = [
    path("", CustomerListView.as_view(), name="customer-list"),
    path("create/", CustomerCreateView.as_view(), name="customer-create"),
    path("detail/<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("update/<int:pk>/", CustomerUpdateView.as_view(), name="customer-update"),
    path("departments/", DepartmentListView.as_view(), name="department-list"),
]
