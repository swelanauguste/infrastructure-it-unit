from django.db import models


class ComputerType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ComputerModel(models.Model):
    name = models.CharField(max_length=100)
    computer_type = models.ForeignKey(ComputerType, on_delete=models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    processor = models.CharField(
        max_length=100, blank=True, null=True, help_text="In GHz(e.g.:i5 2.9 GHz)"
    )
    ram = models.IntegerField("RAM", help_text="In GB")
    hdd = models.IntegerField("HDD/Storage", help_text="In GB")

    def __str__(self):
        return self.name


class Computer(models.Model):
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    computer_name = models.CharField(max_length=100, blank=True, null=True)
    model = models.ForeignKey(ComputerModel, on_delete=models.CASCADE, related_name="computers")
    location = models.CharField(max_length=100)
    ip_addr = models.GenericIPAddressField(blank=True, null=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_received = models.DateField(blank=True, null=True)
    date_installed = models.DateField(blank=True, null=True)
    warranty_info = models.CharField(max_length=100)

    def __str__(self):
        return self.serial_number
