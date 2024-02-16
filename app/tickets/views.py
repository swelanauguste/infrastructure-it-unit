from customers.models import Customer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CommentCreateForm, TicketCreateForm
from .models import Comment, Ticket


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
                form.add_error(
                    "email", "Email address not found, please contact support"
                )
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentCreateForm()
        return context


def add_comment_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.save()
            return redirect("ticket-detail", pk=pk)

    # If the form is not valid or the request method is not POST
    return render(
        request, "ticket_detail.html", {"ticket": ticket, "comment_form": form}
    )
