import random
import string

from customers.models import Customer
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def generate_short_id():
    length = 8  # You can adjust the length as needed
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length)).upper()


class Ticket(models.Model):
    ticket_id = models.CharField(
        default=generate_short_id, editable=False, unique=True, max_length=8
    )
    slug = models.SlugField(max_length=8, unique=True, blank=True, null=True)
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("ticket-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.ticket_id)
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_id}"


class Comment(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="comments"
    )
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.comments[:50]}"
