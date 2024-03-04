# your_app/management/commands/add_os.py
from django.core.management.base import BaseCommand

from ...models import Status


class Command(BaseCommand):
    help = "Add a list of statuses to the Status model"

    def handle(self, *args, **options):
        statuses = ["in-repair", "in-storage", "in-use", "retired", "unusable",]

        for status in statuses:
            status_instance, created = Status.objects.get_or_create(name=status)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added Status: {status}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Status already exists: {status}"))
