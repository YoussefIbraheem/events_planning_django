from .factories import UserFactory
from .models import CustomUser


class UserSeeder:
    
    @staticmethod
    def seed(self, *args, **kwargs):
        factory = UserFactory()
        count = kwargs.get("count", 10)
        for _ in range(count):
            user_data = factory.create()
            user = CustomUser.objects.create_user(**user_data)
            user.save()
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} users"))