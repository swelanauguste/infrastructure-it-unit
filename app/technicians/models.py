from django.db import models


class Technician(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
