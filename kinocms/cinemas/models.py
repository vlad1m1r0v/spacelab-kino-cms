from cloudinary.models import CloudinaryField
from django.db import models
from shared.models import AbstractSeoModel, AbstractBaseModel


class Cinema(AbstractSeoModel):
    name_uk = models.CharField()
    name_en = models.CharField()
    description_uk = models.TextField()
    description_en = models.TextField()
    features_uk = models.TextField()
    features_en = models.TextField()
    logo = CloudinaryField("image")
    upper_banner = CloudinaryField("image")


class CinemaImage(AbstractBaseModel):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    image = CloudinaryField("image")


class Hall(AbstractSeoModel):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name_uk = models.CharField()
    name_en = models.CharField()
    description_uk = models.TextField()
    description_en = models.TextField()
    scheme = CinemaImage("image")
    upper_banner = CinemaImage("image")
    capacity = models.SmallIntegerField(default=200)


class HallImage(AbstractBaseModel):
    cinema = models.ForeignKey(Hall, on_delete=models.CASCADE)
    image = CloudinaryField("image")
