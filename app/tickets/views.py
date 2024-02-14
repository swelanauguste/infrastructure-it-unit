from customers.models import Customer
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CommentCreateForm, TicketCreateForm
from .models import Comment, Ticket
from django.core.exceptions import ObjectDoesNotExist

def create_ticket_view(request):
    if request.method == "POST":
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            description = form.cleaned_data["description"]

            try:
                customer = Customer.objects.get(email=email)
            except ObjectDoesNotExist:
                # Add a custom error to the form for the email field
                form.add_error("email", "Email address not found, please contact support")
                return render(request, "tickets/create_ticket.html", {"form": form})

            ticket = Ticket.objects.create(user=customer, description=description)
            ticket.save()
            messages.success(request, "Ticket was created successfully")
            return redirect("ticket-detail", pk=ticket.pk)
    else:
        form = TicketCreateForm()

    context = {"form": form}
    return render(request, "tickets/create_ticket.html", context)

class TicketListView(ListView):
    model = Ticket


class TicketDetailView(DetailView):
    model = Ticket


# def create_ticket_view(request):
#     if request.method == "POST":
#         form = TicketCreateForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data["email"]
#             description = form.cleaned_data["description"]
#             customer = Customer.objects.get(email=email)
#             if customer:
#                 ticket = Ticket.objects.create(user=customer, description=description)
#                 ticket.save()
#                 messages.success(request, "Ticket was created successfully")
#                 return redirect("ticket-detail", pk=ticket.pk)
#             # print(email, description, customer)
#             else:
#                 messages.warning(request, "email address not found, please contact support")
#                 return render(request, "tickets/create_ticket.html", {"form": form})
#     else:
#         form = TicketCreateForm()
#     context = {"form": form}

#     return render(request, "tickets/create_ticket.html", context)
