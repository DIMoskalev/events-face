from django.core.management import BaseCommand

from src.users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@gmail.com",
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password("123qwe45rt")
        user.save()
