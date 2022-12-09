from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"<[{self.id}] - {self.first_name}, {self.is_employee}>"
