from django.urls import path

from .views import create_ticket_view, TicketListView, TicketDetailView, add_comment_view

urlpatterns = [
    path("", create_ticket_view, name="ticket-create"),
    path("tickets/", TicketListView.as_view(), name="ticket-list"),
    path("tickets/<int:pk>/", TicketDetailView.as_view(), name="ticket-detail"),
    path("ticket/add-comment/<int:pk>/", add_comment_view, name="add-comment"),
]
