from shared.models import AbstractBaseModel
from django.db import models


class City(AbstractBaseModel):
    name = models.CharField(max_length=255)


class Country(AbstractBaseModel):
    name = models.CharField(max_length=255)
