from cloudinary.models import CloudinaryField
from django.db import models
from shared.models import AbstractSeoModel, AbstractBaseModel
from django.core.validators import RegexValidator
from datetime import date, timedelta

YOUTUBE_URL_REGEX = r"^(http(s)?:\/\/)?(www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)"


class Film(AbstractSeoModel):
    name_uk = models.CharField()
    name_en = models.CharField()
    description_uk = models.TextField()
    description_en = models.TextField()
    image = CloudinaryField("image")
    trailer_url = models.URLField(validators=[RegexValidator(YOUTUBE_URL_REGEX)])
    is_3d = models.BooleanField(default=False)
    is_2d = models.BooleanField(default=False)
    is_imax = models.BooleanField(default=False)
    release_date = models.DateField(default=date.today() + timedelta(days=7))
    end_date = models.DateField(default=date.today() + timedelta(days=30))


class FilmImage(AbstractBaseModel):
    image = CloudinaryField("image")
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
