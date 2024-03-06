from django.db import models


class AbstractBaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractSeoModel(AbstractBaseModel):
    seo_url = models.URLField()
    seo_title = models.CharField()
    seo_keywords = models.CharField()
    seo_description = models.TextField()

    class Meta:
        abstract = True
