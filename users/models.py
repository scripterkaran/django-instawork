from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utils.models import UUIDModel


class User(UUIDModel, AbstractUser):
    ADMIN = 1
    STAFF = 2
    ROLES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff')
    )

    phone_number = models.CharField(max_length=128, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLES)

    @staticmethod
    def create_dummy_data():
        return User.objects.create(**{
            "username": "first_name.last_name",
            'first_name': 'first_name',
            'last_name': 'last_name',
            'phone_number': 'first_name',
            'email': 'email@email.com',
            'role': User.ADMIN,
        })
