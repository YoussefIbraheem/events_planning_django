from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class UserType(models.TextChoices):
        ATTENDEE = "attendee", "Attendee"
        ORGANISER = "organiser", "Organiser"

    user_type = models.CharField(
        max_length=20, choices=UserType.choices, default=UserType.ATTENDEE
    )

    def is_attendee(self):
        return self.user_type == self.UserType.ATTENDEE

    def is_organiser(self):
        return self.user_type == self.UserType.ORGANISER
