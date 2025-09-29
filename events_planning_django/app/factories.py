from .models import CustomUser
from faker import Faker

factory_faker = Faker()


class UserFactory:

    @staticmethod
    def create(self, **kwargs):
        return {
            "username": kwargs.get("username", factory_faker.unique.user_name()),
            "email": kwargs.get("email", factory_faker.unique.email()),
            "password": kwargs.get("password", "password@123"),
            "first_name": kwargs.get("first_name", factory_faker.first_name()),
            "last_name": kwargs.get("last_name", factory_faker.last_name()),
            "user_type": kwargs.get("user_type",factory_faker.random_element(list(CustomUser.UserType.values)))
        }
