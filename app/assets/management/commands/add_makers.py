# your_app/management/commands/add_os.py
from django.core.management.base import BaseCommand

from ...models import Maker


class Command(BaseCommand):
    help = "Add a list of makes to the Maker model"

    def handle(self, *args, **options):
        makers = ["dell", "hp", "xerox", "toshiba", "canon", "lenovo", "ricoh"]

        for make in makers:
            make_instance, created = Maker.objects.get_or_create(name=make)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added Maker: {make}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Make already exists: {make}"))
