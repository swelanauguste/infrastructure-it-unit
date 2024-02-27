from django import forms

from .models import Computer, ComputerComment, Monitor, Printer


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerComment
        fields = ["comment"]
        widgets = {"comment": forms.Textarea(attrs={"rows": 4,})}


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = "__all__"
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "date_installed": forms.DateInput(attrs={"type": "date"}),
        }


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = "__all__"
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "date_installed": forms.DateInput(attrs={"type": "date"}),
        }


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = "__all__"
        widgets = {
            "date_received": forms.DateInput(attrs={"type": "date"}),
            "date_installed": forms.DateInput(attrs={"type": "date"}),
        }
