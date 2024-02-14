from django import forms

from .models import Comment, Ticket


class TicketCreateForm(forms.Form):
    email = forms.EmailField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comments"]
