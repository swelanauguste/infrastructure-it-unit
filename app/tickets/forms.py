from django import forms
from technicians.models import Technician

from .models import Comment, Ticket


class TicketAssignTechnicianForm(forms.Form):
    technician_id = forms.ModelChoiceField(
        queryset=Technician.objects.all(), empty_label="Select Technician"
    )


class TicketCreateForm(forms.Form):
    summary = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comments"]
