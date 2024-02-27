# your_app/management/commands/add_os.py
from django.core.management.base import BaseCommand

from ...models import OperatingSystem


class Command(BaseCommand):
    help = "Add a list of OS to the OperatingSystem model"

    def handle(self, *args, **options):
        os_list = ["xp", "vista", "7", "8", "8.1", "10", "11", 'macos', 'linux']

        for os_name in os_list:
            os_instance, created = OperatingSystem.objects.get_or_create(name=os_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added OS: {os_name}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"OS already exists: {os_name}"))
