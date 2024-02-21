from django.contrib import admin
from banners.models import TopBanner, AdvertisementBanner, BannerSettings


@admin.register(TopBanner)
class TopBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementBanner)
class AdvertisementBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerSettings)
class BannerSettingsAdmin(admin.ModelAdmin):
    pass
