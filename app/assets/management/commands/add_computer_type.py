# your_app/management/commands/add_os.py
from django.core.management.base import BaseCommand

from ...models import ComputerType


class Command(BaseCommand):
    help = "Add a list of names to the ComputerType model"

    def handle(self, *args, **options):
        names = ["desktop", "laptop", "other"]

        for name in names:
            type_instance, created = ComputerType.objects.get_or_create(name=name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added name: {name}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Name already exists: {name}"))
