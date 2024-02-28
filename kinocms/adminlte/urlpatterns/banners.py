from django.urls import path
from adminlte.views.banners import BannersView, BackgroundSettingsView, TopBannersView, AdvertisementBannersView

app_name = "banners"

urlpatterns = [
    path("", BannersView.as_view(), name="index"),
    path("background-settings/", BackgroundSettingsView.as_view(), name="background-settings"),
    path("top-banners/", TopBannersView.as_view(), name="top-banners"),
    path("advertisement-banners/", AdvertisementBannersView.as_view(), name="advertisement-banners")
]
