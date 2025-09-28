from django.core.management.base import BaseCommand, CommandError
from app.seeders import UserSeeder


class Command(BaseCommand):
    help = "Seed users into database"

    @staticmethod
    def handle(self, *args, **options):
        try:
            UserSeeder.seed(self, *args, **options)
        except Exception as e:
            raise CommandError(f"Error seeding users: {e}")
