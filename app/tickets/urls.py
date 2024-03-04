from django.urls import path

from .views import (
    CustomerTicketListView,
    TicketDetailView,
    TicketListView,
    add_comment_view,
    create_ticket_view,
    assign_technician_view
)

urlpatterns = [
    path("", create_ticket_view, name="ticket-create"),
    path("tickets/", CustomerTicketListView.as_view(), name="customer-ticket-list"),
    path("customer/ticket/", TicketListView.as_view(), name="ticket-list"),
    path("tickets/<slug:slug>/", TicketDetailView.as_view(), name="ticket-detail"),
     path('assign-technician/<slug:slug>/', assign_technician_view, name='assign-technician'),
    path("ticket/add-comment/<slug:slug>/", add_comment_view, name="add-comment"),
]
