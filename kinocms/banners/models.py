from django.db import models
from cloudinary.models import CloudinaryField

from shared.models import AbstractBaseModel


class BaseBanner(AbstractBaseModel):
    image = CloudinaryField("image")
    url = models.URLField()

    class Meta:
        abstract = True


class AdvertisementBanner(BaseBanner):
    pass


class TopBanner(BaseBanner):
    description = models.TextField()


class Singleton(AbstractBaseModel):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Singleton, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class BannerSettings(Singleton):
    banner_rotation = models.PositiveSmallIntegerField(default=5)
    are_banners_active = models.BooleanField(default=True)
    advertisement_rotation = models.PositiveSmallIntegerField(default=5)
    are_advertisements_active = models.BooleanField(default=True)
    background_image = CloudinaryField("image", null=True, blank=True)
    is_background_image = models.BooleanField(default=True)
