from customers.models import Customer, Department
from django.db import models
from django.shortcuts import reverse


class Maker(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ["name"]

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class MonitorModel(models.Model):
    name = models.CharField(max_length=100)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    image = models.FileField(upload_to="monitor_models/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("monitor-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.maker} - {self.name}"


class Monitor(models.Model):
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    monitor_name = models.CharField(max_length=100, blank=True, null=True)
    model = models.ForeignKey(
        MonitorModel, on_delete=models.CASCADE, related_name="monitors"
    )
    location = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_received = models.DateField(blank=True, null=True)
    date_installed = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True, help_text="Warranty Information")

    class Meta:
        ordering = ["model__name"]

    def get_absolute_url(self):
        return reverse("monitor-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.model.name} - {self.dept}"


class ComputerType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name.upper()


class ComputerModel(models.Model):
    name = models.CharField(max_length=100)
    computer_type = models.ForeignKey(ComputerType, on_delete=models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    processor = models.CharField(
        max_length=100, blank=True, null=True, help_text="In GHz(e.g.:i5 2.9 GHz)"
    )
    ram = models.IntegerField("RAM", help_text="In GB")
    hdd = models.IntegerField("HDD/Storage", help_text="In GB")

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("computer-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.maker} - {self.name}"


class Computer(models.Model):
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    computer_name = models.CharField(max_length=100, blank=True, null=True)
    model = models.ForeignKey(
        ComputerModel, on_delete=models.CASCADE, related_name="computers"
    )
    monitor = models.ManyToManyField(Monitor, related_name="monitors", blank=True)
    os = models.ForeignKey(
        OperatingSystem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Operating System",
    )
    location = models.CharField(max_length=100, blank=True, null=True)
    ip_addr = models.GenericIPAddressField("IP Address", blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_received = models.DateField(blank=True, null=True)
    date_installed = models.DateField(blank=True, null=True)
    warranty_info = models.CharField(max_length=100)
    image = models.FileField(upload_to="system_audit/", blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["computer_name"]

    def get_absolute_url(self):
        return reverse("computer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        if self.computer_name:
            return self.computer_name
        return f"N/A"


class PrinterModel(models.Model):
    name = models.CharField(max_length=100)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    image = models.FileField(upload_to="printer_models/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("printer-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.maker} - {self.name}"


class Printer(models.Model):
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    printer_name = models.CharField(max_length=100, blank=True, null=True)
    model = models.ForeignKey(
        PrinterModel, on_delete=models.CASCADE, related_name="printers"
    )
    location = models.CharField(max_length=100, null=True, blank=True)
    ip_addr = models.GenericIPAddressField(blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_received = models.DateField(blank=True, null=True)
    date_installed = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["ip_addr"]

    def get_absolute_url(self):
        return reverse("printer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.ip_addr} - {self.model.name}"
