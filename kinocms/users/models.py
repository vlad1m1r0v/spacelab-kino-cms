from django.contrib.auth.models import AbstractUser
from django.db import models
from locations.models import City
from shared.models import AbstractBaseModel
from .managers import CustomUserManager


class CustomUser(AbstractUser, AbstractBaseModel):
    email = models.EmailField(unique=True)
    username = None

    nick_name = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    card_number = models.PositiveBigIntegerField(null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    language_choices = [
        ("UK", "Ukrainian"),
        ("EN", "English")
    ]
    language = models.CharField(choices=language_choices, null=True, blank=True)

    sex_choices = [
        ("MALE", "Male"),
        ("FEMALE", "Female")
    ]
    sex = models.CharField(choices=sex_choices, null=True, blank=True)   

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
